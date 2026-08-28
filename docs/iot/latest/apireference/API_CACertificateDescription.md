---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_CACertificateDescription.html
---

# CACertificateDescription
<a name="API_CACertificateDescription"></a>

Describes a CA certificate.

## Contents
<a name="API_CACertificateDescription_Contents"></a>

 ** autoRegistrationStatus **   <a name="iot-Type-CACertificateDescription-autoRegistrationStatus"></a>
Whether the CA certificate configured for auto registration of device certificates. Valid values are "ENABLE" and "DISABLE"
Type: String
Valid Values: `ENABLE | DISABLE`
Required: No

 ** certificateArn **   <a name="iot-Type-CACertificateDescription-certificateArn"></a>
The CA certificate ARN.
Type: String
Required: No

 ** certificateId **   <a name="iot-Type-CACertificateDescription-certificateId"></a>
The CA certificate ID.
Type: String
Length Constraints: Fixed length of 64.
Pattern: `(0x)?[a-fA-F0-9]+`
Required: No

 ** certificateMode **   <a name="iot-Type-CACertificateDescription-certificateMode"></a>
The mode of the CA.
All the device certificates that are registered using this CA will be registered in the same mode as the CA. For more information about certificate mode for device certificates, see [certificate mode](https://docs.aws.amazon.com/iot/latest/apireference/API_CertificateDescription.html#iot-Type-CertificateDescription-certificateMode).
Type: String
Valid Values: `DEFAULT | SNI_ONLY`
Required: No

 ** certificatePem **   <a name="iot-Type-CACertificateDescription-certificatePem"></a>
The CA certificate data, in PEM format.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 65536.
Pattern: `[\s\S]*`
Required: No

 ** creationDate **   <a name="iot-Type-CACertificateDescription-creationDate"></a>
The date the CA certificate was created.
Type: Timestamp
Required: No

 ** customerVersion **   <a name="iot-Type-CACertificateDescription-customerVersion"></a>
The customer version of the CA certificate.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** generationId **   <a name="iot-Type-CACertificateDescription-generationId"></a>
The generation ID of the CA certificate.
Type: String
Required: No

 ** lastModifiedDate **   <a name="iot-Type-CACertificateDescription-lastModifiedDate"></a>
The date the CA certificate was last modified.
Type: Timestamp
Required: No

 ** ownedBy **   <a name="iot-Type-CACertificateDescription-ownedBy"></a>
The owner of the CA certificate.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `[0-9]+`
Required: No

 ** status **   <a name="iot-Type-CACertificateDescription-status"></a>
The status of a CA certificate.
Type: String
Valid Values: `ACTIVE | INACTIVE`
Required: No

 ** validity **   <a name="iot-Type-CACertificateDescription-validity"></a>
When the CA certificate is valid.
Type: [CertificateValidity](API_CertificateValidity.md) object
Required: No

## See Also
<a name="API_CACertificateDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/CACertificateDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/CACertificateDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/CACertificateDescription)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
