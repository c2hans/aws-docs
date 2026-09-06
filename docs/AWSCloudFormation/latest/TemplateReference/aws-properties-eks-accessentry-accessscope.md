---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-eks-accessentry-accessscope.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EKS::AccessEntry AccessScope
<a name="aws-properties-eks-accessentry-accessscope"></a>

The scope of an `AccessPolicy` that's associated to an `AccessEntry`.

## Syntax
<a name="aws-properties-eks-accessentry-accessscope-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-eks-accessentry-accessscope-syntax.json"></a>

```
{
  "[Namespaces](#cfn-eks-accessentry-accessscope-namespaces)" : {{[ String, ... ]}},
  "[Type](#cfn-eks-accessentry-accessscope-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-eks-accessentry-accessscope-syntax.yaml"></a>

```
  [Namespaces](#cfn-eks-accessentry-accessscope-namespaces): {{
    - String}}
  [Type](#cfn-eks-accessentry-accessscope-type): {{String}}
```

## Properties
<a name="aws-properties-eks-accessentry-accessscope-properties"></a>

`Namespaces`  <a name="cfn-eks-accessentry-accessscope-namespaces"></a>
A Kubernetes `namespace` that an access policy is scoped to. A value is required if you specified `namespace` for `Type`.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-eks-accessentry-accessscope-type"></a>
The scope type of an access policy.
*Required*: Yes
*Type*: String
*Allowed values*: `namespace | cluster`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
