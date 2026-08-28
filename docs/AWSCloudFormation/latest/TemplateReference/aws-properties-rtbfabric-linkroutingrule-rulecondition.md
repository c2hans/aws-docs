---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-rtbfabric-linkroutingrule-rulecondition.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::RTBFabric::LinkRoutingRule RuleCondition
<a name="aws-properties-rtbfabric-linkroutingrule-rulecondition"></a>

<a name="aws-properties-rtbfabric-linkroutingrule-rulecondition-description"></a>The `RuleCondition` property type specifies Property description not available. for an [AWS::RTBFabric::LinkRoutingRule](aws-resource-rtbfabric-linkroutingrule.md).

## Syntax
<a name="aws-properties-rtbfabric-linkroutingrule-rulecondition-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-rtbfabric-linkroutingrule-rulecondition-syntax.json"></a>

```
{
  "[HostHeader](#cfn-rtbfabric-linkroutingrule-rulecondition-hostheader)" : {{String}},
  "[HostHeaderWildcard](#cfn-rtbfabric-linkroutingrule-rulecondition-hostheaderwildcard)" : {{String}},
  "[PathExact](#cfn-rtbfabric-linkroutingrule-rulecondition-pathexact)" : {{String}},
  "[PathPrefix](#cfn-rtbfabric-linkroutingrule-rulecondition-pathprefix)" : {{String}},
  "[QueryStringEquals](#cfn-rtbfabric-linkroutingrule-rulecondition-querystringequals)" : {{QueryStringKeyValuePair}},
  "[QueryStringExists](#cfn-rtbfabric-linkroutingrule-rulecondition-querystringexists)" : {{String}}
}
```

### YAML
<a name="aws-properties-rtbfabric-linkroutingrule-rulecondition-syntax.yaml"></a>

```
  [HostHeader](#cfn-rtbfabric-linkroutingrule-rulecondition-hostheader): {{String}}
  [HostHeaderWildcard](#cfn-rtbfabric-linkroutingrule-rulecondition-hostheaderwildcard): {{String}}
  [PathExact](#cfn-rtbfabric-linkroutingrule-rulecondition-pathexact): {{String}}
  [PathPrefix](#cfn-rtbfabric-linkroutingrule-rulecondition-pathprefix): {{String}}
  [QueryStringEquals](#cfn-rtbfabric-linkroutingrule-rulecondition-querystringequals): {{
    QueryStringKeyValuePair}}
  [QueryStringExists](#cfn-rtbfabric-linkroutingrule-rulecondition-querystringexists): {{
    String}}
```

## Properties
<a name="aws-properties-rtbfabric-linkroutingrule-rulecondition-properties"></a>

`HostHeader`  <a name="cfn-rtbfabric-linkroutingrule-rulecondition-hostheader"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^[A-Za-z0-9._~-]+$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HostHeaderWildcard`  <a name="cfn-rtbfabric-linkroutingrule-rulecondition-hostheaderwildcard"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^[A-Za-z0-9._~*-]+$`
*Minimum*: `3`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PathExact`  <a name="cfn-rtbfabric-linkroutingrule-rulecondition-pathexact"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^/[A-Za-z0-9._~/-]*$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PathPrefix`  <a name="cfn-rtbfabric-linkroutingrule-rulecondition-pathprefix"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^/[A-Za-z0-9._~/-]*$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`QueryStringEquals`  <a name="cfn-rtbfabric-linkroutingrule-rulecondition-querystringequals"></a>
Property description not available.
*Required*: No
*Type*: [QueryStringKeyValuePair](aws-properties-rtbfabric-linkroutingrule-querystringkeyvaluepair.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`QueryStringExists`  <a name="cfn-rtbfabric-linkroutingrule-rulecondition-querystringexists"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^[A-Za-z0-9._~-]+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
