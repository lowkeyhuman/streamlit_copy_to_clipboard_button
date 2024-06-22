import streamlit as st

def add_copy_button(text_to_copy):
  html = f"""
    <style>
      body {{
        margin: 0;
      }}
      .copy-button {{
        border: 1px solid rgba(49, 51, 63, 0.2);
        background: white;
        padding: 0.25rem 0.75rem;
        font-weight: 400;
        border-radius: 0.5rem;
        min-height: 2.5rem;
        min-width: 5rem;
        line-height: 1.6;
        font-family: "Source Sans Pro", sans-serif;
        font-size: inherit;
        cursor: pointer;
        color: rgba(49, 51, 63);
        transition: 0.2s ease all;
      }}
      .copy-button:hover {{
        border-color: #F54947;
        color: #F54947;
      }}
      .copy-button:active {{
        background-color: #F54947;
        color: white;
      }}
      .copy-button.copied {{
        border-color: #0ABE82;
        background-color: #0ABE82;
        color: white;
      }}
    </style>

    <button onclick="copyToClipboard()" class="copy-button">Copy</button>
    
    <script>
      function copyToClipboard() {{
        var text_to_copy = `{text_to_copy}`;
        if (text_to_copy == '') return;

        var textarea = document.createElement("textarea");
        textarea.value = text_to_copy;
        document.body.appendChild(textarea);
        textarea.select();
        document.execCommand("copy");
        document.body.removeChild(textarea);

        var copyButton = document.getElementsByClassName('copy-button')[0]
        copyButton.textContent = 'Copied!';
        copyButton.classList.add('copied');
        setTimeout( function(){{
          copyButton.classList.remove('copied');
          copyButton.textContent = 'Copy';
        }}, 1000)
      }}
    </script>
    
    """

  st.components.v1.html(html, height=40)