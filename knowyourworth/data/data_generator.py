import numpy as np
import pandas as pd

def generate_sample_data():
    np.random.seed(42)
    roles = ['Software Engineer', 'Data Scientist', 'Product Manager', 'UX Designer']
    companies = ['Tech Giants', 'Startups', 'Enterprise', 'Consulting']
    locations = ['SF Bay Area', 'New York', 'London', 'Remote']
    levels = ['Junior', 'Mid', 'Senior', 'Lead', 'Principal']
    
    data = []
    for _ in range(1000):
        role = np.random.choice(roles)
        level = np.random.choice(levels)
        company_type = np.random.choice(companies)
        location = np.random.choice(locations)
        years_exp = np.random.randint(0, 15)
        
        base_multiplier = {
            'Software Engineer': 100000,
            'Data Scientist': 95000,
            'Product Manager': 110000,
            'UX Designer': 90000
        }
        
        level_multiplier = {
            'Junior': 0.7,
            'Mid': 1.0,
            'Senior': 1.3,
            'Lead': 1.6,
            'Principal': 2.0
        }
        
        location_multiplier = {
            'SF Bay Area': 1.3,
            'New York': 1.2,
            'London': 1.1,
            'Remote': 1.0
        }
        
        base_salary = (
            base_multiplier[role] * 
            level_multiplier[level] * 
            location_multiplier[location] * 
            (1 + years_exp * 0.05)
        )
        
        bonus = base_salary * np.random.uniform(0.05, 0.20)
        equity = base_salary * np.random.uniform(0.10, 0.40)
        
        data.append({
            'Role': role,
            'Level': level,
            'Company_Type': company_type,
            'Location': location,
            'Years_Experience': years_exp,
            'Base_Salary': base_salary,
            'Bonus': bonus,
            'Equity': equity,
            'Total_Compensation': base_salary + bonus + equity
        })
    
    return pd.DataFrame(data)