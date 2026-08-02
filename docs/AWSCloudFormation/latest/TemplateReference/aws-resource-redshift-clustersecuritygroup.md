---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-redshift-clustersecuritygroup.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Redshift::ClusterSecurityGroup
<a name="aws-resource-redshift-clustersecuritygroup"></a>

Specifies a new Amazon Redshift security group. You use security groups to control access to non-VPC clusters.

For information about managing security groups, go to [Amazon Redshift Cluster Security Groups](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-security-groups.html) in the *Amazon Redshift Cluster Management Guide*.

## Syntax
<a name="aws-resource-redshift-clustersecuritygroup-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-redshift-clustersecuritygroup-syntax.json"></a>

```
{
  "Type" : "AWS::Redshift::ClusterSecurityGroup",
  "Properties" : {
      "[Description](#cfn-redshift-clustersecuritygroup-description)" : {{String}},
      "[Tags](#cfn-redshift-clustersecuritygroup-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-redshift-clustersecuritygroup-syntax.yaml"></a>

```
Type: AWS::Redshift::ClusterSecurityGroup
Properties:
  [Description](#cfn-redshift-clustersecuritygroup-description): {{String}}
  [Tags](#cfn-redshift-clustersecuritygroup-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-redshift-clustersecuritygroup-properties"></a>

`Description`  <a name="cfn-redshift-clustersecuritygroup-description"></a>
A description for the security group.
*Required*: Yes
*Type*: String
*Maximum*: `2147483647`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-redshift-clustersecuritygroup-tags"></a>
Specifies an arbitrary set of tags (key–value pairs) to associate with this security group. Use tags to manage your resources.
*Required*: No
*Type*: Array of [Tag](aws-properties-redshift-clustersecuritygroup-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-redshift-clustersecuritygroup-return-values"></a>

### Ref
<a name="aws-resource-redshift-clustersecuritygroup-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the resource name. For example:

 `{ "Ref": "myClusterSecurityGroup" }`

For the Amazon Redshift cluster security group `myClusterSecurityGroup`, Ref returns the name of the cluster security group.

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-redshift-clustersecuritygroup-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

## Examples
<a name="aws-resource-redshift-clustersecuritygroup--examples"></a>

### Specify a Cluster Security Group
<a name="aws-resource-redshift-clustersecuritygroup--examples--Specify_a_Cluster_Security_Group"></a>

The following example describes an Amazon Redshift cluster security group that you can associate cluster security group ingress rules with.

#### JSON
<a name="aws-resource-redshift-clustersecuritygroup--examples--Specify_a_Cluster_Security_Group--json"></a>

```
"myClusterSecurityGroup": {
  "Type": "AWS::Redshift::ClusterSecurityGroup",
  "Properties": {
    "Description": "Security group to determine where connections to the Amazon Redshift cluster can come from",
    "Tags": [
      {
        "Key": "foo",
        "Value": "bar"
      }
    ]
  }
}
```

#### YAML
<a name="aws-resource-redshift-clustersecuritygroup--examples--Specify_a_Cluster_Security_Group--yaml"></a>

```
myClusterSecurityGroup:
  Type: "AWS::Redshift::ClusterSecurityGroup"
  Properties:
    Description: "Security group to determine where connections to the Amazon Redshift cluster can come from"
    Tags:
      - Key: foo
        Value: bar
```
