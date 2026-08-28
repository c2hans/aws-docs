---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecr-replicationconfiguration-replicationrule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECR::ReplicationConfiguration ReplicationRule
<a name="aws-properties-ecr-replicationconfiguration-replicationrule"></a>

An array of objects representing the replication destinations and repository filters for a replication configuration.

## Syntax
<a name="aws-properties-ecr-replicationconfiguration-replicationrule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ecr-replicationconfiguration-replicationrule-syntax.json"></a>

```
{
  "[Destinations](#cfn-ecr-replicationconfiguration-replicationrule-destinations)" : {{[ ReplicationDestination, ... ]}},
  "[RepositoryFilters](#cfn-ecr-replicationconfiguration-replicationrule-repositoryfilters)" : {{[ RepositoryFilter, ... ]}}
}
```

### YAML
<a name="aws-properties-ecr-replicationconfiguration-replicationrule-syntax.yaml"></a>

```
  [Destinations](#cfn-ecr-replicationconfiguration-replicationrule-destinations): {{
    - ReplicationDestination}}
  [RepositoryFilters](#cfn-ecr-replicationconfiguration-replicationrule-repositoryfilters): {{
    - RepositoryFilter}}
```

## Properties
<a name="aws-properties-ecr-replicationconfiguration-replicationrule-properties"></a>

`Destinations`  <a name="cfn-ecr-replicationconfiguration-replicationrule-destinations"></a>
An array of objects representing the destination for a replication rule.
*Required*: Yes
*Type*: Array of [ReplicationDestination](aws-properties-ecr-replicationconfiguration-replicationdestination.md)
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RepositoryFilters`  <a name="cfn-ecr-replicationconfiguration-replicationrule-repositoryfilters"></a>
An array of objects representing the filters for a replication rule. Specifying a repository filter for a replication rule provides a method for controlling which repositories in a private registry are replicated.
*Required*: No
*Type*: Array of [RepositoryFilter](aws-properties-ecr-replicationconfiguration-repositoryfilter.md)
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
