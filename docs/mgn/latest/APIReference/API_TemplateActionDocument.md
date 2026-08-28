---
source_url: https://docs.aws.amazon.com/mgn/latest/APIReference/API_TemplateActionDocument.html
---

# TemplateActionDocument
<a name="API_TemplateActionDocument"></a>

## Contents
<a name="API_TemplateActionDocument_Contents"></a>

 ** actionID **   <a name="mgn-Type-TemplateActionDocument-actionID"></a>
Template post migration custom action ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `.*[0-9a-zA-Z]`
Required: No

 ** actionName **   <a name="mgn-Type-TemplateActionDocument-actionName"></a>
Template post migration custom action name.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** active **   <a name="mgn-Type-TemplateActionDocument-active"></a>
Template post migration custom action active status.
Type: Boolean
Required: No

 ** category **   <a name="mgn-Type-TemplateActionDocument-category"></a>
Template post migration custom action category.
Type: String
Valid Values: `DISASTER_RECOVERY | OPERATING_SYSTEM | LICENSE_AND_SUBSCRIPTION | VALIDATION | OBSERVABILITY | REFACTORING | SECURITY | NETWORKING | CONFIGURATION | BACKUP | OTHER`
Required: No

 ** description **   <a name="mgn-Type-TemplateActionDocument-description"></a>
Template post migration custom action description.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[0-9a-zA-Z ():/.,'-_#*; ]*`
Required: No

 ** documentIdentifier **   <a name="mgn-Type-TemplateActionDocument-documentIdentifier"></a>
Template post migration custom action document identifier.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** documentVersion **   <a name="mgn-Type-TemplateActionDocument-documentVersion"></a>
Template post migration custom action document version.
Type: String
Pattern: `(\$DEFAULT|\$LATEST|[0-9]+)`
Required: No

 ** externalParameters **   <a name="mgn-Type-TemplateActionDocument-externalParameters"></a>
Template post migration custom action external parameters.
Type: String to [SsmExternalParameter](API_SsmExternalParameter.md) object map
Map Entries: Minimum number of 0 items. Maximum number of 20 items.
Key Length Constraints: Minimum length of 1. Maximum length of 1011.
Key Pattern: `([A-Za-z0-9])+`
Required: No

 ** mustSucceedForCutover **   <a name="mgn-Type-TemplateActionDocument-mustSucceedForCutover"></a>
Template post migration custom action must succeed for cutover.
Type: Boolean
Required: No

 ** operatingSystem **   <a name="mgn-Type-TemplateActionDocument-operatingSystem"></a>
Operating system eligible for this template post migration custom action.
Type: String
Pattern: `(linux|windows)`
Required: No

 ** order **   <a name="mgn-Type-TemplateActionDocument-order"></a>
Template post migration custom action order.
Type: Integer
Valid Range: Minimum value of 1001. Maximum value of 10000.
Required: No

 ** parameters **   <a name="mgn-Type-TemplateActionDocument-parameters"></a>
Template post migration custom action parameters.
Type: String to array of [SsmParameterStoreParameter](API_SsmParameterStoreParameter.md) objects map
Map Entries: Minimum number of 0 items. Maximum number of 20 items.
Key Length Constraints: Minimum length of 1. Maximum length of 1011.
Key Pattern: `([A-Za-z0-9])+`
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

 ** timeoutSeconds **   <a name="mgn-Type-TemplateActionDocument-timeoutSeconds"></a>
Template post migration custom action timeout in seconds.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

## See Also
<a name="API_TemplateActionDocument_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mgn-2020-02-26/TemplateActionDocument)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mgn-2020-02-26/TemplateActionDocument)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mgn-2020-02-26/TemplateActionDocument)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for ApplicationMigrationService. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mgn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
