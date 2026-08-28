---
source_url: https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_EndPoint.html
---

# EndPoint
<a name="API_EndPoint"></a>

Contains information about the Amazon Kinesis data stream where you're sending real-time log data in a real-time log configuration.

## Contents
<a name="API_EndPoint_Contents"></a>

 ** StreamType **   <a name="cloudfront-Type-EndPoint-StreamType"></a>
The type of data stream where you are sending real-time log data. The only valid value is `Kinesis`.
Type: String
Required: Yes

 ** KinesisStreamConfig **   <a name="cloudfront-Type-EndPoint-KinesisStreamConfig"></a>
Contains information about the Amazon Kinesis data stream where you are sending real-time log data in a real-time log configuration.
Type: [KinesisStreamConfig](API_KinesisStreamConfig.md) object
Required: No

## See Also
<a name="API_EndPoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/EndPoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/EndPoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/EndPoint)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudfront` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
