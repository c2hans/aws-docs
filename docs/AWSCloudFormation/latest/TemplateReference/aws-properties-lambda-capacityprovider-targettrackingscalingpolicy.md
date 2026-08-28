---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-capacityprovider-targettrackingscalingpolicy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lambda::CapacityProvider TargetTrackingScalingPolicy
<a name="aws-properties-lambda-capacityprovider-targettrackingscalingpolicy"></a>

A scaling policy for the capacity provider that automatically adjusts capacity to maintain a target value for a specific metric.

## Syntax
<a name="aws-properties-lambda-capacityprovider-targettrackingscalingpolicy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lambda-capacityprovider-targettrackingscalingpolicy-syntax.json"></a>

```
{
  "[PredefinedMetricType](#cfn-lambda-capacityprovider-targettrackingscalingpolicy-predefinedmetrictype)" : {{String}},
  "[TargetValue](#cfn-lambda-capacityprovider-targettrackingscalingpolicy-targetvalue)" : {{Number}}
}
```

### YAML
<a name="aws-properties-lambda-capacityprovider-targettrackingscalingpolicy-syntax.yaml"></a>

```
  [PredefinedMetricType](#cfn-lambda-capacityprovider-targettrackingscalingpolicy-predefinedmetrictype): {{String}}
  [TargetValue](#cfn-lambda-capacityprovider-targettrackingscalingpolicy-targetvalue): {{Number}}
```

## Properties
<a name="aws-properties-lambda-capacityprovider-targettrackingscalingpolicy-properties"></a>

`PredefinedMetricType`  <a name="cfn-lambda-capacityprovider-targettrackingscalingpolicy-predefinedmetrictype"></a>
The predefined metric type to track for scaling decisions.
*Required*: Yes
*Type*: String
*Allowed values*: `LambdaCapacityProviderAverageCPUUtilization | LambdaCapacityProviderAverageGPUUtilization`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TargetValue`  <a name="cfn-lambda-capacityprovider-targettrackingscalingpolicy-targetvalue"></a>
The target value for the metric that the scaling policy attempts to maintain through scaling actions.
*Required*: Yes
*Type*: Number
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
