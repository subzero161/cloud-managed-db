# cloud-managed-db
Assignment 6, HHA 504, AHI, SBU


Assignment 6 - Cloud Managed SQL + ERDs + Dummy Data


1. Create a cloud-managed MySQL DB on either Azure or GCP

2. Create a new database inside of that mysql instance called patient_portal  

3. Create a python script called (sql_table_creation.py) that creates the following tables inside of patient_portal: patients, medications, treatments_procedures, conditions, and social determinants. Be sure to use a .env file to hide your login credentials 

4. Create a python script called (sql_dummy_data.py) using python and send some dummy data into each of the tables. Please see notes for ideas related to dummy data. 

5. Create an ERD for your DB design using MySQL Work Bench. You must have at least two foreignKeys representing a relationship between at least 2 tables. 

6. Github docs to include: 
- a python script that contains the SQL code to create db (sql_table_creation.py) 
- a python script that contains code to insert in some dummy data (sql_dummy_data.py) 
- a readme file that describes a) where you setup the mySQL db, b) any issues you ran into 
- a images folder that contains: 
    - screen shot of a ERD of your proposed setup (use either popSQL or mysql work bench) 
    - screen shots of you connected to the sql server, performing the following queries: 
        - Query1: show databases (e.g., show databases;) 
        - Query2: all of the tables from your database (e.g., show tables;)  
        - Query3: select * from patient_portal.medications 
        - Query4: select * from patient_portal.treatment_procedures
        - Query5: select * from patient_portal.conditions

Be CREATE with your dummy data and find examples that are from real-world codexes: 

    Medications: NDC codes
    Treatments/Procedures: CPT 
    Conditions: ICD10 codes
    Social_Determinants: LOINC codes 


Resources to pull some test data: 
NDC: https://dailymed.nlm.nih.gov/dailymed/index.cfm 
CPT: https://www.aapc.com/codes/cpt-codes-range/
ICD: https://icdcodelookup.com/icd-10/codes
LOINC: https://www.findacode.com/loinc/LG41762-2--socialdeterminantsofhealth.html

REAL CPT Values that are older: https://gist.github.com/lieldulev/439793dc3c5a6613b661c33d71fdd185
