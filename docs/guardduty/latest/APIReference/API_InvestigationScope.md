---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_InvestigationScope.html
---

# InvestigationScope
<a name="API_InvestigationScope"></a>

Contains information about what an investigation analyzed. Only the identifier that matches `InvestigationType` is set.

## Contents
<a name="API_InvestigationScope_Contents"></a>

 ** accountId **   <a name="guardduty-Type-InvestigationScope-accountId"></a>
The ID of the AWS account that the investigation analyzed. Set only when `InvestigationType` is `ACCOUNT`.
Type: String
Length Constraints: Fixed length of 12.
Required: No

 ** adminAccountId **   <a name="guardduty-Type-InvestigationScope-adminAccountId"></a>
The ID of the administrator account of the organization that the investigation analyzed. Set only when `InvestigationType` is `ORGANIZATION`.
Type: String
Length Constraints: Fixed length of 12.
Required: No

 ** findingId **   <a name="guardduty-Type-InvestigationScope-findingId"></a>
The ID of the finding that the investigation analyzed. Set only when `InvestigationType` is `FINDING`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: No

 ** investigationType **   <a name="guardduty-Type-InvestigationScope-investigationType"></a>
The type of investigation. Possible values:
+  `FINDING` – An investigation of a specific GuardDuty finding.
+  `ACCOUNT` – An investigation of the threat posture of an AWS account.
+  `ORGANIZATION` – An investigation of your organization's threat posture.
Type: String
Valid Values: `FINDING | ACCOUNT | ORGANIZATION`
Required: No

 ** queryTimeWindow **   <a name="guardduty-Type-InvestigationScope-queryTimeWindow"></a>
The time window over which the investigation queried data, set only when `InvestigationType` is `ACCOUNT` or `ORGANIZATION`.
Type: [QueryTimeWindow](API_QueryTimeWindow.md) object
Required: No

## See Also
<a name="API_InvestigationScope_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/InvestigationScope)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/InvestigationScope)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/InvestigationScope)
