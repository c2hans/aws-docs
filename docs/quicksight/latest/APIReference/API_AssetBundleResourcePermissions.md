---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_AssetBundleResourcePermissions.html
---

# AssetBundleResourcePermissions
<a name="API_AssetBundleResourcePermissions"></a>

A structure that contains the permissions for the resource that you want to override in an asset bundle import job.

## Contents
<a name="API_AssetBundleResourcePermissions_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Actions **   <a name="QS-Type-AssetBundleResourcePermissions-Actions"></a>
A list of IAM actions to grant permissions on.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Required: Yes

 ** Principals **   <a name="QS-Type-AssetBundleResourcePermissions-Principals"></a>
A list of principals to grant permissions on.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 64 items.
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

## See Also
<a name="API_AssetBundleResourcePermissions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/AssetBundleResourcePermissions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/AssetBundleResourcePermissions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/AssetBundleResourcePermissions)
