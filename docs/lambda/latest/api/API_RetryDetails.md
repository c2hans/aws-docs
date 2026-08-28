---
source_url: https://docs.aws.amazon.com/lambda/latest/api/API_RetryDetails.html
---

# RetryDetails
<a name="API_RetryDetails"></a>

Information about retry attempts for an operation.

## Contents
<a name="API_RetryDetails_Contents"></a>

 ** CurrentAttempt **   <a name="lambda-Type-RetryDetails-CurrentAttempt"></a>
The current attempt number for this operation.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** NextAttemptDelaySeconds **   <a name="lambda-Type-RetryDetails-NextAttemptDelaySeconds"></a>
The delay before the next retry attempt, in seconds.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

## See Also
<a name="API_RetryDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-2015-03-31/RetryDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-2015-03-31/RetryDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-2015-03-31/RetryDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Lambda. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lambda` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
