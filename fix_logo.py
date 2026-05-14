import os

dir_path = r'c:\Users\Abiodun Emmanuel\Documents\CODEBASE\hephzibah-edutech-updated'

nav_old = '<a href="index.html" class="nav-logo"><img src="logo.jpg" alt="Hephzibah Edutech Logo" style="height:34px;width:auto;border-radius:4px;">Hephzibah <span>Edutech</span></a>'
nav_new = '<a href="index.html" class="nav-logo"><img src="images/logo.jpg" alt="Hephzibah Edutech Logo" style="height:34px;width:auto;border-radius:4px;"></a>'

footer_old = '<div class="footer-brand-logo"><img src="logo.jpg" alt="Hephzibah Edutech Logo" style="height:34px;width:auto;border-radius:4px;">Hephzibah <span>Edutech</span></div>'
footer_new = '<div class="footer-brand-logo"><img src="images/logo.jpg" alt="Hephzibah Edutech Logo" style="height:34px;width:auto;border-radius:4px;"></div>'

for filename in os.listdir(dir_path):
    if filename.endswith('.html'):
        filepath = os.path.join(dir_path, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        new_content = content.replace(nav_old, nav_new).replace(footer_old, footer_new)
        
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f'Updated {filename}')
