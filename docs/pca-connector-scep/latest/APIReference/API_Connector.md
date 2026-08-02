---
source_url: https://docs.aws.amazon.com/pca-connector-scep/latest/APIReference/API_Connector.html
---

# Connector
<a name="API_Connector"></a>

Connector for SCEP is a service that links AWS Private Certificate Authority to your SCEP-enabled devices. The connector brokers the exchange of certificates from AWS Private CA to your SCEP-enabled devices and mobile device management systems. The connector is a complex type that contains the connector's configuration settings.

## Contents
<a name="API_Connector_Contents"></a>

 ** Arn **   <a name="pcaconnectorscep-Type-Connector-Arn"></a>
The Amazon Resource Name (ARN) of the connector.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 200.
Pattern: `arn:aws(-[a-z]+)*:pca-connector-scep:[a-z]+(-[a-z]+)+-[1-9]\d*:\d{12}:connector\/[0-9a-f]{8}(-[0-9a-f]{4}){3}-[0-9a-f]{12}`
Required: No

 ** CertificateAuthorityArn **   <a name="pcaconnectorscep-Type-Connector-CertificateAuthorityArn"></a>
The Amazon Resource Name (ARN) of the certificate authority associated with the connector.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 200.
Pattern: `arn:aws(-[a-z]+)*:acm-pca:[a-z]+(-[a-z]+)+-[1-9]\d*:\d{12}:certificate-authority\/[0-9a-f]{8}(-[0-9a-f]{4}){3}-[0-9a-f]{12}`
Required: No

 ** CreatedAt **   <a name="pcaconnectorscep-Type-Connector-CreatedAt"></a>
The date and time that the connector was created.
Type: Timestamp
Required: No

 ** Endpoint **   <a name="pcaconnectorscep-Type-Connector-Endpoint"></a>
The connector's HTTPS public SCEP URL.
Type: String
Required: No

 ** MobileDeviceManagement **   <a name="pcaconnectorscep-Type-Connector-MobileDeviceManagement"></a>
Contains settings relevant to the mobile device management system that you chose for the connector. If you didn't configure `MobileDeviceManagement`, then the connector is for general-purpose use and this object is empty.
Type: [MobileDeviceManagement](API_MobileDeviceManagement.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** OpenIdConfiguration **   <a name="pcaconnectorscep-Type-Connector-OpenIdConfiguration"></a>
Contains OpenID Connect (OIDC) parameters for use with Connector for SCEP for Microsoft Intune. For more information about using Connector for SCEP for Microsoft Intune, see [Using Connector for SCEP for Microsoft Intune](https://docs.aws.amazon.com/privateca/latest/userguide/scep-connector.htmlconnector-for-scep-intune.html).
Type: [OpenIdConfiguration](API_OpenIdConfiguration.md) object
Required: No

 ** Status **   <a name="pcaconnectorscep-Type-Connector-Status"></a>
The connector's status.
Type: String
Valid Values: `CREATING | ACTIVE | DELETING | FAILED`
Required: No

 ** StatusReason **   <a name="pcaconnectorscep-Type-Connector-StatusReason"></a>
Information about why connector creation failed, if status is `FAILED`.
Type: String
Valid Values: `INTERNAL_FAILURE | PRIVATECA_ACCESS_DENIED | PRIVATECA_INVALID_STATE | PRIVATECA_RESOURCE_NOT_FOUND | VPC_ENDPOINT_RESOURCE_NOT_FOUND | VPC_ENDPOINT_DNS_ENTRIES_NOT_FOUND`
Required: No

 ** Type **   <a name="pcaconnectorscep-Type-Connector-Type"></a>
The connector type.
Type: String
Valid Values: `GENERAL_PURPOSE | INTUNE`
Required: No

 ** UpdatedAt **   <a name="pcaconnectorscep-Type-Connector-UpdatedAt"></a>
The date and time that the connector was updated.
Type: Timestamp
Required: No

## See Also
<a name="API_Connector_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pca-connector-scep-2018-05-10/Connector)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pca-connector-scep-2018-05-10/Connector)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pca-connector-scep-2018-05-10/Connector)
