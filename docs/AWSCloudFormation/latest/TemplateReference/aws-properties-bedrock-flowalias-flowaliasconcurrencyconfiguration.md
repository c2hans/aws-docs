---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-flowalias-flowaliasconcurrencyconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::FlowAlias FlowAliasConcurrencyConfiguration
<a name="aws-properties-bedrock-flowalias-flowaliasconcurrencyconfiguration"></a>

Determines how multiple nodes in a flow can run in parallel. Running nodes concurrently can improve your flow's performance.

## Syntax
<a name="aws-properties-bedrock-flowalias-flowaliasconcurrencyconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-flowalias-flowaliasconcurrencyconfiguration-syntax.json"></a>

```
{
  "[MaxConcurrency](#cfn-bedrock-flowalias-flowaliasconcurrencyconfiguration-maxconcurrency)" : {{Number}},
  "[Type](#cfn-bedrock-flowalias-flowaliasconcurrencyconfiguration-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-flowalias-flowaliasconcurrencyconfiguration-syntax.yaml"></a>

```
  [MaxConcurrency](#cfn-bedrock-flowalias-flowaliasconcurrencyconfiguration-maxconcurrency): {{Number}}
  [Type](#cfn-bedrock-flowalias-flowaliasconcurrencyconfiguration-type): {{String}}
```

## Properties
<a name="aws-properties-bedrock-flowalias-flowaliasconcurrencyconfiguration-properties"></a>

`MaxConcurrency`  <a name="cfn-bedrock-flowalias-flowaliasconcurrencyconfiguration-maxconcurrency"></a>
The maximum number of nodes that can be executed concurrently in the flow.
*Required*: No
*Type*: Number
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-bedrock-flowalias-flowaliasconcurrencyconfiguration-type"></a>
The type of concurrency to use for parallel node execution. Specify one of the following options:
+ `Automatic` - Amazon Bedrock determines which nodes can be executed in parallel based on the flow definition and its dependencies.
+ `Manual` - You specify which nodes can be executed in parallel.
*Required*: Yes
*Type*: String
*Allowed values*: `Automatic | Manual`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
