---
source_url: https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_KinesisFirehoseDestination.html
---

# KinesisFirehoseDestination
<a name="API_KinesisFirehoseDestination"></a>

An object that defines an Amazon Kinesis Data Firehose destination for email events. You can use Amazon Kinesis Data Firehose to stream data to other services, such as Amazon S3 and Amazon Redshift.

## Contents
<a name="API_KinesisFirehoseDestination_Contents"></a>

 ** DeliveryStreamArn **   <a name="pinpoint-Type-KinesisFirehoseDestination-DeliveryStreamArn"></a>
The Amazon Resource Name (ARN) of the Amazon Kinesis Data Firehose stream that Amazon Pinpoint sends email events to.
Type: String
Required: Yes

 ** IamRoleArn **   <a name="pinpoint-Type-KinesisFirehoseDestination-IamRoleArn"></a>
The Amazon Resource Name (ARN) of the IAM role that Amazon Pinpoint uses when sending email events to the Amazon Kinesis Data Firehose stream.
Type: String
Required: Yes

## See Also
<a name="API_KinesisFirehoseDestination_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-email-2018-07-26/KinesisFirehoseDestination)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-email-2018-07-26/KinesisFirehoseDestination)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-email-2018-07-26/KinesisFirehoseDestination)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Pinpoint Email. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pinpoint-email` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
