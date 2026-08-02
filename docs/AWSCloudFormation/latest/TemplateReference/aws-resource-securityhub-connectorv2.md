---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-securityhub-connectorv2.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SecurityHub::ConnectorV2
<a name="aws-resource-securityhub-connectorv2"></a>

Grants permission to create a connectorV2 based on input parameters.

## Syntax
<a name="aws-resource-securityhub-connectorv2-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-securityhub-connectorv2-syntax.json"></a>

```
{
  "Type" : "AWS::SecurityHub::ConnectorV2",
  "Properties" : {
      "[Description](#cfn-securityhub-connectorv2-description)" : {{String}},
      "[KmsKeyArn](#cfn-securityhub-connectorv2-kmskeyarn)" : {{String}},
      "[Name](#cfn-securityhub-connectorv2-name)" : {{String}},
      "[Provider](#cfn-securityhub-connectorv2-provider)" : {{Provider}},
      "[Tags](#cfn-securityhub-connectorv2-tags)" : {{{{{Key}}: {{Value}}, ...}}}
    }
}
```

### YAML
<a name="aws-resource-securityhub-connectorv2-syntax.yaml"></a>

```
Type: AWS::SecurityHub::ConnectorV2
Properties:
  [Description](#cfn-securityhub-connectorv2-description): {{String}}
  [KmsKeyArn](#cfn-securityhub-connectorv2-kmskeyarn): {{String}}
  [Name](#cfn-securityhub-connectorv2-name): {{String}}
  [Provider](#cfn-securityhub-connectorv2-provider): {{
    Provider}}
  [Tags](#cfn-securityhub-connectorv2-tags): {{
    {{Key}}: {{Value}}}}
```

## Properties
<a name="aws-resource-securityhub-connectorv2-properties"></a>

`Description`  <a name="cfn-securityhub-connectorv2-description"></a>
The description of the connectorV2.
*Required*: No
*Type*: String
*Pattern*: `.*\S.*`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KmsKeyArn`  <a name="cfn-securityhub-connectorv2-kmskeyarn"></a>
The Amazon Resource Name (ARN) of KMS key used to encrypt secrets for the connectorV2.
*Required*: No
*Type*: String
*Pattern*: `.*\S.*`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-securityhub-connectorv2-name"></a>
The unique name of the connectorV2.
*Required*: Yes
*Type*: String
*Pattern*: `.*\S.*`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Provider`  <a name="cfn-securityhub-connectorv2-provider"></a>
The third-party provider detail for a service configuration.
*Required*: Yes
*Type*: [Provider](aws-properties-securityhub-connectorv2-provider.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-securityhub-connectorv2-tags"></a>
The tags to add to the connectorV2 when you create.
*Required*: No
*Type*: Object of String
*Pattern*: `^(?!aws:)[a-zA-Z+-=._:/]{1,128}$`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-securityhub-connectorv2-return-values"></a>

### Ref
<a name="aws-resource-securityhub-connectorv2-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the `ConnectorV2Arn` for the `ConnectorV2Arn` resource created: `arn:aws:securityhub:region:123456789012:connectorv2/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`.

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-securityhub-connectorv2-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-securityhub-connectorv2-return-values-fn--getatt-fn--getatt"></a>

`ConnectorArn`  <a name="ConnectorArn-fn::getatt"></a>
The ARN of the V2 connector.

`ConnectorId`  <a name="ConnectorId-fn::getatt"></a>
The unique identifier of the V2 connector.

`ConnectorStatus`  <a name="ConnectorStatus-fn::getatt"></a>
The status of the V2 connector.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The timestamp when the V2 connector was created.

`EnablementStatus`  <a name="EnablementStatus-fn::getatt"></a>
Property description not available.

`EnablementStatusReason`  <a name="EnablementStatusReason-fn::getatt"></a>
Provides additional context for the value of `Compliance.Status`.

`Issues`  <a name="Issues-fn::getatt"></a>
Property description not available.

`LastCheckedAt`  <a name="LastCheckedAt-fn::getatt"></a>
The most recent timestamp when the V2 connector was checked on health status.

`LastUpdatedAt`  <a name="LastUpdatedAt-fn::getatt"></a>
The most recent timestamp when the V2 connector was updated.

`Message`  <a name="Message-fn::getatt"></a>
The message of the V2 connector when connector status is FAILED\_TO\_CONNECT.
