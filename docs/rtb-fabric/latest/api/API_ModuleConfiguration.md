---
source_url: https://docs.aws.amazon.com/rtb-fabric/latest/api/API_ModuleConfiguration.html
---

# ModuleConfiguration
<a name="API_ModuleConfiguration"></a>

Describes the configuration of a module.

## Contents
<a name="API_ModuleConfiguration_Contents"></a>

 ** name **   <a name="rtbfabric-Type-ModuleConfiguration-name"></a>
The name of the module.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `[A-Za-z0-9 -]+`
Required: Yes

 ** dependsOn **   <a name="rtbfabric-Type-ModuleConfiguration-dependsOn"></a>
The dependencies of the module.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `[A-Za-z0-9 -]+`
Required: No

 ** moduleParameters **   <a name="rtbfabric-Type-ModuleConfiguration-moduleParameters"></a>
Describes the parameters of a module.
Type: [ModuleParameters](API_ModuleParameters.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** version **   <a name="rtbfabric-Type-ModuleConfiguration-version"></a>
The version of the module.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 25.
Pattern: `[a-z0-9-]{1,25}`
Required: No

## See Also
<a name="API_ModuleConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rtbfabric-2023-05-15/ModuleConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rtbfabric-2023-05-15/ModuleConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rtbfabric-2023-05-15/ModuleConfiguration)
