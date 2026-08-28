---
source_url: https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_ConnectorSummary.html
---

# ConnectorSummary
<a name="API_ConnectorSummary"></a>

Summary description of the AWS Private CA AD connectors belonging to an AWS account.

## Contents
<a name="API_ConnectorSummary_Contents"></a>

 ** Arn **   <a name="PcaConnectorAd-Type-ConnectorSummary-Arn"></a>
 The Amazon Resource Name (ARN) that was returned when you called [CreateConnector](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateConnector.html).
Type: String
Length Constraints: Minimum length of 5. Maximum length of 200.
Pattern: `arn:[\w-]+:pca-connector-ad:[\w-]+:[0-9]+:connector\/[0-9a-f]{8}(-[0-9a-f]{4}){3}-[0-9a-f]{12}`
Required: No

 ** CertificateAuthorityArn **   <a name="PcaConnectorAd-Type-ConnectorSummary-CertificateAuthorityArn"></a>
The Amazon Resource Name (ARN) of the certificate authority being used.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 200.
Pattern: `arn:[\w-]+:acm-pca:[\w-]+:[0-9]+:certificate-authority\/[0-9a-f]{8}(-[0-9a-f]{4}){3}-[0-9a-f]{12}`
Required: No

 ** CertificateEnrollmentPolicyServerEndpoint **   <a name="PcaConnectorAd-Type-ConnectorSummary-CertificateEnrollmentPolicyServerEndpoint"></a>
Certificate enrollment endpoint for Active Directory domain-joined objects to request certificates.
Type: String
Required: No

 ** CreatedAt **   <a name="PcaConnectorAd-Type-ConnectorSummary-CreatedAt"></a>
The date and time that the connector was created.
Type: Timestamp
Required: No

 ** DirectoryId **   <a name="PcaConnectorAd-Type-ConnectorSummary-DirectoryId"></a>
The identifier of the Active Directory.
Type: String
Pattern: `d-[0-9a-f]{10}`
Required: No

 ** Status **   <a name="PcaConnectorAd-Type-ConnectorSummary-Status"></a>
Status of the connector. Status can be creating, active, deleting, or failed.
Type: String
Valid Values: `CREATING | ACTIVE | DELETING | FAILED`
Required: No

 ** StatusReason **   <a name="PcaConnectorAd-Type-ConnectorSummary-StatusReason"></a>
Additional information about the connector status if the status is failed.
Type: String
Valid Values: `CA_CERTIFICATE_REGISTRATION_FAILED | DIRECTORY_ACCESS_DENIED | INTERNAL_FAILURE | INSUFFICIENT_FREE_ADDRESSES | INVALID_SUBNET_IP_PROTOCOL | PRIVATECA_ACCESS_DENIED | PRIVATECA_RESOURCE_NOT_FOUND | SECURITY_GROUP_NOT_IN_VPC | VPC_ACCESS_DENIED | VPC_ENDPOINT_LIMIT_EXCEEDED | VPC_RESOURCE_NOT_FOUND`
Required: No

 ** UpdatedAt **   <a name="PcaConnectorAd-Type-ConnectorSummary-UpdatedAt"></a>
The date and time that the connector was updated.
Type: Timestamp
Required: No

 ** VpcInformation **   <a name="PcaConnectorAd-Type-ConnectorSummary-VpcInformation"></a>
Information of the VPC and security group(s) used with the connector.
Type: [VpcInformation](API_VpcInformation.md) object
Required: No

## See Also
<a name="API_ConnectorSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pca-connector-ad-2018-05-10/ConnectorSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pca-connector-ad-2018-05-10/ConnectorSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pca-connector-ad-2018-05-10/ConnectorSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Private CA Connector for Active Directory. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pca-connector-ad` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
