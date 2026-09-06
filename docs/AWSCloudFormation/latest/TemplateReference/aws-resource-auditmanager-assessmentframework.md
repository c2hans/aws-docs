---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-auditmanager-assessmentframework.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AuditManager::AssessmentFramework
<a name="aws-resource-auditmanager-assessmentframework"></a>

 The file used to structure and automate AWS Audit Manager assessments for a given compliance standard.

## Syntax
<a name="aws-resource-auditmanager-assessmentframework-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-auditmanager-assessmentframework-syntax.json"></a>

```
{
  "Type" : "AWS::AuditManager::AssessmentFramework",
  "Properties" : {
      "[ComplianceType](#cfn-auditmanager-assessmentframework-compliancetype)" : {{String}},
      "[ControlSets](#cfn-auditmanager-assessmentframework-controlsets)" : {{[ ControlSet, ... ]}},
      "[Description](#cfn-auditmanager-assessmentframework-description)" : {{String}},
      "[Name](#cfn-auditmanager-assessmentframework-name)" : {{String}},
      "[Tags](#cfn-auditmanager-assessmentframework-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-auditmanager-assessmentframework-syntax.yaml"></a>

```
Type: AWS::AuditManager::AssessmentFramework
Properties:
  [ComplianceType](#cfn-auditmanager-assessmentframework-compliancetype): {{String}}
  [ControlSets](#cfn-auditmanager-assessmentframework-controlsets): {{
    - ControlSet}}
  [Description](#cfn-auditmanager-assessmentframework-description): {{String}}
  [Name](#cfn-auditmanager-assessmentframework-name): {{String}}
  [Tags](#cfn-auditmanager-assessmentframework-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-auditmanager-assessmentframework-properties"></a>

`ComplianceType`  <a name="cfn-auditmanager-assessmentframework-compliancetype"></a>
 The compliance type that the new custom framework supports, such as CIS or HIPAA.
*Required*: No
*Type*: String
*Pattern*: `^[\w\W\s\S]*$`
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ControlSets`  <a name="cfn-auditmanager-assessmentframework-controlsets"></a>
 The control sets that are associated with the framework.
*Required*: Yes
*Type*: Array of [ControlSet](aws-properties-auditmanager-assessmentframework-controlset.md)
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-auditmanager-assessmentframework-description"></a>
 The description of the framework.
*Required*: No
*Type*: String
*Pattern*: `^[\w\W\s\S]*$`
*Minimum*: `1`
*Maximum*: `1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-auditmanager-assessmentframework-name"></a>
 The name of the framework.
*Required*: Yes
*Type*: String
*Pattern*: `^[^\\]*$`
*Minimum*: `1`
*Maximum*: `300`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-auditmanager-assessmentframework-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-auditmanager-assessmentframework-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-auditmanager-assessmentframework-return-values"></a>

### Ref
<a name="aws-resource-auditmanager-assessmentframework-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-auditmanager-assessmentframework-return-values-fn--getatt"></a>

####
<a name="aws-resource-auditmanager-assessmentframework-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
 The Amazon Resource Name (ARN) of the framework.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
 The time when the framework was created.

`CreatedBy`  <a name="CreatedBy-fn::getatt"></a>
Property description not available.

`FrameworkId`  <a name="FrameworkId-fn::getatt"></a>
The unique identifier for the shared custom framework.

`LastUpdatedAt`  <a name="LastUpdatedAt-fn::getatt"></a>
 The time when the framework was most recently updated.

`LastUpdatedBy`  <a name="LastUpdatedBy-fn::getatt"></a>
Property description not available.

`Type`  <a name="Type-fn::getatt"></a>
 The framework type, such as a standard framework or a custom framework.
