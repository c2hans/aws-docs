---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-greengrass-resourcedefinitionversion-secretsmanagersecretresourcedata.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Greengrass::ResourceDefinitionVersion SecretsManagerSecretResourceData
<a name="aws-properties-greengrass-resourcedefinitionversion-secretsmanagersecretresourcedata"></a>

<a name="aws-properties-greengrass-resourcedefinitionversion-secretsmanagersecretresourcedata-description"></a>Settings for a secret resource, which references a secret from AWS Secrets Manager. AWS IoT Greengrass stores a local, encrypted copy of the secret on the Greengrass core, where it can be securely accessed by connectors and Lambda functions. For more information, see [Deploy Secrets to the AWS IoT Greengrass Core](https://docs.aws.amazon.com/greengrass/v1/developerguide/secrets.html) in the * AWS IoT Greengrass Version 1 Developer Guide *.

<a name="aws-properties-greengrass-resourcedefinitionversion-secretsmanagersecretresourcedata-inheritance"></a> In an CloudFormation template, `SecretsManagerSecretResourceData` can be used in the [https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-resourcedatacontainer.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-greengrass-resourcedefinitionversion-resourcedatacontainer.html) property type.

## Syntax
<a name="aws-properties-greengrass-resourcedefinitionversion-secretsmanagersecretresourcedata-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-greengrass-resourcedefinitionversion-secretsmanagersecretresourcedata-syntax.json"></a>

```
{
  "[AdditionalStagingLabelsToDownload](#cfn-greengrass-resourcedefinitionversion-secretsmanagersecretresourcedata-additionalstaginglabelstodownload)" : {{[ String, ... ]}},
  "[ARN](#cfn-greengrass-resourcedefinitionversion-secretsmanagersecretresourcedata-arn)" : {{String}}
}
```

### YAML
<a name="aws-properties-greengrass-resourcedefinitionversion-secretsmanagersecretresourcedata-syntax.yaml"></a>

```
  [AdditionalStagingLabelsToDownload](#cfn-greengrass-resourcedefinitionversion-secretsmanagersecretresourcedata-additionalstaginglabelstodownload): {{
    - String}}
  [ARN](#cfn-greengrass-resourcedefinitionversion-secretsmanagersecretresourcedata-arn): {{String}}
```

## Properties
<a name="aws-properties-greengrass-resourcedefinitionversion-secretsmanagersecretresourcedata-properties"></a>

`AdditionalStagingLabelsToDownload`  <a name="cfn-greengrass-resourcedefinitionversion-secretsmanagersecretresourcedata-additionalstaginglabelstodownload"></a>
The staging labels whose values you want to make available on the core, in addition to `AWSCURRENT`.
*Required*: No
*Type*: Array of String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ARN`  <a name="cfn-greengrass-resourcedefinitionversion-secretsmanagersecretresourcedata-arn"></a>
The Amazon Resource Name (ARN) of the Secrets Manager secret to make available on the core. The value of the secret's latest version (represented by the `AWSCURRENT` staging label) is included by default.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also
<a name="aws-properties-greengrass-resourcedefinitionversion-secretsmanagersecretresourcedata--seealso"></a>
+ [SecretsManagerSecretResourceData](https://docs.aws.amazon.com/greengrass/v1/apireference/definitions-secretsmanagersecretresourcedata.html) in the * AWS IoT Greengrass Version 1 API Reference *
+  [AWS IoT Greengrass Version 1 Developer Guide](https://docs.aws.amazon.com/greengrass/v1/developerguide/)
