from flask import Flask,request,redirect

app=Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <body>
        <h1>Signup</h1>
    <style>
        .error {{color: red }}
    </style>

        <form method = "POST">
        <table>
        <tr>
            <td>
                <label for = "user-name">Username:</label>
            </td>
            <td>
                <input id="user-name" type = "text" name="user_name_input" value="{name}" />
            </td>
            <td> <span class ="error">{username_error}</span></td>
        </tr>
        <tr>
            <td>
                <label for = "pass-word">Password:</label>
            </td>
            <td>
                <input id= "pass-word" type="password" name="pass_word_input" />
            </td>
            <td><span class= "error">{password_error}</span></td>
        </tr>
        <tr>
            <td>
                <label for="verify-password">Verify Password:</label>
            </td>
            <td>
                <input id= "verify-password" type="password" name = "verify_pass_word_input" />
            </td>
            <td><span class="error">{verify_error}</span></td>
        </tr>
        <tr>
            <td>
                <label for= "email">Email(optional):</label>
            </td>
            <td>
                <input id= "email" type="text" name="email_input" value ="{emailname}"/>
            </td>

            <td><span class= "error">{email_error}</span></td>
        </tr>
        <tr>
            <td>
                <input type="submit" value ="Submit"/>
            </td>
        </tr>
        </table>
        </form>
    </body>
</html>

"""


@app.route("/")
def index():
    return form.format(username_error ='',password_error='',verify_error='',email_error='',name='',emailname='')

app.run()

        


             