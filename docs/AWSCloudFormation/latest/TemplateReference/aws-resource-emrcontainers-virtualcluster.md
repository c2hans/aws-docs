---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-emrcontainers-virtualcluster.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMRContainers::VirtualCluster
<a name="aws-resource-emrcontainers-virtualcluster"></a>

The `AWS::EMRContainers::VirtualCluster` resource specifies a virtual cluster. A virtual cluster is a managed entity on Amazon EMR on EKS. You can create, describe, list, and delete virtual clusters. They do not consume any additional resources in your system. A single virtual cluster maps to a single Kubernetes namespace. Given this relationship, you can model virtual clusters the same way you model Kubernetes namespaces to meet your requirements.

## Syntax
<a name="aws-resource-emrcontainers-virtualcluster-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-emrcontainers-virtualcluster-syntax.json"></a>

```
{
  "Type" : "AWS::EMRContainers::VirtualCluster",
  "Properties" : {
      "[ContainerProvider](#cfn-emrcontainers-virtualcluster-containerprovider)" : {{ContainerProvider}},
      "[Name](#cfn-emrcontainers-virtualcluster-name)" : {{String}},
      "[SecurityConfigurationId](#cfn-emrcontainers-virtualcluster-securityconfigurationid)" : {{String}},
      "[SessionEnabled](#cfn-emrcontainers-virtualcluster-sessionenabled)" : {{Boolean}},
      "[Tags](#cfn-emrcontainers-virtualcluster-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-emrcontainers-virtualcluster-syntax.yaml"></a>

```
Type: AWS::EMRContainers::VirtualCluster
Properties:
  [ContainerProvider](#cfn-emrcontainers-virtualcluster-containerprovider): {{
    ContainerProvider}}
  [Name](#cfn-emrcontainers-virtualcluster-name): {{String}}
  [SecurityConfigurationId](#cfn-emrcontainers-virtualcluster-securityconfigurationid): {{String}}
  [SessionEnabled](#cfn-emrcontainers-virtualcluster-sessionenabled): {{Boolean}}
  [Tags](#cfn-emrcontainers-virtualcluster-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-emrcontainers-virtualcluster-properties"></a>

`ContainerProvider`  <a name="cfn-emrcontainers-virtualcluster-containerprovider"></a>
The container provider of the virtual cluster.
*Required*: Yes
*Type*: [ContainerProvider](aws-properties-emrcontainers-virtualcluster-containerprovider.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-emrcontainers-virtualcluster-name"></a>
The name of the virtual cluster.
*Required*: Yes
*Type*: String
*Pattern*: `[\.\-_/#A-Za-z0-9]+`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SecurityConfigurationId`  <a name="cfn-emrcontainers-virtualcluster-securityconfigurationid"></a>
The ID of the security configuration.
*Required*: No
*Type*: String
*Pattern*: `[0-9a-z]+`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SessionEnabled`  <a name="cfn-emrcontainers-virtualcluster-sessionenabled"></a>
Specifies whether the virtual cluster has session support enabled.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-emrcontainers-virtualcluster-tags"></a>
An array of key-value pairs to apply to this resource.
For more information, see [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html).
*Required*: No
*Type*: Array of [Tag](aws-properties-emrcontainers-virtualcluster-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-emrcontainers-virtualcluster-return-values"></a>

### Ref
<a name="aws-resource-emrcontainers-virtualcluster-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the ID of the virtual cluster.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-emrcontainers-virtualcluster-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-emrcontainers-virtualcluster-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the project, such as `arn:aws:emr-containers:us-east-1:123456789012:/virtualclusters/ab4rp1abcs8xz47n3x0example`.

`Id`  <a name="Id-fn::getatt"></a>
The ID of the virtual cluster, such as `ab4rp1abcs8xz47n3x0example`.

## Examples
<a name="aws-resource-emrcontainers-virtualcluster--examples"></a>

### Specifies a virtual cluster
<a name="aws-resource-emrcontainers-virtualcluster--examples--Specifies_a_virtual_cluster"></a>

#### JSON
<a name="aws-resource-emrcontainers-virtualcluster--examples--Specifies_a_virtual_cluster--json"></a>

```
{
   "Resources": {
      "TestVirtualCluster": {
         "Type": "AWS::EMRContainers::VirtualCluster",
         "Properties": {
            "Name": "VirtualClusterName",
            "ContainerProvider": {
               "Type": "EKS",
               "Id": "EKSClusterName",
               "Info": {
                  "EksInfo": {
                     "Namespace": "EKSNamespace"
                  }
               }
            },
            "Tags": [
               {
                  "Key": "Key1",
                  "Value": "Value1"
               }
            ]
         }
      }
   },
   "Outputs": {
      "PrimaryId": {
         "Value": null
      }
   }
}
```

#### YAML
<a name="aws-resource-emrcontainers-virtualcluster--examples--Specifies_a_virtual_cluster--yaml"></a>

```
Resources:
  TestVirtualCluster:
    Type: 'AWS::EMRContainers::VirtualCluster'
    Properties:
      Name: 'VirtualClusterName'
      ContainerProvider:
        Type: 'EKS'
        Id: 'EKSClusterName'
        Info:
          EksInfo:
            Namespace: 'EKSNamespace'
      Tags:
        - Key: Key1
          Value: Value1
Outputs:
  PrimaryId:
    Value: !Ref TestVirtualCluster
```
