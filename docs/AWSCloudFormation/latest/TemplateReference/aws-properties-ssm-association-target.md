---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ssm-association-target.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SSM::Association Target
<a name="aws-properties-ssm-association-target"></a>

`Target` is a property of the [AWS::SSM::Association](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html) resource that specifies the targets for an SSM document in Systems Manager. You can target all instances in an AWS account by specifying the `InstanceIds` key with a value of `*`. To view a JSON and a YAML example that targets all instances, see the example "Create an association for all managed instances in an AWS account" later in this page.

## Syntax
<a name="aws-properties-ssm-association-target-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ssm-association-target-syntax.json"></a>

```
{
  "[Key](#cfn-ssm-association-target-key)" : {{String}},
  "[Values](#cfn-ssm-association-target-values)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-ssm-association-target-syntax.yaml"></a>

```
  [Key](#cfn-ssm-association-target-key): {{String}}
  [Values](#cfn-ssm-association-target-values): {{
    - String}}
```

## Properties
<a name="aws-properties-ssm-association-target-properties"></a>

`Key`  <a name="cfn-ssm-association-target-key"></a>
User-defined criteria for sending commands that target managed nodes that meet the criteria.
*Required*: Yes
*Type*: String
*Pattern*: `^[\p{L}\p{Z}\p{N}_.:/=+\-@]{1,128}$|resource-groups:Name`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Values`  <a name="cfn-ssm-association-target-values"></a>
User-defined criteria that maps to `Key`. For example, if you specified `tag:ServerRole`, you could specify `value:WebServer` to run a command on instances that include EC2 tags of `ServerRole,WebServer`.
Depending on the type of target, the maximum number of values for a key might be lower than the global maximum of 50.
*Required*: Yes
*Type*: Array of String
*Minimum*: `0`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
