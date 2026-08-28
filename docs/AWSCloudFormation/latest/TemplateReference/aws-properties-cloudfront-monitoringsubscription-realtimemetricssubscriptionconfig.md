---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudfront-monitoringsubscription-realtimemetricssubscriptionconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFront::MonitoringSubscription RealtimeMetricsSubscriptionConfig
<a name="aws-properties-cloudfront-monitoringsubscription-realtimemetricssubscriptionconfig"></a>

A subscription configuration for additional CloudWatch metrics.

## Syntax
<a name="aws-properties-cloudfront-monitoringsubscription-realtimemetricssubscriptionconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudfront-monitoringsubscription-realtimemetricssubscriptionconfig-syntax.json"></a>

```
{
  "[RealtimeMetricsSubscriptionStatus](#cfn-cloudfront-monitoringsubscription-realtimemetricssubscriptionconfig-realtimemetricssubscriptionstatus)" : {{String}}
}
```

### YAML
<a name="aws-properties-cloudfront-monitoringsubscription-realtimemetricssubscriptionconfig-syntax.yaml"></a>

```
  [RealtimeMetricsSubscriptionStatus](#cfn-cloudfront-monitoringsubscription-realtimemetricssubscriptionconfig-realtimemetricssubscriptionstatus): {{String}}
```

## Properties
<a name="aws-properties-cloudfront-monitoringsubscription-realtimemetricssubscriptionconfig-properties"></a>

`RealtimeMetricsSubscriptionStatus`  <a name="cfn-cloudfront-monitoringsubscription-realtimemetricssubscriptionconfig-realtimemetricssubscriptionstatus"></a>
A flag that indicates whether additional CloudWatch metrics are enabled for a given CloudFront distribution.
*Required*: Yes
*Type*: String
*Allowed values*: `Enabled | Disabled`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
