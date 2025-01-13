# Shopping List App

![Shopping List App Home Page ](shopping_list_app/media/readme_images/Home_Screen.png)


## 1. Introduction

### 1.1 Problem Statement
A family that wants to have a shared shopping list that members can update.  
A tool to keep on top of family chores and ensure everybody is doing what they are responsible for.  

### 1.2 Purpose
A simple shared shopping list reminder so that things are not forgotten.  
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
- Children can be rewarded so they can add items to the shopping list upon completing a chore.
- Parents can set rewards on the completion of chores.

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
- **Actor:** Super-User (Parent)
- **Description:** Users can create, edit, and organize shopping lists for groceries.
- **Steps:**
  1. Super-User opens the app and selects "Add an Item".
  2. Super-User adds items to the list peer week beginning and can specify optional notes.
  3. Super-User can edit or remove their items.
  4. Super-User marks an item as "Approved," which is updated across all devices.
  5. Super-User can "Revoke" a previously "Approved" item.
  6. Lists are automatically saved and synced across all family members’ devices.
  
#### 3.2.2 Add to a Shopping List
- **Actor:** Child
- **Description:** User can add items to shopping lists.
- **Steps:**
  1. User opens the app and selects "Add an Item".
  2. User adds items to the list and specifies optional notes.
  3. User can edit or remove only their own items.
  4. Lists are automatically saved and synced across all family members’ devices.

---

## 4. Wireframes
*(Include your wireframes here. You can describe them briefly or provide links to images.)*

![Wireframe1](shopping_list_app/media/readme_images/Wireframe1.png)


![Wireframe2](shopping_list_app/media/readme_images/Wireframe2.png)


---

## 5. Technologies Used

### 5.1 Frontend
- **HTML:** For structuring web content.
- **CSS:** For styling and layout.
- **Bootstrap 5.3.0:** For responsive design and prebuilt components.
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
- **Django's in-built user class :** For managing parent and child roles.

### 5.7 Other 
- **AI engines :** ChatGPT and Claude were used to check details of project scoping and planning as well as assist extensively with aspects of coding.

---

## 6. Validation

### 6.1 HTML Validation
The app’s HTML has been validated using the W3C Markup Validator to ensure proper coding standards.

![W3C Markup Validation approved](shopping_list_app/media/readme_images/HTML_validation.png)

### 6.2 CSS Validation
The app’s CSS has been validated using the W3C CSS Validator to ensure proper coding standards.

![W3C CSS Validation approved](shopping_list_app/media/readme_images/CSS_validation.png)

### 6.3 Testing
- Extensive tests for key functionalities like registering, login, adding, deleting, and approving items are documented in the TESTING.md
[Testing Documentation](TESTING.md)

---