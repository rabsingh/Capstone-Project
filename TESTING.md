# Shopping List App - Complete Test Documentation

Date: January 11, 2025  
Tester: [Your Name]

## 1. User Registration and Authentication Tests

### TC001 - Standard User Registration
**Priority:** High  
**Feature:** User Registration  
**Test Steps:**  
1. Navigate to registration page  
2. Enter new username "testuser"  
3. Enter valid password "Test123!"  
4. Confirm password "Test123!"  
5. Submit registration  

**Expected Result:** Account created, success message shown  
**Actual Result:** [Document Result]  
**Status:** [Pass]  
**Screenshot:** `1.png`


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
**Status:** [Pass]  
**Screenshot:** `2.png`

### TC003 - Duplicate Username Registration
**Priority:** High  
**Test Steps:**  
1. Attempt to register with existing username  
2. Use valid password  
3. Submit registration  

**Expected Result:** Error about existing username  
**Status:** [Pass]  
**Screenshot:** `3.png`

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
   - Week Beginning: [Jan 13th 2025]  
   - Notes: "Test notes"  
4. Submit form  

**Expected Result:** Item created successfully  
**Status:** [Pass/Fail]  
**Screenshot:** `4a.png`
**Screenshot:** `4b.png`

### TC012 - Create Item with Non-Monday Date
**Priority:** High  
**Test Steps:**  
1. Follow item creation process  
2. Enter non-Monday date: [15th Jan 2025]
3. Submit form  

**Expected Result:** Validation error for date  
**Status:** [Pass]  
**Screenshot:** `5.png`

## 3. Item List View Tests

### TC021 - Filter by Week
**Priority:** Medium  
**Test Steps:**  
1. Create multiple items with different weeks  
2. Apply week filter  
3. Check results  

**Expected Result:** Only items from selected week shown  
**Status:** [Pass]  
**Screenshot:** `6.png`

### TC022 - Filter by User
**Priority:** Medium  
**Test Steps:**  
1. Create items with different users  
2. Apply user filter  
3. Verify results  

**Expected Result:** Only selected user's items shown  
**Status:** [Pass]  
**Screenshot:** `7.png`

## 4. Item Editing Tests

### TC031 - Edit Own Item
**Priority:** High  
**Test Steps:**  
1. Locate own item  
2. Modify all fields  
3. Save changes  

**Expected Result:** Changes saved successfully  
**Status:** [Pass]  
**Screenshot:** `8a.png`
**Screenshot:** `8b.png`

### TC032 - Edit Others' Items
**Priority:** High  
**Test Steps:**  
1. Attempt to edit another user's item  
2. Submit changes  

**Expected Result:** No Edit facility other then for own items  
**Status:** [Pass]  
**Screenshot:** `9.png`

## 5. Item Deletion Tests

### TC041 - Delete Own Item
**Priority:** High  
**Test Steps:**  
1. Create test item  
2. Delete item  
3. Verify deletion  

**Expected Result:** Item deleted successfully  
**Status:** [Pass]  
**Screenshot:** `10a.png`
**Screenshot:** `10b.png`

### TC042 - Delete as Super User
**Priority:** High  
**Test Steps:**  
1. Login as staff  
2. Delete any item  
3. Verify deletion  

**Expected Result:** Item deleted successfully  
**Status:** [Pass]  
**Screenshot:** `11a.png`
**Screenshot:** `11b.png`
**Screenshot:** `11c.png`

## 6. Authorization Tests

### TC051 - Authorize as Superuser
**Priority:** High  
**Test Steps:**  
1. Login as superuser  
2. Locate pending item  
3. Toggle authorization  
4. Verify status change  

**Expected Result:** Authorization status changed  
**Status:** [Pass]  
**Screenshot:** `12a.png`
**Screenshot:** `12b.png`

## 7. User Interface Tests

### TC062 - Responsive Design
**Priority:** Medium  
**Test Steps:**  
1. Test on mobile width  
2. Test on tablet width  
3. Test on desktop  

**Expected Result:** Proper display at all sizes  
**Status:** [Pass]  
**Screenshot:** `13a.png`
**Screenshot:** `13b.png`
**Screenshot:** `13c.png`

## 8. Edge Cases

### TC071 - Maximum Length Item Name
**Priority:** Low  
**Test Steps:**  
1. Create item with 100-character name  
2. Submit and verify display  

**Expected Result:** Name accepted and displayed properly  
**Status:** [Pass]  
**Screenshot:** `14.png`

### TC072 - Special Characters
**Priority:** Low  
**Test Steps:**  
1. Create item with special characters  
2. Verify storage and display  

**Expected Result:** Characters handled correctly  
**Status:** [Pass]  
**Screenshot:** `15.png`

## 9. Permission Tests

### TC081 - Staff Access Rights
**Priority:** High  
**Test Steps:**  
1. Login as staff  
2. Attempt all operations  
3. Verify permissions  

**Expected Result:** Appropriate access levels  
**Status:** [Pass]  
**Screenshot:** Evidenced from Screenshot already provided in other tests

### TC082 - Regular User Rights
**Priority:** High  
**Test Steps:**  
1. Login as regular user  
2. Attempt various operations  
3. Verify restrictions  

**Expected Result:** Appropriate restrictions  
**Status:** [Pass]  
**Screenshot:** Evidenced from Screenshot already provided in other tests

## 10. Data Validation Tests

### TC091 - Required Fields
**Priority:** High  
**Test Steps:**  
1. Submit forms with missing data  
2. Check validation messages  

**Expected Result:** Proper validation errors  
**Status:** [Pass]  
**Screenshot:** `16.png`

### TC092 - Field Constraints
**Priority:** High  
**Test Steps:**  
1. Test quantity limits    
2. Verify constraints  

**Expected Result:** All constraints enforced  
**Status:** [Pass]  
**Screenshot:** `17.png`

## Test Summary

### Statistics
**Total Tests:**   
- User Management:  tests  
- Item Operations:  tests  
- Interface:  tests  
- Edge Cases:  tests  

### Results Overview
- **Tests Passed:** [Number]  
- **Tests Failed:** [Number]  
- **Pass Rate:** [Percentage]  

### Environment Details
- **Browser:** [Chrome]  
- **Screen Resolution:** [1920 x 1080]  
- **OS:** [IOS]  

### Known Issues
1. [List any issues found]  
2. [Include severity and impact]  

### Recommendations
1. Grey out all days other then Monday for week beginning  - medium priority 
2. Limit quantity field - low priority

