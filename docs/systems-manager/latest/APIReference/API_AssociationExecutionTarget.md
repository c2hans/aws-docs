---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_AssociationExecutionTarget.html
---

# AssociationExecutionTarget
<a name="API_AssociationExecutionTarget"></a>

Includes information about the specified association execution.

## Contents
<a name="API_AssociationExecutionTarget_Contents"></a>

 ** AssociationId **   <a name="systemsmanager-Type-AssociationExecutionTarget-AssociationId"></a>
The association ID.
Type: String
Pattern: `[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}`
Required: No

 ** AssociationVersion **   <a name="systemsmanager-Type-AssociationExecutionTarget-AssociationVersion"></a>
The association version.
Type: String
Pattern: `^(([$]LATEST)|([1-9][0-9]*))$`
Required: No

 ** DetailedStatus **   <a name="systemsmanager-Type-AssociationExecutionTarget-DetailedStatus"></a>
Detailed information about the execution status.
Type: String
Required: No

 ** ExecutionId **   <a name="systemsmanager-Type-AssociationExecutionTarget-ExecutionId"></a>
The execution ID.
Type: String
Pattern: `[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}`
Required: No

 ** LastExecutionDate **   <a name="systemsmanager-Type-AssociationExecutionTarget-LastExecutionDate"></a>
The date of the last execution.
Type: Timestamp
Required: No

 ** OutputSource **   <a name="systemsmanager-Type-AssociationExecutionTarget-OutputSource"></a>
The location where the association details are saved.
Type: [OutputSource](API_OutputSource.md) object
Required: No

 ** ResourceId **   <a name="systemsmanager-Type-AssociationExecutionTarget-ResourceId"></a>
The resource ID, for example, the managed node ID where the association ran.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** ResourceType **   <a name="systemsmanager-Type-AssociationExecutionTarget-ResourceType"></a>
The resource type, for example, EC2.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Required: No

 ** Status **   <a name="systemsmanager-Type-AssociationExecutionTarget-Status"></a>
The association execution status.
Type: String
Required: No

## See Also
<a name="API_AssociationExecutionTarget_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/AssociationExecutionTarget)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/AssociationExecutionTarget)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/AssociationExecutionTarget)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
