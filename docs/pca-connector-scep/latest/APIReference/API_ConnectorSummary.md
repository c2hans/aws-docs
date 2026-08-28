---
source_url: https://docs.aws.amazon.com/pca-connector-scep/latest/APIReference/API_ConnectorSummary.html
---

# ConnectorSummary
<a name="API_ConnectorSummary"></a>

Lists the AWS Private CA SCEP connectors belonging to your AWS account.

## Contents
<a name="API_ConnectorSummary_Contents"></a>

 ** Arn **   <a name="pcaconnectorscep-Type-ConnectorSummary-Arn"></a>
The Amazon Resource Name (ARN) of the connector.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 200.
Pattern: `arn:aws(-[a-z]+)*:pca-connector-scep:[a-z]+(-[a-z]+)+-[1-9]\d*:\d{12}:connector\/[0-9a-f]{8}(-[0-9a-f]{4}){3}-[0-9a-f]{12}`
Required: No

 ** CertificateAuthorityArn **   <a name="pcaconnectorscep-Type-ConnectorSummary-CertificateAuthorityArn"></a>
The Amazon Resource Name (ARN) of the connector's associated certificate authority.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 200.
Pattern: `arn:aws(-[a-z]+)*:acm-pca:[a-z]+(-[a-z]+)+-[1-9]\d*:\d{12}:certificate-authority\/[0-9a-f]{8}(-[0-9a-f]{4}){3}-[0-9a-f]{12}`
Required: No

 ** CreatedAt **   <a name="pcaconnectorscep-Type-ConnectorSummary-CreatedAt"></a>
The date and time that the challenge was created.
Type: Timestamp
Required: No

 ** Endpoint **   <a name="pcaconnectorscep-Type-ConnectorSummary-Endpoint"></a>
The connector's HTTPS public SCEP URL.
Type: String
Required: No

 ** MobileDeviceManagement **   <a name="pcaconnectorscep-Type-ConnectorSummary-MobileDeviceManagement"></a>
Contains settings relevant to the mobile device management system that you chose for the connector. If you didn't configure `MobileDeviceManagement`, then the connector is for general-purpose use and this object is empty.
Type: [MobileDeviceManagement](API_MobileDeviceManagement.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** OpenIdConfiguration **   <a name="pcaconnectorscep-Type-ConnectorSummary-OpenIdConfiguration"></a>
Contains OpenID Connect (OIDC) parameters for use with Microsoft Intune.
Type: [OpenIdConfiguration](API_OpenIdConfiguration.md) object
Required: No

 ** Status **   <a name="pcaconnectorscep-Type-ConnectorSummary-Status"></a>
The connector's status. Status can be creating, active, deleting, or failed.
Type: String
Valid Values: `CREATING | ACTIVE | DELETING | FAILED`
Required: No

 ** StatusReason **   <a name="pcaconnectorscep-Type-ConnectorSummary-StatusReason"></a>
Information about why connector creation failed, if status is `FAILED`.
Type: String
Valid Values: `INTERNAL_FAILURE | PRIVATECA_ACCESS_DENIED | PRIVATECA_INVALID_STATE | PRIVATECA_RESOURCE_NOT_FOUND | VPC_ENDPOINT_RESOURCE_NOT_FOUND | VPC_ENDPOINT_DNS_ENTRIES_NOT_FOUND`
Required: No

 ** Type **   <a name="pcaconnectorscep-Type-ConnectorSummary-Type"></a>
The connector type.
Type: String
Valid Values: `GENERAL_PURPOSE | INTUNE`
Required: No

 ** UpdatedAt **   <a name="pcaconnectorscep-Type-ConnectorSummary-UpdatedAt"></a>
The date and time that the challenge was updated.
Type: Timestamp
Required: No

## See Also
<a name="API_ConnectorSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pca-connector-scep-2018-05-10/ConnectorSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pca-connector-scep-2018-05-10/ConnectorSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pca-connector-scep-2018-05-10/ConnectorSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Private CA Connector for SCEP. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pca-connector-scep` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
