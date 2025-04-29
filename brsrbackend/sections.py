
def extract_answer(text, question):
    lines = text.splitlines()
    for i, line in enumerate(lines):
        # print(f"Index {i}: {line}")
        if question.lower() in line.lower():
            return lines[i + 1].strip() if i + 1 < len(lines) else "Not found"
    return "Not found"


def parse_brsr_text(text):
    return {
        # SECTION A
        "section_a": {
            "title": "GENERAL DISCLOSURES",
            "one": {
                "subtitle": "Details of the listed entity",
                "questions": {
                    "1": {
                        "question": "Corporate Identity Number (CIN) of the Listed Entity",
                        "answer": extract_answer(text, "Corporate Identity Number (CIN) of the Listed Entity")
                    },
                    "2": {
                        "question": "Name of the Listed Entity",
                        "answer": extract_answer(text, "Name of the Listed Entity")
                    },
                    "3": {
                        "question": "Year of incorporation",
                        "answer": extract_answer(text, "Year of incorporation")
                    },
                    "4": {
                        "question": "Registered office address",
                        "answer": extract_answer(text, "Registered office address")
                    },
                    "5": {
                        "question": "Corporate address",
                        "answer": extract_answer(text, "Corporate address")
                    },
                    "6": {
                        "question": "Email",
                        "answer": extract_answer(text, "Email")
                    },
                    "7": {
                        "question": "Telephone",
                        "answer": extract_answer(text, "Telephone")
                    },
                    "8": {
                        "question": "Website",
                        "answer": extract_answer(text, "Website")
                    },
                    "9": {
                        "question": "Financial year for which reporting is being done",
                        "answer": extract_answer(text, "Financial year for which reporting is being done")
                    },
                    "10": {
                        "question": "Name of the Stock Exchange(s) where shares are listed",
                        "answer": extract_answer(text, "Name of the Stock Exchange(s) where shares are listed")
                    },
                    "11": {
                        "question": "Paid-up Capital",
                        "answer": extract_answer(text, "Paid-up Capital")
                    },
                    "12": {
                        "question": "Name and contact details of the person who may be contacted",
                        "answer": extract_answer(text, "Name and contact details")
                    },
                    "13": {
                        "question": " Reporting boundary - Are the disclosures under this report made on a standalone basis (i.e. only for the entity) or on a consolidated basis (i.e. for the entity and all the entities which form a part of its consolidated financial statements, taken together).",
                        "answer": extract_answer(text, " Reporting boundary - Are the disclosures under this report made on a standalone basis (i.e. only for the entity) or on a consolidated basis (i.e. for the entity and all the entities which form a part of its consolidated financial statements, taken together).")
                    },
                    "14": {
                        "question": "Name of assurance provider",
                        "answer": extract_answer(text, "Name of assurance provider")
                    },
                    "15": {
                        "question": " Type of assurance obtained",
                        "answer": extract_answer(text, " Type of assurance obtained")
                    }

                }
            },
            
            "two": {
                "subtitle": "Products / Services",
                "questions": {
                    "1": {
                        "question": " Details of business activities (accounting for 90% of the turnover)",
                        "answer": extract_answer(text, " Details of business activities (accounting for 90% of the turnover)")
                    },
                    "2": {
                        "question": " Products/Services sold by the entity (accounting for 90% of the entity’s Turnover):",
                        "answer": extract_answer(text, " Products/Services sold by the entity (accounting for 90% of the entity’s Turnover):")
                    }
                }
            },
            "three":{
                "subtitle":"Operations",
                "questions":{
                    "1":{
                        "questions":"No. of locations where plants and/or operations/ offices of the entity are situated:",
                        "answer": extract_answer(text, "No. of locations where plants and/or operations/ offices of the entity are situated:")
                    },
                    "2":{
                        "mainquestion":" Markets served by the entity"
                        },
                    "2.a":{
                        "questions":"No. of Locations",
                        "answer": extract_answer(text, "No. of Locations")
                    },
                    "2.b":{
                        "questions":"What is the contribution of exports as a percentage of the total turnover of the entity?",
                        "answer": extract_answer(text, "What is the contribution of exports as a percentage of the total turnover of the entity?")
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
                        "questions":" Employees and workers (including differently abled):",
                        "answer": extract_answer(text, " Employees and workers (including differently abled):")
                    },
                    "1.b":{
                        "questions":" Differently abled Employees and workers:",
                        "answer": extract_answer(text, " Differently abled Employees and workers:")
                    },
                    "2":{
                        "questions":"Participation/Inclusion/Representation of women",
                        "answer": extract_answer(text, " Participation/Inclusion/Representation of women")
                    },
                    "3":{
                        "questions":" Turnover rate for permanent employees and workers (Disclose trends for the past 3 years)",
                        "answer": extract_answer(text,"Turnover rate for permanent employees and workers (Disclose trends for the past 3 years)")
                    }
                    
                }
            },
             "five":{
                "subtitle":"Holding, Subsidiary and Associate Companies (including joint ventures)",
                "questions":{
                    "1":{
                        "questions":" How many products have undergone a carbon footprint assessment?",
                        "answer": extract_answer(text, "How many products have undergone a carbon footprint assessment?")
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
                        "answer": extract_answer(text, "Whether CSR is applicable as per section 135 of Companies Act, 2013: (Yes/No)")
                    },
                    "1.b":{
                        "questions":"Turnover (in Rs.)",
                        "answer": extract_answer(text, "Turnover (in Rs.)")
                    }                   
                    ,
                    "1.c":{
                        "questions":"Net worth (in Rs.)",
                        "answer": extract_answer(text, "Net worth (in Rs.)")
                    }                   
                                       
                     
                }
            },
             "seven":{
                "subtitle":"Transparency and Disclosures Compliances",
                "questions":{
                    "1":{
                        "questions":" Complaints/Grievances on any of the principles (Principles 1 to 9) under the National Guidelines on Responsible Business Conduct:",
                        "answer": extract_answer(text, " Complaints/Grievances on any of the principles (Principles 1 to 9) under the National Guidelines on Responsible Business Conduct:")
                    },
                    "2":{
                        "mainquestion":"Overview of the entity’s material responsible business conduct issues",
                    },
                    "2.a":{
                        "questions":"Please indicate material responsible business conduct and sustainability issues pertaining to environmental and social matters that present a risk or an opportunity to your business, rationale for identifying the same, approach to adapt or mitigate the risk along-with its financial implications, as per the following format.",
                        "answer":extract_answer(text,"Please indicate material responsible business conduct and sustainability issues pertaining to environmental and social matters that present a risk or an opportunity to your business, rationale for identifying the same, approach to adapt or mitigate the risk along-with its financial implications, as per the following format.")
                    }                    
                }
            }

        },    
        
        # SECTION B        
        "section_b": {
            "title": "MANAGEMENT AND PROCESS DISCLOSURES",
            "one": {
                "subtitle": "Policy and management processes",
                "questions": {
                    "1": {
                        "question": " Whether your entity’s policy/policies cover each principle and its core elements of the NGRBCs. (Yes/No)",
                        "answer": extract_answer(text, " Whether your entity’s policy/policies cover each principle and its core elements of the NGRBCs. (Yes/No)")
                    }
                }
            },
             "two": {
                "subtitle": "Governance, leadership and oversight",
                "questions": {
                    "1": {
                        "question": "Statement by director responsible for the business responsibility report, highlighting ESG related challenges, targets and achievements (listed entity has flexibility regarding the placement of this disclosure)",
                        "answer": extract_answer(text, "Statement by director responsible for the business responsibility report, highlighting ESG related challenges, targets and achievements (listed entity has flexibility regarding the placement of this disclosure)")
                    },
                    "2": {
                        "question": " Details of the highest authority responsible for implementation and oversight of the Business Responsibility policy (ies).",
                        "answer": extract_answer(text, " Details of the highest authority responsible for implementation and oversight of the Business Responsibility policy (ies).")
                    },
                    "3": {
                        "question": ". Does the entity have a specified Committee of the Board/ Director responsible for decision making on sustainability related issues? (Yes / No). If yes, provide details.",
                        "answer": extract_answer(text, ". Does the entity have a specified Committee of the Board/ Director responsible for decision making on sustainability related issues? (Yes / No). If yes, provide details.")
                    },
                    "4":{
                        "mainquestion":"Details of Review of NGRBCs by the Company:"
                        },
                    "4.1": {
                        "question": " Indicate whether review was undertaken by Director / Committee of the Board/ Any other Committee",
                        "answer": extract_answer(text, " Indicate whether review was undertaken by Director / Committee of the Board/ Any other Committee")
                    },                  
                    "4.2": {
                        "question": " Frequency(Annually/ Half yearly/ Quarterly/ Any other – please specify)",
                        "answer": extract_answer(text, " Frequency(Annually/ Half yearly/ Quarterly/ Any other – please specify)")
                    },

                    "5": {
                        "question": " Has the entity carried out independent assessment/ evaluation of the working of its policies by an external agency? (Yes/No). If yes, provide name of the agency.",
                        "answer": extract_answer(text, " Has the entity carried out independent assessment/ evaluation of the working of its policies by an external agency? (Yes/No). If yes, provide name of the agency.")
                    },
                    "6": {
                        "question": " If answer to question (1) above is “No” i.e. not all Principles are covered by a policy, reasons to be stated, as below:",
                        "answer": extract_answer(text, " If answer to question (1) above is “No” i.e. not all Principles are covered by a policy, reasons to be stated, as below:")
                    },
                    "7":{
                      "mainquestion":"Supply Chain Mangement"  
                    },
                    "7.a": {
                        "question": "Upstream (Suppliers & Logistics Partners)",
                        "answer": extract_answer(text, "Upstream (Suppliers & Logistics Partners)")
                    },
                                        
                    "7.b": {
                        "question": "Downstream (Distributors & Customers)",
                        "answer": extract_answer(text, "Downstream (Distributors & Customers)")
                    },                    
                }
            },
        },
        
        
        # SECTION C
        "section_c": {
            "title": "PRINCIPLE WISE PERFORMANCE DISCLOSURE",
            "one": {
                "subtitle": "Principle 1 : Businesses should conduct and govern themselves with integrity, and in a manner ",
                "questions": {
                    "1": {
                        "question": "Percentage coverage by training and awareness programmes",
                        "answer": extract_answer(text, "Percentage coverage by training and awareness programmes")
                    },
                    "2": {
                        "question": " Details of fines / penalties /punishment/ award/ compounding fees/ settlement amount paid in proceedings (by the entity or by directors / KMPs) with regulators/ law enforcement agencies/ judicial institutions, in the financial year, in the following format (Note: the entity shall make disclosures on the basis of materiality as specified in Regulation 30 of SEBI (Listing Obligations and Disclosure Obligations) Regulations, 2015 and as disclosed on the entity’s website",
                        "answer": extract_answer(text, " Details of fines / penalties /punishment/ award/ compounding fees/ settlement amount paid in proceedings (by the entity or by directors / KMPs) with regulators/ law enforcement agencies/ judicial institutions, in the financial year, in the following format (Note: the entity shall make disclosures on the basis of materiality as specified in Regulation 30 of SEBI (Listing Obligations and Disclosure Obligations) Regulations, 2015 and as disclosed on the entity’s website")
                    },
                    "2.a": {
                        "question": "Monetary",
                        "answer": extract_answer(text, "Monetary")
                    },
                    "2.b": {
                        "question": "Non-Monetary",
                        "answer": extract_answer(text, "Non-Monetary")
                    },
                    "3": {
                        "question": " Of the instances disclosed in Question 2 above, details of the Appeal/ Revision preferred in cases where monetary or non-monetary action has been appealed.",
                        "answer": extract_answer(text, " Of the instances disclosed in Question 2 above, details of the Appeal/ Revision preferred in cases where monetary or non-monetary action has been appealed.")
                    },
                    "4": {
                        "question": "Does the entity have an anti-corruption or anti-bribery policy? If yes, provide details in brief and if available, provide a web-link to the policy.",
                        "answer": extract_answer(text, "Does the entity have an anti-corruption or anti-bribery policy? If yes, provide details in brief and if available, provide a web-link to the policy.")
                    },
                    "5": {
                        "question": " Number of Directors/KMPs/employees/workers against whom disciplinary action was taken by any law enforcement agency for the charges of bribery/ corruption",
                        "answer": extract_answer(text, " Number of Directors/KMPs/employees/workers against whom disciplinary action was taken by any law enforcement agency for the charges of bribery/ corruption")
                    },
                    "6": {
                        "question": " Details of complaints with regard to conflict of interest",
                        "answer": extract_answer(text, " Details of complaints with regard to conflict of interest")
                    },
                    "7": {
                        "question": "Provide details of any corrective action taken or underway on issues related to fines / penalties / action taken by regulators/ law enforcement agencies/ judicial institutions, on cases of corruption and conflicts of interest.",
                        "answer": extract_answer(text, "Provide details of any corrective action taken or underway on issues related to fines / penalties / action taken by regulators/ law enforcement agencies/ judicial institutions, on cases of corruption and conflicts of interest.")
                    },
                    "8": {
                        "question": " Number of days of accounts payables ((Accounts payable *365) / Cost of goods/services procured) in the following format:",
                        "answer": extract_answer(text, " Number of days of accounts payables ((Accounts payable *365) / Cost of goods/services procured) in the following format:")
                    },
                    "9":{
                        "mainquestion":"Open-ness of business"
                    },
                    "9.a": {
                        "question": " Provide details of concentration of purchases and sales with trading houses, dealers, and related parties along-with loans and advances & investments, with related parties, in the following format:",
                        "answer": extract_answer(text, " Provide details of concentration of purchases and sales with trading houses, dealers, and related parties along-with loans and advances & investments, with related parties, in the following format:")
                    },
                    "10": {
                        "question": ". Awareness programmes conducted for value chain partners on any of the Principles during the financial year:",
                        "answer": extract_answer(text, ". Awareness programmes conducted for value chain partners on any of the Principles during the financial year:")
                    },
                    "11": {
                        "question": " Does the entity have processes in place to avoid/ manage conflict of interests involving members of the Board? (Yes/No) If Yes, provide details of the same.",
                        "answer": extract_answer(text, " Does the entity have processes in place to avoid/ manage conflict of interests involving members of the Board? (Yes/No) If Yes, provide details of the same.")
                    }
                }
            },
            "two": {
                "subtitle": "Principle 2 : Businesses should provide goods and services in a manner that is sustainable and ",
                "questions": {
                    "1": {
                        "question": "Percentage of R&D and capital expenditure (capex) investments in specific technologies to improve the environmental and social impacts of product and processes to total R&D and capex investments made by the entity, respectively.",
                        "answer": extract_answer(text, "Percentage of R&D and capital expenditure (capex) investments in specific technologies to improve the environmental and social impacts of product and processes to total R&D and capex investments made by the entity, respectively.")
                    },
                    "2": {
                        "question": " Does the entity have procedures in place for sustainable sourcing? (Yes/No)",
                        "answer": extract_answer(text, "Does the entity have procedures in place for sustainable sourcing? (Yes/No)")
                    },
                    "2.a": {
                        "question": "If yes, what percentage of inputs were sourced sustainably?",
                        "answer": extract_answer(text, " If yes, what percentage of inputs were sourced sustainably?")
                    },
                    "3": {
                        "question": "Describe the processes in place to safely reclaim your products for reusing, recycling and disposing at the end of life, for :",
                        "answer": extract_answer(text, "Describe the processes in place to safely reclaim your products for reusing, recycling and disposing at the end of life, for :")
                    },
                    "4": {
                        "question": "Whether Extended Producer Responsibility (EPR) is applicable to the entity’s activities (Yes / No). If yes, whether the waste collection plan is in line with the Extended Producer Responsibility (EPR) plan submitted to Pollution Control Boards? If not, provide steps taken to address the same.",
                        "answer": extract_answer(text, "Whether Extended Producer Responsibility (EPR) is applicable to the entity’s activities (Yes / No). If yes, whether the waste collection plan is in line with the Extended Producer Responsibility (EPR) plan submitted to Pollution Control Boards? If not, provide steps taken to address the same.")
                    },
                    "5": {
                        "question": "Has the entity conducted Life Cycle Perspective / Assessments (LCA) for any of its products (for manufacturing industry) or for its services (for service industry)? If yes, provide details in the following format?",
                        "answer": extract_answer(text, "Has the entity conducted Life Cycle Perspective / Assessments (LCA) for any of its products (for manufacturing industry) or for its services (for service industry)? If yes, provide details in the following format?")
                    },
                    "6": {
                        "question": "If there are any significant social or environmental concerns and/or risks arising from production or disposal of your products / services, as identified in the Life Cycle Perspective / Assessments (LCA) or through any other means, briefly describe the same along-with action taken to mitigate the same.",
                        "answer": extract_answer(text, "If there are any significant social or environmental concerns and/or risks arising from production or disposal of your products / services, as identified in the Life Cycle Perspective / Assessments (LCA) or through any other means, briefly describe the same along-with action taken to mitigate the same.")
                    },
                    "7": {
                        "question": "Percentage of recycled or reused input material to total material (by value) used in production (for manufacturing industry) or providing services (for service industry)",
                        "answer": extract_answer(text, "Percentage of recycled or reused input material to total material (by value) used in production (for manufacturing industry) or providing services (for service industry)")
                    },
                    "8": {
                        "question": " Of the products and packaging reclaimed at end of life of products, amount (in metric tonnes) reused, recycled, and safely disposed, as per the following format:",
                        "answer": extract_answer(text, " Of the products and packaging reclaimed at end of life of products, amount (in metric tonnes) reused, recycled, and safely disposed, as per the following format:")
                    },
                    "9": {
                        "question": "Reclaimed products and their packaging materials (as percentage of products sold) for each product category.",
                        "answer": extract_answer(text, "Reclaimed products and their packaging materials (as percentage of products sold) for each product category.")
                    },
                    
                }
            },
            "three": {
                "subtitle": "Principle 3 : Businesses should respect and promote the well-being of all employees, including",
                "questions": {
                    "1": {
                        "mainquestion":"Details of measures "
                    },
                    "1.a": {
                        "question": "Details of measures for the well-being of employees:",
                        "answer": extract_answer(text, "Details of measures for the well-being of employees:")
                    },
                    "1.b": {
                        "question": "Details of measures for the well-being of workers:",
                        "answer": extract_answer(text, "Details of measures for the well-being of workers:")
                    },
                    "1.c": {
                        "question": " Spending on measures towards well-being of employees and workers (including permanent and other than permanent) in the following format –",
                        "answer": extract_answer(text, " Spending on measures towards well-being of employees and workers (including permanent and other than permanent) in the following format –")
                    },
                    "2": {
                        "question": "Details of retirement benefits, for Current and Previous FY",
                        "answer": extract_answer(text, "Details of retirement benefits, for Current and Previous FY")
                    },
                    "3": {
                        "question": " Accessibility of workplaces",
                        "answer": extract_answer(text, " Accessibility of workplaces")
                    },
                    "4": {
                        "question": " Does the entity have an equal opportunity policy as per the Rights of Persons with Disabilities Act, 2016? If so, provide a web-link to the policy.",
                        "answer": extract_answer(text, " Does the entity have an equal opportunity policy as per the Rights of Persons with Disabilities Act, 2016? If so, provide a web-link to the policy.")
                    },
                    "5": {
                        "question": " Return to work and Retention rates of permanent employees and workers that took parental leave.",
                        "answer": extract_answer(text, " Return to work and Retention rates of permanent employees and workers that took parental leave.")
                    },
                    "6": {
                        "question": " Is there a mechanism available to receive and redress grievances for the following categories of employees and worker? If yes, give details of the mechanism in brief",
                        "answer": extract_answer(text, " Is there a mechanism available to receive and redress grievances for the following categories of employees and worker? If yes, give details of the mechanism in brief")
                    },
                    "7": {
                        "question": " Membership of employees and worker in association(s) or Unions recognised by the listed entity:",
                        "answer": extract_answer(text, " Membership of employees and worker in association(s) or Unions recognised by the listed entity:")
                    },
                    "8": {
                        "question": " Details of training given to employees and workers:",
                        "answer": extract_answer(text, " Details of training given to employees and workers:")
                    },
                    "9": {
                        "question": "Details of performance and career development reviews of employees and workers",
                        "answer": extract_answer(text, "Details of performance and career development reviews of employees and workers")
                    },
                    "10": {
                        "mainquestion":"Health and safety management system:"
                    },
                    "10.a": {
                        "question": "Whether an occupational health and safety management system has been implemented by the entity? (Yes/ No). If yes, the coverage such system?",
                        "answer": extract_answer(text, " Whether an occupational health and safety management system has been implemented by the entity? (Yes/ No). If yes, the coverage such system?")
                    },
                    "10.b": {
                        "question": " What are the processes used to identify work-related hazards and assess risks on a routine and non-routine basis by the entity?",
                        "answer": extract_answer(text, " What are the processes used to identify work-related hazards and assess risks on a routine and non-routine basis by the entity?")
                    },
                    "10.c": {
                        "question": " c. Whether you have processes for workers to report the work related hazards and to remove themselves from such risks. (Y/N)",
                        "answer": extract_answer(text, " c. Whether you have processes for workers to report the work related hazards and to remove themselves from such risks. (Y/N)")
                    },
                    "10.d": {
                        "question": " Do the employees/ worker of the entity have access to non-occupational medical and healthcare services? (Yes/ No)",
                        "answer": extract_answer(text, " Do the employees/ worker of the entity have access to non-occupational medical and healthcare services? (Yes/ No)")
                    },
                    "11": {
                        "question": "Details of safety related incidents, in the following format:",
                        "answer": extract_answer(text, "Details of safety related incidents, in the following format:")
                    },
                    "12": {
                        "question": " Describe the measures taken by the entity to ensure a safe and healthy work place",
                        "answer": extract_answer(text, " Describe the measures taken by the entity to ensure a safe and healthy work place")
                    },
                    "13": {
                        "question": "Number of Complaints on the following made by employees and workers:",
                        "answer": extract_answer(text, "Number of Complaints on the following made by employees and workers:")
                    },
                    "14": {
                        "question": " Assessments for the year:",
                        "answer": extract_answer(text, " Assessments for the year:")
                    },
                    "15": {
                        "question": ". Provide details of any corrective action taken or underway to address safety-related incidents (if any) and on significant risks / concerns arising from assessments of health & safety practices and working conditions.",
                        "answer": extract_answer(text, ". Provide details of any corrective action taken or underway to address safety-related incidents (if any) and on significant risks / concerns arising from assessments of health & safety practices and working conditions.")
                    },
                    "16": {
                        "mainquestion":" Does the entity extend any life insurance or any compensatory package in the event of death of (A) Employees (Y/N)"
                    },
                    "16.a": {
                        "question": " (A) Employees (Y/N)",
                        "answer": extract_answer(text, " (A) Employees (Y/N)")
                    },
                    
                    "16.b": {
                        "question": " (B) Workers (Y/N)",
                        "answer": extract_answer(text, " (B) Workers (Y/N)")
                    },
                    "17": {
                        "question": " Provide the measures undertaken by the entity to ensure that statutory dues have been deducted and deposited by the value chain partners",
                        "answer": extract_answer(text, " Provide the measures undertaken by the entity to ensure that statutory dues have been deducted and deposited by the value chain partners")
                    },
                    "18": {
                        "question": " Provide the number of employees / workers having suffered high consequence work-related injury / ill-health / fatalities (as reported in Q11 of Essential Indicators above), who have been are rehabilitated and placed in suitable employment or whose family members have been placed in suitable employment:",
                        "answer": extract_answer(text, " Provide the number of employees / workers having suffered high consequence work-related injury / ill-health / fatalities (as reported in Q11 of Essential Indicators above), who have been are rehabilitated and placed in suitable employment or whose family members have been placed in suitable employment:")
                    },
                    "19": {
                        "question": "Does the entity provide transition assistance programs to facilitate continued employability and the management of career endings resulting from retirement or termination of employment? (Yes/ No)",
                        "answer": extract_answer(text, "Does the entity provide transition assistance programs to facilitate continued employability and the management of career endings resulting from retirement or termination of employment? (Yes/ No)")
                    },
                    "20": {
                        "question": " Details on assessment of value chain partners:",
                        "answer": extract_answer(text, " Details on assessment of value chain partners:")
                    },
                    "21": {
                        "question": "Provide details of any corrective actions taken or underway to address significant risks / concerns arising from assessments of health and safety practices and working conditions of value chain partners.",
                        "answer": extract_answer(text, "Provide details of any corrective actions taken or underway to address significant risks / concerns arising from assessments of health and safety practices and working conditions of value chain partners.")
                    },
                }
            },
            
            "four": {
                "subtitle": "Principle 4 : Businesses should respect the interests of and be responsive to all its stakeholders",
                "questions": {
                    "1": {
                        "question": "Describe the processes for identifying key stakeholder groups of the entity.",
                        "answer": extract_answer(text, "Describe the processes for identifying key stakeholder groups of the entity.")
                    },
                    "2": {
                        "question": "List stakeholder groups identified as key for your entity and the frequency of engagement with each stakeholder group.",
                        "answer": extract_answer(text, "List stakeholder groups identified as key for your entity and the frequency of engagement with each stakeholder group.")
                    },
                    "3": {
                        "question": "Provide the processes for consultation between stakeholders and the Board on economic, environmental, and social topics or if consultation is delegated, how is feedback from such consultations provided to the Board.",
                        "answer": extract_answer(text, "Provide the processes for consultation between stakeholders and the Board on economic, environmental, and social topics or if consultation is delegated, how is feedback from such consultations provided to the Board.")
                    },
                    "4": {
                        "question": "Whether stakeholder consultation is used to support the identification and management of environmental, and social topics (Yes / No). If so, provide details of instances as to how the inputs received from stakeholders on these topics were incorporated into policies and activities of the entity",
                        "answer": extract_answer(text, "Whether stakeholder consultation is used to support the identification and management of environmental, and social topics (Yes / No). If so, provide details of instances as to how the inputs received from stakeholders on these topics were incorporated into policies and activities of the entity")
                    },
                    "5": {
                        "question": " Provide details of instances of engagement with, and actions taken to, address the concerns of vulnerable/ marginalized stakeholder groups.",
                        "answer": extract_answer(text, " Provide details of instances of engagement with, and actions taken to, address the concerns of vulnerable/ marginalized stakeholder groups.")
                    },
                }
            },
            
            "five": {
                "subtitle": "Principle 5 : Businesses should respect and promote human rights",
                "questions": {
                    "1": {
                        "question": "Employees and workers who have been provided training on human rights issues and policy(ies) of the entity, in the following format:",
                        "answer": extract_answer(text, "Employees and workers who have been provided training on human rights issues and policy(ies) of the entity, in the following format:")
                    },
                    "2": {
                        "question": "Details of minimum wages paid to employees and workers, in the following format:",
                        "answer": extract_answer(text, "Details of minimum wages paid to employees and workers, in the following format:")
                    },
                    
                    "3": {
                        "mainquestion":" Details of remuneration/salary/wages"
                    },
                    "3.a": {
                        "question": " Median remuneration / wages:",
                        "answer": extract_answer(text, " Median remuneration / wages:")
                    },
                    "3.b": {
                        "question": "Gross wages paid to females as % of total wages paid by the entity, in the following format:",
                        "answer": extract_answer(text, "Gross wages paid to females as % of total wages paid by the entity, in the following format:")
                    },                    
                    "4": {
                        "question": "Do you have a focal point (Individual/ Committee) responsible for addressing human rights impacts or issues caused or contributed to by the business? (Yes/ No)",
                        "answer": extract_answer(text, "Do you have a focal point (Individual/ Committee) responsible for addressing human rights impacts or issues caused or contributed to by the business? (Yes/ No)")
                    },
                    
                    "5": {
                        "question": "Describe the internal mechanisms in place to redress grievances related to human rights issues.",
                        "answer": extract_answer(text, "Describe the internal mechanisms in place to redress grievances related to human rights issues.")
                    },
                    
                    "6": {
                        "question": "Number of Complaints on the following made by employees and workers:",
                        "answer": extract_answer(text, "Number of Complaints on the following made by employees and workers:")
                    },
                    
                    "7": {
                        "question": "Complaints filed under the Sexual Harassment of Women at Workplace (Prevention, Prohibition and Redressal) Act, 2013, in the following format:",
                        "answer": extract_answer(text, "Complaints filed under the Sexual Harassment of Women at Workplace (Prevention, Prohibition and Redressal) Act, 2013, in the following format:")
                    },
                    
                    "8": {
                        "question": "Mechanisms to prevent adverse consequences to the complainant in discrimination and harassment cases.",
                        "answer": extract_answer(text, "Mechanisms to prevent adverse consequences to the complainant in discrimination and harassment cases.")
                    },
                    
                    "9": {
                        "question": "Do human rights requirements form part of your business agreements and contracts? (Yes/ No)",
                        "answer": extract_answer(text, "Do human rights requirements form part of your business agreements and contracts? (Yes/ No)")
                    },
                    
                    "10": {
                        "question": " Assessments for the year:",
                        "answer": extract_answer(text, " Assessments for the year:")
                    },
                    
                    "11": {
                        "question": " Provide details of any corrective actions taken or underway to address significant risks / concerns arising from the assessments at Question 10 above.",
                        "answer": extract_answer(text, " Provide details of any corrective actions taken or underway to address significant risks / concerns arising from the assessments at Question 10 above.")
                    },
                    
                    "12": {
                        "question": " Details of a business process being modified / introduced as a result of addressing human rights grievances/complaints.",
                        "answer": extract_answer(text, " Details of a business process being modified / introduced as a result of addressing human rights grievances/complaints.")
                    },
                    
                    "13": {
                        "question": "Details of the scope and coverage of any Human rights due-diligence conducted",
                        "answer": extract_answer(text, "Details of the scope and coverage of any Human rights due-diligence conducted")
                    },
                    
                    "14": {
                        "question": " Is the premise/office of the entity accessible to differently abled visitors, as per the requirements of the Rights of Persons with Disabilities Act, 2016?",
                        "answer": extract_answer(text, " Is the premise/office of the entity accessible to differently abled visitors, as per the requirements of the Rights of Persons with Disabilities Act, 2016?")
                    },
                    
                    "15": {
                        "question": "Details on assessment of value chain partners:",
                        "answer": extract_answer(text, "Details on assessment of value chain partners:")
                    },
                    
                    "16": {
                        "question": "Provide details of any corrective actions taken or underway to address significant risks / concerns arising from the assessments at Question 4 above.",
                        "answer": extract_answer(text, "Provide details of any corrective actions taken or underway to address significant risks / concerns arising from the assessments at Question 4 above.")
                    },
                    
                    
                }
            },
            
            "six": {
                "subtitle": "Principle 6 : Businesses should respect and make efforts to protect and restore the environment",
                "questions": {
                    "1": {
                        "question": "Details of total energy consumption (in Joules or multiples) and energy intensity, in the following format:",
                        "answer": extract_answer(text, "Details of total energy consumption (in Joules or multiples) and energy intensity, in the following format:")
                    },
                    "2": {
                    "question": "Does the entity have any sites / facilities identified as designated consumers (DCs) under the Performance, Achieve and Trade (PAT) Scheme of the Government of India? (Y/N) If yes, disclose whether targets set under the PAT scheme have been achieved. In case targets have not been achieved, provide the remedial action taken, if any.",
                    "answer": extract_answer(text, "Does the entity have any sites / facilities identified as designated consumers (DCs) under the Performance, Achieve and Trade (PAT) Scheme of the Government of India? (Y/N) If yes, disclose whether targets set under the PAT scheme have been achieved. In case targets have not been achieved, provide the remedial action taken, if any.")
                    },
                    "3": {
                    "question": "Provide details of the following disclosures related to water, in the following format:",
                    "answer": extract_answer(text, "Provide details of the following disclosures related to water, in the following format:")
                    },

                    "4": {
                    "question": "Provide the following details related to water discharged:",
                    "answer": extract_answer(text, "Provide the following details related to water discharged:")
                    },

                    "5": {
                    "question": "Has the entity implemented a mechanism for Zero Liquid Discharge? If yes, provide details of its coverage and implementation",
                    "answer": extract_answer(text, "Has the entity implemented a mechanism for Zero Liquid Discharge? If yes, provide details of its coverage and implementation")
                    },

                    "6": {
                    "question": "Please provide details of air emissions (other than GHG emissions) by the entity, in the following format:",
                    "answer": extract_answer(text, "Please provide details of air emissions (other than GHG emissions) by the entity, in the following format:")
                    },

                    "7": {
                    "question": "Provide details of greenhouse gas emissions (Scope 1 and Scope 2 emissions) & its intensity, in the following format:",
                    "answer": extract_answer(text, "Provide details of greenhouse gas emissions (Scope 1 and Scope 2 emissions) & its intensity, in the following format:")
                    },

                    "8": {
                    "question": "Provide details of greenhouse gas emissions (Scope 1 and Scope 2 emissions) & its intensity, in the following format:",
                    "answer": extract_answer(text, "Provide details of greenhouse gas emissions (Scope 1 and Scope 2 emissions) & its intensity, in the following format:")
                    },

                    "9": {
                    "question": "Provide details related to waste management by the entity, in the following format:",
                    "answer": extract_answer(text, "Provide details related to waste management by the entity, in the following format:")
                    },

                    "10": {
                    "question": "Briefly describe the waste management practices adopted in your establishments. Describe the strategy adopted by your company to reduce usage of hazardous and toxic chemicals in your products and processes and the practices adopted to manage such wastes.",
                    "answer": extract_answer(text, "Briefly describe the waste management practices adopted in your establishments. Describe the strategy adopted by your company to reduce usage of hazardous and toxic chemicals in your products and processes and the practices adopted to manage such wastes.")
                    },

                    "11": {
                    "question": "If the entity has operations/offices in/around ecologically sensitive areas (such as national parks, wildlife sanctuaries, biosphere reserves, wetlands, biodiversity hotspots, forests, coastal regulation zones etc.) where environmental approvals / clearances are required, please specify details in the following format:",
                    "answer": extract_answer(text, "If the entity has operations/offices in/around ecologically sensitive areas (such as national parks, wildlife sanctuaries, biosphere reserves, wetlands, biodiversity hotspots, forests, coastal regulation zones etc.) where environmental approvals / clearances are required, please specify details in the following format:")
                    },

                    "12": {
                    "question": "Details of environmental impact assessments of projects undertaken by the entity based on applicable laws, in the current financial year:",
                    "answer": extract_answer(text, "Details of environmental impact assessments of projects undertaken by the entity based on applicable laws, in the current financial year:")
                    },

                    "13": {
                    "question": "Is the entity compliant with the applicable environmental law/ regulations/ guidelines in India; such as the Water (Prevention and Control of Pollution) Act, Air (Prevention and Control of Pollution) Act, Environment protection act and rules thereunder (Y/N). If not, provide details of all such non-compliances, in the following format:",
                    "answer": extract_answer(text, "Is the entity compliant with the applicable environmental law/ regulations/ guidelines in India; such as the Water (Prevention and Control of Pollution) Act, Air (Prevention and Control of Pollution) Act, Environment protection act and rules thereunder (Y/N). If not, provide details of all such non-compliances, in the following format:")
                    },

                    "14": {
                    "question": "Water withdrawal, consumption and discharge in areas of water stress (in kilolitres):",
                    "answer": extract_answer(text, "Water withdrawal, consumption and discharge in areas of water stress (in kilolitres):")
                    },

                    "15": {
                    "question": "Please provide details of total Scope 3 emissions & its intensity, in the following format",
                    "answer": extract_answer(text, "Please provide details of total Scope 3 emissions & its intensity, in the following format")

                        },
                    "15.a": {
                    "question": "Please provide details of total Scope 3 emissions & its intensity, in the following format",
                    "answer": extract_answer(text, "Please provide details of total Scope 3 emissions & its intensity, in the following format")
                    },
                                        
                    "16": {
                    "question": "With respect to the ecologically sensitive areas reported at Question 10 of Essential Indicators above, provide details of significant direct & indirect impact of the entity on biodiversity in such areas along-with prevention and remediation activities",
                    "answer": extract_answer(text, "With respect to the ecologically sensitive areas reported at Question 10 of Essential Indicators above, provide details of significant direct & indirect impact of the entity on biodiversity in such areas along-with prevention and remediation activities")
                    },

                    "17": {
                    "question": "If the entity has undertaken any specific initiatives or used innovative technology or solutions to improve resource efficiency, or reduce impact due to emissions / effluent discharge / waste generated, please provide details of the same as well as outcome of such initiatives, as per the following format:",
                    "answer": extract_answer(text, "If the entity has undertaken any specific initiatives or used innovative technology or solutions to improve resource efficiency, or reduce impact due to emissions / effluent discharge / waste generated, please provide details of the same as well as outcome of such initiatives, as per the following format:")
                    },

                    "18": {
                    "question": "Does the entity have a business continuity and disaster management plan? Give details in 100 words/ web link.",
                    "answer": extract_answer(text, "Does the entity have a business continuity and disaster management plan? Give details in 100 words/ web link.")
                    },

                    "19": {
                    "question": "Disclose any significant adverse impact to the environment, arising from the value chain of the entity. What mitigation or adaptation measures have been taken by the entity in this regard.",
                    "answer": extract_answer(text, "Disclose any significant adverse impact to the environment, arising from the value chain of the entity. What mitigation or adaptation measures have been taken by the entity in this regard.")
                    },

                    "20": {
                    "question": "Percentage of value chain partners (by value of business done with such partners) that were assessed for environmental impacts.",
                    "answer": extract_answer(text, "Percentage of value chain partners (by value of business done with such partners) that were assessed for environmental impacts.")
                    },

                    "21": {
                    "question": "How many Green Credits have been generated or procured:",
                    "answer": extract_answer(text, "How many Green Credits have been generated or procured:")
                    },

                    "21.a": {
                    "question": "By the listed entity",
                    "answer": extract_answer(text, "By the listed entity")
                    },

                    "22.b": {
                    "question": "By the top ten (in terms of value of purchases and sales,respectively) value chain partners”",
                    "answer": extract_answer(text, "By the top ten (in terms of value of purchases and sales,respectively) value chain partners”")
                    },


                }
            },
            
            "seven": {
                "subtitle": "Principle 7 : Businesses, when engaging in influencing public and regulatory policy, should do so in a manner that is responsible and transparent",
                "questions": {
                    "1": {
                        "mainquestion":"Trade and industry"
                    },
                    "1.a": {
                        "question": "Number of affiliations with trade and industry chambers/ associations.",
                        "answer": extract_answer(text, "Number of affiliations with trade and industry chambers/ associations.")
                    },
                    "1.b": {
                        "question": "List the top 10 trade and industry chambers/ associations (determined based on the total members of such body) the entity is a member of/ affiliated to, in the following format",
                        "answer": extract_answer(text, "List the top 10 trade and industry chambers/ associations (determined based on the total members of such body) the entity is a member of/ affiliated to, in the following format")
                    },
                    "2": {
                        "question": "Provide details of corrective action taken or underway on any issues related to anti-competitive conduct by the entity, based on adverse orders from regulatory authorities.",
                        "answer": extract_answer(text, "Provide details of corrective action taken or underway on any issues related to anti-competitive conduct by the entity, based on adverse orders from regulatory authorities.")
                    },
                    "3": {
                        "question": "Details of public policy positions advocated by the entity:",
                        "answer": extract_answer(text, "Details of public policy positions advocated by the entity:")
                    },
                }
            },
            
            "eight": {
                "subtitle": "Principle 8 : Businesses should promote inclusive growth and equitable development",
                "questions": {
                    "1": {
                        "question": "Details of Social Impact Assessments (SIA) of projects undertaken by the entity based on applicable laws, in the current financial year.",
                        "answer": extract_answer(text, "Details of Social Impact Assessments (SIA) of projects undertaken by the entity based on applicable laws, in the current financial year.")
                    },
                    "2": {
                        "question": "Provide information on project(s) for which ongoing Rehabilitation and Resettlement (R&R) is being undertaken by your entity, in the following format",
                        "answer": extract_answer(text, "Provide information on project(s) for which ongoing Rehabilitation and Resettlement (R&R) is being undertaken by your entity, in the following formatProvide information on project(s) for which ongoing Rehabilitation and Resettlement (R&R) is being undertaken by your entity, in the following format")
                    },
                    "3": {
                        "question": "Describe the mechanisms to receive and redress grievances of the community.",
                        "answer": extract_answer(text, "Describe the mechanisms to receive and redress grievances of the community.")
                    },
                    "4": {
                        "question": "Percentage of input material (inputs to total inputs by value) sourced from suppliers",
                        "answer": extract_answer(text, "Percentage of input material (inputs to total inputs by value) sourced from suppliers")
                    },
                    "5": {
                        "question": "Job creation in smaller towns – Disclose wages paid to persons employed (including employees or workers employed on a permanent or non-permanent / on contract basis) in the following locations, as % of total wage cost",
                        "answer": extract_answer(text, "Job creation in smaller towns – Disclose wages paid to persons employed (including employees or workers employed on a permanent or non-permanent / on contract basis) in the following locations, as % of total wage cost")
                    },
                    "6": {
                        "question": "Provide details of actions taken to mitigate any negative social impacts identified in the Social Impact Assessments (Reference: Question 1 of Essential Indicators above):",
                        "answer": extract_answer(text, "Provide details of actions taken to mitigate any negative social impacts identified in the Social Impact Assessments (Reference: Question 1 of Essential Indicators above):")
                    },
                    "7": {
                        "question": "Provide the following information on CSR projects undertaken by your entity in designated aspirational districts as identified by government bodies",
                        "answer": extract_answer(text, "Provide the following information on CSR projects undertaken by your entity in designated aspirational districts as identified by government bodies")
                    },
                    "8": {
                        "question": "Do you have a preferential procurement policy where you give preference to purchase from suppliers comprising marginalized /vulnerable groups? (Yes/No)",
                        "answer": extract_answer(text, "Do you have a preferential procurement policy where you give preference to purchase from suppliers comprising marginalized /vulnerable groups? (Yes/No)")
                    },
                    "8.a": {
                        "question": "From which marginalized /vulnerable groups do you procure?",
                        "answer": extract_answer(text, "From which marginalized /vulnerable groups do you procure?")
                    },
                    "8.b": {
                        "question": "What percentage of total procurement (by value) does it constitute?",
                        "answer": extract_answer(text, "What percentage of total procurement (by value) does it constitute?")
                    },
                    "9": {
                        "question": "Details of the benefits derived and shared from the intellectual properties owned or acquired by your entity (in the current financial year), based on traditional knowledge:",
                        "answer": extract_answer(text, "Details of the benefits derived and shared from the intellectual properties owned or acquired by your entity (in the current financial year), based on traditional knowledge:")
                    },
                    "10": {
                        "question": "Details of corrective actions taken or underway, based on any adverse order in intellectual property related disputes wherein usage of traditional knowledge is involved.",
                        "answer": extract_answer(text, "Details of corrective actions taken or underway, based on any adverse order in intellectual property related disputes wherein usage of traditional knowledge is involved.")
                    },
                    "11": {
                        "question": "Details of beneficiaries of CSR Projects:",
                        "answer": extract_answer(text, "Details of beneficiaries of CSR Projects:")
                    },
                }
            },
            
            "nine": {
                "subtitle": "Principle 9 : Businesses should engage with and provide value to their consumers in a responsible manner",
                "questions": {
                    "1": {
                        "mainquestion":"Describe the mechanisms in place to receive and respond to consumer complaints and feedback."
                    },
                    "1.a": {
                    "question": "Turnover of products and/ services as a percentage of turnover from all products/service that carry information about:",
                    "answer": extract_answer(text, "Turnover of products and/ services as a percentage of turnover from all products/service that carry information about:")
                    },
                    "2": {
                    "question": "Number of consumer complaints in respect of the following:",
                    "answer": extract_answer(text, "Number of consumer complaints in respect of the following:")
                    },

                    "3": {
                    "question": "Details of instances of product recalls on account of safety issues:",
                    "answer": extract_answer(text, "Details of instances of product recalls on account of safety issues:")
                    },

                    "4": {
                    "question": "Does the entity have a framework/policy on cyber security and risks related to data privacy? (Yes/No). If available, provide weblink of the policy.",
                    "answer": extract_answer(text, "Does the entity have a framework/policy on cyber security and risks related to data privacy? (Yes/No). If available, provide weblink of the policy.")
                    },

                    "5": {
                    "question": "Provide details of any corrective actions taken or underway on issues relating to advertising, and delivery of essential services; cyber security and data privacy of customers; re-occurrence of instances of product recalls; penalty / action taken by regulatory authorities on safety of products / services.",
                    "answer": extract_answer(text, "Provide details of any corrective actions taken or underway on issues relating to advertising, and delivery of essential services; cyber security and data privacy of customers; re-occurrence of instances of product recalls; penalty / action taken by regulatory authorities on safety of products / services.")
                    },

                    "6": {
                    "question": "Provide the following information relating to data breaches:",
                    "answer": extract_answer(text, "Provide the following information relating to data breaches:")
                    },

                    "7": {
                    "question": "Channels / platforms where information on products and services of the entity can be accessed (provide web link, if available).",
                    "answer": extract_answer(text, "Channels / platforms where information on products and services of the entity can be accessed (provide web link, if available).")
                    },

                    "8": {
                    "question": "Steps taken to inform and educate consumers about safe and responsible usage of products and/or services.",
                    "answer": extract_answer(text, "Steps taken to inform and educate consumers about safe and responsible usage of products and/or services.")
                    },

                    "9": {
                    "question": "Mechanisms in place to inform consumers of any risk of disruption/discontinuation of essential services.",
                    "answer": extract_answer(text, "Mechanisms in place to inform consumers of any risk of disruption/discontinuation of essential services.")
                    },
                    "10": {
                    "question": "Does the entity display product information on the product over and above what is mandated as per local laws? (Yes/No/Not Applicable) If yes, provide details in brief. Did your entity carry out any survey with regard to consumer satisfaction relating to the major products / services of the entity, significant locations of operation of the entity or the entity as a whole? (Yes/No)",
                    "answer": extract_answer(text, "Does the entity display product information on the product over and above what is mandated as per local laws? (Yes/No/Not Applicable) If yes, provide details in brief. Did your entity carry out any survey with regard to consumer satisfaction relating to the major products / services of the entity, significant locations of operation of the entity or the entity as a whole? (Yes/No)")
                    },

                    "11": {
                    "question": "Provide the following information relating to data breaches:",
                    "answer": extract_answer(text, "Provide the following information relating to data breaches:")
                    },
                    "11.a": {
                    "question": "Number of instances of data breaches along-with impact",
                    "answer": extract_answer(text, "Number of instances of data breaches along-with impact")
                    },
                    "11.b": {
                    "question": "Percentage of data breaches involving personally identifiable information of customers",
                    "answer": extract_answer(text, "Percentage of data breaches involving personally identifiable information of customers")
                    },

                }
            },
            
        }
    
    
    }


