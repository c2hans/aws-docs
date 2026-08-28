---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-securitylake-subscriber-source.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SecurityLake::Subscriber Source
<a name="aws-properties-securitylake-subscriber-source"></a>

Sources are logs and events generated from a single system that match a specific event class in the Open Cybersecurity Schema Framework (OCSF) schema. Amazon Security Lake can collect logs and events from a variety of sources, including natively supported AWS services and third-party custom sources.

## Syntax
<a name="aws-properties-securitylake-subscriber-source-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-securitylake-subscriber-source-syntax.json"></a>

```
{
  "[AwsLogSource](#cfn-securitylake-subscriber-source-awslogsource)" : {{AwsLogSource}},
  "[CustomLogSource](#cfn-securitylake-subscriber-source-customlogsource)" : {{CustomLogSource}}
}
```

### YAML
<a name="aws-properties-securitylake-subscriber-source-syntax.yaml"></a>

```
  [AwsLogSource](#cfn-securitylake-subscriber-source-awslogsource): {{
    AwsLogSource}}
  [CustomLogSource](#cfn-securitylake-subscriber-source-customlogsource): {{
    CustomLogSource}}
```

## Properties
<a name="aws-properties-securitylake-subscriber-source-properties"></a>

`AwsLogSource`  <a name="cfn-securitylake-subscriber-source-awslogsource"></a>
The natively supported AWS service which is used a Amazon Security Lake source to collect logs and events from.
*Required*: No
*Type*: [AwsLogSource](aws-properties-securitylake-subscriber-awslogsource.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CustomLogSource`  <a name="cfn-securitylake-subscriber-source-customlogsource"></a>
The custom log source AWS which is used a Amazon Security Lake source to collect logs and events from.
*Required*: No
*Type*: [CustomLogSource](aws-properties-securitylake-subscriber-customlogsource.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
