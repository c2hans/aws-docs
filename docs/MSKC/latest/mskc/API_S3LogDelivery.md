---
source_url: https://docs.aws.amazon.com/MSKC/latest/mskc/API_S3LogDelivery.html
---

# S3LogDelivery
<a name="API_S3LogDelivery"></a>

Details about delivering logs to Amazon S3.

## Contents
<a name="API_S3LogDelivery_Contents"></a>

 ** enabled **   <a name="MSKC-Type-S3LogDelivery-enabled"></a>
Specifies whether connector logs get sent to the specified Amazon S3 destination.
Type: Boolean
Required: Yes

 ** bucket **   <a name="MSKC-Type-S3LogDelivery-bucket"></a>
The name of the S3 bucket that is the destination for log delivery.
Type: String
Required: No

 ** prefix **   <a name="MSKC-Type-S3LogDelivery-prefix"></a>
The S3 prefix that is the destination for log delivery.
Type: String
Required: No

## See Also
<a name="API_S3LogDelivery_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kafkaconnect-2021-09-14/S3LogDelivery)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kafkaconnect-2021-09-14/S3LogDelivery)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kafkaconnect-2021-09-14/S3LogDelivery)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon MSK Connect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query MSKC` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
