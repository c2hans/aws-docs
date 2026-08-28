---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_MatchObjectSize.html
---

# MatchObjectSize
<a name="API_control_MatchObjectSize"></a>

 A filter condition that specifies the object size range of included objects in bytes. Only integers are supported.

## Contents
<a name="API_control_MatchObjectSize_Contents"></a>

 ** BytesGreaterThan **   <a name="AmazonS3-Type-control_MatchObjectSize-BytesGreaterThan"></a>
 Specifies the minimum object size in Bytes. The value must be a positive number, greater than 0 and less than 50 TB.
Type: Long
Required: No

 ** BytesLessThan **   <a name="AmazonS3-Type-control_MatchObjectSize-BytesLessThan"></a>
 Specifies the maximum object size in Bytes. The value must be a positive number, greater than the minimum object size and less than 50 TB.
Type: Long
Required: No

## See Also
<a name="API_control_MatchObjectSize_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/MatchObjectSize)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/MatchObjectSize)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/MatchObjectSize)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
