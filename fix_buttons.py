from bs4 import BeautifulSoup

def fix_buttons():
    with open('index.html', 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

    # Add custom CSS to fix button padding and wrapping
    css_fix = """
    <style>
    /* Fix button overlapping and wrapping issues */
    .links, .links.medium {
        width: auto !important;
        min-width: max-content !important;
        padding-left: 24px !important;
        padding-right: 24px !important;
        display: inline-flex !important;
        align-items: center !important;
        justify-content: center !important;
    }
    
    .links__wrap {
        width: max-content !important;
        display: flex !important;
        align-items: center !important;
        gap: 12px !important;
    }
    
    .link__text, .link__text p.letter-wrap {
        width: auto !important;
        white-space: nowrap !important;
        margin: 0 !important;
    }
    
    .link__arrow {
        position: static !important;
        margin-left: 5px !important;
    }
    </style>
    """
    
    soup.head.append(BeautifulSoup(css_fix, 'html.parser'))

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(str(soup))

if __name__ == '__main__':
    fix_buttons()
    print("Buttons fixed")
