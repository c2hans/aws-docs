---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_PrivacyBudgetSummary.html
---

# PrivacyBudgetSummary
<a name="API_PrivacyBudgetSummary"></a>

An array that summaries the specified privacy budget. This summary includes collaboration information, creation information, membership information, and privacy budget information.

## Contents
<a name="API_PrivacyBudgetSummary_Contents"></a>

 ** budget **   <a name="API-Type-PrivacyBudgetSummary-budget"></a>
The provided privacy budget.
Type: [PrivacyBudget](API_PrivacyBudget.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** collaborationArn **   <a name="API-Type-PrivacyBudgetSummary-collaborationArn"></a>
The ARN of the collaboration that contains this privacy budget.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100.
Pattern: `arn:aws:[\w]+:[\w]{2}-[\w]{4,9}-[\d]:[\d]{12}:collaboration/[\d\w-]+`
Required: Yes

 ** collaborationId **   <a name="API-Type-PrivacyBudgetSummary-collaborationId"></a>
The unique identifier of the collaboration that contains this privacy budget.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** createTime **   <a name="API-Type-PrivacyBudgetSummary-createTime"></a>
The time at which the privacy budget was created.
Type: Timestamp
Required: Yes

 ** id **   <a name="API-Type-PrivacyBudgetSummary-id"></a>
The unique identifier of the privacy budget.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** membershipArn **   <a name="API-Type-PrivacyBudgetSummary-membershipArn"></a>
The Amazon Resource Name (ARN) of the member who created the privacy budget summary.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100.
Pattern: `arn:aws:[\w]+:[\w]{2}-[\w]{4,9}-[\d]:[\d]{12}:membership/[\d\w-]+`
Required: Yes

 ** membershipId **   <a name="API-Type-PrivacyBudgetSummary-membershipId"></a>
The identifier for a membership resource.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** privacyBudgetTemplateArn **   <a name="API-Type-PrivacyBudgetSummary-privacyBudgetTemplateArn"></a>
The ARN of the privacy budget template.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100.
Pattern: `arn:aws:[\w]+:[\w]{2}-[\w]{4,9}-[\d]:[\d]{12}:privacybudgettemplate/[\d\w-]+`
Required: Yes

 ** privacyBudgetTemplateId **   <a name="API-Type-PrivacyBudgetSummary-privacyBudgetTemplateId"></a>
The unique identifier of the privacy budget template.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** type **   <a name="API-Type-PrivacyBudgetSummary-type"></a>
Specifies the type of the privacy budget.
Type: String
Valid Values: `DIFFERENTIAL_PRIVACY | ACCESS_BUDGET`
Required: Yes

 ** updateTime **   <a name="API-Type-PrivacyBudgetSummary-updateTime"></a>
The most recent time at which the privacy budget was updated.
Type: Timestamp
Required: Yes

## See Also
<a name="API_PrivacyBudgetSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/PrivacyBudgetSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/PrivacyBudgetSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/PrivacyBudgetSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
