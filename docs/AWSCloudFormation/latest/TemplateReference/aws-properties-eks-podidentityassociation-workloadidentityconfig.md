---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-eks-podidentityassociation-workloadidentityconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EKS::PodIdentityAssociation WorkloadIdentityConfig

<a name="aws-properties-eks-podidentityassociation-workloadidentityconfig-description"></a>The `WorkloadIdentityConfig` property type specifies Property description not available. for an [AWS::EKS::PodIdentityAssociation](aws-resource-eks-podidentityassociation.md).

## Syntax
<a name="aws-properties-eks-podidentityassociation-workloadidentityconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-eks-podidentityassociation-workloadidentityconfig-syntax.json"></a>

```
{
  "[Enabled](#cfn-eks-podidentityassociation-workloadidentityconfig-enabled)" : {{Boolean}},
  "[ProviderArn](#cfn-eks-podidentityassociation-workloadidentityconfig-providerarn)" : {{String}},
  "[TemplateArn](#cfn-eks-podidentityassociation-workloadidentityconfig-templatearn)" : {{String}}
}
```

### YAML
<a name="aws-properties-eks-podidentityassociation-workloadidentityconfig-syntax.yaml"></a>

```
  [Enabled](#cfn-eks-podidentityassociation-workloadidentityconfig-enabled): {{Boolean}}
  [ProviderArn](#cfn-eks-podidentityassociation-workloadidentityconfig-providerarn): {{String}}
  [TemplateArn](#cfn-eks-podidentityassociation-workloadidentityconfig-templatearn): {{String}}
```

## Properties
<a name="aws-properties-eks-podidentityassociation-workloadidentityconfig-properties"></a>

`Enabled`  <a name="cfn-eks-podidentityassociation-workloadidentityconfig-enabled"></a>
Property description not available.
*Required*: Yes
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ProviderArn`  <a name="cfn-eks-podidentityassociation-workloadidentityconfig-providerarn"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws[a-zA-Z-]*:iam::([0-9]{12}|o-[a-z0-9]{10,32}):workload-identity-provider/[^/]+$`
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TemplateArn`  <a name="cfn-eks-podidentityassociation-workloadidentityconfig-templatearn"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws[a-zA-Z-]*:iam::[0-9]{12}:workload-identity-template/[^/]+$`
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
