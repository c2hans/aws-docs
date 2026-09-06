---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-eks-addon-podidentityassociation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EKS::Addon PodIdentityAssociation
<a name="aws-properties-eks-addon-podidentityassociation"></a>

Amazon EKS Pod Identity associations provide the ability to manage credentials for your applications, similar to the way that Amazon EC2 instance profiles provide credentials to Amazon EC2 instances.

## Syntax
<a name="aws-properties-eks-addon-podidentityassociation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-eks-addon-podidentityassociation-syntax.json"></a>

```
{
  "[RoleArn](#cfn-eks-addon-podidentityassociation-rolearn)" : {{String}},
  "[ServiceAccount](#cfn-eks-addon-podidentityassociation-serviceaccount)" : {{String}}
}
```

### YAML
<a name="aws-properties-eks-addon-podidentityassociation-syntax.yaml"></a>

```
  [RoleArn](#cfn-eks-addon-podidentityassociation-rolearn): {{String}}
  [ServiceAccount](#cfn-eks-addon-podidentityassociation-serviceaccount): {{String}}
```

## Properties
<a name="aws-properties-eks-addon-podidentityassociation-properties"></a>

`RoleArn`  <a name="cfn-eks-addon-podidentityassociation-rolearn"></a>
The Amazon Resource Name (ARN) of the IAM role to associate with the service account. The EKS Pod Identity agent manages credentials to assume this role for applications in the containers in the Pods that use this service account.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws[a-zA-Z-]*:iam::\d{12}:(role)\/*`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ServiceAccount`  <a name="cfn-eks-addon-podidentityassociation-serviceaccount"></a>
The name of the Kubernetes service account inside the cluster to associate the IAM credentials with.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
