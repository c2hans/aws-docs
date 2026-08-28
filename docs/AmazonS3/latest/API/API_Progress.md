---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_Progress.html
---

# Progress
<a name="API_Progress"></a>

This data type contains information about progress of an operation.

## Contents
<a name="API_Progress_Contents"></a>

 ** BytesProcessed **   <a name="AmazonS3-Type-Progress-BytesProcessed"></a>
The current number of uncompressed object bytes processed.
Type: Long
Required: No

 ** BytesReturned **   <a name="AmazonS3-Type-Progress-BytesReturned"></a>
The current number of bytes of records payload data returned.
Type: Long
Required: No

 ** BytesScanned **   <a name="AmazonS3-Type-Progress-BytesScanned"></a>
The current number of object bytes scanned.
Type: Long
Required: No

## See Also
<a name="API_Progress_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/Progress)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/Progress)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/Progress)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
