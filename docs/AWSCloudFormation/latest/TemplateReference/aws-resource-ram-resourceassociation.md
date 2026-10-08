---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ram-resourceassociation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::RAM::ResourceAssociation
<a name="aws-resource-ram-resourceassociation"></a>

Associates a specified resource with a resource share.

## Syntax
<a name="aws-resource-ram-resourceassociation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ram-resourceassociation-syntax.json"></a>

```
{
  "Type" : "AWS::RAM::ResourceAssociation",
  "Properties" : {
      "[ResourceArn](#cfn-ram-resourceassociation-resourcearn)" : {{String}},
      "[ResourceShareArn](#cfn-ram-resourceassociation-resourcesharearn)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-ram-resourceassociation-syntax.yaml"></a>

```
Type: AWS::RAM::ResourceAssociation
Properties:
  [ResourceArn](#cfn-ram-resourceassociation-resourcearn): {{String}}
  [ResourceShareArn](#cfn-ram-resourceassociation-resourcesharearn): {{String}}
```

## Properties
<a name="aws-resource-ram-resourceassociation-properties"></a>

`ResourceArn`  <a name="cfn-ram-resourceassociation-resourcearn"></a>
Specifies the [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the resource to associate with the resource share.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ResourceShareArn`  <a name="cfn-ram-resourceassociation-resourcesharearn"></a>
Specifies the [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the resource share.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-ram-resourceassociation-return-values"></a>

### Ref
<a name="aws-resource-ram-resourceassociation-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the resource share ARN and resource ARN in the format `resource-share-arn|resource-arn`. For example: `arn:aws:ram:us-east-1:999999999999:resource-share/27d09b4b-5e12-41d1-a4f2-19ded10982e2|arn:aws:license-manager:us-east-1:999999999999:license-configuration:lic-36be0485f5ae379cc74cf8e9242ab143`.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-ram-resourceassociation-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-ram-resourceassociation-return-values-fn--getatt-fn--getatt"></a>

`AssociationType`  <a name="AssociationType-fn::getatt"></a>
The type of entity included in this association. This value is always `RESOURCE` for this resource type.

`CreationTime`  <a name="CreationTime-fn::getatt"></a>
The date and time when the association was created.

`External`  <a name="External-fn::getatt"></a>
Indicates whether the principal belongs to the same organization in AWS Organizations as the AWS account that owns the resource share.

`LastUpdatedTime`  <a name="LastUpdatedTime-fn::getatt"></a>
The date and time when the association was last updated.

`Status`  <a name="Status-fn::getatt"></a>
The current status of the association. Possible values include `ASSOCIATING`, `ASSOCIATED`, `FAILED`, `DISASSOCIATING`, `DISASSOCIATED`, `SUSPENDED`, `SUSPENDING`, and `RESTORING`.

## Examples
<a name="aws-resource-ram-resourceassociation--examples"></a>

### Associating a resource with a resource share
<a name="aws-resource-ram-resourceassociation--examples--Associating_a_resource_with_a_resource_share"></a>

The following example associates a resource with a resource share.

#### YAML
<a name="aws-resource-ram-resourceassociation--examples--Associating_a_resource_with_a_resource_share--yaml"></a>

```
AWSTemplateFormatVersion: '2010-09-09'
Resources:
  MyResourceAssociation:
    Type: AWS::RAM::ResourceAssociation
    Properties:
      ResourceShareArn: !Sub arn:aws:ram:${AWS::Region}:${AWS::AccountId}:resource-share/27d09b4b-5e12-41d1-a4f2-19ded10982e2
      ResourceArn: !Sub arn:aws:license-manager:${AWS::Region}:${AWS::AccountId}:license-configuration:lic-36be0485f5ae379cc74cf8e9242ab143
```

#### JSON
<a name="aws-resource-ram-resourceassociation--examples--Associating_a_resource_with_a_resource_share--json"></a>

```
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Resources": {
    "MyResourceAssociation": {
      "Type": "AWS::RAM::ResourceAssociation",
      "Properties": {
        "ResourceShareArn": {
          "Fn::Sub": "arn:aws:ram:${AWS::Region}:${AWS::AccountId}:resource-share/27d09b4b-5e12-41d1-a4f2-19ded10982e2"
        },
        "ResourceArn": {
          "Fn::Sub": "arn:aws:license-manager:${AWS::Region}:${AWS::AccountId}:license-configuration:lic-36be0485f5ae379cc74cf8e9242ab143"
        }
      }
    }
  }
}
```

## See also
<a name="aws-resource-ram-resourceassociation--seealso"></a>
+ [AssociateResourceShare](https://docs.aws.amazon.com/ram/latest/APIReference/API_AssociateResourceShare.html) in the *AWS Resource Access Manager API Reference*
+  [AWS Resource Access Manager User Guide](https://docs.aws.amazon.com/ram/latest/userguide)
