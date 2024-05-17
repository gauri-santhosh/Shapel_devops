from flask import Flask, render_template, request, redirect, url_for, session
import psycopg2

app = Flask(__name__)
app.secret_key = 'Manju123#'  # Ensure this secret key is kept secure

# Function to authenticate user
def authenticate_user(username, password):
    try:
        # Connect to your PostgreSQL database
        conn = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="Manju123#",
            host="localhost",
            port="5432"
        )

        # Create a cursor object
        cur = conn.cursor()

        # Prepare the query to fetch user credentials
        query = "SELECT * FROM login WHERE username = %s AND password = %s"

        # Execute the query with username and password as parameters
        cur.execute(query, (username, password))

        # Fetch the first row (if any)
        user = cur.fetchone()

        # Close the cursor and connection
        cur.close()
        conn.close()

        # Return user data if authentication is successful, None otherwise
        return user

    except psycopg2.Error as e:
        print("Error connecting to the database:", e)
        return None

# Route for index page (default landing page)
@app.route('/')
def index():
    return render_template('index.html')

# Route for login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Authenticate the user
        authenticated_user = authenticate_user(username, password)
        
        if authenticated_user:
            # Store user information in session
            session['user'] = {
                'name': authenticated_user[0],
                'email': authenticated_user[1],
                'username': username,
            }
            session['logged_in'] = True
            # Redirect to home page upon successful login
            return redirect(url_for('index'))
        else:
            return "Authentication failed. Invalid username or password."
    else:
        return render_template('login.html')

# Route for registration page
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        new_email = request.form['email']
        new_username = request.form['username']
        new_password = request.form['password']
        new_fullname = request.form['fullname']
        new_phone = request.form['phone']
        new_gender = request.form['gender']
        
        try:
            # Connect to your PostgreSQL database
            conn = psycopg2.connect(
                dbname="postgres",
                user="postgres",
                password="Manju123#",
                host="localhost",
                port="5432"
            )

            # Create a cursor object
            cur = conn.cursor()

            # Check if the username or email already exists in the database
            cur.execute("SELECT * FROM login WHERE username = %s OR email = %s", (new_username, new_email))
            existing_user = cur.fetchone()

            if existing_user:
                return "Username or email already exists. Please choose a different one."

            # If username or email doesn't exist, insert the new user into the database
            cur.execute("INSERT INTO login (fullname, username, email, phone, password, gender) VALUES (%s, %s, %s, %s, %s, %s)",
                        (new_fullname, new_username, new_email, new_phone, new_password, new_gender))
            conn.commit()

            # Close the cursor and connection
            cur.close()
            conn.close()

            # Redirect to login page after successful registration
            return redirect(url_for('login'))

        except psycopg2.Error as e:
            print("Error connecting to the database:", e)
            return "An error occurred during registration. Please try again later."

    else:
        return render_template('register.html')

# Route for about page
@app.route('/about')
def about():
    return render_template('about.html')

# Route for blog page
@app.route('/blog')
def blog():
    return render_template('blog.html')

# Route for gallery page
@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

# Route for service page
@app.route('/service')
def service():
    return render_template('service.html')

# Route for booking page
@app.route('/booking', methods=['GET', 'POST'])
def booking():
    if request.method == 'POST':
        # Handle booking form submission here
        pass
    else:
        return render_template('booking.html')

if __name__ == '_main_':
    app.run(host="0.0.0.0", port=5000)