---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-knowledgebase-accesscontrolconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::KnowledgeBase AccessControlConfiguration
<a name="aws-properties-quicksight-knowledgebase-accesscontrolconfiguration"></a>

The access control settings for a knowledge base. Use this structure to enable or disable document-level access control lists (ACLs) that filter query results based on the permissions from the source data connector.

## Syntax
<a name="aws-properties-quicksight-knowledgebase-accesscontrolconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-knowledgebase-accesscontrolconfiguration-syntax.json"></a>

```
{
  "[IsACLEnabled](#cfn-quicksight-knowledgebase-accesscontrolconfiguration-isaclenabled)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-quicksight-knowledgebase-accesscontrolconfiguration-syntax.yaml"></a>

```
  [IsACLEnabled](#cfn-quicksight-knowledgebase-accesscontrolconfiguration-isaclenabled): {{Boolean}}
```

## Properties
<a name="aws-properties-quicksight-knowledgebase-accesscontrolconfiguration-properties"></a>

`IsACLEnabled`  <a name="cfn-quicksight-knowledgebase-accesscontrolconfiguration-isaclenabled"></a>
Specifies whether ACLs are enabled for the knowledge base.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
