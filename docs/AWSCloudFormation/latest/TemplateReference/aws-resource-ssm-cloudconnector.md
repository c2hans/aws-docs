---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ssm-cloudconnector.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SSM::CloudConnector
<a name="aws-resource-ssm-cloudconnector"></a>

The `AWS::SSM::CloudConnector` resource creates a cloud connector in AWS Systems Manager. With a cloud connector, you can manage resources in external cloud providers such as Microsoft Azure.

## Syntax
<a name="aws-resource-ssm-cloudconnector-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ssm-cloudconnector-syntax.json"></a>

```
{
  "Type" : "AWS::SSM::CloudConnector",
  "Properties" : {
      "[ConfigConnectorArn](#cfn-ssm-cloudconnector-configconnectorarn)" : {{String}},
      "[Configuration](#cfn-ssm-cloudconnector-configuration)" : {{CloudConnectorConfiguration}},
      "[Description](#cfn-ssm-cloudconnector-description)" : {{String}},
      "[DisplayName](#cfn-ssm-cloudconnector-displayname)" : {{String}},
      "[RoleArn](#cfn-ssm-cloudconnector-rolearn)" : {{String}},
      "[Tags](#cfn-ssm-cloudconnector-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-ssm-cloudconnector-syntax.yaml"></a>

```
Type: AWS::SSM::CloudConnector
Properties:
  [ConfigConnectorArn](#cfn-ssm-cloudconnector-configconnectorarn): {{String}}
  [Configuration](#cfn-ssm-cloudconnector-configuration): {{
    CloudConnectorConfiguration}}
  [Description](#cfn-ssm-cloudconnector-description): {{String}}
  [DisplayName](#cfn-ssm-cloudconnector-displayname): {{String}}
  [RoleArn](#cfn-ssm-cloudconnector-rolearn): {{String}}
  [Tags](#cfn-ssm-cloudconnector-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-ssm-cloudconnector-properties"></a>

`ConfigConnectorArn`  <a name="cfn-ssm-cloudconnector-configconnectorarn"></a>
The ARN of the AWS Config connector associated with the cloud connector.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws(-cn|-us-gov)?:config:[a-z0-9-]+:\d{12}:connector/.+$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Configuration`  <a name="cfn-ssm-cloudconnector-configuration"></a>
The configuration for the cloud connector.
*Required*: Yes
*Type*: [CloudConnectorConfiguration](aws-properties-ssm-cloudconnector-cloudconnectorconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-ssm-cloudconnector-description"></a>
The description of the cloud connector.
*Required*: No
*Type*: String
*Pattern*: `^[\p{L}\p{Z}\p{N}\p{P}\p{M}]*$`
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DisplayName`  <a name="cfn-ssm-cloudconnector-displayname"></a>
The display name of the cloud connector.
*Required*: Yes
*Type*: String
*Pattern*: `^[\p{L}\p{Z}\p{N}\p{P}\p{M}]*$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RoleArn`  <a name="cfn-ssm-cloudconnector-rolearn"></a>
The ARN of the IAM role used by the cloud connector to access resources in your AWS account.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws[a-z0-9-]*:iam::\d{12}:role/[\w-/.@+=,]{1,1017}$`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-ssm-cloudconnector-tags"></a>
The metadata that you assign to a resource. Use tags to categorize a resource in different ways, such as by purpose, owner, or environment.
*Required*: No
*Type*: Array of [Tag](aws-properties-ssm-cloudconnector-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-ssm-cloudconnector-return-values"></a>

### Ref
<a name="aws-resource-ssm-cloudconnector-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the ARN of the cloud connector. For example:

 `arn:aws:ssm:us-east-1:111122223333:cloud-connector/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-ssm-cloudconnector-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-ssm-cloudconnector-return-values-fn--getatt-fn--getatt"></a>

`CloudConnectorArn`  <a name="CloudConnectorArn-fn::getatt"></a>
The ARN of the cloud connector. For example: `arn:aws:ssm:us-east-1:111122223333:cloud-connector/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`.

`CloudConnectorId`  <a name="CloudConnectorId-fn::getatt"></a>
The unique identifier of the cloud connector. For example: `a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The timestamp when the cloud connector was created.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
The timestamp when the cloud connector was last updated.

## Examples
<a name="aws-resource-ssm-cloudconnector--examples"></a>

### Create a cloud connector to Microsoft Azure
<a name="aws-resource-ssm-cloudconnector--examples--Create_a_cloud_connector_to_Microsoft_Azure"></a>

The following example creates a cloud connector that connects AWS Systems Manager to a Microsoft Azure tenant, targeting a specific Azure subscription.

#### JSON
<a name="aws-resource-ssm-cloudconnector--examples--Create_a_cloud_connector_to_Microsoft_Azure--json"></a>

```
{
    "Type": "AWS::SSM::CloudConnector",
    "Properties": {
        "DisplayName": "MyAzureCloudConnector",
        "Description": "Cloud connector for managing Azure resources",
        "RoleArn": "arn:aws:iam::111122223333:role/CloudConnectorRole",
        "ConfigConnectorArn": "arn:aws:config:us-east-1:111122223333:connector/my-connector",
        "Configuration": {
            "AzureConfiguration": {
                "TenantId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
                "ApplicationId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
                "TenantDisplayName": "My Azure Tenant",
                "ApplicationDisplayName": "My Azure App",
                "Targets": {
                    "Subscriptions": [
                        {
                            "Id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE33333",
                            "DisplayName": "Production Subscription"
                        }
                    ]
                }
            }
        },
        "Tags": [
            {
                "Key": "Environment",
                "Value": "Production"
            }
        ]
    }
}
```

#### YAML
<a name="aws-resource-ssm-cloudconnector--examples--Create_a_cloud_connector_to_Microsoft_Azure--yaml"></a>

```
Type: AWS::SSM::CloudConnector
Properties:
  DisplayName: MyAzureCloudConnector
  Description: Cloud connector for managing Azure resources
  RoleArn: arn:aws:iam::111122223333:role/CloudConnectorRole
  ConfigConnectorArn: arn:aws:config:us-east-1:111122223333:connector/my-connector
  Configuration:
    AzureConfiguration:
      TenantId: a1b2c3d4-5678-90ab-cdef-EXAMPLE11111
      ApplicationId: a1b2c3d4-5678-90ab-cdef-EXAMPLE22222
      TenantDisplayName: My Azure Tenant
      ApplicationDisplayName: My Azure App
      Targets:
        Subscriptions:
          - Id: a1b2c3d4-5678-90ab-cdef-EXAMPLE33333
            DisplayName: Production Subscription
  Tags:
    - Key: Environment
      Value: Production
```
