---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-auditmanager-assessment-awsservice.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AuditManager::Assessment AWSService
<a name="aws-properties-auditmanager-assessment-awsservice"></a>

The `AWSService` property type specifies an AWS service such as Amazon S3, AWS CloudTrail, and so on.

## Syntax
<a name="aws-properties-auditmanager-assessment-awsservice-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-auditmanager-assessment-awsservice-syntax.json"></a>

```
{
  "[ServiceName](#cfn-auditmanager-assessment-awsservice-servicename)" : {{String}}
}
```

### YAML
<a name="aws-properties-auditmanager-assessment-awsservice-syntax.yaml"></a>

```
  [ServiceName](#cfn-auditmanager-assessment-awsservice-servicename): {{String}}
```

## Properties
<a name="aws-properties-auditmanager-assessment-awsservice-properties"></a>

`ServiceName`  <a name="cfn-auditmanager-assessment-awsservice-servicename"></a>
 The name of the AWS service.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9-\s().]+$`
*Minimum*: `1`
*Maximum*: `40`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also
<a name="aws-properties-auditmanager-assessment-awsservice--seealso"></a>
+ [AWSService](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_AWSService.html) in the *AWS Audit Manager API Reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
