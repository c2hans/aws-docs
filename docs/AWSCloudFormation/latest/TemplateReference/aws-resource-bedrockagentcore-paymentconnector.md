---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-bedrockagentcore-paymentconnector.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::PaymentConnector
<a name="aws-resource-bedrockagentcore-paymentconnector"></a>

Creates a new payment connector for a payment manager. A payment connector integrates with a supported payment provider to enable payment processing capabilities.

## Syntax
<a name="aws-resource-bedrockagentcore-paymentconnector-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-bedrockagentcore-paymentconnector-syntax.json"></a>

```
{
  "Type" : "AWS::BedrockAgentCore::PaymentConnector",
  "Properties" : {
      "[ConnectorName](#cfn-bedrockagentcore-paymentconnector-connectorname)" : {{String}},
      "[ConnectorType](#cfn-bedrockagentcore-paymentconnector-connectortype)" : {{String}},
      "[CredentialProviderConfigurations](#cfn-bedrockagentcore-paymentconnector-credentialproviderconfigurations)" : {{[ CredentialsProviderConfiguration, ... ]}},
      "[Description](#cfn-bedrockagentcore-paymentconnector-description)" : {{String}},
      "[PaymentManagerId](#cfn-bedrockagentcore-paymentconnector-paymentmanagerid)" : {{String}},
      "[ProvisionMode](#cfn-bedrockagentcore-paymentconnector-provisionmode)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-bedrockagentcore-paymentconnector-syntax.yaml"></a>

```
Type: AWS::BedrockAgentCore::PaymentConnector
Properties:
  [ConnectorName](#cfn-bedrockagentcore-paymentconnector-connectorname): {{String}}
  [ConnectorType](#cfn-bedrockagentcore-paymentconnector-connectortype): {{String}}
  [CredentialProviderConfigurations](#cfn-bedrockagentcore-paymentconnector-credentialproviderconfigurations): {{
    - CredentialsProviderConfiguration}}
  [Description](#cfn-bedrockagentcore-paymentconnector-description): {{String}}
  [PaymentManagerId](#cfn-bedrockagentcore-paymentconnector-paymentmanagerid): {{String}}
  [ProvisionMode](#cfn-bedrockagentcore-paymentconnector-provisionmode): {{String}}
```

## Properties
<a name="aws-resource-bedrockagentcore-paymentconnector-properties"></a>

`ConnectorName`  <a name="cfn-bedrockagentcore-paymentconnector-connectorname"></a>
The name of the payment connector.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z][a-zA-Z0-9_]{0,47}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ConnectorType`  <a name="cfn-bedrockagentcore-paymentconnector-connectortype"></a>
The type of payment connector, which determines the payment provider integration.
*Required*: Yes
*Type*: String
*Allowed values*: `CoinbaseCDP | StripePrivy`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`CredentialProviderConfigurations`  <a name="cfn-bedrockagentcore-paymentconnector-credentialproviderconfigurations"></a>
The credential provider configurations for the payment connector. These configurations specify how the connector authenticates with the payment provider.
*Required*: No
*Type*: Array of [CredentialsProviderConfiguration](aws-properties-bedrockagentcore-paymentconnector-credentialsproviderconfiguration.md)
*Minimum*: `0`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-bedrockagentcore-paymentconnector-description"></a>
A description of the payment connector.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9\s]+$`
*Minimum*: `1`
*Maximum*: `4096`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PaymentManagerId`  <a name="cfn-bedrockagentcore-paymentconnector-paymentmanagerid"></a>
The unique identifier of the payment manager to create the connector for.
*Required*: Yes
*Type*: String
*Pattern*: `^([0-9a-z][-]?){1,100}-[0-9a-z]{10}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ProvisionMode`  <a name="cfn-bedrockagentcore-paymentconnector-provisionmode"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `MANUAL | QUICK_CREATE`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-bedrockagentcore-paymentconnector-return-values"></a>

### Ref
<a name="aws-resource-bedrockagentcore-paymentconnector-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-bedrockagentcore-paymentconnector-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-bedrockagentcore-paymentconnector-return-values-fn--getatt-fn--getatt"></a>

`AuthorizationUrl`  <a name="AuthorizationUrl-fn::getatt"></a>
Property description not available.

`ConnectorCreatedAt`  <a name="ConnectorCreatedAt-fn::getatt"></a>
The timestamp when the payment connector was created.

`ConnectorLastUpdatedAt`  <a name="ConnectorLastUpdatedAt-fn::getatt"></a>
The timestamp when the payment connector was last updated.

`ConnectorStatus`  <a name="ConnectorStatus-fn::getatt"></a>
The current status of the payment connector. Possible values include `CREATING`, `READY`, `UPDATING`, `DELETING`, `CREATE_FAILED`, `UPDATE_FAILED`, and `DELETE_FAILED`.

`PaymentConnectorArn`  <a name="PaymentConnectorArn-fn::getatt"></a>
The unique identifier of the payment connector.

`PaymentConnectorId`  <a name="PaymentConnectorId-fn::getatt"></a>
The unique identifier of the payment connector.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
