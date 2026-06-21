def run():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # Fix the small text above if it was missed
    html = html.replace('<p class="ml4 en">WE ARE</p>', '<p class="ml4 en">NAGI IS</p>')
    html = html.replace('<p class="ml4 en">WE&nbsp;ARE</p>', '<p class="ml4 en">NAGI IS</p>')

    # Update the hero text lines
    html = html.replace('<h1 class="ml3 _1 en">An AI-native</h1>', '<h1 class="ml3 _1 en">Calm in the</h1>')
    html = html.replace('<h1 class="ml3 _2 en">research<br></h1>', '<h1 class="ml3 _2 en">ocean of<br></h1>')
    html = html.replace('<h1 class="ml3 _3 en">environment</h1>', '<h1 class="ml3 _3 en">research</h1>')
    
    # Just in case there are no <br> tags or different spacing
    html = html.replace('<h1 class="ml3 _2 en">research</h1>', '<h1 class="ml3 _2 en">ocean of</h1>')

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)

if __name__ == '__main__':
    run()
    print("Hero updated")
