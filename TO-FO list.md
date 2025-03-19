# To-Do List Application

This is a simple command-line To-Do List application written in Python. It allows users to add tasks, view them, and mark them as done.

## Features

-   **Add Tasks:** Users can add multiple tasks at once.
-   **View Tasks:** Displays all tasks with their status (done or not done).
-   **Mark Tasks as Done:** Users can mark specific tasks as completed.
-   **Exit:** Allows users to exit the application.

## How to Run

1.  **Clone the repository:**
    ```bash
    git clone <repository_url>
    ```
2.  **Navigate to the project directory:**
    ```bash
    cd <project_directory>
    ```
3.  **Run the Python script:**
    ```bash
    python main.py
    ```

## Usage

1.  When the application starts, you will see a menu with the following options:
    -   `1. add task`
    -   `2. show task`
    -   `3. Mark as done task`
    -   `4. exit`
2.  **To add tasks:**
    -   Enter `1` and press Enter.
    -   Enter the number of tasks you want to add and press Enter.
    -   Enter each task one by one, pressing Enter after each task.
3.  **To view tasks:**
    -   Enter `2` and press Enter.
    -   The application will display all tasks with their status.
4.  **To mark a task as done:**
    -   Enter `3` and press Enter.
    -   Enter the task number (index + 1) you want to mark as done and press Enter.
5.  **To exit the application:**
    -   Enter `4` and press Enter.

## Example


=====TO-DO LIST=====
1.add task
2.show task
3.Mark as done task
4.exit
Enter the choice:1
enter no. of task2
Enter task:Buy groceries
Task added.
Enter task:Finish report
Task added.
=====TO-DO LIST=====
1.add task
2.show task
3.Mark as done task
4.exit
Enter the choice:2
1.Buy groceries-not done
2.Finish report-not done
=====TO-DO LIST=====
1.add task
2.show task
3.Mark as done task
4.exit
Enter the choice:3
Enter task no. to mark as done:1
Task is done as mark 1
=====TO-DO LIST=====
1.add task
2.show task
3.Mark as done task
4.exit
Enter the choice:2
1.Buy groceries-done
2.Finish report-not done
=====TO-DO LIST=====
1.add task
2.show task
3.Mark as done task
4.exit
Enter the choice:4
Exiting To-Do list
[{'task': 'Buy groceries', 'done': True}, {'task': 'Finish report', 'done': False}]

## Code structure

* `main.py`: Contains the main application logic.

## Future Improvements

-   Add functionality to edit tasks.
-   Implement task prioritization.
-   Save tasks to a file for persistence.
-   Implement a graphical user interface (GUI).
-   Add error handling for invalid user inputs.
-   Add date and time functionality.

