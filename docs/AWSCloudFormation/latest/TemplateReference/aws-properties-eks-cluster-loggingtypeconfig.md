---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-eks-cluster-loggingtypeconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EKS::Cluster LoggingTypeConfig
<a name="aws-properties-eks-cluster-loggingtypeconfig"></a>

The enabled logging type. For a list of the valid logging types, see the [`types` property of `LogSetup`](https://docs.aws.amazon.com/eks/latest/APIReference/API_LogSetup.html#AmazonEKS-Type-LogSetup-types) in the *Amazon EKS API Reference*.

## Syntax
<a name="aws-properties-eks-cluster-loggingtypeconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-eks-cluster-loggingtypeconfig-syntax.json"></a>

```
{
  "[Type](#cfn-eks-cluster-loggingtypeconfig-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-eks-cluster-loggingtypeconfig-syntax.yaml"></a>

```
  [Type](#cfn-eks-cluster-loggingtypeconfig-type): {{String}}
```

## Properties
<a name="aws-properties-eks-cluster-loggingtypeconfig-properties"></a>

`Type`  <a name="cfn-eks-cluster-loggingtypeconfig-type"></a>
The name of the log type.
*Required*: No
*Type*: String
*Allowed values*: `api | audit | authenticator | controllerManager | scheduler`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
