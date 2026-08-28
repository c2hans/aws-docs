---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-auditmanager-assessment-scope.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AuditManager::Assessment Scope
<a name="aws-properties-auditmanager-assessment-scope"></a>

The `Scope` property type specifies the wrapper that contains the AWS accounts and services that are in scope for the assessment.

## Syntax
<a name="aws-properties-auditmanager-assessment-scope-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-auditmanager-assessment-scope-syntax.json"></a>

```
{
  "[AwsAccounts](#cfn-auditmanager-assessment-scope-awsaccounts)" : {{[ AWSAccount, ... ]}},
  "[AwsServices](#cfn-auditmanager-assessment-scope-awsservices)" : {{[ AWSService, ... ]}}
}
```

### YAML
<a name="aws-properties-auditmanager-assessment-scope-syntax.yaml"></a>

```
  [AwsAccounts](#cfn-auditmanager-assessment-scope-awsaccounts): {{
    - AWSAccount}}
  [AwsServices](#cfn-auditmanager-assessment-scope-awsservices): {{
    - AWSService}}
```

## Properties
<a name="aws-properties-auditmanager-assessment-scope-properties"></a>

`AwsAccounts`  <a name="cfn-auditmanager-assessment-scope-awsaccounts"></a>
 The AWS accounts that are included in the scope of the assessment.
*Required*: No
*Type*: Array of [AWSAccount](aws-properties-auditmanager-assessment-awsaccount.md)
*Minimum*: `1`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AwsServices`  <a name="cfn-auditmanager-assessment-scope-awsservices"></a>
 The AWS services that are included in the scope of the assessment.
This API parameter is no longer supported. If you use this parameter to specify one or more AWS services, Audit Manager ignores this input. Instead, the value for `awsServices` will show as empty.
*Required*: No
*Type*: Array of [AWSService](aws-properties-auditmanager-assessment-awsservice.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also
<a name="aws-properties-auditmanager-assessment-scope--seealso"></a>
+ [Scope](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_Scope.html) in the *AWS Audit Manager API Reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
