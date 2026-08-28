---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-gameliftstreams-streamgroup-defaultapplication.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::GameLiftStreams::StreamGroup DefaultApplication
<a name="aws-properties-gameliftstreams-streamgroup-defaultapplication"></a>

Represents the default Amazon GameLift Streams application that a stream group hosts.

## Syntax
<a name="aws-properties-gameliftstreams-streamgroup-defaultapplication-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-gameliftstreams-streamgroup-defaultapplication-syntax.json"></a>

```
{
  "[Arn](#cfn-gameliftstreams-streamgroup-defaultapplication-arn)" : {{String}},
  "[Id](#cfn-gameliftstreams-streamgroup-defaultapplication-id)" : {{String}}
}
```

### YAML
<a name="aws-properties-gameliftstreams-streamgroup-defaultapplication-syntax.yaml"></a>

```
  [Arn](#cfn-gameliftstreams-streamgroup-defaultapplication-arn): {{String}}
  [Id](#cfn-gameliftstreams-streamgroup-defaultapplication-id): {{String}}
```

## Properties
<a name="aws-properties-gameliftstreams-streamgroup-defaultapplication-properties"></a>

`Arn`  <a name="cfn-gameliftstreams-streamgroup-defaultapplication-arn"></a>
An [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html) that uniquely identifies the application resource. Example ARN: `arn:aws:gameliftstreams:us-west-2:111122223333:application/a-9ZY8X7Wv6`.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws:gameliftstreams:([^: ]*):([0-9]{12}):([^: ]*)$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Id`  <a name="cfn-gameliftstreams-streamgroup-defaultapplication-id"></a>
An ID that uniquely identifies the application resource. Example ID: `a-9ZY8X7Wv6`.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9-]+$`
*Minimum*: `1`
*Maximum*: `32`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
