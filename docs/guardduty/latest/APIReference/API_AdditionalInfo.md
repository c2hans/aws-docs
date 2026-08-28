---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_AdditionalInfo.html
---

# AdditionalInfo
<a name="API_AdditionalInfo"></a>

Contains additional information about the detected threat.

## Contents
<a name="API_AdditionalInfo_Contents"></a>

 ** deviceName **   <a name="guardduty-Type-AdditionalInfo-deviceName"></a>
The device name of the EBS volume, if applicable.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Required: No

 ** versionId **   <a name="guardduty-Type-AdditionalInfo-versionId"></a>
The version ID of the S3 object, if applicable.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Required: No

## See Also
<a name="API_AdditionalInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/AdditionalInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/AdditionalInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/AdditionalInfo)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GuardDuty. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query guardduty` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
