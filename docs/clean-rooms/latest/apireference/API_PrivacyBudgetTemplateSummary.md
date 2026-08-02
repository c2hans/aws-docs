---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_PrivacyBudgetTemplateSummary.html
---

# PrivacyBudgetTemplateSummary
<a name="API_PrivacyBudgetTemplateSummary"></a>

A summary of the privacy budget template. The summary includes membership information, collaboration information, and creation information.

## Contents
<a name="API_PrivacyBudgetTemplateSummary_Contents"></a>

 ** arn **   <a name="API-Type-PrivacyBudgetTemplateSummary-arn"></a>
The ARN of the privacy budget template.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100.
Pattern: `arn:aws:[\w]+:[\w]{2}-[\w]{4,9}-[\d]:[\d]{12}:privacybudgettemplate/[\d\w-]+`
Required: Yes

 ** collaborationArn **   <a name="API-Type-PrivacyBudgetTemplateSummary-collaborationArn"></a>
The ARN of the collaboration that contains this privacy budget template.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100.
Pattern: `arn:aws:[\w]+:[\w]{2}-[\w]{4,9}-[\d]:[\d]{12}:collaboration/[\d\w-]+`
Required: Yes

 ** collaborationId **   <a name="API-Type-PrivacyBudgetTemplateSummary-collaborationId"></a>
The unique ID of the collaboration that contains this privacy budget template.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** createTime **   <a name="API-Type-PrivacyBudgetTemplateSummary-createTime"></a>
The time at which the privacy budget template was created.
Type: Timestamp
Required: Yes

 ** id **   <a name="API-Type-PrivacyBudgetTemplateSummary-id"></a>
The unique identifier of the privacy budget template.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** membershipArn **   <a name="API-Type-PrivacyBudgetTemplateSummary-membershipArn"></a>
The Amazon Resource Name (ARN) of the member who created the privacy budget template.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100.
Pattern: `arn:aws:[\w]+:[\w]{2}-[\w]{4,9}-[\d]:[\d]{12}:membership/[\d\w-]+`
Required: Yes

 ** membershipId **   <a name="API-Type-PrivacyBudgetTemplateSummary-membershipId"></a>
The identifier for a membership resource.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** privacyBudgetType **   <a name="API-Type-PrivacyBudgetTemplateSummary-privacyBudgetType"></a>
The type of the privacy budget template.
Type: String
Valid Values: `DIFFERENTIAL_PRIVACY | ACCESS_BUDGET`
Required: Yes

 ** updateTime **   <a name="API-Type-PrivacyBudgetTemplateSummary-updateTime"></a>
The most recent time at which the privacy budget template was updated.
Type: Timestamp
Required: Yes

## See Also
<a name="API_PrivacyBudgetTemplateSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/PrivacyBudgetTemplateSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/PrivacyBudgetTemplateSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/PrivacyBudgetTemplateSummary)
