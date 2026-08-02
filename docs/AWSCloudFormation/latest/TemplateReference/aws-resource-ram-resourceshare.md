---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ram-resourceshare.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::RAM::ResourceShare
<a name="aws-resource-ram-resourceshare"></a>

Creates a resource share. You can provide a list of the Amazon Resource Names (ARNs) for the resources that you want to share, a list of principals you want to share the resources with, and the permissions to grant those principals.

**Note**
Sharing a resource makes it available for use by principals outside of the AWS account that created the resource. Sharing doesn't change any permissions or quotas that apply to the resource in the account that created it.

## Syntax
<a name="aws-resource-ram-resourceshare-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ram-resourceshare-syntax.json"></a>

```
{
  "Type" : "AWS::RAM::ResourceShare",
  "Properties" : {
      "[AllowExternalPrincipals](#cfn-ram-resourceshare-allowexternalprincipals)" : {{Boolean}},
      "[Name](#cfn-ram-resourceshare-name)" : {{String}},
      "[PermissionArns](#cfn-ram-resourceshare-permissionarns)" : {{[ String, ... ]}},
      "[Principals](#cfn-ram-resourceshare-principals)" : {{[ String, ... ]}},
      "[ResourceArns](#cfn-ram-resourceshare-resourcearns)" : {{[ String, ... ]}},
      "[ResourceShareConfiguration](#cfn-ram-resourceshare-resourceshareconfiguration)" : {{ResourceShareConfiguration}},
      "[Sources](#cfn-ram-resourceshare-sources)" : {{[ String, ... ]}},
      "[Tags](#cfn-ram-resourceshare-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-ram-resourceshare-syntax.yaml"></a>

```
Type: AWS::RAM::ResourceShare
Properties:
  [AllowExternalPrincipals](#cfn-ram-resourceshare-allowexternalprincipals): {{Boolean}}
  [Name](#cfn-ram-resourceshare-name): {{String}}
  [PermissionArns](#cfn-ram-resourceshare-permissionarns): {{
    - String}}
  [Principals](#cfn-ram-resourceshare-principals): {{
    - String}}
  [ResourceArns](#cfn-ram-resourceshare-resourcearns): {{
    - String}}
  [ResourceShareConfiguration](#cfn-ram-resourceshare-resourceshareconfiguration): {{
    ResourceShareConfiguration}}
  [Sources](#cfn-ram-resourceshare-sources): {{
    - String}}
  [Tags](#cfn-ram-resourceshare-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-ram-resourceshare-properties"></a>

`AllowExternalPrincipals`  <a name="cfn-ram-resourceshare-allowexternalprincipals"></a>
Specifies whether principals outside your organization in AWS Organizations can be associated with a resource share. A value of `true` lets you share with individual AWS accounts that are *not* in your organization. A value of `false` only has meaning if your account is a member of an AWS Organization. The default value is `true`.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-ram-resourceshare-name"></a>
Specifies the name of the resource share.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PermissionArns`  <a name="cfn-ram-resourceshare-permissionarns"></a>
Specifies the [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com//general/latest/gr/aws-arns-and-namespaces.html) of the AWS RAM permission to associate with the resource share. If you do not specify an ARN for the permission, AWS RAM automatically attaches the default version of the permission for each resource type. You can associate only one permission with each resource type included in the resource share.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Principals`  <a name="cfn-ram-resourceshare-principals"></a>
Specifies the principals to associate with the resource share. The possible values are:
+ An AWS account ID
+ An Amazon Resource Name (ARN) of an organization in AWS Organizations
+ An ARN of an organizational unit (OU) in AWS Organizations
+ An ARN of an IAM role
+ An ARN of an IAM user
Not all resource types can be shared with IAM roles and users. For more information, see the column **Can share with IAM roles and users** in the tables on [Shareable AWS resources](https://docs.aws.amazon.com/ram/latest/userguide/shareable.html) in the *AWS Resource Access Manager User Guide*.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceArns`  <a name="cfn-ram-resourceshare-resourcearns"></a>
Specifies a list of one or more ARNs of the resources to associate with the resource share.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceShareConfiguration`  <a name="cfn-ram-resourceshare-resourceshareconfiguration"></a>
The configuration of the resource share
*Required*: No
*Type*: [ResourceShareConfiguration](aws-properties-ram-resourceshare-resourceshareconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Sources`  <a name="cfn-ram-resourceshare-sources"></a>
Specifies from which source accounts the service principal has access to the resources in this resource share.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-ram-resourceshare-tags"></a>
Specifies one or more tags to attach to the resource share itself. It doesn't attach the tags to the resources associated with the resource share.
*Required*: No
*Type*: Array of [Tag](aws-properties-ram-resourceshare-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-ram-resourceshare-return-values"></a>

### Ref
<a name="aws-resource-ram-resourceshare-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns The ID of the resource share.

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-ram-resourceshare-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-ram-resourceshare-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the resource share.

`CreationTime`  <a name="CreationTime-fn::getatt"></a>
The date and time when the resource share was created.

`FeatureSet`  <a name="FeatureSet-fn::getatt"></a>
Indicates what features are available for this resource share. This parameter can have one of the following values:
+ **STANDARD** – A resource share that supports all functionality. These resource shares are visible to all principals you share the resource share with. You can modify these resource shares in AWS RAM using the console or APIs. This resource share might have been created by AWS RAM, or it might have been **CREATED\_FROM\_POLICY** and then promoted.
+ **CREATED\_FROM\_POLICY** – The customer manually shared a resource by attaching a resource-based policy. That policy did not match any existing managed permissions, so AWS RAM created this customer managed permission automatically on the customer's behalf based on the attached policy document. This type of resource share is visible only to the AWS account that created it. You can't modify it in AWS RAM unless you promote it. For more information, see PromoteResourceShareCreatedFromPolicy.
+ **PROMOTING\_TO\_STANDARD** – This resource share was originally `CREATED_FROM_POLICY`, but the customer ran the PromoteResourceShareCreatedFromPolicy and that operation is still in progress. This value changes to `STANDARD` when complete.

`LastUpdatedTime`  <a name="LastUpdatedTime-fn::getatt"></a>
The date and time when the resource share was last updated.

`OwningAccountId`  <a name="OwningAccountId-fn::getatt"></a>
The ID of the AWS account that owns the resource share.

`Status`  <a name="Status-fn::getatt"></a>
The current status of the resource share.

## Examples
<a name="aws-resource-ram-resourceshare--examples"></a>

### Creating a resource share
<a name="aws-resource-ram-resourceshare--examples--Creating_a_resource_share"></a>

The following example demonstrates how to create a resource share.

#### YAML
<a name="aws-resource-ram-resourceshare--examples--Creating_a_resource_share--yaml"></a>

```
AWSTemplateFormatVersion: 2010-09-09
Resources:
  myresourceshare:
    Type: "AWS::RAM::ResourceShare"
    Properties:
      Name: "My Resource Share"
      ResourceArns:
        - "arn:aws:ec2:us-east-1:123456789012:resource-type/12345678-1234-1234-1234-12345678"
      Principals:
        - "210987654321"
      Tags:
        - Key: "Key1"
          Value: "Value1"
        - Key: "Key2"
          Value: "Value2"
```

#### JSON
<a name="aws-resource-ram-resourceshare--examples--Creating_a_resource_share--json"></a>

```
{
  "AWSTemplateFormatVersion": "2010-09-09T00:00:00.000Z",
  "Resources": {
    "myresourceshare": {
      "Type": "AWS::RAM::ResourceShare",
      "Properties": {
        "Name": "My Resource Share",
        "ResourceArns": [
          "arn:aws:ec2:us-east-1:123456789012:resource-type/12345678-1234-1234-1234-12345678"
        ],
        "Principals": [
          "210987654321"
        ],
        "Tags": [
          {
            "Key": "Key1",
            "Value": "Value1"
          },
          {
            "Key": "Key2",
            "Value": "Value2"
          }
        ]
      }
    }
  }
}
```

## See also
<a name="aws-resource-ram-resourceshare--seealso"></a>
+ [CreateResourceShare](https://docs.aws.amazon.com/ram/latest/APIReference/API_CreateResourceShare.html) in the *AWS Resource Access Manager API Reference*
+  [AWS Resource Access Manager User Guide](https://docs.aws.amazon.com/ram/latest/userguide)
