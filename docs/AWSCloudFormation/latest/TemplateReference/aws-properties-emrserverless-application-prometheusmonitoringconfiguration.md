---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-emrserverless-application-prometheusmonitoringconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMRServerless::Application PrometheusMonitoringConfiguration
<a name="aws-properties-emrserverless-application-prometheusmonitoringconfiguration"></a>

The monitoring configuration object you can configure to send metrics to Amazon Managed Service for Prometheus for a job run.

## Syntax
<a name="aws-properties-emrserverless-application-prometheusmonitoringconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-emrserverless-application-prometheusmonitoringconfiguration-syntax.json"></a>

```
{
  "[RemoteWriteUrl](#cfn-emrserverless-application-prometheusmonitoringconfiguration-remotewriteurl)" : {{String}}
}
```

### YAML
<a name="aws-properties-emrserverless-application-prometheusmonitoringconfiguration-syntax.yaml"></a>

```
  [RemoteWriteUrl](#cfn-emrserverless-application-prometheusmonitoringconfiguration-remotewriteurl): {{String}}
```

## Properties
<a name="aws-properties-emrserverless-application-prometheusmonitoringconfiguration-properties"></a>

`RemoteWriteUrl`  <a name="cfn-emrserverless-application-prometheusmonitoringconfiguration-remotewriteurl"></a>
The remote write URL in the Amazon Managed Service for Prometheus workspace to send metrics to.
*Required*: No
*Type*: String
*Pattern*: `^https://aps-workspaces.([a-z]{2}-[a-z-]{1,20}-[1-9]).amazonaws(.[0-9A-Za-z]{2,4})+/workspaces/[-_.0-9A-Za-z]{1,100}/api/v1/remote_write$`
*Minimum*: `1`
*Maximum*: `10280`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
