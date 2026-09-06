---
source_url: https://docs.aws.amazon.com/finspace/latest/data-api/API_PermissionGroupByUser.html
---

After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/data-api/amazon-finspace-end-of-support.html).

# PermissionGroupByUser
<a name="API_PermissionGroupByUser"></a>

The structure of a permission group associated with a user.

## Contents
<a name="API_PermissionGroupByUser_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** membershipStatus **   <a name="finspace-Type-PermissionGroupByUser-membershipStatus"></a>
Indicates the status of the user within a permission group.
+  `ADDITION_IN_PROGRESS` – The user is currently being added to the permission group.
+  `ADDITION_SUCCESS` – The user is successfully added to the permission group.
+  `REMOVAL_IN_PROGRESS` – The user is currently being removed from the permission group.
Type: String
Valid Values: `ADDITION_IN_PROGRESS | ADDITION_SUCCESS | REMOVAL_IN_PROGRESS`
Required: No

 ** name **   <a name="finspace-Type-PermissionGroupByUser-name"></a>
The name of the permission group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `.*\S.*`
Required: No

 ** permissionGroupId **   <a name="finspace-Type-PermissionGroupByUser-permissionGroupId"></a>
The unique identifier for the permission group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 26.
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_PermissionGroupByUser_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/finspace-2020-07-13/PermissionGroupByUser)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/finspace-2020-07-13/PermissionGroupByUser)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/finspace-2020-07-13/PermissionGroupByUser)
