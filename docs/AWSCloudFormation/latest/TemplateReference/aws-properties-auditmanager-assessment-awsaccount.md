---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-auditmanager-assessment-awsaccount.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AuditManager::Assessment AWSAccount
<a name="aws-properties-auditmanager-assessment-awsaccount"></a>

The `AWSAccount` property type specifies the wrapper of the AWS account details, such as account ID, email address, and so on.

## Syntax
<a name="aws-properties-auditmanager-assessment-awsaccount-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-auditmanager-assessment-awsaccount-syntax.json"></a>

```
{
  "[EmailAddress](#cfn-auditmanager-assessment-awsaccount-emailaddress)" : {{String}},
  "[Id](#cfn-auditmanager-assessment-awsaccount-id)" : {{String}},
  "[Name](#cfn-auditmanager-assessment-awsaccount-name)" : {{String}}
}
```

### YAML
<a name="aws-properties-auditmanager-assessment-awsaccount-syntax.yaml"></a>

```
  [EmailAddress](#cfn-auditmanager-assessment-awsaccount-emailaddress): {{String}}
  [Id](#cfn-auditmanager-assessment-awsaccount-id): {{String}}
  [Name](#cfn-auditmanager-assessment-awsaccount-name): {{String}}
```

## Properties
<a name="aws-properties-auditmanager-assessment-awsaccount-properties"></a>

`EmailAddress`  <a name="cfn-auditmanager-assessment-awsaccount-emailaddress"></a>
 The email address that's associated with the AWS account.
*Required*: No
*Type*: String
*Pattern*: `^.*@.*$`
*Minimum*: `1`
*Maximum*: `320`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Id`  <a name="cfn-auditmanager-assessment-awsaccount-id"></a>
 The identifier for the AWS account.
*Required*: No
*Type*: String
*Pattern*: `^[0-9]{12}$`
*Minimum*: `12`
*Maximum*: `12`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-auditmanager-assessment-awsaccount-name"></a>
 The name of the AWS account.
*Required*: No
*Type*: String
*Pattern*: `^[\u0020-\u007E]+$`
*Minimum*: `1`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also
<a name="aws-properties-auditmanager-assessment-awsaccount--seealso"></a>
+ [AWSAccount](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_AWSAccount.html) in the *AWS Audit Manager API Reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
