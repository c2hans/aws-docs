---
source_url: https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_DeploymentParameters.html
---

# DeploymentParameters
<a name="API_DeploymentParameters"></a>

The deployment parameters for an experiment run, including dynamic extension parameters and tags.

## Contents
<a name="API_DeploymentParameters_Contents"></a>

 ** DynamicExtensionParameters **   <a name="appconfig-Type-DeploymentParameters-DynamicExtensionParameters"></a>
A map of extension parameters for the deployment.
Type: String to string map
Map Entries: Maximum number of 10 items.
Key Pattern: `^([^#\n]{1,96})#([^\/#\n]{1,64})$`
Value Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** Tags **   <a name="appconfig-Type-DeploymentParameters-Tags"></a>
The tags to assign to the deployment.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Maximum length of 256.
Required: No

## See Also
<a name="API_DeploymentParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appconfig-2019-10-09/DeploymentParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appconfig-2019-10-09/DeploymentParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appconfig-2019-10-09/DeploymentParameters)
