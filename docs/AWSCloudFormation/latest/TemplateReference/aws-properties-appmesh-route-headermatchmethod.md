---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appmesh-route-headermatchmethod.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppMesh::Route HeaderMatchMethod
<a name="aws-properties-appmesh-route-headermatchmethod"></a>

An object that represents the method and value to match with the header value sent in a request. Specify one match method.

## Syntax
<a name="aws-properties-appmesh-route-headermatchmethod-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appmesh-route-headermatchmethod-syntax.json"></a>

```
{
  "[Exact](#cfn-appmesh-route-headermatchmethod-exact)" : {{String}},
  "[Prefix](#cfn-appmesh-route-headermatchmethod-prefix)" : {{String}},
  "[Range](#cfn-appmesh-route-headermatchmethod-range)" : {{MatchRange}},
  "[Regex](#cfn-appmesh-route-headermatchmethod-regex)" : {{String}},
  "[Suffix](#cfn-appmesh-route-headermatchmethod-suffix)" : {{String}}
}
```

### YAML
<a name="aws-properties-appmesh-route-headermatchmethod-syntax.yaml"></a>

```
  [Exact](#cfn-appmesh-route-headermatchmethod-exact): {{String}}
  [Prefix](#cfn-appmesh-route-headermatchmethod-prefix): {{String}}
  [Range](#cfn-appmesh-route-headermatchmethod-range): {{
    MatchRange}}
  [Regex](#cfn-appmesh-route-headermatchmethod-regex): {{String}}
  [Suffix](#cfn-appmesh-route-headermatchmethod-suffix): {{String}}
```

## Properties
<a name="aws-properties-appmesh-route-headermatchmethod-properties"></a>

`Exact`  <a name="cfn-appmesh-route-headermatchmethod-exact"></a>
The value sent by the client must match the specified value exactly.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Prefix`  <a name="cfn-appmesh-route-headermatchmethod-prefix"></a>
The value sent by the client must begin with the specified characters.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Range`  <a name="cfn-appmesh-route-headermatchmethod-range"></a>
An object that represents the range of values to match on.
*Required*: No
*Type*: [MatchRange](aws-properties-appmesh-route-matchrange.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Regex`  <a name="cfn-appmesh-route-headermatchmethod-regex"></a>
The value sent by the client must include the specified characters.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Suffix`  <a name="cfn-appmesh-route-headermatchmethod-suffix"></a>
The value sent by the client must end with the specified characters.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
