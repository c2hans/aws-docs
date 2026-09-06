---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_ActionConfiguration.html
---

# ActionConfiguration
<a name="API_ActionConfiguration"></a>

Specifies an allowed action and its associated filter configuration.

## Contents
<a name="API_ActionConfiguration_Contents"></a>

 ** action **   <a name="qbusiness-Type-ActionConfiguration-action"></a>
The Amazon Q Business action that is allowed.
Type: String
Pattern: `qbusiness:[a-zA-Z]+`
Required: Yes

 ** filterConfiguration **   <a name="qbusiness-Type-ActionConfiguration-filterConfiguration"></a>
The filter configuration for the action, if any.
Type: [ActionFilterConfiguration](API_ActionFilterConfiguration.md) object
Required: No

## See Also
<a name="API_ActionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/ActionConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/ActionConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/ActionConfiguration)
