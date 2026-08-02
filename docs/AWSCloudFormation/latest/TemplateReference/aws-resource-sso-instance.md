---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-sso-instance.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SSO::Instance
<a name="aws-resource-sso-instance"></a>

Creates an instance of IAM Identity Center for a standalone AWS account that is not managed by AWS Organizations or a member AWS account in an organization. You can create only one instance per account and across all AWS Regions.

The CreateInstance request is rejected if the following apply:
+ The instance is created within the organization management account.
+ An instance already exists in the same account.

## Syntax
<a name="aws-resource-sso-instance-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-sso-instance-syntax.json"></a>

```
{
  "Type" : "AWS::SSO::Instance",
  "Properties" : {
      "[Name](#cfn-sso-instance-name)" : {{String}},
      "[Tags](#cfn-sso-instance-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-sso-instance-syntax.yaml"></a>

```
Type: AWS::SSO::Instance
Properties:
  [Name](#cfn-sso-instance-name): {{String}}
  [Tags](#cfn-sso-instance-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-sso-instance-properties"></a>

`Name`  <a name="cfn-sso-instance-name"></a>
The name of the Identity Center instance.
*Required*: No
*Type*: String
*Pattern*: `^[\w+=,.@-]+$`
*Minimum*: `1`
*Maximum*: `32`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-sso-instance-tags"></a>
Specifies tags to be attached to the instance of IAM Identity Center.
*Required*: No
*Type*: Array of [Tag](aws-properties-sso-instance-tag.md)
*Maximum*: `75`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-sso-instance-return-values"></a>

### Ref
<a name="aws-resource-sso-instance-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns a generated ID, combined by all fields with the delimiter `|`.

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-sso-instance-return-values-fn--getatt"></a>

####
<a name="aws-resource-sso-instance-return-values-fn--getatt-fn--getatt"></a>

`IdentityStoreId`  <a name="IdentityStoreId-fn::getatt"></a>
The identifier of the identity store that is connected to the Identity Center instance.

`InstanceArn`  <a name="InstanceArn-fn::getatt"></a>
The ARN of the Identity Center instance under which the operation will be executed. For more information about ARNs, see [Amazon Resource Names (ARNs) and AWS Service Namespaces](/general/latest/gr/aws-arns-and-namespaces.html) in the *AWS General Reference*.

`OwnerAccountId`  <a name="OwnerAccountId-fn::getatt"></a>
The AWS account ID number of the owner of the Identity Center instance.

`Status`  <a name="Status-fn::getatt"></a>
The current status of this Identity Center instance.

## Examples
<a name="aws-resource-sso-instance--examples"></a>

### Creating a new instance of IAM Identity Center
<a name="aws-resource-sso-instance--examples--Creating_a_new_instance_of"></a>

The following example creates an instance of IAM Identity Center for a specific AWS account.

#### JSON
<a name="aws-resource-sso-instance--examples--Creating_a_new_instance_of--json"></a>

```
"Instance": {
    "Type": "AWS::SSO::Instance",
    "Properties": {
        "Name": "InstanceExample",
        "Tags": {
            "InstanceTagKey1": "InstanceTagValue1"
        }
    }
}
```

#### YAML
<a name="aws-resource-sso-instance--examples--Creating_a_new_instance_of--yaml"></a>

```
 Instance:
    Type: AWS::SSO::Instance
    Properties:
        Name: InstanceExample
        Tags:
            InstanceTagKey1: 'InstanceTagValue1'
```
