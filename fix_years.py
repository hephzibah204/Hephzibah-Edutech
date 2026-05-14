import os
import re

dir_path = r'c:\Users\Abiodun Emmanuel\Documents\CODEBASE\hephzibah-edutech-updated'

# Patterns to replace
replacements = {
    '2025': '2026',
    'January 2025': 'May 2026',
    'February 2025': 'May 2026',
    '📅 January 2025': '📅 May 2026',
    '📅 February 2025': '📅 May 2026',
    '2025-01-01': '2026-05-14',
    '2025-01-15': '2026-05-14',
    '2025-02-10': '2026-05-14',
    '2025-02-15': '2026-05-14',
    '2025-02-20': '2026-05-14',
}

for filename in os.listdir(dir_path):
    if filename.endswith('.html') or filename.endswith('.xml'):
        filepath = os.path.join(dir_path, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        new_content = content
        for old, new in replacements.items():
            new_content = new_content.replace(old, new)
        
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f'Updated {filename}')
