---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_PrivacyBudgetTemplate.html
---

# PrivacyBudgetTemplate
<a name="API_PrivacyBudgetTemplate"></a>

An object that defines the privacy budget template.

## Contents
<a name="API_PrivacyBudgetTemplate_Contents"></a>

 ** arn **   <a name="API-Type-PrivacyBudgetTemplate-arn"></a>
The ARN of the privacy budget template.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100.
Pattern: `arn:aws:[\w]+:[\w]{2}-[\w]{4,9}-[\d]:[\d]{12}:privacybudgettemplate/[\d\w-]+`
Required: Yes

 ** autoRefresh **   <a name="API-Type-PrivacyBudgetTemplate-autoRefresh"></a>
How often the privacy budget refreshes.
If you plan to regularly bring new data into the collaboration, use `CALENDAR_MONTH` to automatically get a new privacy budget for the collaboration every calendar month. Choosing this option allows arbitrary amounts of information to be revealed about rows of the data when repeatedly queried across refreshes. Avoid choosing this if the same rows will be repeatedly queried between privacy budget refreshes.
Type: String
Valid Values: `CALENDAR_MONTH | NONE`
Required: Yes

 ** collaborationArn **   <a name="API-Type-PrivacyBudgetTemplate-collaborationArn"></a>
The ARN of the collaboration that contains this privacy budget template.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100.
Pattern: `arn:aws:[\w]+:[\w]{2}-[\w]{4,9}-[\d]:[\d]{12}:collaboration/[\d\w-]+`
Required: Yes

 ** collaborationId **   <a name="API-Type-PrivacyBudgetTemplate-collaborationId"></a>
The unique ID of the collaboration that contains this privacy budget template.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** createTime **   <a name="API-Type-PrivacyBudgetTemplate-createTime"></a>
The time at which the privacy budget template was created.
Type: Timestamp
Required: Yes

 ** id **   <a name="API-Type-PrivacyBudgetTemplate-id"></a>
The unique identifier of the privacy budget template.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** membershipArn **   <a name="API-Type-PrivacyBudgetTemplate-membershipArn"></a>
The Amazon Resource Name (ARN) of the member who created the privacy budget template.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100.
Pattern: `arn:aws:[\w]+:[\w]{2}-[\w]{4,9}-[\d]:[\d]{12}:membership/[\d\w-]+`
Required: Yes

 ** membershipId **   <a name="API-Type-PrivacyBudgetTemplate-membershipId"></a>
The identifier for a membership resource.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** parameters **   <a name="API-Type-PrivacyBudgetTemplate-parameters"></a>
Specifies the epsilon and noise parameters for the privacy budget template.
Type: [PrivacyBudgetTemplateParametersOutput](API_PrivacyBudgetTemplateParametersOutput.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** privacyBudgetType **   <a name="API-Type-PrivacyBudgetTemplate-privacyBudgetType"></a>
Specifies the type of the privacy budget template.
Type: String
Valid Values: `DIFFERENTIAL_PRIVACY | ACCESS_BUDGET`
Required: Yes

 ** updateTime **   <a name="API-Type-PrivacyBudgetTemplate-updateTime"></a>
The most recent time at which the privacy budget template was updated.
Type: Timestamp
Required: Yes

## See Also
<a name="API_PrivacyBudgetTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/PrivacyBudgetTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/PrivacyBudgetTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/PrivacyBudgetTemplate)
