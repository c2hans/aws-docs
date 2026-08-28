---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_ConfigExportDeliveryInfo.html
---

# ConfigExportDeliveryInfo
<a name="API_ConfigExportDeliveryInfo"></a>

Provides status of the delivery of the snapshot or the configuration history to the specified Amazon S3 bucket. Also provides the status of notifications about the Amazon S3 delivery to the specified Amazon SNS topic.

## Contents
<a name="API_ConfigExportDeliveryInfo_Contents"></a>

 ** lastAttemptTime **   <a name="config-Type-ConfigExportDeliveryInfo-lastAttemptTime"></a>
The time of the last attempted delivery.
Type: Timestamp
Required: No

 ** lastErrorCode **   <a name="config-Type-ConfigExportDeliveryInfo-lastErrorCode"></a>
The error code from the last attempted delivery.
Type: String
Required: No

 ** lastErrorMessage **   <a name="config-Type-ConfigExportDeliveryInfo-lastErrorMessage"></a>
The error message from the last attempted delivery.
Type: String
Required: No

 ** lastStatus **   <a name="config-Type-ConfigExportDeliveryInfo-lastStatus"></a>
Status of the last attempted delivery.
Type: String
Valid Values: `Success | Failure | Not_Applicable`
Required: No

 ** lastSuccessfulTime **   <a name="config-Type-ConfigExportDeliveryInfo-lastSuccessfulTime"></a>
The time of the last successful delivery.
Type: Timestamp
Required: No

 ** nextDeliveryTime **   <a name="config-Type-ConfigExportDeliveryInfo-nextDeliveryTime"></a>
The time that the next delivery occurs.
Type: Timestamp
Required: No

## See Also
<a name="API_ConfigExportDeliveryInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/ConfigExportDeliveryInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/ConfigExportDeliveryInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/ConfigExportDeliveryInfo)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
