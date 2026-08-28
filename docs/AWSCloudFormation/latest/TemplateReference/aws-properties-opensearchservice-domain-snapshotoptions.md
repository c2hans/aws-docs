---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-opensearchservice-domain-snapshotoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::OpenSearchService::Domain SnapshotOptions
<a name="aws-properties-opensearchservice-domain-snapshotoptions"></a>

**DEPRECATED**. This setting is only relevant to domains running legacy Elasticsearch OSS versions earlier than 5.3. It does not apply to OpenSearch domains.

The automated snapshot configuration for the OpenSearch Service domain indexes.

## Syntax
<a name="aws-properties-opensearchservice-domain-snapshotoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-opensearchservice-domain-snapshotoptions-syntax.json"></a>

```
{
  "[AutomatedSnapshotStartHour](#cfn-opensearchservice-domain-snapshotoptions-automatedsnapshotstarthour)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-opensearchservice-domain-snapshotoptions-syntax.yaml"></a>

```
  [AutomatedSnapshotStartHour](#cfn-opensearchservice-domain-snapshotoptions-automatedsnapshotstarthour): {{Integer}}
```

## Properties
<a name="aws-properties-opensearchservice-domain-snapshotoptions-properties"></a>

`AutomatedSnapshotStartHour`  <a name="cfn-opensearchservice-domain-snapshotoptions-automatedsnapshotstarthour"></a>
The hour in UTC during which the service takes an automated daily snapshot of the indexes in the OpenSearch Service domain. For example, if you specify 0, OpenSearch Service takes an automated snapshot everyday between midnight and 1 am. You can specify a value between 0 and 23.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
