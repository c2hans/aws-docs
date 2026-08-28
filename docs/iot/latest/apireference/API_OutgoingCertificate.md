---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_OutgoingCertificate.html
---

# OutgoingCertificate
<a name="API_OutgoingCertificate"></a>

A certificate that has been transferred but not yet accepted.

## Contents
<a name="API_OutgoingCertificate_Contents"></a>

 ** certificateArn **   <a name="iot-Type-OutgoingCertificate-certificateArn"></a>
The certificate ARN.
Type: String
Required: No

 ** certificateId **   <a name="iot-Type-OutgoingCertificate-certificateId"></a>
The certificate ID.
Type: String
Length Constraints: Fixed length of 64.
Pattern: `(0x)?[a-fA-F0-9]+`
Required: No

 ** creationDate **   <a name="iot-Type-OutgoingCertificate-creationDate"></a>
The certificate creation date.
Type: Timestamp
Required: No

 ** transferDate **   <a name="iot-Type-OutgoingCertificate-transferDate"></a>
The date the transfer was initiated.
Type: Timestamp
Required: No

 ** transferMessage **   <a name="iot-Type-OutgoingCertificate-transferMessage"></a>
The transfer message.
Type: String
Length Constraints: Maximum length of 128.
Pattern: `[\s\S]*`
Required: No

 ** transferredTo **   <a name="iot-Type-OutgoingCertificate-transferredTo"></a>
The AWS account to which the transfer was made.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `[0-9]+`
Required: No

## See Also
<a name="API_OutgoingCertificate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/OutgoingCertificate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/OutgoingCertificate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/OutgoingCertificate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
