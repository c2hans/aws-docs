---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-capacityprovider-capacityproviderscalingconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lambda::CapacityProvider CapacityProviderScalingConfig
<a name="aws-properties-lambda-capacityprovider-capacityproviderscalingconfig"></a>

Configuration that defines how the capacity provider scales compute instances based on demand and policies.

## Syntax
<a name="aws-properties-lambda-capacityprovider-capacityproviderscalingconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lambda-capacityprovider-capacityproviderscalingconfig-syntax.json"></a>

```
{
  "[MaxVCpuCount](#cfn-lambda-capacityprovider-capacityproviderscalingconfig-maxvcpucount)" : {{Integer}},
  "[ScalingMode](#cfn-lambda-capacityprovider-capacityproviderscalingconfig-scalingmode)" : {{String}},
  "[ScalingPolicies](#cfn-lambda-capacityprovider-capacityproviderscalingconfig-scalingpolicies)" : {{[ TargetTrackingScalingPolicy, ... ]}}
}
```

### YAML
<a name="aws-properties-lambda-capacityprovider-capacityproviderscalingconfig-syntax.yaml"></a>

```
  [MaxVCpuCount](#cfn-lambda-capacityprovider-capacityproviderscalingconfig-maxvcpucount): {{Integer}}
  [ScalingMode](#cfn-lambda-capacityprovider-capacityproviderscalingconfig-scalingmode): {{String}}
  [ScalingPolicies](#cfn-lambda-capacityprovider-capacityproviderscalingconfig-scalingpolicies): {{
    - TargetTrackingScalingPolicy}}
```

## Properties
<a name="aws-properties-lambda-capacityprovider-capacityproviderscalingconfig-properties"></a>

`MaxVCpuCount`  <a name="cfn-lambda-capacityprovider-capacityproviderscalingconfig-maxvcpucount"></a>
The maximum number of vCPUs that the capacity provider can provision across all compute instances.
*Required*: No
*Type*: Integer
*Minimum*: `2`
*Maximum*: `15000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ScalingMode`  <a name="cfn-lambda-capacityprovider-capacityproviderscalingconfig-scalingmode"></a>
The scaling mode that determines how the capacity provider responds to changes in demand.
*Required*: No
*Type*: String
*Allowed values*: `Auto | Manual`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ScalingPolicies`  <a name="cfn-lambda-capacityprovider-capacityproviderscalingconfig-scalingpolicies"></a>
A list of target tracking scaling policies for the capacity provider.
*Required*: No
*Type*: Array of [TargetTrackingScalingPolicy](aws-properties-lambda-capacityprovider-targettrackingscalingpolicy.md)
*Minimum*: `1`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
