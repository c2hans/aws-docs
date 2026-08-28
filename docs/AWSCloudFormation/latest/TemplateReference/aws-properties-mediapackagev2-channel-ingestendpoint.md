---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediapackagev2-channel-ingestendpoint.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaPackageV2::Channel IngestEndpoint
<a name="aws-properties-mediapackagev2-channel-ingestendpoint"></a>

The input URL where the source stream should be sent.

## Syntax
<a name="aws-properties-mediapackagev2-channel-ingestendpoint-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediapackagev2-channel-ingestendpoint-syntax.json"></a>

```
{
  "[Id](#cfn-mediapackagev2-channel-ingestendpoint-id)" : {{String}},
  "[Url](#cfn-mediapackagev2-channel-ingestendpoint-url)" : {{String}}
}
```

### YAML
<a name="aws-properties-mediapackagev2-channel-ingestendpoint-syntax.yaml"></a>

```
  [Id](#cfn-mediapackagev2-channel-ingestendpoint-id): {{String}}
  [Url](#cfn-mediapackagev2-channel-ingestendpoint-url): {{String}}
```

## Properties
<a name="aws-properties-mediapackagev2-channel-ingestendpoint-properties"></a>

`Id`  <a name="cfn-mediapackagev2-channel-ingestendpoint-id"></a>
The identifier associated with the ingest endpoint of the channel.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Url`  <a name="cfn-mediapackagev2-channel-ingestendpoint-url"></a>
The URL associated with the ingest endpoint of the channel.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
