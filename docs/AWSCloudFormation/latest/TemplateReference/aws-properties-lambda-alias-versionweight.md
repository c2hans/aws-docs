---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-alias-versionweight.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lambda::Alias VersionWeight
<a name="aws-properties-lambda-alias-versionweight"></a>

The [traffic-shifting](https://docs.aws.amazon.com/lambda/latest/dg/lambda-traffic-shifting-using-aliases.html) configuration of a Lambda function alias.

## Syntax
<a name="aws-properties-lambda-alias-versionweight-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lambda-alias-versionweight-syntax.json"></a>

```
{
  "[FunctionVersion](#cfn-lambda-alias-versionweight-functionversion)" : {{String}},
  "[FunctionWeight](#cfn-lambda-alias-versionweight-functionweight)" : {{Number}}
}
```

### YAML
<a name="aws-properties-lambda-alias-versionweight-syntax.yaml"></a>

```
  [FunctionVersion](#cfn-lambda-alias-versionweight-functionversion): {{String}}
  [FunctionWeight](#cfn-lambda-alias-versionweight-functionweight): {{Number}}
```

## Properties
<a name="aws-properties-lambda-alias-versionweight-properties"></a>

`FunctionVersion`  <a name="cfn-lambda-alias-versionweight-functionversion"></a>
The qualifier of the second version.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FunctionWeight`  <a name="cfn-lambda-alias-versionweight-functionweight"></a>
The percentage of traffic that the alias routes to the second version.
*Required*: Yes
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Examples
<a name="aws-properties-lambda-alias-versionweight--examples"></a>

### Routing Configuration
<a name="aws-properties-lambda-alias-versionweight--examples--Routing_Configuration"></a>

An alias that routes half of incoming requests to a second version.

#### YAML
<a name="aws-properties-lambda-alias-versionweight--examples--Routing_Configuration--yaml"></a>

```
  alias:
    Type: AWS::Lambda::Alias
    Properties:
      FunctionName: !Ref function
      FunctionVersion: !GetAtt newVersion.Version
      Name: BLUE
      RoutingConfig:
        AdditionalVersionWeights:
          - FunctionVersion: !GetAtt version.Version
            FunctionWeight: 0.5
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
