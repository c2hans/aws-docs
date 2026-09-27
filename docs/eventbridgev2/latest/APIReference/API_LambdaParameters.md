---
source_url: https://docs.aws.amazon.com/eventbridgev2/latest/APIReference/API_LambdaParameters.html
---

# LambdaParameters
<a name="API_LambdaParameters"></a>

Lambda invocation parameters for subscribers. Values are forwarded to the Lambda Invoke API. Every string member accepts a literal or a JSONata expression (e.g. "{% $events.Data.qualifier %}").

## Contents
<a name="API_LambdaParameters_Contents"></a>

 ** DurableExecutionName **   <a name="eventbridgev2-Type-LambdaParameters-DurableExecutionName"></a>
Durable execution name. Accepts a JSONata expression.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Required: No

 ** InvocationTimeoutSeconds **   <a name="eventbridgev2-Type-LambdaParameters-InvocationTimeoutSeconds"></a>
Timeout in seconds for each invocation of the target. String-typed so the value may be a JSONata expression.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Required: No

 ** InvocationType **   <a name="eventbridgev2-Type-LambdaParameters-InvocationType"></a>
Lambda invocation type. EVENT invokes the function asynchronously; REQUEST\_RESPONSE waits for its result.
Type: String
Valid Values: `EVENT | REQUEST_RESPONSE`
Required: No

 ** Qualifier **   <a name="eventbridgev2-Type-LambdaParameters-Qualifier"></a>
Lambda qualifier: $LATEST, $LATEST.PUBLISHED, a numeric version, or an alias. Accepts a JSONata expression.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Required: No

 ** TenantId **   <a name="eventbridgev2-Type-LambdaParameters-TenantId"></a>
Tenant identifier. Accepts a JSONata expression.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Required: No

## See Also
<a name="API_LambdaParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridgev2-2025-05-15/LambdaParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridgev2-2025-05-15/LambdaParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridgev2-2025-05-15/LambdaParameters)
