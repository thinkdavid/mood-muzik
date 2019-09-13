#Current Goals
- Complete Authorization Workflow(/login/views.success.py)
- Create User Accounts Based on Spotify Account (/login/models.py)
- *High Level*: Collect Information on User Sessions
- Create Front End to Prompt User to Opt-In to Session and specify type of Session (/login/models.Session.py) -- may need to create a new template
- In general, figure out how to connect templates to a JS front-end (login/templates)
- Eventually Perform Data Modeling/Reccomendations Based On Session Data
- Sessions should contain
    + Lists of Songs
        * song attibutes will need to be determined somehow -- maybe another api
    + Session Attributes
        * time
        * mood
        * weather
        * why are you listening to music? (party? gym? study? car?)