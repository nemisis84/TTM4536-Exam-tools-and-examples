import base64

# Your script
script = '<script>alert("small.png")</script>'

# Encode it
encoded_script = base64.b64encode(script.encode()).decode()

print(encoded_script)
