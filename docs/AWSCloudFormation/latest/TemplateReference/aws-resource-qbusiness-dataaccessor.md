---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-qbusiness-dataaccessor.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QBusiness::DataAccessor
<a name="aws-resource-qbusiness-dataaccessor"></a>

**Note**
Amazon Q Business will no longer be open to new customers starting on July 31, 2026. If you would like to use the service, please sign up prior to July 30. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

Creates a new data accessor for an ISV to access data from a Amazon Q Business application. The data accessor is an entity that represents the ISV's access to the Amazon Q Business application's data. It includes the IAM role ARN for the ISV, a friendly name, and a set of action configurations that define the specific actions the ISV is allowed to perform and any associated data filters. When the data accessor is created, an IAM Identity Center application is also created to manage the ISV's identity and authentication for accessing the Amazon Q Business application.

## Syntax
<a name="aws-resource-qbusiness-dataaccessor-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-qbusiness-dataaccessor-syntax.json"></a>

```
{
  "Type" : "AWS::QBusiness::DataAccessor",
  "Properties" : {
      "[ActionConfigurations](#cfn-qbusiness-dataaccessor-actionconfigurations)" : {{[ ActionConfiguration, ... ]}},
      "[ApplicationId](#cfn-qbusiness-dataaccessor-applicationid)" : {{String}},
      "[AuthenticationDetail](#cfn-qbusiness-dataaccessor-authenticationdetail)" : {{DataAccessorAuthenticationDetail}},
      "[DisplayName](#cfn-qbusiness-dataaccessor-displayname)" : {{String}},
      "[Principal](#cfn-qbusiness-dataaccessor-principal)" : {{String}},
      "[Tags](#cfn-qbusiness-dataaccessor-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-qbusiness-dataaccessor-syntax.yaml"></a>

```
Type: AWS::QBusiness::DataAccessor
Properties:
  [ActionConfigurations](#cfn-qbusiness-dataaccessor-actionconfigurations): {{
    - ActionConfiguration}}
  [ApplicationId](#cfn-qbusiness-dataaccessor-applicationid): {{String}}
  [AuthenticationDetail](#cfn-qbusiness-dataaccessor-authenticationdetail): {{
    DataAccessorAuthenticationDetail}}
  [DisplayName](#cfn-qbusiness-dataaccessor-displayname): {{String}}
  [Principal](#cfn-qbusiness-dataaccessor-principal): {{String}}
  [Tags](#cfn-qbusiness-dataaccessor-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-qbusiness-dataaccessor-properties"></a>

`ActionConfigurations`  <a name="cfn-qbusiness-dataaccessor-actionconfigurations"></a>
A list of action configurations specifying the allowed actions and any associated filters.
*Required*: Yes
*Type*: Array of [ActionConfiguration](aws-properties-qbusiness-dataaccessor-actionconfiguration.md)
*Minimum*: `1`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ApplicationId`  <a name="cfn-qbusiness-dataaccessor-applicationid"></a>
The unique identifier of the Amazon Q Business application.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9][a-zA-Z0-9-]{35}$`
*Minimum*: `36`
*Maximum*: `36`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`AuthenticationDetail`  <a name="cfn-qbusiness-dataaccessor-authenticationdetail"></a>
The authentication configuration details for the data accessor. This specifies how the ISV authenticates when accessing data through this data accessor.
*Required*: No
*Type*: [DataAccessorAuthenticationDetail](aws-properties-qbusiness-dataaccessor-dataaccessorauthenticationdetail.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DisplayName`  <a name="cfn-qbusiness-dataaccessor-displayname"></a>
The friendly name of the data accessor.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9][a-zA-Z0-9_-]*$`
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Principal`  <a name="cfn-qbusiness-dataaccessor-principal"></a>
The Amazon Resource Name (ARN) of the IAM role for the ISV associated with this data accessor.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws:iam::[0-9]{12}:role/[a-zA-Z0-9_/+=,.@-]+$`
*Minimum*: `1`
*Maximum*: `1284`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-qbusiness-dataaccessor-tags"></a>
The tags to associate with the data accessor.
*Required*: No
*Type*: Array of [Tag](aws-properties-qbusiness-dataaccessor-tag.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-qbusiness-dataaccessor-return-values"></a>

### Ref
<a name="aws-resource-qbusiness-dataaccessor-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the application and data accessor ID. For example:

 `{"Ref": "ApplicationId|DataAccessorId"}`

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-qbusiness-dataaccessor-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-qbusiness-dataaccessor-return-values-fn--getatt-fn--getatt"></a>

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The timestamp when the data accessor was created.

`DataAccessorArn`  <a name="DataAccessorArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the data accessor.

`DataAccessorId`  <a name="DataAccessorId-fn::getatt"></a>
The unique identifier of the data accessor.

`IdcApplicationArn`  <a name="IdcApplicationArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the associated IAM Identity Center application.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
The timestamp when the data accessor was last updated.
