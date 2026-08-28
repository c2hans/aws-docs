---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecr-replicationconfiguration-repositoryfilter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECR::ReplicationConfiguration RepositoryFilter
<a name="aws-properties-ecr-replicationconfiguration-repositoryfilter"></a>

The filter settings used with image replication. Specifying a repository filter to a replication rule provides a method for controlling which repositories in a private registry are replicated. If no filters are added, the contents of all repositories are replicated.

## Syntax
<a name="aws-properties-ecr-replicationconfiguration-repositoryfilter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ecr-replicationconfiguration-repositoryfilter-syntax.json"></a>

```
{
  "[Filter](#cfn-ecr-replicationconfiguration-repositoryfilter-filter)" : {{String}},
  "[FilterType](#cfn-ecr-replicationconfiguration-repositoryfilter-filtertype)" : {{String}}
}
```

### YAML
<a name="aws-properties-ecr-replicationconfiguration-repositoryfilter-syntax.yaml"></a>

```
  [Filter](#cfn-ecr-replicationconfiguration-repositoryfilter-filter): {{String}}
  [FilterType](#cfn-ecr-replicationconfiguration-repositoryfilter-filtertype): {{String}}
```

## Properties
<a name="aws-properties-ecr-replicationconfiguration-repositoryfilter-properties"></a>

`Filter`  <a name="cfn-ecr-replicationconfiguration-repositoryfilter-filter"></a>
The repository filter details. When the `PREFIX_MATCH` filter type is specified, this value is required and should be the repository name prefix to configure replication for.
*Required*: Yes
*Type*: String
*Pattern*: `^(?:[a-z0-9]+(?:[._-][a-z0-9]*)*/)*[a-z0-9]*(?:[._-][a-z0-9]*)*$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FilterType`  <a name="cfn-ecr-replicationconfiguration-repositoryfilter-filtertype"></a>
The repository filter type. The only supported value is `PREFIX_MATCH`, which is a repository name prefix specified with the `filter` parameter.
*Required*: Yes
*Type*: String
*Allowed values*: `PREFIX_MATCH`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
