---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-monitoringschedule-monitoringappspecification.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::MonitoringSchedule MonitoringAppSpecification
<a name="aws-properties-sagemaker-monitoringschedule-monitoringappspecification"></a>

Container image configuration object for the monitoring job.

## Syntax
<a name="aws-properties-sagemaker-monitoringschedule-monitoringappspecification-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-monitoringschedule-monitoringappspecification-syntax.json"></a>

```
{
  "[ContainerArguments](#cfn-sagemaker-monitoringschedule-monitoringappspecification-containerarguments)" : {{[ String, ... ]}},
  "[ContainerEntrypoint](#cfn-sagemaker-monitoringschedule-monitoringappspecification-containerentrypoint)" : {{[ String, ... ]}},
  "[ImageUri](#cfn-sagemaker-monitoringschedule-monitoringappspecification-imageuri)" : {{String}},
  "[PostAnalyticsProcessorSourceUri](#cfn-sagemaker-monitoringschedule-monitoringappspecification-postanalyticsprocessorsourceuri)" : {{String}},
  "[RecordPreprocessorSourceUri](#cfn-sagemaker-monitoringschedule-monitoringappspecification-recordpreprocessorsourceuri)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-monitoringschedule-monitoringappspecification-syntax.yaml"></a>

```
  [ContainerArguments](#cfn-sagemaker-monitoringschedule-monitoringappspecification-containerarguments): {{
    - String}}
  [ContainerEntrypoint](#cfn-sagemaker-monitoringschedule-monitoringappspecification-containerentrypoint): {{
    - String}}
  [ImageUri](#cfn-sagemaker-monitoringschedule-monitoringappspecification-imageuri): {{String}}
  [PostAnalyticsProcessorSourceUri](#cfn-sagemaker-monitoringschedule-monitoringappspecification-postanalyticsprocessorsourceuri): {{String}}
  [RecordPreprocessorSourceUri](#cfn-sagemaker-monitoringschedule-monitoringappspecification-recordpreprocessorsourceuri): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-monitoringschedule-monitoringappspecification-properties"></a>

`ContainerArguments`  <a name="cfn-sagemaker-monitoringschedule-monitoringappspecification-containerarguments"></a>
An array of arguments for the container used to run the monitoring job.
*Required*: No
*Type*: Array of String
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ContainerEntrypoint`  <a name="cfn-sagemaker-monitoringschedule-monitoringappspecification-containerentrypoint"></a>
Specifies the entrypoint for a container used to run the monitoring job.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `256 | 100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ImageUri`  <a name="cfn-sagemaker-monitoringschedule-monitoringappspecification-imageuri"></a>
The container image to be run by the monitoring job.
*Required*: Yes
*Type*: String
*Pattern*: `.*`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PostAnalyticsProcessorSourceUri`  <a name="cfn-sagemaker-monitoringschedule-monitoringappspecification-postanalyticsprocessorsourceuri"></a>
An Amazon S3 URI to a script that is called after analysis has been performed. Applicable only for the built-in (first party) containers.
*Required*: No
*Type*: String
*Pattern*: `^(https|s3)://([^/]+)/?(.*)$`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RecordPreprocessorSourceUri`  <a name="cfn-sagemaker-monitoringschedule-monitoringappspecification-recordpreprocessorsourceuri"></a>
An Amazon S3 URI to a script that is called per row prior to running analysis. It can base64 decode the payload and convert it into a flattened JSON so that the built-in container can use the converted data. Applicable only for the built-in (first party) containers.
*Required*: No
*Type*: String
*Pattern*: `^(https|s3)://([^/]+)/?(.*)$`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
