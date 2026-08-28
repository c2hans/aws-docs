---
source_url: https://docs.aws.amazon.com/IAM/latest/APIReference/API_VirtualMFADevice.html
---

# VirtualMFADevice
<a name="API_VirtualMFADevice"></a>

Contains information about a virtual MFA device.

## Contents
<a name="API_VirtualMFADevice_Contents"></a>

 ** SerialNumber **
The serial number associated with `VirtualMFADevice`.
Type: String
Length Constraints: Minimum length of 9. Maximum length of 256.
Pattern: `[\w+=/:,.@-]+`
Required: Yes

 ** Base32StringSeed **
 The base32 seed defined as specified in [RFC3548](https://tools.ietf.org/html/rfc3548.txt). The `Base32StringSeed` is base32-encoded.
Type: Base64-encoded binary data object
Required: No

 ** EnableDate **
The date and time on which the virtual MFA device was enabled.
Type: Timestamp
Required: No

 ** QRCodePNG **
 A QR code PNG image that encodes `otpauth://totp/$virtualMFADeviceName@$AccountName?secret=$Base32String` where `$virtualMFADeviceName` is one of the create call arguments. `AccountName` is the user name if set (otherwise, the account ID otherwise), and `Base32String` is the seed in base32 format. The `Base32String` value is base64-encoded.
Type: Base64-encoded binary data object
Required: No

 ** Tags.member.N **
A list of tags that are attached to the virtual MFA device. For more information about tagging, see [Tagging IAM resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html) in the *IAM User Guide*.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Maximum number of 50 items.
Required: No

 ** User **
The IAM user associated with this virtual MFA device.
Type: [User](API_User.md) object
Required: No

## See Also
<a name="API_VirtualMFADevice_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-2010-05-08/VirtualMFADevice)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-2010-05-08/VirtualMFADevice)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-2010-05-08/VirtualMFADevice)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Identity and Access Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query IAM` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
