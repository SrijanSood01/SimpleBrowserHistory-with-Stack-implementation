A simple command-line application simulating a browser's back and forward history using stacks in Python. This program allows you to visit pages, navigate backward, and forward through the history, and view the current page.

Features
Visit a Page: Add a new page to your browsing history.
Go Back: Go to the previously visited page.
Go Forward: Return to a page after going back.
Show Current Page: Display the current page.
Clear Forward History: Automatically clears forward history when visiting a new page.
How It Works
This project uses two stacks:

back_stack: Holds pages you've visited before the current page.
forward_stack: Holds pages after you've gone back.
Each action (visit, back, and forward) manipulates these stacks to maintain a simple browsing history.

Getting Started
Prerequisites
Python 3.x installed on your system.
Running the Application
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/SimpleBrowserHistory.git
cd SimpleBrowserHistory
Run the script:

bash
Copy code
python browser_history.py
Follow the on-screen instructions to navigate through the browser history.

Usage
In the command-line interface, use the following commands:

visit <page>: Visit a new page (replace <page> with the name of the page, e.g., visit google.com).
back: Go back to the previous page.
forward: Move forward in the browsing history, if possible.
current: Display the current page.
exit: Exit the application.
Example
plaintext
Copy code
Options: visit <page>, back, forward, current, exit
Enter command: visit google.com
Visited google.com

Enter command: visit github.com
Visited github.com

Enter command: back
Back to google.com

Enter command: forward
Forward to github.com

Enter command: current
Current page: github.com

Enter command: exit
Exiting browser history simulation.
