---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudfront-continuousdeploymentpolicy-sessionstickinessconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFront::ContinuousDeploymentPolicy SessionStickinessConfig
<a name="aws-properties-cloudfront-continuousdeploymentpolicy-sessionstickinessconfig"></a>

Session stickiness provides the ability to define multiple requests from a single viewer as a single session. This prevents the potentially inconsistent experience of sending some of a given user's requests to your staging distribution, while others are sent to your primary distribution. Define the session duration using TTL values.

## Syntax
<a name="aws-properties-cloudfront-continuousdeploymentpolicy-sessionstickinessconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudfront-continuousdeploymentpolicy-sessionstickinessconfig-syntax.json"></a>

```
{
  "[IdleTTL](#cfn-cloudfront-continuousdeploymentpolicy-sessionstickinessconfig-idlettl)" : {{Integer}},
  "[MaximumTTL](#cfn-cloudfront-continuousdeploymentpolicy-sessionstickinessconfig-maximumttl)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-cloudfront-continuousdeploymentpolicy-sessionstickinessconfig-syntax.yaml"></a>

```
  [IdleTTL](#cfn-cloudfront-continuousdeploymentpolicy-sessionstickinessconfig-idlettl): {{Integer}}
  [MaximumTTL](#cfn-cloudfront-continuousdeploymentpolicy-sessionstickinessconfig-maximumttl): {{Integer}}
```

## Properties
<a name="aws-properties-cloudfront-continuousdeploymentpolicy-sessionstickinessconfig-properties"></a>

`IdleTTL`  <a name="cfn-cloudfront-continuousdeploymentpolicy-sessionstickinessconfig-idlettl"></a>
The amount of time after which you want sessions to cease if no requests are received. Allowed values are 300–3600 seconds (5–60 minutes).
*Required*: Yes
*Type*: Integer
*Minimum*: `300`
*Maximum*: `3600`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaximumTTL`  <a name="cfn-cloudfront-continuousdeploymentpolicy-sessionstickinessconfig-maximumttl"></a>
The maximum amount of time to consider requests from the viewer as being part of the same session. Allowed values are 300–3600 seconds (5–60 minutes).
*Required*: Yes
*Type*: Integer
*Minimum*: `300`
*Maximum*: `3600`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
