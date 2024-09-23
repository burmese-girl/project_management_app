STATUS_CHOICES = [
    ('new', 'New'),
    ('open', 'Open'),
    ('fixed', 'Fixed'),
    ('rejected', 'Rejected'),
    ('in_progress', 'In Progress'),
    ('closed', 'Closed'),
    ('test_passed', 'Test Passed'),
]

PROJECT_ROLES = [
    ('admin', 'Admin'), # admin of the project with full permissions
    ('manager', 'Manager'),
    ('team lead', 'Team Lead'),
    ('staff', 'Staff')
]

TASK_TYPES = [
    ('task', 'Task'),
    ('story', 'Story'),
    ('bug', 'Bug')
]