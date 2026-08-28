---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudfront-continuousdeploymentpolicy-continuousdeploymentpolicyconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFront::ContinuousDeploymentPolicy ContinuousDeploymentPolicyConfig
<a name="aws-properties-cloudfront-continuousdeploymentpolicy-continuousdeploymentpolicyconfig"></a>

Contains the configuration for a continuous deployment policy.

## Syntax
<a name="aws-properties-cloudfront-continuousdeploymentpolicy-continuousdeploymentpolicyconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudfront-continuousdeploymentpolicy-continuousdeploymentpolicyconfig-syntax.json"></a>

```
{
  "[Enabled](#cfn-cloudfront-continuousdeploymentpolicy-continuousdeploymentpolicyconfig-enabled)" : {{Boolean}},
  "[SingleHeaderPolicyConfig](#cfn-cloudfront-continuousdeploymentpolicy-continuousdeploymentpolicyconfig-singleheaderpolicyconfig)" : {{SingleHeaderPolicyConfig}},
  "[SingleWeightPolicyConfig](#cfn-cloudfront-continuousdeploymentpolicy-continuousdeploymentpolicyconfig-singleweightpolicyconfig)" : {{SingleWeightPolicyConfig}},
  "[StagingDistributionDnsNames](#cfn-cloudfront-continuousdeploymentpolicy-continuousdeploymentpolicyconfig-stagingdistributiondnsnames)" : {{[ String, ... ]}},
  "[TrafficConfig](#cfn-cloudfront-continuousdeploymentpolicy-continuousdeploymentpolicyconfig-trafficconfig)" : {{TrafficConfig}},
  "[Type](#cfn-cloudfront-continuousdeploymentpolicy-continuousdeploymentpolicyconfig-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-cloudfront-continuousdeploymentpolicy-continuousdeploymentpolicyconfig-syntax.yaml"></a>

```
  [Enabled](#cfn-cloudfront-continuousdeploymentpolicy-continuousdeploymentpolicyconfig-enabled): {{Boolean}}
  [SingleHeaderPolicyConfig](#cfn-cloudfront-continuousdeploymentpolicy-continuousdeploymentpolicyconfig-singleheaderpolicyconfig): {{
    SingleHeaderPolicyConfig}}
  [SingleWeightPolicyConfig](#cfn-cloudfront-continuousdeploymentpolicy-continuousdeploymentpolicyconfig-singleweightpolicyconfig): {{
    SingleWeightPolicyConfig}}
  [StagingDistributionDnsNames](#cfn-cloudfront-continuousdeploymentpolicy-continuousdeploymentpolicyconfig-stagingdistributiondnsnames): {{
    - String}}
  [TrafficConfig](#cfn-cloudfront-continuousdeploymentpolicy-continuousdeploymentpolicyconfig-trafficconfig): {{
    TrafficConfig}}
  [Type](#cfn-cloudfront-continuousdeploymentpolicy-continuousdeploymentpolicyconfig-type): {{String}}
```

## Properties
<a name="aws-properties-cloudfront-continuousdeploymentpolicy-continuousdeploymentpolicyconfig-properties"></a>

`Enabled`  <a name="cfn-cloudfront-continuousdeploymentpolicy-continuousdeploymentpolicyconfig-enabled"></a>
A Boolean that indicates whether this continuous deployment policy is enabled (in effect). When this value is `true`, this policy is enabled and in effect. When this value is `false`, this policy is not enabled and has no effect.
*Required*: Yes
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SingleHeaderPolicyConfig`  <a name="cfn-cloudfront-continuousdeploymentpolicy-continuousdeploymentpolicyconfig-singleheaderpolicyconfig"></a>
This configuration determines which HTTP requests are sent to the staging distribution. If the HTTP request contains a header and value that matches what you specify here, the request is sent to the staging distribution. Otherwise the request is sent to the primary distribution.
*Required*: No
*Type*: [SingleHeaderPolicyConfig](aws-properties-cloudfront-continuousdeploymentpolicy-singleheaderpolicyconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SingleWeightPolicyConfig`  <a name="cfn-cloudfront-continuousdeploymentpolicy-continuousdeploymentpolicyconfig-singleweightpolicyconfig"></a>
This configuration determines the percentage of HTTP requests that are sent to the staging distribution.
*Required*: No
*Type*: [SingleWeightPolicyConfig](aws-properties-cloudfront-continuousdeploymentpolicy-singleweightpolicyconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StagingDistributionDnsNames`  <a name="cfn-cloudfront-continuousdeploymentpolicy-continuousdeploymentpolicyconfig-stagingdistributiondnsnames"></a>
The CloudFront domain name of the staging distribution. For example: `d111111abcdef8.cloudfront.net`.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TrafficConfig`  <a name="cfn-cloudfront-continuousdeploymentpolicy-continuousdeploymentpolicyconfig-trafficconfig"></a>
Contains the parameters for routing production traffic from your primary to staging distributions.
*Required*: No
*Type*: [TrafficConfig](aws-properties-cloudfront-continuousdeploymentpolicy-trafficconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-cloudfront-continuousdeploymentpolicy-continuousdeploymentpolicyconfig-type"></a>
The type of traffic configuration.
*Required*: No
*Type*: String
*Allowed values*: `SingleWeight | SingleHeader`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
