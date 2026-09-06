---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-securityhub-connectorv2-servicenowproviderconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SecurityHub::ConnectorV2 ServiceNowProviderConfiguration
<a name="aws-properties-securityhub-connectorv2-servicenowproviderconfiguration"></a>

The initial configuration settings required to establish an integration between Security Hub and ServiceNow ITSM.

## Syntax
<a name="aws-properties-securityhub-connectorv2-servicenowproviderconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-securityhub-connectorv2-servicenowproviderconfiguration-syntax.json"></a>

```
{
  "[InstanceName](#cfn-securityhub-connectorv2-servicenowproviderconfiguration-instancename)" : {{String}},
  "[SecretArn](#cfn-securityhub-connectorv2-servicenowproviderconfiguration-secretarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-securityhub-connectorv2-servicenowproviderconfiguration-syntax.yaml"></a>

```
  [InstanceName](#cfn-securityhub-connectorv2-servicenowproviderconfiguration-instancename): {{String}}
  [SecretArn](#cfn-securityhub-connectorv2-servicenowproviderconfiguration-secretarn): {{String}}
```

## Properties
<a name="aws-properties-securityhub-connectorv2-servicenowproviderconfiguration-properties"></a>

`InstanceName`  <a name="cfn-securityhub-connectorv2-servicenowproviderconfiguration-instancename"></a>
The instance name of ServiceNow ITSM.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SecretArn`  <a name="cfn-securityhub-connectorv2-servicenowproviderconfiguration-secretarn"></a>
The Amazon Resource Name (ARN) of the AWS Secrets Manager secret that contains the ServiceNow credentials.
*Required*: Yes
*Type*: String
*Pattern*: `.*\S.*`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
