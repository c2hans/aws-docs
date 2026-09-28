---
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_HarnessHookLambdaTarget.html
---

# HarnessHookLambdaTarget
<a name="API_HarnessHookLambdaTarget"></a>

The configuration for an AWS Lambda hook target.

## Contents
<a name="API_HarnessHookLambdaTarget_Contents"></a>

 ** arn **   <a name="bedrockagentcorecontrol-Type-HarnessHookLambdaTarget-arn"></a>
The ARN of the Lambda function to invoke.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws(-[^:]+)?:lambda:[a-z0-9-]+:[0-9]{12}:function:.+`
Required: Yes

 ** failureMode **   <a name="bedrockagentcorecontrol-Type-HarnessHookLambdaTarget-failureMode"></a>
The behavior when the Lambda function times out, returns an error, or returns an invalid response. The default is `DENY`.
Type: String
Valid Values: `allow | deny`
Required: No

 ** timeoutSeconds **   <a name="bedrockagentcorecontrol-Type-HarnessHookLambdaTarget-timeoutSeconds"></a>
The maximum number of seconds to wait for the Lambda function response. The default is 60 seconds.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 900.
Required: No

## See Also
<a name="API_HarnessHookLambdaTarget_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/HarnessHookLambdaTarget)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/HarnessHookLambdaTarget)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/HarnessHookLambdaTarget)
