---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsRedshiftClusterHsmStatus.html
---

# AwsRedshiftClusterHsmStatus
<a name="API_AwsRedshiftClusterHsmStatus"></a>

Information about whether an Amazon Redshift cluster finished applying any hardware changes to security module (HSM) settings that were specified in a modify cluster command.

## Contents
<a name="API_AwsRedshiftClusterHsmStatus_Contents"></a>

 ** HsmClientCertificateIdentifier **   <a name="securityhub-Type-AwsRedshiftClusterHsmStatus-HsmClientCertificateIdentifier"></a>
The name of the HSM client certificate that the Amazon Redshift cluster uses to retrieve the data encryption keys that are stored in an HSM.
Type: String
Pattern: `.*\S.*`
Required: No

 ** HsmConfigurationIdentifier **   <a name="securityhub-Type-AwsRedshiftClusterHsmStatus-HsmConfigurationIdentifier"></a>
The name of the HSM configuration that contains the information that the Amazon Redshift cluster can use to retrieve and store keys in an HSM.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Status **   <a name="securityhub-Type-AwsRedshiftClusterHsmStatus-Status"></a>
Indicates whether the Amazon Redshift cluster has finished applying any HSM settings changes specified in a modify cluster command.
Type: String
Valid values: `active` \| `applying`
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsRedshiftClusterHsmStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsRedshiftClusterHsmStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsRedshiftClusterHsmStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsRedshiftClusterHsmStatus)
