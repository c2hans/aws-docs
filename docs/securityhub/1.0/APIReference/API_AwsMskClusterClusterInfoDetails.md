---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsMskClusterClusterInfoDetails.html
---

# AwsMskClusterClusterInfoDetails
<a name="API_AwsMskClusterClusterInfoDetails"></a>

 Provide details about an Amazon Managed Streaming for Apache Kafka (Amazon MSK) cluster.

## Contents
<a name="API_AwsMskClusterClusterInfoDetails_Contents"></a>

 ** ClientAuthentication **   <a name="securityhub-Type-AwsMskClusterClusterInfoDetails-ClientAuthentication"></a>
 Provides information for different modes of client authentication.
Type: [AwsMskClusterClusterInfoClientAuthenticationDetails](API_AwsMskClusterClusterInfoClientAuthenticationDetails.md) object
Required: No

 ** ClusterName **   <a name="securityhub-Type-AwsMskClusterClusterInfoDetails-ClusterName"></a>
 The name of the cluster.
Type: String
Pattern: `.*\S.*`
Required: No

 ** CurrentVersion **   <a name="securityhub-Type-AwsMskClusterClusterInfoDetails-CurrentVersion"></a>
 The current version of the cluster.
Type: String
Pattern: `.*\S.*`
Required: No

 ** EncryptionInfo **   <a name="securityhub-Type-AwsMskClusterClusterInfoDetails-EncryptionInfo"></a>
 Includes encryption-related information, such as the AWS KMS key used for encrypting data at rest and whether you want Amazon MSK to encrypt your data in transit.
Type: [AwsMskClusterClusterInfoEncryptionInfoDetails](API_AwsMskClusterClusterInfoEncryptionInfoDetails.md) object
Required: No

 ** EnhancedMonitoring **   <a name="securityhub-Type-AwsMskClusterClusterInfoDetails-EnhancedMonitoring"></a>
 Specifies the level of monitoring for the cluster.
Type: String
Pattern: `.*\S.*`
Required: No

 ** NumberOfBrokerNodes **   <a name="securityhub-Type-AwsMskClusterClusterInfoDetails-NumberOfBrokerNodes"></a>
 The number of broker nodes in the cluster.
Type: Integer
Required: No

## See Also
<a name="API_AwsMskClusterClusterInfoDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsMskClusterClusterInfoDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsMskClusterClusterInfoDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsMskClusterClusterInfoDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
