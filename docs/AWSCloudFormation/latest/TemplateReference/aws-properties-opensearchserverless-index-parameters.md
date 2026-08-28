---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-opensearchserverless-index-parameters.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::OpenSearchServerless::Index Parameters
<a name="aws-properties-opensearchserverless-index-parameters"></a>

Additional parameters for the k-NN algorithm.

## Syntax
<a name="aws-properties-opensearchserverless-index-parameters-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-opensearchserverless-index-parameters-syntax.json"></a>

```
{
  "[EfConstruction](#cfn-opensearchserverless-index-parameters-efconstruction)" : {{Integer}},
  "[M](#cfn-opensearchserverless-index-parameters-m)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-opensearchserverless-index-parameters-syntax.yaml"></a>

```
  [EfConstruction](#cfn-opensearchserverless-index-parameters-efconstruction): {{Integer}}
  [M](#cfn-opensearchserverless-index-parameters-m): {{Integer}}
```

## Properties
<a name="aws-properties-opensearchserverless-index-parameters-properties"></a>

`EfConstruction`  <a name="cfn-opensearchserverless-index-parameters-efconstruction"></a>
The size of the dynamic list used during k-NN graph creation.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`M`  <a name="cfn-opensearchserverless-index-parameters-m"></a>
Number of neighbors to consider during k-NN search.
*Required*: No
*Type*: Integer
*Minimum*: `2`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
