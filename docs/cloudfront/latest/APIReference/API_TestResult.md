---
source_url: https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_TestResult.html
---

# TestResult
<a name="API_TestResult"></a>

Contains the result of testing a CloudFront function with `TestFunction`.

## Contents
<a name="API_TestResult_Contents"></a>

 ** ComputeUtilization **   <a name="cloudfront-Type-TestResult-ComputeUtilization"></a>
The amount of time that the function took to run as a percentage of the maximum allowed time. For example, a compute utilization of 35 means that the function completed in 35% of the maximum allowed time.
Type: String
Required: No

 ** FunctionErrorMessage **   <a name="cloudfront-Type-TestResult-FunctionErrorMessage"></a>
If the result of testing the function was an error, this field contains the error message.
Type: String
Required: No

 ** FunctionExecutionLogs **   <a name="cloudfront-Type-TestResult-FunctionExecutionLogs"></a>
Contains the log lines that the function wrote (if any) when running the test.
Type: Array of strings
Required: No

 ** FunctionOutput **   <a name="cloudfront-Type-TestResult-FunctionOutput"></a>
The event object returned by the function. For more information about the structure of the event object, see [Event object structure](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/functions-event-structure.html) in the *Amazon CloudFront Developer Guide*.
Type: String
Required: No

 ** FunctionSummary **   <a name="cloudfront-Type-TestResult-FunctionSummary"></a>
Contains configuration information and metadata about the CloudFront function that was tested.
Type: [FunctionSummary](API_FunctionSummary.md) object
Required: No

## See Also
<a name="API_TestResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/TestResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/TestResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/TestResult)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudfront` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
