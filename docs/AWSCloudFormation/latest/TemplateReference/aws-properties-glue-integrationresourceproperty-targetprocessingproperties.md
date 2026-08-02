---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-glue-integrationresourceproperty-targetprocessingproperties.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Glue::IntegrationResourceProperty TargetProcessingProperties
<a name="aws-properties-glue-integrationresourceproperty-targetprocessingproperties"></a>

The structure used to define the resource properties associated with the integration target.

## Syntax
<a name="aws-properties-glue-integrationresourceproperty-targetprocessingproperties-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-glue-integrationresourceproperty-targetprocessingproperties-syntax.json"></a>

```
{
  "[ConnectionName](#cfn-glue-integrationresourceproperty-targetprocessingproperties-connectionname)" : {{String}},
  "[EventBusArn](#cfn-glue-integrationresourceproperty-targetprocessingproperties-eventbusarn)" : {{String}},
  "[KmsArn](#cfn-glue-integrationresourceproperty-targetprocessingproperties-kmsarn)" : {{String}},
  "[RoleArn](#cfn-glue-integrationresourceproperty-targetprocessingproperties-rolearn)" : {{String}}
}
```

### YAML
<a name="aws-properties-glue-integrationresourceproperty-targetprocessingproperties-syntax.yaml"></a>

```
  [ConnectionName](#cfn-glue-integrationresourceproperty-targetprocessingproperties-connectionname): {{String}}
  [EventBusArn](#cfn-glue-integrationresourceproperty-targetprocessingproperties-eventbusarn): {{String}}
  [KmsArn](#cfn-glue-integrationresourceproperty-targetprocessingproperties-kmsarn): {{String}}
  [RoleArn](#cfn-glue-integrationresourceproperty-targetprocessingproperties-rolearn): {{String}}
```

## Properties
<a name="aws-properties-glue-integrationresourceproperty-targetprocessingproperties-properties"></a>

`ConnectionName`  <a name="cfn-glue-integrationresourceproperty-targetprocessingproperties-connectionname"></a>
The AWS Glue network connection to configure the AWS Glue job running in the customer VPC.
*Required*: No
*Type*: String
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EventBusArn`  <a name="cfn-glue-integrationresourceproperty-targetprocessingproperties-eventbusarn"></a>
The ARN of an Eventbridge event bus to receive the integration status notification.
*Required*: No
*Type*: String
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KmsArn`  <a name="cfn-glue-integrationresourceproperty-targetprocessingproperties-kmsarn"></a>
The ARN of the KMS key used for encryption.
*Required*: No
*Type*: String
*Pattern*: `arn:aws:kms:.*:[0-9]+:.*`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RoleArn`  <a name="cfn-glue-integrationresourceproperty-targetprocessingproperties-rolearn"></a>
The IAM role to access the AWS Glue database.
*Required*: Yes
*Type*: String
*Pattern*: `arn:aws:iam:.*:[0-9]+:.*`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
