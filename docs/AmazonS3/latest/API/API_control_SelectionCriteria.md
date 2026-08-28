---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_SelectionCriteria.html
---

# SelectionCriteria
<a name="API_control_SelectionCriteria"></a>

## Contents
<a name="API_control_SelectionCriteria_Contents"></a>

 ** Delimiter **   <a name="AmazonS3-Type-control_SelectionCriteria-Delimiter"></a>
A container for the delimiter of the selection criteria being used.
Type: String
Length Constraints: Maximum length of 1.
Required: No

 ** MaxDepth **   <a name="AmazonS3-Type-control_SelectionCriteria-MaxDepth"></a>
The max depth of the selection criteria
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 10.
Required: No

 ** MinStorageBytesPercentage **   <a name="AmazonS3-Type-control_SelectionCriteria-MinStorageBytesPercentage"></a>
The minimum percentage of total bucket storage that a prefix must hold for its metrics to be included.
Type: Double
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

## See Also
<a name="API_control_SelectionCriteria_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/SelectionCriteria)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/SelectionCriteria)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/SelectionCriteria)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
