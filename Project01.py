class Task:
    
    def __init__(self, title, description, due_date, category="Uncategorized", priority="Low"):
        
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = False
        self.category = category
        self.priority = priority

    def task_details(self):
        
        print(f'Title: {self.title}')
        print(f'Description: {self.description}')
        print(f'Due Date: {self.due_date}')
        print(f'Category: {self.category}')
        print(f'Priority: {self.priority}')
        print(f'Completed: {"Yes" if self.completed else "No"}')

class TaskManager:
    
    def __init__(self):
        
        self.tasks = []

    def create_task(self):
        
        title = input('Enter task title: ')
        description = input('Enter task description: ')
        due_date = input('Enter due date (YYYY-MM-DD): ')
        category = input('Enter task category: ')
        priority = input('Enter task priority (Low/Medium/High): ')
        new_task = Task(title, description, due_date, category, priority)
        self.tasks.append(new_task)
        
        print(f'Task "{title}" created.')

    def edit_task(self):
        
        title = input('Enter the title of the task to edit: ')
        
        for task in self.tasks:
            
            if task.title == title:
                
                print('Enter new task details:')
                task.title = input('New title: ')
                task.description = input('New description: ')
                task.due_date = input('New due date (YYYY-MM-DD): ')
                task.category = input('New category: ')
                task.priority = input('New priority (Low/Medium/High): ')
                
                print(f'Task "{title}" edited.')
                
                return
            
        print(f'Task "{title}" not found.')

    def delete_task(self):
        
        title = input('Enter the title of the task to delete: ')
        
        for task in self.tasks:
            
            if task.title == title:
                
                self.tasks.remove(task)
                print(f'Task "{title}" deleted.')
                
                return
        print(f'Task "{title}" not found.')

    def view_task_list(self, show_completed=False):
        
        print('\nTasks:')
        
        for task in self.tasks:
            
            if (show_completed or not task.completed) and task.priority != 'Completed':
                print(f'{task.title} - Due Date: {task.due_date} - Category: {task.category} - Priority: {task.priority}')

    def view_completed(self):
        
        print('\nCompleted Tasks:')
        for task in self.tasks:
            
            if task.completed:
                task.task_details()

    def mark_complete(self):
        
        title = input('Enter the title of the task to mark as completed: ')
        
        for task in self.tasks:
            
            if task.title == title:
                
                task.completed = True
                task.priority = 'Completed'
                print(f'Task "{title}" marked as completed.')
                
                return
            
        print(f'Task "{title}" not found.')

    def view_tasks_by_category(self):
        
        categories = set(task.category for task in self.tasks)
        print('\nCategories:')
        
        for category in categories:
            
            print(f'{category}')
            
            for task in self.tasks:
                
                if task.category == category:
                    
                    print(f'  {task.title} - Due Date: {task.due_date} - Priority: {task.priority}')

    def view_tasks_by_priority(self, priority):
        
        print(f'\nTasks with Priority "{priority}":')
        
        for task in self.tasks:
            
            if task.priority == priority:
                
                task.task_details()

    def duplicate_task(self):
        
        title = input('Enter the title of the task to duplicate: ')
        
        for task in self.tasks:
            
            if task.title == title:
                
                new_task = Task(
                    f'Duplicate of {title}',
                    task.description,
                    task.due_date,
                    task.category,
                    task.priority
                )
                
                self.tasks.append(new_task)
                print(f'Task "{title}" duplicated.')
                
                return
            
        print(f'Task "{title}" not found.')
        
    def search_tasks(self):
        keyword = input('Enter the keyword to search for (title or category): ')
        found_tasks = []
        for task in self.tasks:
            if keyword.lower() in task.title.lower() or keyword.lower() in task.category.lower():
                found_tasks.append(task)
        if found_tasks:
            print('\nFound Tasks:')
            for found_task in found_tasks:
                found_task.task_details()
        else:
            print(f'No tasks found with the keyword "{keyword}".')

def menu():
    
    print('-'*30)
    print('1: Create a Task')
    print('2: Edit a Task')
    print('3: Delete a Task')
    print('4: View Task List')
    print('5: View Completed Task List')
    print('6: Mark a Task Completed')
    print('7: View Tasks by Category')
    print('8: View Tasks by Priority')
    print('9: Duplicate a Task')
    print('10: Search')
    print('0: Quit')
    print('-'*30)

if __name__ == "__main__":
    
    task_manager = TaskManager()

    while True:
        
        menu()
        
        user_choice = input("Enter your choice: ")
        if user_choice == '0':
            
            quit
            break
        
        elif user_choice == '1':
            
            task_manager.create_task()
            
        elif user_choice == '2':
            
            task_manager.edit_task()
            
        elif user_choice == '3':
            
            task_manager.delete_task()
            
        elif user_choice == '4':
            
            task_manager.view_task_list()
            
        elif user_choice == '5':
            
            task_manager.view_completed()
            
        elif user_choice == '6':
            
            task_manager.mark_complete()
            
        elif user_choice == '7':
            
            task_manager.view_tasks_by_category()
            
        elif user_choice == '8':
            
            priority = input('Enter priority to filter (Low/Medium/High): ')
            task_manager.view_tasks_by_priority(priority)
            
        elif user_choice == '9':
            
            task_manager.duplicate_task()
            
        elif user_choice == '10':
            
            task_manager.search_tasks()
            
        else:
            
            print('Invalid choice')