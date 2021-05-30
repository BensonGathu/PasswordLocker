# Password Locker App
#### By Benson Gathu
## Description
An application that will help us manage our passwords and even generate new passwords for us.
### Installation
* Clone this repository to your local computer.
* Ensure you have python3 installed in your computer.
* From the terminal navigate to the cloned project folder.
* Run python3 run.py code in the terminal to launch.
## Usage
* Once you launch, You can either create a new user, or login or exit the application.
* If you choose to create a new account, use cu as the code and follow the prompts.
* Once logged in, you can:
1. View Your saved credentials.
2. Add new credentials.
3. Remove credentials.
4. Search credentials.
5. Log Out. 
### Running unit tests
* Run python3 credentials_test.py for credential class tests.
* Run python3 user_test.py for user class tests. 
## Requirements
* Project should have two classes, a User class and Credentials class.
* Application should have an authentication system that enables a user to log into their account and view their credentials. A user should be able to login to their account using the password that they created and NOT any password.
* Project should make use of docstrings to document methods and functions.
* Project must have a test class that test each individual method in your classes.
## Bugs
Since there is no database to support the app, once you exit or log out of a session you loose all the credentials and created user. You have to create a new user for every session. You can still use the default login but if you exit the app, you will still loose all the credentials you created.
## Technical Requirements
* Project should contain a proper detailed README markdown file, with the full description of the project, setup instructions, dependencies, technologies used, authors, license information and contact information.
* Project should have descriptive and properly outlined commits.
* Project code should be pushed to Github with a description of the app provided in the Github Repository.
## Technologies used
* Python
## License
Copyright (c) [2021] [Benson Gathu]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.