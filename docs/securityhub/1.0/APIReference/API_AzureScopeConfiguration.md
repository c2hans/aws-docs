---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AzureScopeConfiguration.html
---

# AzureScopeConfiguration
<a name="API_AzureScopeConfiguration"></a>

The scope configuration for an Azure connector, defining the tenant or subscription scope.

## Contents
<a name="API_AzureScopeConfiguration_Contents"></a>

 ** ScopeType **   <a name="securityhub-Type-AzureScopeConfiguration-ScopeType"></a>
The type of scope. Valid values are `tenant` and `subscription`.
Type: String
Valid Values: `TENANT | SUBSCRIPTION`
Required: Yes

 ** ScopeValues **   <a name="securityhub-Type-AzureScopeConfiguration-ScopeValues"></a>
The list of scope values, such as subscription IDs, when the scope type is `subscription`.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AzureScopeConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AzureScopeConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AzureScopeConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AzureScopeConfiguration)
