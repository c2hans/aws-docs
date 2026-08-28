---
source_url: https://docs.aws.amazon.com/drs/latest/APIReference/API_LaunchAction.html
---

# LaunchAction
<a name="API_LaunchAction"></a>

Launch action.

## Contents
<a name="API_LaunchAction_Contents"></a>

 ** actionCode **   <a name="drs-Type-LaunchAction-actionCode"></a>
Launch action code.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `([A-Za-z0-9-/:])+`
Required: No

 ** actionId **   <a name="drs-Type-LaunchAction-actionId"></a>
Launch action Id.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}`
Required: No

 ** actionVersion **   <a name="drs-Type-LaunchAction-actionVersion"></a>
Launch action version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10.
Pattern: `(\$DEFAULT|\$LATEST|[0-9]+)`
Required: No

 ** active **   <a name="drs-Type-LaunchAction-active"></a>
Whether the launch action is active.
Type: Boolean
Required: No

 ** category **   <a name="drs-Type-LaunchAction-category"></a>
Launch action category.
Type: String
Valid Values: `MONITORING | VALIDATION | CONFIGURATION | SECURITY | OTHER`
Required: No

 ** description **   <a name="drs-Type-LaunchAction-description"></a>
Launch action description.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[0-9a-zA-Z ():/.,'-_#*; ]*`
Required: No

 ** name **   <a name="drs-Type-LaunchAction-name"></a>
Launch action name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9][A-Za-z0-9 /_-]*`
Required: No

 ** optional **   <a name="drs-Type-LaunchAction-optional"></a>
Whether the launch will not be marked as failed if this action fails.
Type: Boolean
Required: No

 ** order **   <a name="drs-Type-LaunchAction-order"></a>
Launch action order.
Type: Integer
Valid Range: Minimum value of 2. Maximum value of 10000.
Required: No

 ** parameters **   <a name="drs-Type-LaunchAction-parameters"></a>
Launch action parameters.
Type: String to [LaunchActionParameter](API_LaunchActionParameter.md) object map
Map Entries: Minimum number of 0 items. Maximum number of 20 items.
Key Length Constraints: Minimum length of 1. Maximum length of 1011.
Key Pattern: `([A-Za-z0-9])+`
Required: No

 ** type **   <a name="drs-Type-LaunchAction-type"></a>
Launch action type.
Type: String
Valid Values: `SSM_AUTOMATION | SSM_COMMAND`
Required: No

## See Also
<a name="API_LaunchAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/drs-2020-02-26/LaunchAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/drs-2020-02-26/LaunchAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/drs-2020-02-26/LaunchAction)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elastic Disaster Recovery. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query drs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
