---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_InboundConnectorSummary.html
---

# InboundConnectorSummary

A summary of an inbound connector, including its ID, ARN, name, status, tenant URL, configuration, and timestamps.

## Contents
<a name="API_InboundConnectorSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Arn **   <a name="QS-Type-InboundConnectorSummary-Arn"></a>
The ARN of the inbound connector.
Type: String
Required: Yes

 ** CreatedTime **   <a name="QS-Type-InboundConnectorSummary-CreatedTime"></a>
The time when the inbound connector was created.
Type: Timestamp
Required: Yes

 ** InboundConnectorConfiguration **   <a name="QS-Type-InboundConnectorSummary-InboundConnectorConfiguration"></a>
The configuration of the inbound connector.
Type: [InboundConnectorConfig](API_InboundConnectorConfig.md) object
Required: Yes

 ** InboundConnectorId **   <a name="QS-Type-InboundConnectorSummary-InboundConnectorId"></a>
The ID of the inbound connector.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`
Required: Yes

 ** LastUpdatedTime **   <a name="QS-Type-InboundConnectorSummary-LastUpdatedTime"></a>
The time when the inbound connector was last updated.
Type: Timestamp
Required: Yes

 ** Name **   <a name="QS-Type-InboundConnectorSummary-Name"></a>
The name of the inbound connector.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** Status **   <a name="QS-Type-InboundConnectorSummary-Status"></a>
The status of the inbound connector.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: Yes

 ** TenantUrl **   <a name="QS-Type-InboundConnectorSummary-TenantUrl"></a>
The endpoint URL that clients use to reach Quick Sight through the inbound connector.
Type: String
Required: Yes

 ** Description **   <a name="QS-Type-InboundConnectorSummary-Description"></a>
The description of the inbound connector.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[A-Za-z0-9 _.,!?\-]*`
Required: No

## See Also
<a name="API_InboundConnectorSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/InboundConnectorSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/InboundConnectorSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/InboundConnectorSummary)
