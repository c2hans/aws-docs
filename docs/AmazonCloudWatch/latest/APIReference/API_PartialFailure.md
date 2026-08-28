---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_PartialFailure.html
---

# PartialFailure
<a name="API_PartialFailure"></a>

This array is empty if the API operation was successful for all the rules specified in the request. If the operation could not process one of the rules, the following data is returned for each of those rules.

## Contents
<a name="API_PartialFailure_Contents"></a>

 ** ExceptionType **   <a name="ACW-Type-PartialFailure-ExceptionType"></a>
The type of error.
Type: String
Required: No

 ** FailureCode **   <a name="ACW-Type-PartialFailure-FailureCode"></a>
The code of the error.
Type: String
Required: No

 ** FailureDescription **   <a name="ACW-Type-PartialFailure-FailureDescription"></a>
A description of the error.
Type: String
Required: No

 ** FailureResource **   <a name="ACW-Type-PartialFailure-FailureResource"></a>
The specified rule that could not be deleted.
Type: String
Required: No

## See Also
<a name="API_PartialFailure_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/PartialFailure)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/PartialFailure)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/PartialFailure)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
