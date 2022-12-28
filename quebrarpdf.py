import pikepdf 
from tqdm import tqdm 
passwords = [] 
password_text_file = "Password Text File"
for line in open(password_text_file): 
    passwords.append(line.strip()) 
      
for password in tqdm(passwords, "Cracking PDF File"): 
    try: 
      
        with pikepdf.open("Protected PDF File", password = password) as p: 
            print("[+] Password found:", password) 
            break
              
    
    except pikepdf._qpdf.PasswordError as e: 
      
        continue