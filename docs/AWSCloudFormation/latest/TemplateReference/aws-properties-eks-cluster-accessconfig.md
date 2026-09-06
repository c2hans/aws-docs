---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-eks-cluster-accessconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EKS::Cluster AccessConfig
<a name="aws-properties-eks-cluster-accessconfig"></a>

The access configuration for the cluster.

## Syntax
<a name="aws-properties-eks-cluster-accessconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-eks-cluster-accessconfig-syntax.json"></a>

```
{
  "[AuthenticationMode](#cfn-eks-cluster-accessconfig-authenticationmode)" : {{String}},
  "[BootstrapClusterCreatorAdminPermissions](#cfn-eks-cluster-accessconfig-bootstrapclustercreatoradminpermissions)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-eks-cluster-accessconfig-syntax.yaml"></a>

```
  [AuthenticationMode](#cfn-eks-cluster-accessconfig-authenticationmode): {{String}}
  [BootstrapClusterCreatorAdminPermissions](#cfn-eks-cluster-accessconfig-bootstrapclustercreatoradminpermissions): {{Boolean}}
```

## Properties
<a name="aws-properties-eks-cluster-accessconfig-properties"></a>

`AuthenticationMode`  <a name="cfn-eks-cluster-accessconfig-authenticationmode"></a>
The desired authentication mode for the cluster. If you create a cluster by using the EKS API, AWS SDKs, or AWS CloudFormation, the default is `CONFIG_MAP`. If you create the cluster by using the AWS Management Console, the default value is `API_AND_CONFIG_MAP`.
*Required*: No
*Type*: String
*Allowed values*: `CONFIG_MAP | API_AND_CONFIG_MAP | API`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BootstrapClusterCreatorAdminPermissions`  <a name="cfn-eks-cluster-accessconfig-bootstrapclustercreatoradminpermissions"></a>
Specifies whether or not the cluster creator IAM principal was set as a cluster admin access entry during cluster creation time. The default value is `true`.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
