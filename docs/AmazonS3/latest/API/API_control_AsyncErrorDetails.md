---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_AsyncErrorDetails.html
---

# AsyncErrorDetails
<a name="API_control_AsyncErrorDetails"></a>

Error details for the failed asynchronous operation.

## Contents
<a name="API_control_AsyncErrorDetails_Contents"></a>

 ** Code **   <a name="AmazonS3-Type-control_AsyncErrorDetails-Code"></a>
A string that uniquely identifies the error condition.
Type: String
Length Constraints: Maximum length of 1024.
Required: No

 ** Message **   <a name="AmazonS3-Type-control_AsyncErrorDetails-Message"></a>
A generic description of the error condition in English.
Type: String
Length Constraints: Maximum length of 1024.
Required: No

 ** RequestId **   <a name="AmazonS3-Type-control_AsyncErrorDetails-RequestId"></a>
The ID of the request associated with the error.
Type: String
Length Constraints: Maximum length of 1024.
Required: No

 ** Resource **   <a name="AmazonS3-Type-control_AsyncErrorDetails-Resource"></a>
The identifier of the resource associated with the error.
Type: String
Length Constraints: Maximum length of 1024.
Required: No

## See Also
<a name="API_control_AsyncErrorDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/AsyncErrorDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/AsyncErrorDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/AsyncErrorDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
