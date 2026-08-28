---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-dynamodb-globaltable-globaltablewitness.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DynamoDB::GlobalTable GlobalTableWitness
<a name="aws-properties-dynamodb-globaltable-globaltablewitness"></a>

The witness Region for the MRSC global table. A MRSC global table can be configured with either three replicas, or with two replicas and one witness.

The witness must be in a different Region than the replicas and within the same Region set:
+ US Region set: US East (N. Virginia), US East (Ohio), US West (Oregon)
+ EU Region set: Europe (Ireland), Europe (London), Europe (Paris), Europe (Frankfurt)
+ AP Region set: Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka)

## Syntax
<a name="aws-properties-dynamodb-globaltable-globaltablewitness-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-dynamodb-globaltable-globaltablewitness-syntax.json"></a>

```
{
  "[Region](#cfn-dynamodb-globaltable-globaltablewitness-region)" : {{String}}
}
```

### YAML
<a name="aws-properties-dynamodb-globaltable-globaltablewitness-syntax.yaml"></a>

```
  [Region](#cfn-dynamodb-globaltable-globaltablewitness-region): {{String}}
```

## Properties
<a name="aws-properties-dynamodb-globaltable-globaltablewitness-properties"></a>

`Region`  <a name="cfn-dynamodb-globaltable-globaltablewitness-region"></a>
The name of the AWSRegion that serves as a witness for the MRSC global table.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
