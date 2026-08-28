---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-glue-integration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Glue::Integration
<a name="aws-resource-glue-integration"></a>

The `AWS::Glue::Integration` resource specifies an AWS Glue zero-ETL integration from a data source to a target. For more information, see [ zero-ETL integration supported by AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/zero-etl-using.html) and [ integration structure](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-integrations.html) in the AWS Glue developer guide.

## Syntax
<a name="aws-resource-glue-integration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-glue-integration-syntax.json"></a>

```
{
  "Type" : "AWS::Glue::Integration",
  "Properties" : {
      "[AdditionalEncryptionContext](#cfn-glue-integration-additionalencryptioncontext)" : {{{{{Key}}: {{Value}}, ...}}},
      "[DataFilter](#cfn-glue-integration-datafilter)" : {{String}},
      "[Description](#cfn-glue-integration-description)" : {{String}},
      "[IntegrationConfig](#cfn-glue-integration-integrationconfig)" : {{IntegrationConfig}},
      "[IntegrationName](#cfn-glue-integration-integrationname)" : {{String}},
      "[KmsKeyId](#cfn-glue-integration-kmskeyid)" : {{String}},
      "[SourceArn](#cfn-glue-integration-sourcearn)" : {{String}},
      "[Tags](#cfn-glue-integration-tags)" : {{[ Tag, ... ]}},
      "[TargetArn](#cfn-glue-integration-targetarn)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-glue-integration-syntax.yaml"></a>

```
Type: AWS::Glue::Integration
Properties:
  [AdditionalEncryptionContext](#cfn-glue-integration-additionalencryptioncontext): {{
    {{Key}}: {{Value}}}}
  [DataFilter](#cfn-glue-integration-datafilter): {{String}}
  [Description](#cfn-glue-integration-description): {{String}}
  [IntegrationConfig](#cfn-glue-integration-integrationconfig): {{
    IntegrationConfig}}
  [IntegrationName](#cfn-glue-integration-integrationname): {{String}}
  [KmsKeyId](#cfn-glue-integration-kmskeyid): {{String}}
  [SourceArn](#cfn-glue-integration-sourcearn): {{String}}
  [Tags](#cfn-glue-integration-tags): {{
    - Tag}}
  [TargetArn](#cfn-glue-integration-targetarn): {{String}}
```

## Properties
<a name="aws-resource-glue-integration-properties"></a>

`AdditionalEncryptionContext`  <a name="cfn-glue-integration-additionalencryptioncontext"></a>
An optional set of non-secret key–value pairs that contains additional contextual information for encryption. This can only be provided if `KMSKeyId` is provided.
*Required*: No
*Type*: Object of String
*Pattern*: `^[\s\S]*$`
*Minimum*: `0`
*Maximum*: `131072`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DataFilter`  <a name="cfn-glue-integration-datafilter"></a>
Selects source tables for the integration using Maxwell filter syntax.
*Required*: No
*Type*: String
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-glue-integration-description"></a>
A description for the integration.
*Required*: No
*Type*: String
*Maximum*: `1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IntegrationConfig`  <a name="cfn-glue-integration-integrationconfig"></a>
The structure used to define properties associated with the zero-ETL integration. For more information, see [IntegrationConfig structure.](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-integrations.html#aws-glue-api-integrations-IntegrationConfig)
*Required*: No
*Type*: [IntegrationConfig](aws-properties-glue-integration-integrationconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`IntegrationName`  <a name="cfn-glue-integration-integrationname"></a>
A unique name for the integration.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`KmsKeyId`  <a name="cfn-glue-integration-kmskeyid"></a>
The ARN of a KMS key used for encrypting the channel.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SourceArn`  <a name="cfn-glue-integration-sourcearn"></a>
The ARN for the source of the integration.
*Required*: Yes
*Type*: String
*Pattern*: `arn:aws:.*:.*:[0-9]+:.*`
*Maximum*: `512`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-glue-integration-tags"></a>
Metadata assigned to the resource consisting of a list of key-value pairs.
*Required*: No
*Type*: Array of [Tag](aws-properties-glue-integration-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TargetArn`  <a name="cfn-glue-integration-targetarn"></a>
The ARN for the target of the integration.
*Required*: Yes
*Type*: String
*Pattern*: `arn:aws:.*:.*:[0-9]+:.*`
*Maximum*: `512`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-glue-integration-return-values"></a>

### Ref
<a name="aws-resource-glue-integration-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-glue-integration-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-glue-integration-return-values-fn--getatt-fn--getatt"></a>

`CreateTime`  <a name="CreateTime-fn::getatt"></a>
The time when the integration was created, in UTC.

`IntegrationArn`  <a name="IntegrationArn-fn::getatt"></a>
The Amazon Resource Name (ARN) for the created integration.

`Status`  <a name="Status-fn::getatt"></a>
The status of the integration being created.
The possible statuses are:
+ CREATING: The integration is being created.
+ ACTIVE: The integration creation succeeds.
+ MODIFYING: The integration is being modified.
+ FAILED: The integration creation fails.
+ DELETING: The integration is deleted.
+ SYNCING: The integration is synchronizing.
+ NEEDS\_ATTENTION: The integration needs attention, such as synchronization.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
