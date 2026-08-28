---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_Runbook.html
---

# Runbook
<a name="API_Runbook"></a>

Information about an Automation runbook used in a runbook workflow in Change Manager.

**Note**
The Automation runbooks specified for the runbook workflow can't run until all required approvals for the change request have been received.

## Contents
<a name="API_Runbook_Contents"></a>

 ** DocumentName **   <a name="systemsmanager-Type-Runbook-DocumentName"></a>
The name of the Automation runbook used in a runbook workflow.
Type: String
Pattern: `^[a-zA-Z0-9_\-.:/]{3,128}$`
Required: Yes

 ** DocumentVersion **   <a name="systemsmanager-Type-Runbook-DocumentVersion"></a>
The version of the Automation runbook used in a runbook workflow.
Type: String
Pattern: `([$]LATEST|[$]DEFAULT|^[1-9][0-9]*$)`
Required: No

 ** MaxConcurrency **   <a name="systemsmanager-Type-Runbook-MaxConcurrency"></a>
The `MaxConcurrency` value specified by the user when the operation started, indicating the maximum number of resources that the runbook operation can run on at the same time.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 7.
Pattern: `^([1-9][0-9]*|[1-9][0-9]%|[1-9]%|100%)$`
Required: No

 ** MaxErrors **   <a name="systemsmanager-Type-Runbook-MaxErrors"></a>
The `MaxErrors` value specified by the user when the execution started, indicating the maximum number of errors that can occur during the operation before the updates are stopped or rolled back.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 7.
Pattern: `^([1-9][0-9]*|[0]|[1-9][0-9]%|[0-9]%|100%)$`
Required: No

 ** Parameters **   <a name="systemsmanager-Type-Runbook-Parameters"></a>
The key-value map of execution parameters, which were supplied when calling `StartChangeRequestExecution`.
Type: String to array of strings map
Map Entries: Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 50.
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

 ** TargetLocations **   <a name="systemsmanager-Type-Runbook-TargetLocations"></a>
Information about the AWS Regions and AWS accounts targeted by the current Runbook operation.
Type: Array of [TargetLocation](API_TargetLocation.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: No

 ** TargetMaps **   <a name="systemsmanager-Type-Runbook-TargetMaps"></a>
A key-value mapping of runbook parameters to target resources. Both Targets and TargetMaps can't be specified together.
Type: Array of string to array of strings maps
Array Members: Minimum number of 0 items. Maximum number of 300 items.
Map Entries: Maximum number of 20 items.
Key Length Constraints: Minimum length of 1. Maximum length of 50.
Array Members: Minimum number of 0 items. Maximum number of 25 items.
Length Constraints: Minimum length of 1. Maximum length of 50.
Required: No

 ** TargetParameterName **   <a name="systemsmanager-Type-Runbook-TargetParameterName"></a>
The name of the parameter used as the target resource for the rate-controlled runbook workflow. Required if you specify `Targets`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Required: No

 ** Targets **   <a name="systemsmanager-Type-Runbook-Targets"></a>
A key-value mapping to target resources that the runbook operation performs tasks on. Required if you specify `TargetParameterName`.
Type: Array of [Target](API_Target.md) objects
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Required: No

## See Also
<a name="API_Runbook_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/Runbook)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/Runbook)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/Runbook)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
