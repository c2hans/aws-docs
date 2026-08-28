---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-auditmanager-assessment-delegation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AuditManager::Assessment Delegation
<a name="aws-properties-auditmanager-assessment-delegation"></a>

The `Delegation` property type specifies the assignment of a control set to a delegate for review.

## Syntax
<a name="aws-properties-auditmanager-assessment-delegation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-auditmanager-assessment-delegation-syntax.json"></a>

```
{
  "[AssessmentId](#cfn-auditmanager-assessment-delegation-assessmentid)" : {{String}},
  "[AssessmentName](#cfn-auditmanager-assessment-delegation-assessmentname)" : {{String}},
  "[Comment](#cfn-auditmanager-assessment-delegation-comment)" : {{String}},
  "[ControlSetId](#cfn-auditmanager-assessment-delegation-controlsetid)" : {{String}},
  "[CreatedBy](#cfn-auditmanager-assessment-delegation-createdby)" : {{String}},
  "[CreationTime](#cfn-auditmanager-assessment-delegation-creationtime)" : {{Number}},
  "[Id](#cfn-auditmanager-assessment-delegation-id)" : {{String}},
  "[LastUpdated](#cfn-auditmanager-assessment-delegation-lastupdated)" : {{Number}},
  "[RoleArn](#cfn-auditmanager-assessment-delegation-rolearn)" : {{String}},
  "[RoleType](#cfn-auditmanager-assessment-delegation-roletype)" : {{String}},
  "[Status](#cfn-auditmanager-assessment-delegation-status)" : {{String}}
}
```

### YAML
<a name="aws-properties-auditmanager-assessment-delegation-syntax.yaml"></a>

```
  [AssessmentId](#cfn-auditmanager-assessment-delegation-assessmentid): {{String}}
  [AssessmentName](#cfn-auditmanager-assessment-delegation-assessmentname): {{String}}
  [Comment](#cfn-auditmanager-assessment-delegation-comment): {{String}}
  [ControlSetId](#cfn-auditmanager-assessment-delegation-controlsetid): {{String}}
  [CreatedBy](#cfn-auditmanager-assessment-delegation-createdby): {{String}}
  [CreationTime](#cfn-auditmanager-assessment-delegation-creationtime): {{Number}}
  [Id](#cfn-auditmanager-assessment-delegation-id): {{String}}
  [LastUpdated](#cfn-auditmanager-assessment-delegation-lastupdated): {{Number}}
  [RoleArn](#cfn-auditmanager-assessment-delegation-rolearn): {{String}}
  [RoleType](#cfn-auditmanager-assessment-delegation-roletype): {{String}}
  [Status](#cfn-auditmanager-assessment-delegation-status): {{String}}
```

## Properties
<a name="aws-properties-auditmanager-assessment-delegation-properties"></a>

`AssessmentId`  <a name="cfn-auditmanager-assessment-delegation-assessmentid"></a>
 The identifier for the assessment that's associated with the delegation.
*Required*: No
*Type*: String
*Pattern*: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
*Minimum*: `36`
*Maximum*: `36`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AssessmentName`  <a name="cfn-auditmanager-assessment-delegation-assessmentname"></a>
 The name of the assessment that's associated with the delegation.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9-_\.]+$`
*Minimum*: `1`
*Maximum*: `127`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Comment`  <a name="cfn-auditmanager-assessment-delegation-comment"></a>
 The comment that's related to the delegation.
*Required*: No
*Type*: String
*Pattern*: `^[\w\W\s\S]*$`
*Maximum*: `350`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ControlSetId`  <a name="cfn-auditmanager-assessment-delegation-controlsetid"></a>
 The identifier for the control set that's associated with the delegation.
*Required*: No
*Type*: String
*Pattern*: `^[\w\W\s\S]*$`
*Minimum*: `1`
*Maximum*: `300`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreatedBy`  <a name="cfn-auditmanager-assessment-delegation-createdby"></a>
 The user or role that created the delegation.
*Minimum*: `1`
*Maximum*: `100`
*Pattern*: `^[a-zA-Z0-9-_()\\[\\]\\s]+$`
*Required*: No
*Type*: String
*Pattern*: `^arn:.*:*:.*`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreationTime`  <a name="cfn-auditmanager-assessment-delegation-creationtime"></a>
 Specifies when the delegation was created.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Id`  <a name="cfn-auditmanager-assessment-delegation-id"></a>
 The unique identifier for the delegation.
*Required*: No
*Type*: String
*Pattern*: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
*Minimum*: `36`
*Maximum*: `36`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LastUpdated`  <a name="cfn-auditmanager-assessment-delegation-lastupdated"></a>
 Specifies when the delegation was last updated.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RoleArn`  <a name="cfn-auditmanager-assessment-delegation-rolearn"></a>
 The Amazon Resource Name (ARN) of the IAM role.
*Required*: No
*Type*: String
*Pattern*: `^arn:.*:iam:.*`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RoleType`  <a name="cfn-auditmanager-assessment-delegation-roletype"></a>
 The type of customer persona.
In `CreateAssessment`, `roleType` can only be `PROCESS_OWNER`.
In `UpdateSettings`, `roleType` can only be `PROCESS_OWNER`.
In `BatchCreateDelegationByAssessment`, `roleType` can only be `RESOURCE_OWNER`.
*Required*: No
*Type*: String
*Allowed values*: `PROCESS_OWNER | RESOURCE_OWNER`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Status`  <a name="cfn-auditmanager-assessment-delegation-status"></a>
 The status of the delegation.
*Required*: No
*Type*: String
*Allowed values*: `IN_PROGRESS | UNDER_REVIEW | COMPLETE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also
<a name="aws-properties-auditmanager-assessment-delegation--seealso"></a>
+ [Delegation](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_Delegation.html) in the *AWS Audit Manager API Reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
