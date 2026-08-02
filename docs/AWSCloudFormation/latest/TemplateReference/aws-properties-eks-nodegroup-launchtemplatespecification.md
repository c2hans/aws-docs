---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-eks-nodegroup-launchtemplatespecification.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EKS::Nodegroup LaunchTemplateSpecification
<a name="aws-properties-eks-nodegroup-launchtemplatespecification"></a>

An object representing a node group launch template specification. The launch template can't include [https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateNetworkInterface.html](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateNetworkInterface.html), [https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_IamInstanceProfile.html](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_IamInstanceProfile.html), [https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RequestSpotInstances.html](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RequestSpotInstances.html), [https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_HibernationOptionsRequest.html](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_HibernationOptionsRequest.html), or [https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_TerminateInstances.html](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_TerminateInstances.html), or the node group deployment or update will fail. For more information about launch templates, see [https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateLaunchTemplate.html](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateLaunchTemplate.html) in the Amazon EC2 API Reference. For more information about using launch templates with Amazon EKS, see [Customizing managed nodes with launch templates](https://docs.aws.amazon.com/eks/latest/userguide/launch-templates.html) in the *Amazon EKS User Guide*.

You must specify either the launch template ID or the launch template name in the request, but not both.

## Syntax
<a name="aws-properties-eks-nodegroup-launchtemplatespecification-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-eks-nodegroup-launchtemplatespecification-syntax.json"></a>

```
{
  "[Id](#cfn-eks-nodegroup-launchtemplatespecification-id)" : {{String}},
  "[Name](#cfn-eks-nodegroup-launchtemplatespecification-name)" : {{String}},
  "[Version](#cfn-eks-nodegroup-launchtemplatespecification-version)" : {{String}}
}
```

### YAML
<a name="aws-properties-eks-nodegroup-launchtemplatespecification-syntax.yaml"></a>

```
  [Id](#cfn-eks-nodegroup-launchtemplatespecification-id): {{String}}
  [Name](#cfn-eks-nodegroup-launchtemplatespecification-name): {{String}}
  [Version](#cfn-eks-nodegroup-launchtemplatespecification-version): {{String}}
```

## Properties
<a name="aws-properties-eks-nodegroup-launchtemplatespecification-properties"></a>

`Id`  <a name="cfn-eks-nodegroup-launchtemplatespecification-id"></a>
The ID of the launch template.
You must specify either the launch template ID or the launch template name in the request, but not both. After node group creation, you cannot use a different ID.
*Required*: Conditional
*Type*: String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-eks-nodegroup-launchtemplatespecification-name"></a>
The name of the launch template.
You must specify either the launch template name or the launch template ID in the request, but not both. After node group creation, you cannot use a different name.
*Required*: Conditional
*Type*: String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Version`  <a name="cfn-eks-nodegroup-launchtemplatespecification-version"></a>
The version number of the launch template to use. If no version is specified, then the template's default version is used. You can use a different version for node group updates.
*Required*: No
*Type*: String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
