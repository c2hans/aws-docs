---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-kafkaconnect-workerconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::KafkaConnect::WorkerConfiguration
<a name="aws-resource-kafkaconnect-workerconfiguration"></a>

Creates a worker configuration using the specified properties.

## Syntax
<a name="aws-resource-kafkaconnect-workerconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-kafkaconnect-workerconfiguration-syntax.json"></a>

```
{
  "Type" : "AWS::KafkaConnect::WorkerConfiguration",
  "Properties" : {
      "[Description](#cfn-kafkaconnect-workerconfiguration-description)" : {{String}},
      "[Name](#cfn-kafkaconnect-workerconfiguration-name)" : {{String}},
      "[PropertiesFileContent](#cfn-kafkaconnect-workerconfiguration-propertiesfilecontent)" : {{String}},
      "[Tags](#cfn-kafkaconnect-workerconfiguration-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-kafkaconnect-workerconfiguration-syntax.yaml"></a>

```
Type: AWS::KafkaConnect::WorkerConfiguration
Properties:
  [Description](#cfn-kafkaconnect-workerconfiguration-description): {{String}}
  [Name](#cfn-kafkaconnect-workerconfiguration-name): {{String}}
  [PropertiesFileContent](#cfn-kafkaconnect-workerconfiguration-propertiesfilecontent): {{String}}
  [Tags](#cfn-kafkaconnect-workerconfiguration-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-kafkaconnect-workerconfiguration-properties"></a>

`Description`  <a name="cfn-kafkaconnect-workerconfiguration-description"></a>
The description of a worker configuration.
*Required*: No
*Type*: String
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-kafkaconnect-workerconfiguration-name"></a>
The name of the worker configuration.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PropertiesFileContent`  <a name="cfn-kafkaconnect-workerconfiguration-propertiesfilecontent"></a>
Base64 encoded contents of the connect-distributed.properties file.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-kafkaconnect-workerconfiguration-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-kafkaconnect-workerconfiguration-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-kafkaconnect-workerconfiguration-return-values"></a>

### Ref
<a name="aws-resource-kafkaconnect-workerconfiguration-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-kafkaconnect-workerconfiguration-return-values-fn--getatt"></a>

####
<a name="aws-resource-kafkaconnect-workerconfiguration-return-values-fn--getatt-fn--getatt"></a>

`Revision`  <a name="Revision-fn::getatt"></a>
The revision of the worker configuration.

`WorkerConfigurationArn`  <a name="WorkerConfigurationArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the worker configuration.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
