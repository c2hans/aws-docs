---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_CACertificate.html
---

# CACertificate
<a name="API_CACertificate"></a>

A CA certificate.

## Contents
<a name="API_CACertificate_Contents"></a>

 ** certificateArn **   <a name="iot-Type-CACertificate-certificateArn"></a>
The ARN of the CA certificate.
Type: String
Required: No

 ** certificateId **   <a name="iot-Type-CACertificate-certificateId"></a>
The ID of the CA certificate.
Type: String
Length Constraints: Fixed length of 64.
Pattern: `(0x)?[a-fA-F0-9]+`
Required: No

 ** creationDate **   <a name="iot-Type-CACertificate-creationDate"></a>
The date the CA certificate was created.
Type: Timestamp
Required: No

 ** status **   <a name="iot-Type-CACertificate-status"></a>
The status of the CA certificate.
The status value REGISTER\_INACTIVE is deprecated and should not be used.
Type: String
Valid Values: `ACTIVE | INACTIVE`
Required: No

## See Also
<a name="API_CACertificate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/CACertificate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/CACertificate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/CACertificate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
