# Shopping List App

## 1. Introduction

### 1.1 Problem Statement
A family that wants to have a shared shopping list that members can update.  
A tool to keep on top of family chores and ensure everybody is doing what they are responsible for.  

### 1.2 Purpose
A simple shared shopping list reminder and to-do list so that things are not forgotten.  
A group management app.  

### 1.3 Target Audience
Any group of people who share tasks and responsibilities, such as:
- Families
- Student houses
- Shared accommodations

---

## 2. Features

### 2.1 MVP Features
- The primary feature is a shopping list that can be added, deleted, and amended.
- Quick and simple entry of items to be added to the shopping list by an authorized user with their own login.

### 2.2 Additional Features
- A chore list that links to the shopping list.
- Children can be rewarded with the ability to add items to the shopping list upon completing a chore.
- Parents can set rewards that children can select after completing tasks.

---

## 3. User Stories & Use Cases

### 3.1 User Stories
- **As a parent**, I want to add members to my shopping list app so that they can use my app.
- **As a parent**, I want to have a simple, easy-to-use shopping list always to hand so I never forget buying items for the home.
- **As a child**, I want to add items that I need my parents to buy so I have what I need.
- **As a parent**, I want to approve any items added to the list so I have the final say on what is purchased.
- **As an admin**, I want to control who uses the app and how they use it.

### 3.2 Use Cases
#### 3.2.1 Create and Manage Shopping Lists
- **Actor:** Parent
- **Description:** Users can create, edit, and organize shopping lists for groceries.
- **Steps:**
  1. User opens the app and selects "Shopping List."
  2. User clicks "Create New List" and provides a name (e.g., "Weekly Groceries").
  3. User adds items to the list and can specify optional notes.
  4. User can edit or remove items.
  5. Lists are automatically saved and synced across all family members’ devices.
- **Alternate Paths:**
  - User deletes a shopping list.
  - User marks an item as "Approved," which is updated across all devices.

#### 3.2.2 Add to a Shopping List
- **Actor:** Child
- **Description:** User can add items to shopping lists for groceries.
- **Steps:**
  1. User opens the app and selects "Shopping List."
  2. User adds items to the list and specifies optional notes.
  3. User can edit or remove items.
  4. Lists are automatically saved and synced across all family members’ devices.

---

## 4. Wireframes
*(Include your wireframes here. You can describe them briefly or provide links to images.)*

---

## 5. Technologies Used

### 5.1 Frontend
- **HTML:** For structuring web content.
- **CSS:** For styling and layout.
- **Bootstrap:** For responsive design and prebuilt components.
- **JavaScript:** For dynamic user interactions.

### 5.2 Backend
- **Python:** Programming language.
- **Django:** Web framework for building the backend logic and database integration.

### 5.3 Database
- **PostgreSQL:** Relational database for storing application data.

### 5.4 Deployment
- **Heroku:** Platform for hosting the application.

### 5.5 Version Control
- **GitHub:** For code hosting and version control.

### 5.6 Authentication
- **JWT-based authentication:** For managing parent and child roles.

---

## 6. Validation

### 6.1 CSS Validation
The app’s CSS has been validated using the W3C CSS Validator to ensure proper coding standards. *(Include a link to the validation results or a badge if available.)*

### 6.2 Input Validation
- Ensures that fields like item name, quantity, and user roles are filled in correctly.

### 6.3 Testing
- Unit tests for key functionalities like adding, deleting, and approving items.

---

## 7. Acknowledgments
- Django and Bootstrap communities for their tools and resources.
- W3C for validation tools.
- Heroku for hosting support.

---

