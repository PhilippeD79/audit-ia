# Script pour ajouter le lien Charte dans la navigation
import os

files_to_update = [
    'C:\\Users\\phili\\Documents\\audit-ia\\index.html',
    'C:\\Users\\phili\\Documents\\audit-ia\\fondements.html',
    'C:\\Users\\phili\\Documents\\audit-ia\\sequence-1.html',
    'C:\\Users\\phili\\Documents\\audit-ia\\sequence-2.html',
    'C:\\Users\\phili\\Documents\\audit-ia\\sequence-3.html',
    'C:\\Users\\phili\\Documents\\audit-ia\\sequence-4.html'
]

# Pour index.html (ancres)
def update_index(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    old_nav = '''            <ul>
                <li><a href="#protocole">Séquences</a></li>
                <li><a href="#cas-ecole">Cas d'école</a></li>
                <li><a href="#fondements">Fondements</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>'''
    
    new_nav = '''            <ul>
                <li><a href="#protocole">Séquences</a></li>
                <li><a href="#cas-ecole">Cas d'école</a></li>
                <li><a href="#fondements">Fondements</a></li>
                <li><a href="charte.html">Charte</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>'''
    
    if old_nav in content:
        content = content.replace(old_nav, new_nav)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

# Pour les autres pages (liens vers fichiers)
def update_other_pages(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Chercher la navigation avec Fondements
    old_patterns = [
        '<li><a href="fondements.html">Fondements</a></li>',
        '<li><a href="../fondements.html">Fondements</a></li>'
    ]
    
    for old_pattern in old_patterns:
        if old_pattern in content:
            # Ajouter Charte après Fondements
            new_pattern = old_pattern + '\n                <li><a href="charte.html">Charte</a></li>'
            content = content.replace(old_pattern, new_pattern)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
    return False

# Mettre à jour tous les fichiers
for filepath in files_to_update:
    if not os.path.exists(filepath):
        print(f"[SKIP] {os.path.basename(filepath)} - fichier non trouve")
        continue
    
    if 'index.html' in filepath:
        if update_index(filepath):
            print(f"[OK] {os.path.basename(filepath)} - navigation mise a jour")
        else:
            print(f"[WARN] {os.path.basename(filepath)} - pattern non trouve")
    else:
        if update_other_pages(filepath):
            print(f"[OK] {os.path.basename(filepath)} - navigation mise a jour")
        else:
            print(f"[WARN] {os.path.basename(filepath)} - pattern non trouve")

print("\n[DONE] Mise a jour terminee !")
