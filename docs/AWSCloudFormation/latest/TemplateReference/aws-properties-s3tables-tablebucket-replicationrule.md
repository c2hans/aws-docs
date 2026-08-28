---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-s3tables-tablebucket-replicationrule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3Tables::TableBucket ReplicationRule
<a name="aws-properties-s3tables-tablebucket-replicationrule"></a>

<a name="aws-properties-s3tables-tablebucket-replicationrule-description"></a>The `ReplicationRule` property type specifies Property description not available. for an [AWS::S3Tables::TableBucket](aws-resource-s3tables-tablebucket.md).

## Syntax
<a name="aws-properties-s3tables-tablebucket-replicationrule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-s3tables-tablebucket-replicationrule-syntax.json"></a>

```
{
  "[Destinations](#cfn-s3tables-tablebucket-replicationrule-destinations)" : {{[ ReplicationDestination, ... ]}}
}
```

### YAML
<a name="aws-properties-s3tables-tablebucket-replicationrule-syntax.yaml"></a>

```
  [Destinations](#cfn-s3tables-tablebucket-replicationrule-destinations): {{
    - ReplicationDestination}}
```

## Properties
<a name="aws-properties-s3tables-tablebucket-replicationrule-properties"></a>

`Destinations`  <a name="cfn-s3tables-tablebucket-replicationrule-destinations"></a>
Property description not available.
*Required*: Yes
*Type*: Array of [ReplicationDestination](aws-properties-s3tables-tablebucket-replicationdestination.md)
*Minimum*: `1`
*Maximum*: `5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
