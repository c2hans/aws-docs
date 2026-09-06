---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_ScopeConfiguration.html
---

# ScopeConfiguration
<a name="API_ScopeConfiguration"></a>

The scope of resources that Amazon Inspector scans for a single scanning type, including the scope level, the targeted resources, and the current state.

## Contents
<a name="API_ScopeConfiguration_Contents"></a>

 ** scopeType **   <a name="inspector2-Type-ScopeConfiguration-scopeType"></a>
The type of scope. Valid values are `TENANT`, which scans all resources in the Azure tenant, and `SUBSCRIPTION`, which scans only the resources in the specified Azure subscriptions.
Type: String
Valid Values: `TENANT | SUBSCRIPTION`
Required: Yes

 ** scopeValues **   <a name="inspector2-Type-ScopeConfiguration-scopeValues"></a>
The list of scope values. For subscription-level scope, these are Azure subscription IDs.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: No

 ** state **   <a name="inspector2-Type-ScopeConfiguration-state"></a>
The current state of the scope configuration.
Type: String
Valid Values: `ACTIVE | PENDING | ERROR | DISABLED`
Required: No

 ** stateReason **   <a name="inspector2-Type-ScopeConfiguration-stateReason"></a>
The reason for the current state of the scope configuration.
Type: String
Required: No

## See Also
<a name="API_ScopeConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/ScopeConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/ScopeConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/ScopeConfiguration)
