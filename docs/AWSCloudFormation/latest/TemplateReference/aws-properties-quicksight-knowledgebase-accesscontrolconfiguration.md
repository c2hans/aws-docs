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
This setting works together with the data source connector's ACL crawling. To enforce document-level access control end to end, set `isACLEnabled` to `true` and enable ACL crawling on the connector. For example, for an Amazon S3 data source, set `accessControlConfiguration.crawlAcl` to `true` in the connector template. For more information, see `KbTemplateConfiguration`. Enabling only one of the two settings does not produce a fully ACL-enforced knowledge base.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
