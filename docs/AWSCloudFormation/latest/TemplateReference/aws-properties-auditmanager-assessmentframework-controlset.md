---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-auditmanager-assessmentframework-controlset.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AuditManager::AssessmentFramework ControlSet
<a name="aws-properties-auditmanager-assessmentframework-controlset"></a>

 A set of controls in AWS Audit Manager.

## Syntax
<a name="aws-properties-auditmanager-assessmentframework-controlset-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-auditmanager-assessmentframework-controlset-syntax.json"></a>

```
{
  "[Controls](#cfn-auditmanager-assessmentframework-controlset-controls)" : {{[ ControlSetControl, ... ]}},
  "[Name](#cfn-auditmanager-assessmentframework-controlset-name)" : {{String}}
}
```

### YAML
<a name="aws-properties-auditmanager-assessmentframework-controlset-syntax.yaml"></a>

```
  [Controls](#cfn-auditmanager-assessmentframework-controlset-controls): {{
    - ControlSetControl}}
  [Name](#cfn-auditmanager-assessmentframework-controlset-name): {{String}}
```

## Properties
<a name="aws-properties-auditmanager-assessmentframework-controlset-properties"></a>

`Controls`  <a name="cfn-auditmanager-assessmentframework-controlset-controls"></a>
 The list of controls within the control set.
*Required*: Yes
*Type*: Array of [ControlSetControl](aws-properties-auditmanager-assessmentframework-controlsetcontrol.md)
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-auditmanager-assessmentframework-controlset-name"></a>
 The name of the control set.
*Required*: Yes
*Type*: String
*Pattern*: `^[^\\_]*$`
*Minimum*: `1`
*Maximum*: `300`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
