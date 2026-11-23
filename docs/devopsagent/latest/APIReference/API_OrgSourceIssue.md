---
source_url: https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_OrgSourceIssue.html
---

# OrgSourceIssue

Describes an issue encountered while deploying or evaluating an AWS Organization source configuration.

## Contents
<a name="API_OrgSourceIssue_Contents"></a>

 ** accountCount **   <a name="devopsagent-Type-OrgSourceIssue-accountCount"></a>
The number of accounts affected by this issue.
Type: Integer
Valid Range: Minimum value of 1.
Required: Yes

 ** accountIds **   <a name="devopsagent-Type-OrgSourceIssue-accountIds"></a>
The AWS account IDs affected by this issue.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 1000 items.
Pattern: `\d{12}`
Required: Yes

 ** reasonCode **   <a name="devopsagent-Type-OrgSourceIssue-reasonCode"></a>
A code that identifies the reason for the issue.
Type: String
Valid Values: `accountSuspended | accountNotInScope | managementAccountNotSupported | stackInstanceInoperable | accessDenied | deploymentFailed | secondaryAccountLimitExceeded`
Required: Yes

 ** message **   <a name="devopsagent-Type-OrgSourceIssue-message"></a>
A description of the issue.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

## See Also
<a name="API_OrgSourceIssue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-agent-2026-01-01/OrgSourceIssue)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-agent-2026-01-01/OrgSourceIssue)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-agent-2026-01-01/OrgSourceIssue)
