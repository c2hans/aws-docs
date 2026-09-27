---
source_url: https://docs.aws.amazon.com/eventbridgev2/latest/APIReference/API_UniversalTargetParameters.html
---

# UniversalTargetParameters
<a name="API_UniversalTargetParameters"></a>

Parameters for USI (Universal Service Integration) targets. Used when TargetArn is in the format arn:aws:events:::aws-sdk:{service}:{apiAction}

## Contents
<a name="API_UniversalTargetParameters_Contents"></a>

 ** Input **   <a name="eventbridgev2-Type-UniversalTargetParameters-Input"></a>
JSON string or JSONata expression that produces the API request. Supports {% ... %} JSONata expressions for dynamic values from the event.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 262144.
Required: Yes

 ** InvocationTimeoutSeconds **   <a name="eventbridgev2-Type-UniversalTargetParameters-InvocationTimeoutSeconds"></a>
Timeout in seconds for each invocation of the target (1-30, default 30). Must be a literal integer; JSONata expressions are not supported for this field. String-typed to match the other targets' timeout fields. Defaults to 30s when unset.
Type: String
Required: No

## See Also
<a name="API_UniversalTargetParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridgev2-2025-05-15/UniversalTargetParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridgev2-2025-05-15/UniversalTargetParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridgev2-2025-05-15/UniversalTargetParameters)
