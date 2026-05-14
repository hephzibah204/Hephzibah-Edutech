import os

dir_path = r'c:\Users\Abiodun Emmanuel\Documents\CODEBASE\hephzibah-edutech-updated'
whatsapp_html = '\n<!-- FLOATING WHATSAPP BUTTON -->\n<a href="https://wa.me/2349077780156" class="floating-whatsapp" target="_blank" rel="noopener noreferrer" aria-label="Chat with us on WhatsApp">✆</a>\n'

for filename in os.listdir(dir_path):
    if filename.endswith('.html'):
        filepath = os.path.join(dir_path, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if 'class="floating-whatsapp"' in content:
            continue # Skip if already exists
            
        if '</body>' in content:
            new_content = content.replace('</body>', whatsapp_html + '</body>')
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f'Injected WhatsApp button into {filename}')
