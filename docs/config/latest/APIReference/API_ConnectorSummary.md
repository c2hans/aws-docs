---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_ConnectorSummary.html
---

# ConnectorSummary
<a name="API_ConnectorSummary"></a>

A summary of a connector.

## Contents
<a name="API_ConnectorSummary_Contents"></a>

 ** arn **   <a name="config-Type-ConnectorSummary-arn"></a>
The Amazon Resource Name (ARN) of the connector.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Required: Yes

 ** createdTime **   <a name="config-Type-ConnectorSummary-createdTime"></a>
The date and time that the connector was created.
Type: Timestamp
Required: Yes

 ** name **   <a name="config-Type-ConnectorSummary-name"></a>
The name of the connector.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** provider **   <a name="config-Type-ConnectorSummary-provider"></a>
The third-party cloud service provider. Currently, `AZURE` is supported.
Type: String
Valid Values: `AZURE`
Required: Yes

 ** tenantIdentifier **   <a name="config-Type-ConnectorSummary-tenantIdentifier"></a>
The Azure tenant identifier for the connector.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

## See Also
<a name="API_ConnectorSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/ConnectorSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/ConnectorSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/ConnectorSummary)
