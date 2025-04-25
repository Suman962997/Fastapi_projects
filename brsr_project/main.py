import json
import pdfplumber
import docx
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
import google.generativeai as genai
from google.api_core.exceptions import ResourceExhausted
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
import os

# Configure Gemini
genai.configure(api_key="AIzaSyAZ7GTHvo3ttXPQtEHVtEsRemUMuXzTpTI" )




app = FastAPI()
app = FastAPI(title="Document Extractor API" )
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://192.168.2.72:3000","http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)





KEYS_TO_EXTRACT = """
Corporate Identity Number (CIN) of the Listed Entity
Name of the Listed Entity
Year of incorporation
Registered office address
Corporate address		
Email
Telephone
Website
Financial year for which reporting is being done
Name of the Stock Exchange(s) where shares are listed
Paid-up Capital
Name and contact details
Reporting boundary - Are the disclosures under this report made on a standalone basis (i.e. only for the entity) or on a consolidated basis (i.e. for the entity and all the entities which form a part of its consolidated financial statements, taken together)
Name of assurance provider
Type of assurance obtained
Details of business activities (accounting for 90% of the turnover)
Products/Services sold by the entity (accounting for 90% of the entity’s Turnover):
No. of locations where plants and/or operations/ offices of the entity are situated:
Markets served by the entity
No. of Locations
What is the contribution of exports as a percentage of the total turnover of the entity?
Employees and workers (including differently abled):
Differently abled Employees and workers:
Participation/Inclusion/Representation of women
Turnover rate for permanent employees and workers (Disclose trends for the past 3 years)
How many products have undergone a carbon footprint assessment?
Whether CSR is applicable as per section 135 of Companies Act, 2013: (Yes/No)
Turnover (in Rs.)
Net worth (in Rs.)
Net worth (in Rs.)
Complaints/Grievances on any of the principles (Principles 1 to 9) under the National Guidelines on Responsible Business Conduct:
Please indicate material responsible business conduct and sustainability issues pertaining to environmental and social matters that present a risk or an opportunity to your business, rationale for identifying the same, approach to adapt or mitigate the risk along-with its financial implications, as per the following format.


"""

def extract_json_from_text(text):
    brace_stack = []
    start_index = None
    for i, char in enumerate(text):
        if char == '{':
            if start_index is None:
                start_index = i
            brace_stack.append('{')
        elif char == '}':
            if brace_stack:
                brace_stack.pop()
                if not brace_stack:
                    json_str = text[start_index:i + 1]
                    try:
                        return json.loads(json_str)
                    except json.JSONDecodeError:
                        continue
    return None

def extract_text_from_pdf(file):
    with pdfplumber.open(file) as pdf:
        return "\n".join([page.extract_text() for page in pdf.pages if page.extract_text()])

def extract_text_from_docx(file):
    doc = docx.Document(file)
    return "\n".join([para.text for para in doc.paragraphs])

def chunk_text(text,max_tokens=1500):
    paragraphs = text.split("\n" )
    chunks, current_chunk = [], ""
    for para in paragraphs:
        if len(current_chunk) + len(para) < max_tokens:
            current_chunk += para + "\n"
        else:
            chunks.append(current_chunk)
            current_chunk = para + "\n"
    if current_chunk:
        chunks.append(current_chunk)
    return chunks

def extract_fields_with_gemini(text_chunk: str) -> dict:
    model = genai.GenerativeModel("gemini-2.0-flash" )
    prompt = f"""
You are an expert in information extraction. Extract the following details from the provided text and return them in valid JSON format with keys exactly as listed below. Only return the JSON — no extra commentary.

{KEYS_TO_EXTRACT}

TEXT:
{text_chunk}
"""
    try:
        response = model.generate_content(prompt)
        parsed = extract_json_from_text(response.text)
        return parsed if parsed else {}
    except ResourceExhausted:
        raise HTTPException(status_code=429, detail="Gemini API quota exceeded." )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def merge_results(results):
    final = {}
    for result in results:
        for k, v in result.items():
            if k not in final or not final[k]:
                final[k] = v
    return final


def parse_brsr_text(json_merge):
    return {
        # SECTION A
        "section_a": {
            "title": "GENERAL DISCLOSURES",
            "one": {
                "subtitle": "Details of the listed entity",
                "questions": {
                    "1": {
                        "question": "Corporate Identity Number (CIN) of the Listed Entity",
                        "answer": (json_merge["Corporate Identity Number (CIN) of the Listed Entity"])
                    },
                    "2": {
                        "question": "Name of the Listed Entity",
                        "answer": (json_merge["Name of the Listed Entity"])
                    },
                    "3": {
                        "question": "Year of incorporation",
                        "answer": (json_merge["Year of incorporation"])
                    },
                    "4": {
                        "question": "Registered office address",
                        "answer": (json_merge["Registered office address"])
                    },
                    "5": {
                        "question": "Corporate address",
                        "answer": (json_merge["Corporate address"])
                    },
                    "6": {
                        "question": "Email",
                        "answer": (json_merge["Email"])
                    },
                    "7": {
                        "question": "Telephone",
                        "answer": (json_merge["Telephone"])
                    },
                    "8": {
                        "question": "Website",
                        "answer": (json_merge["Website"])
                    },
                    "9": {
                        "question": "Financial year for which reporting is being done",
                        "answer": (json_merge["Financial year for which reporting is being done"])
                    },
                    "10": {
                        "question": "Name of the Stock Exchange(s) where shares are listed",
                        "answer": (json_merge["Name of the Stock Exchange(s) where shares are listed"])
                    },
                    "11": {
                        "question": "Paid-up Capital",
                        "answer": (json_merge["Paid-up Capital"])
                    },
                    "12": {
                        "question": "Name and contact details of the person who may be contacted",
                        "answer": (json_merge["Name and contact details"])
                    },
                    "13": {
                        "question": "Reporting boundary - Are the disclosures under this report made on a standalone basis (i.e. only for the entity) or on a consolidated basis (i.e. for the entity and all the entities which form a part of its consolidated financial statements, taken together)",
                        "answer": (json_merge["Reporting boundary - Are the disclosures under this report made on a standalone basis (i.e. only for the entity) or on a consolidated basis (i.e. for the entity and all the entities which form a part of its consolidated financial statements, taken together)"])
                    },
                    "14": {
                        "question": "Name of assurance provider",
                        "answer": (json_merge["Name of assurance provider"])
                    },
                    "15": {
                        "question": "Type of assurance obtained",
                        "answer": (json_merge["Type of assurance obtained"])
                    }

                }
            },
            
            "two": {
                "subtitle": "Products / Services",
                "questions": {
                    "1": {
                        "question": "Details of business activities (accounting for 90% of the turnover)",
                        "answer": (json_merge["Details of business activities (accounting for 90% of the turnover)"])
                    },
                    "2": {
                        "question": "Products/Services sold by the entity (accounting for 90% of the entity’s Turnover):",
                        "answer": (json_merge["Products/Services sold by the entity (accounting for 90% of the entity’s Turnover):"])
                    }
                }
            },
            "three":{
                "subtitle":"Operations",
                "questions":{
                    "1":{
                        "questions":"No. of locations where plants and/or operations/ offices of the entity are situated:",
                        "answer": (json_merge["No. of locations where plants and/or operations/ offices of the entity are situated:"])
                    },
                    "2":{
                        "mainquestion":" Markets served by the entity"
                        },
                    "2.a":{
                        "questions":"No. of Locations",
                        "answer": (json_merge["No. of Locations"])
                    },
                    "2.b":{
                        "questions":"What is the contribution of exports as a percentage of the total turnover of the entity?",
                        "answer": (json_merge["What is the contribution of exports as a percentage of the total turnover of the entity?"])
                    }
                    
                }
            },
            "four":{
                "subtitle":"Employees",
                "questions":{
                    "1":{
                        "mainquestion":" Details as at the end of Financial Year"
                        },
                    "1.a":{
                        "questions":"Employees and workers (including differently abled):",
                        "answer": (json_merge["Employees and workers (including differently abled):"])
                    },
                    "1.b":{
                        "questions":"Differently abled Employees and workers:",
                        "answer": (json_merge["Differently abled Employees and workers:"])
                    },
                    "2":{
                        "questions":"Participation/Inclusion/Representation of women",
                        "answer": (json_merge["Participation/Inclusion/Representation of women"])
                    },
                    "3":{
                        "questions":"Turnover rate for permanent employees and workers (Disclose trends for the past 3 years)",
                        "answer": (json_merge["Turnover rate for permanent employees and workers (Disclose trends for the past 3 years)"])
                    }
                    
                }
            },
             "five":{
                "subtitle":"Holding, Subsidiary and Associate Companies (including joint ventures)",
                "questions":{
                    "1":{
                        "questions":" How many products have undergone a carbon footprint assessment?",
                        "answer": (json_merge["How many products have undergone a carbon footprint assessment?"])
                    }                    
                }
            },
             "six":{
                "subtitle":" CSR Details",
                "questions":{
                "1":{
                     "mainquestion":" CSR_details",
                    },
                    "1.a":{
                        "questions":"Whether CSR is applicable as per section 135 of Companies Act, 2013: (Yes/No)",
                        "answer": (json_merge["Whether CSR is applicable as per section 135 of Companies Act, 2013: (Yes/No)"])
                    },
                    "1.b":{
                        "questions":"Turnover (in Rs.)",
                        "answer": (json_merge["Turnover (in Rs.)"])
                    }                   
                    ,
                    "1.c":{
                        "questions":"Net worth (in Rs.)",
                        "answer": (json_merge["Net worth (in Rs.)"])
                    }                   
                                       
                     
                }
            },
             "seven":{
                "subtitle":"Transparency and Disclosures Compliances",
                "questions":{
                    "1":{
                        "questions":" Complaints/Grievances on any of the principles (Principles 1 to 9) under the National Guidelines on Responsible Business Conduct:",
                        "answer": (json_merge["Complaints/Grievances on any of the principles (Principles 1 to 9) under the National Guidelines on Responsible Business Conduct:"])
                    },
                    "2":{
                        "mainquestion":"Overview of the entity’s material responsible business conduct issues",
                    },
                    "2.a":{
                        "questions":"Please indicate material responsible business conduct and sustainability issues pertaining to environmental and social matters that present a risk or an opportunity to your business, rationale for identifying the same, approach to adapt or mitigate the risk along-with its financial implications, as per the following format.",
                        "answer":(json_merge["Please indicate material responsible business conduct and sustainability issues pertaining to environmental and social matters that present a risk or an opportunity to your business, rationale for identifying the same, approach to adapt or mitigate the risk along-with its financial implications, as per the following format."])
                    }                    
                    }}},}



@app.post("/extract/" )
async def extract_document(file: UploadFile = File(...)):
    if not (file.filename.endswith(".pdf" ) or file.filename.endswith(".docx" )):
        raise HTTPException(status_code=400, detail="Only PDF or DOCX files are supported." )
    
    content = await file.read()
    temp_path = f"temp_{file.filename}"
    
    with open(temp_path, "wb" ) as f:
        f.write(content)
 
    try:
        if file.filename.endswith(".pdf" ):
            text = extract_text_from_pdf(temp_path)
        else:
            text = extract_text_from_docx(temp_path)
        
        chunks = chunk_text(text)
        results = [extract_fields_with_gemini(chunk) for chunk in chunks[:5]]
        merged = merge_results(results)
        print(merged)
        
        return parse_brsr_text(merged)
        
        # return JSONResponse(content=merged)
    finally:
        import os
        if os.path.exists(temp_path):
            os.remove(temp_path)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=False, log_level="debug")
