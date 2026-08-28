---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecr-replicationconfiguration-replicationdestination.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECR::ReplicationConfiguration ReplicationDestination
<a name="aws-properties-ecr-replicationconfiguration-replicationdestination"></a>

An array of objects representing the destination for a replication rule.

## Syntax
<a name="aws-properties-ecr-replicationconfiguration-replicationdestination-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ecr-replicationconfiguration-replicationdestination-syntax.json"></a>

```
{
  "[Region](#cfn-ecr-replicationconfiguration-replicationdestination-region)" : {{String}},
  "[RegistryId](#cfn-ecr-replicationconfiguration-replicationdestination-registryid)" : {{String}}
}
```

### YAML
<a name="aws-properties-ecr-replicationconfiguration-replicationdestination-syntax.yaml"></a>

```
  [Region](#cfn-ecr-replicationconfiguration-replicationdestination-region): {{String}}
  [RegistryId](#cfn-ecr-replicationconfiguration-replicationdestination-registryid): {{String}}
```

## Properties
<a name="aws-properties-ecr-replicationconfiguration-replicationdestination-properties"></a>

`Region`  <a name="cfn-ecr-replicationconfiguration-replicationdestination-region"></a>
The Region to replicate to.
*Required*: Yes
*Type*: String
*Pattern*: `[0-9a-z-]{2,25}`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RegistryId`  <a name="cfn-ecr-replicationconfiguration-replicationdestination-registryid"></a>
The AWS account ID of the Amazon ECR private registry to replicate to. When configuring cross-Region replication within your own registry, specify your own account ID.
*Required*: Yes
*Type*: String
*Pattern*: `^[0-9]{12}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
