---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-redshift-integration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Redshift::Integration
<a name="aws-resource-redshift-integration"></a>

Describes a zero-ETL or S3 integration.

## Syntax
<a name="aws-resource-redshift-integration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-redshift-integration-syntax.json"></a>

```
{
  "Type" : "AWS::Redshift::Integration",
  "Properties" : {
      "[AdditionalEncryptionContext](#cfn-redshift-integration-additionalencryptioncontext)" : {{{{{Key}}: {{Value}}, ...}}},
      "[IntegrationName](#cfn-redshift-integration-integrationname)" : {{String}},
      "[KMSKeyId](#cfn-redshift-integration-kmskeyid)" : {{String}},
      "[SourceArn](#cfn-redshift-integration-sourcearn)" : {{String}},
      "[Tags](#cfn-redshift-integration-tags)" : {{[ Tag, ... ]}},
      "[TargetArn](#cfn-redshift-integration-targetarn)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-redshift-integration-syntax.yaml"></a>

```
Type: AWS::Redshift::Integration
Properties:
  [AdditionalEncryptionContext](#cfn-redshift-integration-additionalencryptioncontext): {{
    {{Key}}: {{Value}}}}
  [IntegrationName](#cfn-redshift-integration-integrationname): {{String}}
  [KMSKeyId](#cfn-redshift-integration-kmskeyid): {{String}}
  [SourceArn](#cfn-redshift-integration-sourcearn): {{String}}
  [Tags](#cfn-redshift-integration-tags): {{
    - Tag}}
  [TargetArn](#cfn-redshift-integration-targetarn): {{String}}
```

## Properties
<a name="aws-resource-redshift-integration-properties"></a>

`AdditionalEncryptionContext`  <a name="cfn-redshift-integration-additionalencryptioncontext"></a>
The encryption context for the integration. For more information, see [Encryption context](https://docs.aws.amazon.com/) in the *AWS Key Management Service Developer Guide*.
*Required*: No
*Type*: Object of String
*Pattern*: `^[\s\S]*$`
*Minimum*: `0`
*Maximum*: `131072`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`IntegrationName`  <a name="cfn-redshift-integration-integrationname"></a>
The name of the integration.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KMSKeyId`  <a name="cfn-redshift-integration-kmskeyid"></a>
The AWS Key Management Service (AWS KMS) key identifier for the key used to encrypt the integration.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SourceArn`  <a name="cfn-redshift-integration-sourcearn"></a>
The Amazon Resource Name (ARN) of the database used as the source for replication.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-redshift-integration-tags"></a>
The list of tags associated with the integration.
*Required*: No
*Type*: Array of [Tag](aws-properties-redshift-integration-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TargetArn`  <a name="cfn-redshift-integration-targetarn"></a>
The Amazon Resource Name (ARN) of the Amazon Redshift data warehouse to use as the target for replication.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-redshift-integration-return-values"></a>

### Ref
<a name="aws-resource-redshift-integration-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-redshift-integration-return-values-fn--getatt"></a>

####
<a name="aws-resource-redshift-integration-return-values-fn--getatt-fn--getatt"></a>

`CreateTime`  <a name="CreateTime-fn::getatt"></a>
The time (UTC) when the integration was created.

`IntegrationArn`  <a name="IntegrationArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the integration.
