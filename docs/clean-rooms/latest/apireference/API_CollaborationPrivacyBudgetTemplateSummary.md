---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_CollaborationPrivacyBudgetTemplateSummary.html
---

# CollaborationPrivacyBudgetTemplateSummary
<a name="API_CollaborationPrivacyBudgetTemplateSummary"></a>

A summary of the collaboration's privacy budget template. This summary includes information about who created the privacy budget template and what collaborations it belongs to.

## Contents
<a name="API_CollaborationPrivacyBudgetTemplateSummary_Contents"></a>

 ** arn **   <a name="API-Type-CollaborationPrivacyBudgetTemplateSummary-arn"></a>
The ARN of the collaboration privacy budget template.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100.
Pattern: `arn:aws:[\w]+:[\w]{2}-[\w]{4,9}-[\d]:[\d]{12}:privacybudgettemplate/[\d\w-]+`
Required: Yes

 ** collaborationArn **   <a name="API-Type-CollaborationPrivacyBudgetTemplateSummary-collaborationArn"></a>
The ARN of the collaboration that contains this collaboration privacy budget template.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100.
Pattern: `arn:aws:[\w]+:[\w]{2}-[\w]{4,9}-[\d]:[\d]{12}:collaboration/[\d\w-]+`
Required: Yes

 ** collaborationId **   <a name="API-Type-CollaborationPrivacyBudgetTemplateSummary-collaborationId"></a>
The unique identifier of the collaboration that contains this collaboration privacy budget template.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** createTime **   <a name="API-Type-CollaborationPrivacyBudgetTemplateSummary-createTime"></a>
The time at which the collaboration privacy budget template was created.
Type: Timestamp
Required: Yes

 ** creatorAccountId **   <a name="API-Type-CollaborationPrivacyBudgetTemplateSummary-creatorAccountId"></a>
The unique identifier of the account that created this collaboration privacy budget template.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d+`
Required: Yes

 ** id **   <a name="API-Type-CollaborationPrivacyBudgetTemplateSummary-id"></a>
The unique identifier of the collaboration privacy budget template.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** privacyBudgetType **   <a name="API-Type-CollaborationPrivacyBudgetTemplateSummary-privacyBudgetType"></a>
The type of the privacy budget template.
Type: String
Valid Values: `DIFFERENTIAL_PRIVACY | ACCESS_BUDGET`
Required: Yes

 ** updateTime **   <a name="API-Type-CollaborationPrivacyBudgetTemplateSummary-updateTime"></a>
The most recent time at which the collaboration privacy budget template was updated.
Type: Timestamp
Required: Yes

## See Also
<a name="API_CollaborationPrivacyBudgetTemplateSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/CollaborationPrivacyBudgetTemplateSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/CollaborationPrivacyBudgetTemplateSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/CollaborationPrivacyBudgetTemplateSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
