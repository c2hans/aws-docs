---
source_url: https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_Connector.html
---

# Connector
<a name="API_Connector"></a>

 AWS Private CA Connector for Active Directory is a service that links your Active Directory with AWS Private CA. The connector brokers the exchange of certificates from AWS Private CA to domain-joined users and machines managed with Active Directory.

## Contents
<a name="API_Connector_Contents"></a>

 ** Arn **   <a name="PcaConnectorAd-Type-Connector-Arn"></a>
The Amazon Resource Name (ARN) that was returned when you called [CreateConnector](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateConnector.html).
Type: String
Length Constraints: Minimum length of 5. Maximum length of 200.
Pattern: `arn:[\w-]+:pca-connector-ad:[\w-]+:[0-9]+:connector\/[0-9a-f]{8}(-[0-9a-f]{4}){3}-[0-9a-f]{12}`
Required: No

 ** CertificateAuthorityArn **   <a name="PcaConnectorAd-Type-Connector-CertificateAuthorityArn"></a>
The Amazon Resource Name (ARN) of the certificate authority being used.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 200.
Pattern: `arn:[\w-]+:acm-pca:[\w-]+:[0-9]+:certificate-authority\/[0-9a-f]{8}(-[0-9a-f]{4}){3}-[0-9a-f]{12}`
Required: No

 ** CertificateEnrollmentPolicyServerEndpoint **   <a name="PcaConnectorAd-Type-Connector-CertificateEnrollmentPolicyServerEndpoint"></a>
Certificate enrollment endpoint for Active Directory domain-joined objects reach out to when requesting certificates.
Type: String
Required: No

 ** CreatedAt **   <a name="PcaConnectorAd-Type-Connector-CreatedAt"></a>
The date and time that the connector was created.
Type: Timestamp
Required: No

 ** DirectoryId **   <a name="PcaConnectorAd-Type-Connector-DirectoryId"></a>
The identifier of the Active Directory.
Type: String
Pattern: `d-[0-9a-f]{10}`
Required: No

 ** Status **   <a name="PcaConnectorAd-Type-Connector-Status"></a>
Status of the connector. Status can be creating, active, deleting, or failed.
Type: String
Valid Values: `CREATING | ACTIVE | DELETING | FAILED`
Required: No

 ** StatusReason **   <a name="PcaConnectorAd-Type-Connector-StatusReason"></a>
Additional information about the connector status if the status is failed.
Type: String
Valid Values: `CA_CERTIFICATE_REGISTRATION_FAILED | DIRECTORY_ACCESS_DENIED | INTERNAL_FAILURE | INSUFFICIENT_FREE_ADDRESSES | INVALID_SUBNET_IP_PROTOCOL | PRIVATECA_ACCESS_DENIED | PRIVATECA_RESOURCE_NOT_FOUND | SECURITY_GROUP_NOT_IN_VPC | VPC_ACCESS_DENIED | VPC_ENDPOINT_LIMIT_EXCEEDED | VPC_RESOURCE_NOT_FOUND`
Required: No

 ** UpdatedAt **   <a name="PcaConnectorAd-Type-Connector-UpdatedAt"></a>
The date and time that the connector was updated.
Type: Timestamp
Required: No

 ** VpcInformation **   <a name="PcaConnectorAd-Type-Connector-VpcInformation"></a>
Information of the VPC and security group(s) used with the connector.
Type: [VpcInformation](API_VpcInformation.md) object
Required: No

## See Also
<a name="API_Connector_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pca-connector-ad-2018-05-10/Connector)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pca-connector-ad-2018-05-10/Connector)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pca-connector-ad-2018-05-10/Connector)
