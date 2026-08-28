---
source_url: https://docs.aws.amazon.com/MSKC/latest/mskc/API_FirehoseLogDelivery.html
---

# FirehoseLogDelivery
<a name="API_FirehoseLogDelivery"></a>

The settings for delivering logs to Amazon Kinesis Data Firehose.

## Contents
<a name="API_FirehoseLogDelivery_Contents"></a>

 ** enabled **   <a name="MSKC-Type-FirehoseLogDelivery-enabled"></a>
Specifies whether connector logs get delivered to Amazon Kinesis Data Firehose.
Type: Boolean
Required: Yes

 ** deliveryStream **   <a name="MSKC-Type-FirehoseLogDelivery-deliveryStream"></a>
The name of the Kinesis Data Firehose delivery stream that is the destination for log delivery.
Type: String
Required: No

## See Also
<a name="API_FirehoseLogDelivery_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kafkaconnect-2021-09-14/FirehoseLogDelivery)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kafkaconnect-2021-09-14/FirehoseLogDelivery)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kafkaconnect-2021-09-14/FirehoseLogDelivery)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon MSK Connect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query MSKC` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
