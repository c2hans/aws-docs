---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsMskClusterClusterInfoEncryptionInfoEncryptionInTransitDetails.html
---

# AwsMskClusterClusterInfoEncryptionInfoEncryptionInTransitDetails
<a name="API_AwsMskClusterClusterInfoEncryptionInfoEncryptionInTransitDetails"></a>

 The settings for encrypting data in transit.

## Contents
<a name="API_AwsMskClusterClusterInfoEncryptionInfoEncryptionInTransitDetails_Contents"></a>

 ** ClientBroker **   <a name="securityhub-Type-AwsMskClusterClusterInfoEncryptionInfoEncryptionInTransitDetails-ClientBroker"></a>
 Indicates the encryption setting for data in transit between clients and brokers.
Type: String
Pattern: `.*\S.*`
Required: No

 ** InCluster **   <a name="securityhub-Type-AwsMskClusterClusterInfoEncryptionInfoEncryptionInTransitDetails-InCluster"></a>
 When set to `true`, it indicates that data communication among the broker nodes of the cluster is encrypted. When set to `false`, the communication happens in plain text. The default value is `true`.
Type: Boolean
Required: No

## See Also
<a name="API_AwsMskClusterClusterInfoEncryptionInfoEncryptionInTransitDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsMskClusterClusterInfoEncryptionInfoEncryptionInTransitDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsMskClusterClusterInfoEncryptionInfoEncryptionInTransitDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsMskClusterClusterInfoEncryptionInfoEncryptionInTransitDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
