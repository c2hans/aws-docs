---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-mediaconnect-flowentitlement.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::FlowEntitlement
<a name="aws-resource-mediaconnect-flowentitlement"></a>

The `AWS::MediaConnect::FlowEntitlement` resource defines the permission that an AWS account grants to another AWS account to allow access to the content in a specific AWS Elemental MediaConnect flow. The content originator grants an entitlement to a specific AWS account (the subscriber). When an entitlement is granted, the subscriber can create a flow using the originator's flow as the source. Each flow can have up to 50 entitlements.

## Syntax
<a name="aws-resource-mediaconnect-flowentitlement-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-mediaconnect-flowentitlement-syntax.json"></a>

```
{
  "Type" : "AWS::MediaConnect::FlowEntitlement",
  "Properties" : {
      "[DataTransferSubscriberFeePercent](#cfn-mediaconnect-flowentitlement-datatransfersubscriberfeepercent)" : {{Integer}},
      "[Description](#cfn-mediaconnect-flowentitlement-description)" : {{String}},
      "[Encryption](#cfn-mediaconnect-flowentitlement-encryption)" : {{Encryption}},
      "[EntitlementStatus](#cfn-mediaconnect-flowentitlement-entitlementstatus)" : {{String}},
      "[FlowArn](#cfn-mediaconnect-flowentitlement-flowarn)" : {{String}},
      "[Name](#cfn-mediaconnect-flowentitlement-name)" : {{String}},
      "[Subscribers](#cfn-mediaconnect-flowentitlement-subscribers)" : {{[ String, ... ]}},
      "[Tags](#cfn-mediaconnect-flowentitlement-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-mediaconnect-flowentitlement-syntax.yaml"></a>

```
Type: AWS::MediaConnect::FlowEntitlement
Properties:
  [DataTransferSubscriberFeePercent](#cfn-mediaconnect-flowentitlement-datatransfersubscriberfeepercent): {{Integer}}
  [Description](#cfn-mediaconnect-flowentitlement-description): {{String}}
  [Encryption](#cfn-mediaconnect-flowentitlement-encryption): {{
    Encryption}}
  [EntitlementStatus](#cfn-mediaconnect-flowentitlement-entitlementstatus): {{String}}
  [FlowArn](#cfn-mediaconnect-flowentitlement-flowarn): {{String}}
  [Name](#cfn-mediaconnect-flowentitlement-name): {{String}}
  [Subscribers](#cfn-mediaconnect-flowentitlement-subscribers): {{
    - String}}
  [Tags](#cfn-mediaconnect-flowentitlement-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-mediaconnect-flowentitlement-properties"></a>

`DataTransferSubscriberFeePercent`  <a name="cfn-mediaconnect-flowentitlement-datatransfersubscriberfeepercent"></a>
The percentage of the entitlement data transfer fee that you want the subscriber to be responsible for.
*Required*: No
*Type*: Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Description`  <a name="cfn-mediaconnect-flowentitlement-description"></a>
A description of the entitlement. This description appears only on the MediaConnect console and is not visible outside of the current AWS account.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Encryption`  <a name="cfn-mediaconnect-flowentitlement-encryption"></a>
 Encryption information.
*Required*: No
*Type*: [Encryption](aws-properties-mediaconnect-flowentitlement-encryption.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EntitlementStatus`  <a name="cfn-mediaconnect-flowentitlement-entitlementstatus"></a>
An indication of whether the new entitlement should be enabled or disabled as soon as it is created. If you don't specify the entitlementStatus field in your request, MediaConnect sets it to ENABLED.
*Required*: No
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FlowArn`  <a name="cfn-mediaconnect-flowentitlement-flowarn"></a>
The Amazon Resource Name (ARN) of the flow.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-mediaconnect-flowentitlement-name"></a>
The name of the entitlement. This value must be unique within the current flow.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Subscribers`  <a name="cfn-mediaconnect-flowentitlement-subscribers"></a>
The AWS account IDs that you want to share your content with. The receiving accounts (subscribers) will be allowed to create their own flows using your content as the source.
*Required*: Yes
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-mediaconnect-flowentitlement-tags"></a>
An array of key-value pairs to apply to this resource.
For more information, see [Resource tags](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-resource-tags.html).
*Required*: No
*Type*: Array of [Tag](aws-properties-mediaconnect-flowentitlement-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-mediaconnect-flowentitlement-return-values"></a>

### Ref
<a name="aws-resource-mediaconnect-flowentitlement-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the entitlement ARN. For example:

 `{ "Ref": "arn:aws:mediaconnect:us-west-2:111122223333:entitlement:1-11aa22bb11aa22bb-3333cccc4444:AnyCompany_Entitlement" }`

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-mediaconnect-flowentitlement-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-mediaconnect-flowentitlement-return-values-fn--getatt-fn--getatt"></a>

`EntitlementArn`  <a name="EntitlementArn-fn::getatt"></a>
The entitlement ARN.
