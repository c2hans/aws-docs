---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-auditmanager-assessmentframework-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AuditManager::AssessmentFramework Tag
<a name="aws-properties-auditmanager-assessmentframework-tag"></a>

<a name="aws-properties-auditmanager-assessmentframework-tag-description"></a>The `Tag` property type specifies Property description not available. for an [AWS::AuditManager::AssessmentFramework](aws-resource-auditmanager-assessmentframework.md).

## Syntax
<a name="aws-properties-auditmanager-assessmentframework-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-auditmanager-assessmentframework-tag-syntax.json"></a>

```
{
  "[Key](#cfn-auditmanager-assessmentframework-tag-key)" : {{String}},
  "[Value](#cfn-auditmanager-assessmentframework-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-auditmanager-assessmentframework-tag-syntax.yaml"></a>

```
  [Key](#cfn-auditmanager-assessmentframework-tag-key): {{String}}
  [Value](#cfn-auditmanager-assessmentframework-tag-value): {{String}}
```

## Properties
<a name="aws-properties-auditmanager-assessmentframework-tag-properties"></a>

`Key`  <a name="cfn-auditmanager-assessmentframework-tag-key"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^(?!aws:)[a-zA-Z+-=._:/]+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-auditmanager-assessmentframework-tag-value"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
