---
source_url: https://docs.aws.amazon.com/lambda/latest/api/API_StepDetails.html
---

# StepDetails
<a name="API_StepDetails"></a>

Details about a step operation.

## Contents
<a name="API_StepDetails_Contents"></a>

 ** Attempt **   <a name="lambda-Type-StepDetails-Attempt"></a>
The current attempt number for this step.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** Error **   <a name="lambda-Type-StepDetails-Error"></a>
Details about the step failure.
Type: [ErrorObject](API_ErrorObject.md) object
Required: No

 ** NextAttemptTimestamp **   <a name="lambda-Type-StepDetails-NextAttemptTimestamp"></a>
The date and time when the next attempt is scheduled, in [ISO-8601 format](https://www.w3.org/TR/NOTE-datetime) (YYYY-MM-DDThh:mm:ss.sTZD). Only populated when the step is in a pending state.
Type: Timestamp
Required: No

 ** Result **   <a name="lambda-Type-StepDetails-Result"></a>
The JSON response payload from the step operation.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 6291456.
Required: No

## See Also
<a name="API_StepDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-2015-03-31/StepDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-2015-03-31/StepDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-2015-03-31/StepDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Lambda. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lambda` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
