class BrowserHistory:
    def __init__(self):
        self.back_stack = []
        self.forward_stack = []
        self.current_page = None

    def visit_page(self, page):
        
        if self.current_page:
            self.back_stack.append(self.current_page)
        
       
        self.current_page = page
        self.forward_stack.clear()
        print(f"Visited {page}")

    def go_back(self):
       
        if not self.back_stack:
            print("No pages to go back to.")
            return
        
        
        self.forward_stack.append(self.current_page)
        self.current_page = self.back_stack.pop()
        print(f"Back to {self.current_page}")

    def go_forward(self):
     
        if not self.forward_stack:
            print("No pages to go forward to.")
            return
        
        self.back_stack.append(self.current_page)
        self.current_page = self.forward_stack.pop()
        print(f"Forward to {self.current_page}")

    def show_current_page(self):
        if self.current_page:
            print(f"Current page: {self.current_page}")
        else:
            print("No page currently visited.")


if __name__ == "__main__":
    browser = BrowserHistory()
    while True:
        print("\nOptions: visit <page>, back, forward, current, exit")
        command = input("Enter command: ").strip().lower()

        if command.startswith("visit"):
            _, page = command.split(maxsplit=1)
            browser.visit_page(page)
        elif command == "back":
            browser.go_back()
        elif command == "forward":
            browser.go_forward()
        elif command == "current":
            browser.show_current_page()
        elif command == "exit":
            print("Exiting browser history simulation.")
            break
        else:
            print("Invalid command. Please try again.")
