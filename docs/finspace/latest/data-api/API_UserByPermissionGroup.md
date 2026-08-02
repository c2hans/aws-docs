---
source_url: https://docs.aws.amazon.com/finspace/latest/data-api/API_UserByPermissionGroup.html
---

After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/data-api/amazon-finspace-end-of-support.html).

# UserByPermissionGroup
<a name="API_UserByPermissionGroup"></a>

The structure of a user associated with a permission group.

## Contents
<a name="API_UserByPermissionGroup_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** apiAccess **   <a name="finspace-Type-UserByPermissionGroup-apiAccess"></a>
Indicates whether the user can access FinSpace API operations.
+  `ENABLED` – The user has permissions to use the API operations.
+  `DISABLED` – The user does not have permissions to use any API operations.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** apiAccessPrincipalArn **   <a name="finspace-Type-UserByPermissionGroup-apiAccessPrincipalArn"></a>
The IAM ARN identifier that is attached to FinSpace API calls.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `^arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+$`
Required: No

 ** emailAddress **   <a name="finspace-Type-UserByPermissionGroup-emailAddress"></a>
The email address of the user. The email address serves as a unique identifier for each user and cannot be changed after it's created.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 320.
Pattern: `[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}`
Required: No

 ** firstName **   <a name="finspace-Type-UserByPermissionGroup-firstName"></a>
The first name of the user.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `.*\S.*`
Required: No

 ** lastName **   <a name="finspace-Type-UserByPermissionGroup-lastName"></a>
The last name of the user.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `.*\S.*`
Required: No

 ** membershipStatus **   <a name="finspace-Type-UserByPermissionGroup-membershipStatus"></a>
Indicates the status of the user within a permission group.
+  `ADDITION_IN_PROGRESS` – The user is currently being added to the permission group.
+  `ADDITION_SUCCESS` – The user is successfully added to the permission group.
+  `REMOVAL_IN_PROGRESS` – The user is currently being removed from the permission group.
Type: String
Valid Values: `ADDITION_IN_PROGRESS | ADDITION_SUCCESS | REMOVAL_IN_PROGRESS`
Required: No

 ** status **   <a name="finspace-Type-UserByPermissionGroup-status"></a>
The current status of the user.
+  `CREATING` – The user creation is in progress.
+  `ENABLED` – The user is created and is currently active.
+  `DISABLED` – The user is currently inactive.
Type: String
Valid Values: `CREATING | ENABLED | DISABLED`
Required: No

 ** type **   <a name="finspace-Type-UserByPermissionGroup-type"></a>
 Indicates the type of user.
+  `SUPER_USER` – A user with permission to all the functionality and data in FinSpace.
+  `APP_USER` – A user with specific permissions in FinSpace. The users are assigned permissions by adding them to a permission group.
Type: String
Valid Values: `SUPER_USER | APP_USER`
Required: No

 ** userId **   <a name="finspace-Type-UserByPermissionGroup-userId"></a>
The unique identifier for the user.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 26.
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_UserByPermissionGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/finspace-2020-07-13/UserByPermissionGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/finspace-2020-07-13/UserByPermissionGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/finspace-2020-07-13/UserByPermissionGroup)
