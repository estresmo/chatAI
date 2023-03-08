# chatAI

Simple project using flask for connect to OpenAI gpt-3

Need to have a json file called `users.json` to store users. The users.ex.json is an example of that, (using werkzeug.security  generate_password_hash for generate passwords)

You need to change OPENAI_ORG var in app.py putting your organizarion ID provided by OpenAI and also need to add your OPENAI_API_KEY to env vars