---
source_url: https://docs.aws.amazon.com/finspace/latest/data-api/API_PermissionGroupParams.html
---

After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/data-api/amazon-finspace-end-of-support.html).

# PermissionGroupParams
<a name="API_PermissionGroupParams"></a>

Permission group parameters for Dataset permissions.

Here is an example of how you could specify the `PermissionGroupParams`:

 ` { "permissionGroupId": "0r6fCRtSTUk4XPfXQe3M0g", "datasetPermissions": [ {"permission": "ViewDatasetDetails"}, {"permission": "AddDatasetData"}, {"permission": "EditDatasetMetadata"}, {"permission": "DeleteDataset"} ] } `

## Contents
<a name="API_PermissionGroupParams_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** datasetPermissions **   <a name="finspace-Type-PermissionGroupParams-datasetPermissions"></a>
List of resource permissions.
Type: Array of [ResourcePermission](API_ResourcePermission.md) objects
Required: No

 ** permissionGroupId **   <a name="finspace-Type-PermissionGroupParams-permissionGroupId"></a>
The unique identifier for the `PermissionGroup`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 26.
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_PermissionGroupParams_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/finspace-2020-07-13/PermissionGroupParams)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/finspace-2020-07-13/PermissionGroupParams)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/finspace-2020-07-13/PermissionGroupParams)
