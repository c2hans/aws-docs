---
source_url: https://docs.aws.amazon.com/finspace/latest/data-api/API_PermissionGroup.html
---

After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/data-api/amazon-finspace-end-of-support.html).

# PermissionGroup
<a name="API_PermissionGroup"></a>

The structure for a permission group.

## Contents
<a name="API_PermissionGroup_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** applicationPermissions **   <a name="finspace-Type-PermissionGroup-applicationPermissions"></a>
Indicates the permissions that are granted to a specific group for accessing the FinSpace application.
When assigning application permissions, be aware that the permission `ManageUsersAndGroups` allows users to grant themselves or others access to any functionality in their FinSpace environment's application. It should only be granted to trusted users.
+  `CreateDataset` – Group members can create new datasets.
+  `ManageClusters` – Group members can manage Apache Spark clusters from FinSpace notebooks.
+  `ManageUsersAndGroups` – Group members can manage users and permission groups. This is a privileged permission that allows users to grant themselves or others access to any functionality in the application. It should only be granted to trusted users.
+  `ManageAttributeSets` – Group members can manage attribute sets.
+  `ViewAuditData` – Group members can view audit data.
+  `AccessNotebooks` – Group members will have access to FinSpace notebooks.
+  `GetTemporaryCredentials` – Group members can get temporary API credentials.
Type: Array of strings
Valid Values: `CreateDataset | ManageClusters | ManageUsersAndGroups | ManageAttributeSets | ViewAuditData | AccessNotebooks | GetTemporaryCredentials`
Required: No

 ** createTime **   <a name="finspace-Type-PermissionGroup-createTime"></a>
The timestamp at which the group was created in FinSpace. The value is determined as epoch time in milliseconds.
Type: Long
Required: No

 ** description **   <a name="finspace-Type-PermissionGroup-description"></a>
 A brief description for the permission group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4000.
Pattern: `[\s\S]*`
Required: No

 ** lastModifiedTime **   <a name="finspace-Type-PermissionGroup-lastModifiedTime"></a>
Describes the last time the permission group was updated. The value is determined as epoch time in milliseconds.
Type: Long
Required: No

 ** membershipStatus **   <a name="finspace-Type-PermissionGroup-membershipStatus"></a>
Indicates the status of the user within a permission group.
+  `ADDITION_IN_PROGRESS` – The user is currently being added to the permission group.
+  `ADDITION_SUCCESS` – The user is successfully added to the permission group.
+  `REMOVAL_IN_PROGRESS` – The user is currently being removed from the permission group.
Type: String
Valid Values: `ADDITION_IN_PROGRESS | ADDITION_SUCCESS | REMOVAL_IN_PROGRESS`
Required: No

 ** name **   <a name="finspace-Type-PermissionGroup-name"></a>
The name of the permission group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `.*\S.*`
Required: No

 ** permissionGroupId **   <a name="finspace-Type-PermissionGroup-permissionGroupId"></a>
 The unique identifier for the permission group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 26.
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_PermissionGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/finspace-2020-07-13/PermissionGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/finspace-2020-07-13/PermissionGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/finspace-2020-07-13/PermissionGroup)
