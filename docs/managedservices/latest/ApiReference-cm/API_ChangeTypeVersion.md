---
source_url: https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_ChangeTypeVersion.html
---

# ChangeTypeVersion
<a name="API_ChangeTypeVersion"></a>

Information about a specific version of a change type.

## Contents
<a name="API_ChangeTypeVersion_Contents"></a>

 ** AccessLevel **   <a name="amscm-Type-ChangeTypeVersion-AccessLevel"></a>

Type: [ChangeTypeAccessLevel](API_ChangeTypeAccessLevel.md) object
Required: No

 ** ApprovalCondition **   <a name="amscm-Type-ChangeTypeVersion-ApprovalCondition"></a>
The approval requirements for the change type version.
Type: [ChangeTypeApprovalCondition](API_ChangeTypeApprovalCondition.md) object
Required: No

 ** AutomationStatus **   <a name="amscm-Type-ChangeTypeVersion-AutomationStatus"></a>
The automation status (`Automated` or `Manual`) of the change type version.
Type: [ChangeTypeAutomationStatus](API_ChangeTypeAutomationStatus.md) object
Required: No

 ** ChangeTypeId **   <a name="amscm-Type-ChangeTypeVersion-ChangeTypeId"></a>
The unique ID of the change type, in the form ct-2ty5seo8rxfsc.
Type: String
Required: No

 ** CreatedTime **   <a name="amscm-Type-ChangeTypeVersion-CreatedTime"></a>
The date and time that the change type version was created.
Type: String
Required: No

 ** DeprecationMessage **   <a name="amscm-Type-ChangeTypeVersion-DeprecationMessage"></a>
Information about the reasons for deprecating the change type version.
Type: String
Required: No

 ** DeprecationTime **   <a name="amscm-Type-ChangeTypeVersion-DeprecationTime"></a>
The date and time that the change type version was deprecated.
Type: String
Required: No

 ** ExecutionInputSchema **   <a name="amscm-Type-ChangeTypeVersion-ExecutionInputSchema"></a>
A JSON schema that describes the parameters for the change type.
Type: String
Required: No

 ** ExecutionOutputSchema **   <a name="amscm-Type-ChangeTypeVersion-ExecutionOutputSchema"></a>
A JSON schema that describes the output for the change type.
Type: String
Required: No

 ** ExpectedExecutionDurationInMinutes **   <a name="amscm-Type-ChangeTypeVersion-ExpectedExecutionDurationInMinutes"></a>
The number of minutes that the change should take to execute.
Type: Integer
Required: No

 ** Name **   <a name="amscm-Type-ChangeTypeVersion-Name"></a>
The title of the JSON Schema `ExecutionInputSchema` of the change type version.
Type: String
Required: No

 ** Version **   <a name="amscm-Type-ChangeTypeVersion-Version"></a>
The version number for this change type version.
Type: String
Required: No

## See Also
<a name="API_ChangeTypeVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amscm-2020-05-21/ChangeTypeVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amscm-2020-05-21/ChangeTypeVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amscm-2020-05-21/ChangeTypeVersion)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Managed Services. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managedservices` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
