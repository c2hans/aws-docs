---
source_url: https://docs.aws.amazon.com/IAM/latest/APIReference/API_MFADevice.html
---

# MFADevice
<a name="API_MFADevice"></a>

Contains information about an MFA device.

This data type is used as a response element in the [ListMFADevices](https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListMFADevices.html) operation.

## Contents
<a name="API_MFADevice_Contents"></a>

 ** EnableDate **
The date when the MFA device was enabled for the user.
Type: Timestamp
Required: Yes

 ** SerialNumber **
The serial number that uniquely identifies the MFA device. For virtual MFA devices, the serial number is the device ARN.
Type: String
Length Constraints: Minimum length of 9. Maximum length of 256.
Pattern: `[\w+=/:,.@-]+`
Required: Yes

 ** UserName **
The user with whom the MFA device is associated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\w+=,.@-]+`
Required: Yes

## See Also
<a name="API_MFADevice_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-2010-05-08/MFADevice)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-2010-05-08/MFADevice)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-2010-05-08/MFADevice)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Identity and Access Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query IAM` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
