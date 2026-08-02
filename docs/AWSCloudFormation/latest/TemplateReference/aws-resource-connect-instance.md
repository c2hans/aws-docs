---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-connect-instance.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::Instance
<a name="aws-resource-connect-instance"></a>

 *This is a preview release for Connect Customer. It is subject to change.*

Initiates an Connect Customer instance with all the supported channels enabled. It does not attach any storage, such as Amazon Simple Storage Service (Amazon S3) or Amazon Kinesis.

Connect Customer enforces a limit on the total number of instances that you can create or delete in 30 days. If you exceed this limit, you will get an error message indicating there has been an excessive number of attempts at creating or deleting instances. You must wait 30 days before you can restart creating and deleting instances in your account.

## Syntax
<a name="aws-resource-connect-instance-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-connect-instance-syntax.json"></a>

```
{
  "Type" : "AWS::Connect::Instance",
  "Properties" : {
      "[Attributes](#cfn-connect-instance-attributes)" : {{Attributes}},
      "[DirectoryId](#cfn-connect-instance-directoryid)" : {{String}},
      "[IdentityManagementType](#cfn-connect-instance-identitymanagementtype)" : {{String}},
      "[InstanceAlias](#cfn-connect-instance-instancealias)" : {{String}},
      "[Tags](#cfn-connect-instance-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-connect-instance-syntax.yaml"></a>

```
Type: AWS::Connect::Instance
Properties:
  [Attributes](#cfn-connect-instance-attributes): {{
    Attributes}}
  [DirectoryId](#cfn-connect-instance-directoryid): {{String}}
  [IdentityManagementType](#cfn-connect-instance-identitymanagementtype): {{String}}
  [InstanceAlias](#cfn-connect-instance-instancealias): {{String}}
  [Tags](#cfn-connect-instance-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-connect-instance-properties"></a>

`Attributes`  <a name="cfn-connect-instance-attributes"></a>
A toggle for an individual feature at the instance level.
*Required*: Yes
*Type*: [Attributes](aws-properties-connect-instance-attributes.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DirectoryId`  <a name="cfn-connect-instance-directoryid"></a>
The identifier for the directory.
*Required*: No
*Type*: String
*Pattern*: `^d-[0-9a-f]{10}$`
*Minimum*: `12`
*Maximum*: `12`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`IdentityManagementType`  <a name="cfn-connect-instance-identitymanagementtype"></a>
The identity management type.
*Required*: Yes
*Type*: String
*Allowed values*: `SAML | CONNECT_MANAGED | EXISTING_DIRECTORY`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`InstanceAlias`  <a name="cfn-connect-instance-instancealias"></a>
The alias of instance. `InstanceAlias` is only required when `IdentityManagementType` is `CONNECT_MANAGED` or `SAML`. `InstanceAlias` is not required when `IdentityManagementType` is `EXISTING_DIRECTORY`.
*Required*: No
*Type*: String
*Pattern*: `^(?!d-)([\da-zA-Z]+)([-]*[\da-zA-Z])*$`
*Minimum*: `1`
*Maximum*: `45`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-connect-instance-tags"></a>
An array of key-value pairs to apply to this resource.
*Required*: No
*Type*: Array of [Tag](aws-properties-connect-instance-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-connect-instance-return-values"></a>

### Ref
<a name="aws-resource-connect-instance-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the ID of the Connect Customer instance.

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-connect-instance-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-connect-instance-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the instance.

`CreatedTime`  <a name="CreatedTime-fn::getatt"></a>
When the instance was created.

`Id`  <a name="Id-fn::getatt"></a>
The identifier of the Connect Customer instance. You can find the instanceId in the ARN of the instance.

`InstanceStatus`  <a name="InstanceStatus-fn::getatt"></a>
The state of the instance.

`ServiceRole`  <a name="ServiceRole-fn::getatt"></a>
The service role of the instance.
