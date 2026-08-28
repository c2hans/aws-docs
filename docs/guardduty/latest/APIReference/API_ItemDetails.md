---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ItemDetails.html
---

# ItemDetails
<a name="API_ItemDetails"></a>

Contains detailed information about where a threat was detected.

## Contents
<a name="API_ItemDetails_Contents"></a>

 ** additionalInfo **   <a name="guardduty-Type-ItemDetails-additionalInfo"></a>
Additional information about the detected threat item.
Type: [AdditionalInfo](API_AdditionalInfo.md) object
Required: No

 ** hash **   <a name="guardduty-Type-ItemDetails-hash"></a>
The hash value of the infected item.
Type: String
Required: No

 ** itemPath **   <a name="guardduty-Type-ItemDetails-itemPath"></a>
The path where the threat was detected.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Required: No

 ** resourceArn **   <a name="guardduty-Type-ItemDetails-resourceArn"></a>
Amazon Resource Name (ARN) of the resource where the threat was detected.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Required: No

## See Also
<a name="API_ItemDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/ItemDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/ItemDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/ItemDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GuardDuty. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query guardduty` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
