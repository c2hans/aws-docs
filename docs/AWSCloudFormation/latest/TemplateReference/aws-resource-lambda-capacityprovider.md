---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-lambda-capacityprovider.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lambda::CapacityProvider
<a name="aws-resource-lambda-capacityprovider"></a>

Creates a capacity provider that manages compute resources for Lambda functions

## Syntax
<a name="aws-resource-lambda-capacityprovider-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-lambda-capacityprovider-syntax.json"></a>

```
{
  "Type" : "AWS::Lambda::CapacityProvider",
  "Properties" : {
      "[CapacityProviderName](#cfn-lambda-capacityprovider-capacityprovidername)" : {{String}},
      "[CapacityProviderScalingConfig](#cfn-lambda-capacityprovider-capacityproviderscalingconfig)" : {{CapacityProviderScalingConfig}},
      "[InstanceRequirements](#cfn-lambda-capacityprovider-instancerequirements)" : {{InstanceRequirements}},
      "[KmsKeyArn](#cfn-lambda-capacityprovider-kmskeyarn)" : {{String}},
      "[PermissionsConfig](#cfn-lambda-capacityprovider-permissionsconfig)" : {{CapacityProviderPermissionsConfig}},
      "[PropagateTags](#cfn-lambda-capacityprovider-propagatetags)" : {{PropagateTagsConfig}},
      "[Tags](#cfn-lambda-capacityprovider-tags)" : {{[ Tag, ... ]}},
      "[TelemetryConfig](#cfn-lambda-capacityprovider-telemetryconfig)" : {{CapacityProviderTelemetryConfig}},
      "[VpcConfig](#cfn-lambda-capacityprovider-vpcconfig)" : {{CapacityProviderVpcConfig}}
    }
}
```

### YAML
<a name="aws-resource-lambda-capacityprovider-syntax.yaml"></a>

```
Type: AWS::Lambda::CapacityProvider
Properties:
  [CapacityProviderName](#cfn-lambda-capacityprovider-capacityprovidername): {{String}}
  [CapacityProviderScalingConfig](#cfn-lambda-capacityprovider-capacityproviderscalingconfig): {{
    CapacityProviderScalingConfig}}
  [InstanceRequirements](#cfn-lambda-capacityprovider-instancerequirements): {{
    InstanceRequirements}}
  [KmsKeyArn](#cfn-lambda-capacityprovider-kmskeyarn): {{String}}
  [PermissionsConfig](#cfn-lambda-capacityprovider-permissionsconfig): {{
    CapacityProviderPermissionsConfig}}
  [PropagateTags](#cfn-lambda-capacityprovider-propagatetags): {{
    PropagateTagsConfig}}
  [Tags](#cfn-lambda-capacityprovider-tags): {{
    - Tag}}
  [TelemetryConfig](#cfn-lambda-capacityprovider-telemetryconfig): {{
    CapacityProviderTelemetryConfig}}
  [VpcConfig](#cfn-lambda-capacityprovider-vpcconfig): {{
    CapacityProviderVpcConfig}}
```

## Properties
<a name="aws-resource-lambda-capacityprovider-properties"></a>

`CapacityProviderName`  <a name="cfn-lambda-capacityprovider-capacityprovidername"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^(arn:aws[a-zA-Z-]*:lambda:(eusc-)?[a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1}:\d{12}:capacity-provider:[a-zA-Z0-9-_]+)|[a-zA-Z0-9-_]+$`
*Minimum*: `1`
*Maximum*: `140`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`CapacityProviderScalingConfig`  <a name="cfn-lambda-capacityprovider-capacityproviderscalingconfig"></a>
The scaling configuration for the capacity provider.
*Required*: No
*Type*: [CapacityProviderScalingConfig](aws-properties-lambda-capacityprovider-capacityproviderscalingconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InstanceRequirements`  <a name="cfn-lambda-capacityprovider-instancerequirements"></a>
The instance requirements for compute resources managed by the capacity provider.
*Required*: No
*Type*: [InstanceRequirements](aws-properties-lambda-capacityprovider-instancerequirements.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`KmsKeyArn`  <a name="cfn-lambda-capacityprovider-kmskeyarn"></a>
The ARN of the KMS key used to encrypt the capacity provider's resources.
*Required*: No
*Type*: String
*Pattern*: `^(arn:(aws[a-zA-Z-]*)?:[a-z0-9-.]+:.*)|()$`
*Minimum*: `0`
*Maximum*: `10000`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PermissionsConfig`  <a name="cfn-lambda-capacityprovider-permissionsconfig"></a>
The permissions configuration for the capacity provider.
*Required*: Yes
*Type*: [CapacityProviderPermissionsConfig](aws-properties-lambda-capacityprovider-capacityproviderpermissionsconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PropagateTags`  <a name="cfn-lambda-capacityprovider-propagatetags"></a>
Configuration for tag propagation to managed resources launched by the capacity provider.
*Required*: No
*Type*: [PropagateTagsConfig](aws-properties-lambda-capacityprovider-propagatetagsconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-lambda-capacityprovider-tags"></a>
A key-value pair that provides metadata for the capacity provider.
*Required*: No
*Type*: Array of [Tag](aws-properties-lambda-capacityprovider-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TelemetryConfig`  <a name="cfn-lambda-capacityprovider-telemetryconfig"></a>
The telemetry configuration for the capacity provider, including logging settings.
*Required*: No
*Type*: [CapacityProviderTelemetryConfig](aws-properties-lambda-capacityprovider-capacityprovidertelemetryconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VpcConfig`  <a name="cfn-lambda-capacityprovider-vpcconfig"></a>
The VPC configuration for the capacity provider.
*Required*: Yes
*Type*: [CapacityProviderVpcConfig](aws-properties-lambda-capacityprovider-capacityprovidervpcconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-lambda-capacityprovider-return-values"></a>

### Ref
<a name="aws-resource-lambda-capacityprovider-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-lambda-capacityprovider-return-values-fn--getatt"></a>

####
<a name="aws-resource-lambda-capacityprovider-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Property description not available.

`State`  <a name="State-fn::getatt"></a>
The current state of the capacity provider.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
