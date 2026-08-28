---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_ControlScope.html
---

# ControlScope
<a name="API_ControlScope"></a>

A framework consists of one or more controls. Each control has its own control scope. The control scope can include one or more resource types, a combination of a tag key and value, or a combination of one resource type and one resource ID. If no scope is specified, evaluations for the rule are triggered when any resource in your recording group changes in configuration.

**Note**
To set a control scope that includes all of a particular resource, leave the `ControlScope` empty or do not pass it when calling `CreateFramework`.

## Contents
<a name="API_ControlScope_Contents"></a>

 ** ComplianceResourceIds **   <a name="Backup-Type-ControlScope-ComplianceResourceIds"></a>
The ID of the only AWS resource that you want your control scope to contain.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: No

 ** ComplianceResourceTypes **   <a name="Backup-Type-ControlScope-ComplianceResourceTypes"></a>
Describes whether the control scope includes one or more types of resources, such as `EFS` or `RDS`.
Type: Array of strings
Required: No

 ** Tags **   <a name="Backup-Type-ControlScope-Tags"></a>
The tag key-value pair applied to those AWS resources that you want to trigger an evaluation for a rule. A maximum of one key-value pair can be provided. The tag value is optional, but it cannot be an empty string if you are creating or editing a framework from the console (though the value can be an empty string when included in a CloudFormation template).
The structure to assign a tag is: `[{"Key":"string","Value":"string"}]`.
Type: String to string map
Required: No

## See Also
<a name="API_ControlScope_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-2018-11-15/ControlScope)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-2018-11-15/ControlScope)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-2018-11-15/ControlScope)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Backup. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-backup` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
