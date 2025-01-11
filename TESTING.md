# Shopping List App - Complete Test Documentation

Date: January 11, 2025  
Tester: [Your Name]

## 1. User Registration and Authentication Tests

### TC001 - Standard User Registration
**Priority:** High  
**Feature:** User Registration  
**Test Steps:**  
1. Navigate to registration page  
2. Enter new username "testuser1"  
3. Enter valid password "Test123!"  
4. Confirm password "Test123!"  
5. Submit registration  

**Expected Result:** Account created, success message shown  
**Actual Result:** [Document Result]  
**Status:** [Pass/Fail]  
**Screenshot:** `TC001_REG_STANDARD.png`

### TC002 - Registration with Mismatched Passwords
**Priority:** High  
**Feature:** User Registration  
**Test Steps:**  
1. Navigate to registration page  
2. Enter username "testuser2"  
3. Enter password "Test123!"  
4. Enter confirmation "Test456!"  
5. Submit registration  

**Expected Result:** Error message about password mismatch  
**Actual Result:** [Document Result]  
**Status:** [Pass/Fail]  
**Screenshot:** `TC002_REG_MISMATCH.png`

### TC003 - Duplicate Username Registration
**Priority:** High  
**Test Steps:**  
1. Attempt to register with existing username  
2. Use valid password  
3. Submit registration  

**Expected Result:** Error about existing username  
**Status:** [Pass/Fail]  
**Screenshot:** `TC003_REG_DUPLICATE.png`

## 2. Item Creation Tests

### TC011 - Create Valid Item
**Priority:** High  
**Feature:** Item Creation  
**Test Steps:**  
1. Login as test user  
2. Navigate to Add Item page  
3. Enter:  
   - Item name: "Test Item"  
   - Quantity: 1  
   - Week Beginning: [Next Monday's date]  
   - Notes: "Test notes"  
4. Submit form  

**Expected Result:** Item created successfully  
**Status:** [Pass/Fail]  
**Screenshot:** `TC011_ITEM_CREATE.png`

### TC012 - Create Item with Non-Monday Date
**Priority:** High  
**Test Steps:**  
1. Follow item creation process  
2. Enter non-Monday date  
3. Submit form  

**Expected Result:** Validation error for date  
**Status:** [Pass/Fail]  
**Screenshot:** `TC012_ITEM_INVALID_DATE.png`

## 3. Item List View Tests

### TC021 - Filter by Week
**Priority:** Medium  
**Test Steps:**  
1. Create multiple items with different weeks  
2. Apply week filter  
3. Check results  

**Expected Result:** Only items from selected week shown  
**Status:** [Pass/Fail]  
**Screenshot:** `TC021_FILTER_WEEK.png`

### TC022 - Filter by User
**Priority:** Medium  
**Test Steps:**  
1. Create items with different users  
2. Apply user filter  
3. Verify results  

**Expected Result:** Only selected user's items shown  
**Status:** [Pass/Fail]  
**Screenshot:** `TC022_FILTER_USER.png`

## 4. Item Editing Tests

### TC031 - Edit Own Item
**Priority:** High  
**Test Steps:**  
1. Locate own item  
2. Modify all fields  
3. Save changes  

**Expected Result:** Changes saved successfully  
**Status:** [Pass/Fail]  
**Screenshot:** `TC031_EDIT_OWN.png`

### TC032 - Edit Others' Items
**Priority:** High  
**Test Steps:**  
1. Attempt to edit another user's item  
2. Submit changes  

**Expected Result:** Access denied message  
**Status:** [Pass/Fail]  
**Screenshot:** `TC032_EDIT_OTHER.png`

## 5. Item Deletion Tests

### TC041 - Delete Own Item
**Priority:** High  
**Test Steps:**  
1. Create test item  
2. Delete item  
3. Verify deletion  

**Expected Result:** Item deleted successfully  
**Status:** [Pass/Fail]  
**Screenshot:** `TC041_DELETE_OWN.png`

### TC042 - Delete as Staff
**Priority:** High  
**Test Steps:**  
1. Login as staff  
2. Delete any item  
3. Verify deletion  

**Expected Result:** Item deleted successfully  
**Status:** [Pass/Fail]  
**Screenshot:** `TC042_DELETE_STAFF.png`

## 6. Authorization Tests

### TC051 - Authorize as Superuser
**Priority:** High  
**Test Steps:**  
1. Login as superuser  
2. Locate pending item  
3. Toggle authorization  
4. Verify status change  

**Expected Result:** Authorization status changed  
**Status:** [Pass/Fail]  
**Screenshot:** `TC051_AUTH_SUPER.png`

### TC052 - Authorize as Regular User
**Priority:** High  
**Test Steps:**  
1. Login as regular user  
2. Attempt to authorize item  

**Expected Result:** Permission denied  
**Status:** [Pass/Fail]  
**Screenshot:** `TC052_AUTH_REGULAR.png`

## 7. User Interface Tests

### TC061 - Form Validation Display
**Priority:** Medium  
**Test Steps:**  
1. Submit forms with invalid data  
2. Check error messages  
3. Verify styling  

**Expected Result:** Clear error messages shown  
**Status:** [Pass/Fail]  
**Screenshot:** `TC061_UI_VALIDATION.png`

### TC062 - Responsive Design
**Priority:** Medium  
**Test Steps:**  
1. Test on mobile width  
2. Test on tablet width  
3. Test on desktop  

**Expected Result:** Proper display at all sizes  
**Status:** [Pass/Fail]  
**Screenshot:** `TC062_UI_RESPONSIVE.png`

## 8. Edge Cases

### TC071 - Maximum Length Item Name
**Priority:** Low  
**Test Steps:**  
1. Create item with 100-character name  
2. Submit and verify display  

**Expected Result:** Name accepted and displayed properly  
**Status:** [Pass/Fail]  
**Screenshot:** `TC071_EDGE_MAXNAME.png`

### TC072 - Special Characters
**Priority:** Low  
**Test Steps:**  
1. Create item with special characters  
2. Verify storage and display  

**Expected Result:** Characters handled correctly  
**Status:** [Pass/Fail]  
**Screenshot:** `TC072_EDGE_SPECIAL.png`

## 9. Permission Tests

### TC081 - Staff Access Rights
**Priority:** High  
**Test Steps:**  
1. Login as staff  
2. Attempt all operations  
3. Verify permissions  

**Expected Result:** Appropriate access levels  
**Status:** [Pass/Fail]  
**Screenshot:** `TC081_PERM_STAFF.png`

### TC082 - Regular User Rights
**Priority:** High  
**Test Steps:**  
1. Login as regular user  
2. Attempt various operations  
3. Verify restrictions  

**Expected Result:** Appropriate restrictions  
**Status:** [Pass/Fail]  
**Screenshot:** `TC082_PERM_USER.png`

## 10. Data Validation Tests

### TC091 - Required Fields
**Priority:** High  
**Test Steps:**  
1. Submit forms with missing data  
2. Check validation messages  

**Expected Result:** Proper validation errors  
**Status:** [Pass/Fail]  
**Screenshot:** `TC091_VAL_REQUIRED.png`

### TC092 - Field Constraints
**Priority:** High  
**Test Steps:**  
1. Test quantity limits  
2. Test date validation  
3. Verify constraints  

**Expected Result:** All constraints enforced  
**Status:** [Pass/Fail]  
**Screenshot:** `TC092_VAL_CONSTRAINTS.png`

## Test Summary

### Statistics
**Total Tests:** 20  
- User Management: 3 tests  
- Item Operations: 12 tests  
- Interface: 3 tests  
- Edge Cases: 2 tests  

### Results Overview
- **Tests Passed:** [Number]  
- **Tests Failed:** [Number]  
- **Pass Rate:** [Percentage]  

### Environment Details
- **Browser:** [Version]  
- **Screen Resolution:** [Resolution]  
- **OS:** [Operating System]  

### Known Issues
1. [List any issues found]  
2. [Include severity and impact]  

### Recommendations
1. [List improvements]  
2. [Include priority]  

## Screenshot Organization
