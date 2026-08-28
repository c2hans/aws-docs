---
source_url: https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_RetryConfigInput.html
---

# RetryConfigInput
<a name="API_RetryConfigInput"></a>

This structure contains information about the canary's retry configuration.

**Note**
The default account level concurrent execution limit from Lambda is 1000. When you have more than 1000 canaries, it's possible there are more than 1000 Lambda invocations due to retries and the console might hang. For more information on the Lambda execution limit, see [Understanding Lambda function scaling](https://docs.aws.amazon.com/lambda/latest/dg/lambda-concurrency.html#:~:text=As%20your%20functions%20receive%20more,functions%20in%20an%20AWS%20Region).

**Note**
For canary with `MaxRetries = 2`, you need to set the `CanaryRunConfigInput.TimeoutInSeconds` to less than 600 seconds to avoid validation errors.

## Contents
<a name="API_RetryConfigInput_Contents"></a>

 ** MaxRetries **   <a name="synthetics-Type-RetryConfigInput-MaxRetries"></a>
The maximum number of retries. The value must be less than or equal to 2.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 2.
Required: Yes

## See Also
<a name="API_RetryConfigInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/synthetics-2017-10-11/RetryConfigInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/synthetics-2017-10-11/RetryConfigInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/synthetics-2017-10-11/RetryConfigInput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch Synthetics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonSynthetics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
