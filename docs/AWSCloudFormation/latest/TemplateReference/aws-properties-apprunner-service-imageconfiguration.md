---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-apprunner-service-imageconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppRunner::Service ImageConfiguration
<a name="aws-properties-apprunner-service-imageconfiguration"></a>

Describes the configuration that AWS App Runner uses to run an App Runner service using an image pulled from a source image repository.

## Syntax
<a name="aws-properties-apprunner-service-imageconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-apprunner-service-imageconfiguration-syntax.json"></a>

```
{
  "[Port](#cfn-apprunner-service-imageconfiguration-port)" : {{String}},
  "[RuntimeEnvironmentSecrets](#cfn-apprunner-service-imageconfiguration-runtimeenvironmentsecrets)" : {{[ KeyValuePair, ... ]}},
  "[RuntimeEnvironmentVariables](#cfn-apprunner-service-imageconfiguration-runtimeenvironmentvariables)" : {{[ KeyValuePair, ... ]}},
  "[StartCommand](#cfn-apprunner-service-imageconfiguration-startcommand)" : {{String}}
}
```

### YAML
<a name="aws-properties-apprunner-service-imageconfiguration-syntax.yaml"></a>

```
  [Port](#cfn-apprunner-service-imageconfiguration-port): {{String}}
  [RuntimeEnvironmentSecrets](#cfn-apprunner-service-imageconfiguration-runtimeenvironmentsecrets): {{
    - KeyValuePair}}
  [RuntimeEnvironmentVariables](#cfn-apprunner-service-imageconfiguration-runtimeenvironmentvariables): {{
    - KeyValuePair}}
  [StartCommand](#cfn-apprunner-service-imageconfiguration-startcommand): {{String}}
```

## Properties
<a name="aws-properties-apprunner-service-imageconfiguration-properties"></a>

`Port`  <a name="cfn-apprunner-service-imageconfiguration-port"></a>
The port that your application listens to in the container.
Default: `8080`
*Required*: No
*Type*: String
*Pattern*: `.*`
*Minimum*: `0`
*Maximum*: `51200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RuntimeEnvironmentSecrets`  <a name="cfn-apprunner-service-imageconfiguration-runtimeenvironmentsecrets"></a>
An array of key-value pairs representing the secrets and parameters that get referenced to your service as an environment variable. The supported values are either the full Amazon Resource Name (ARN) of the AWS Secrets Manager secret or the full ARN of the parameter in the AWS Systems Manager Parameter Store.
+  If the AWS Systems Manager Parameter Store parameter exists in the same AWS Region as the service that you're launching, you can use either the full ARN or name of the secret. If the parameter exists in a different Region, then the full ARN must be specified.
+  Currently, cross account referencing of AWS Systems Manager Parameter Store parameter is not supported.
*Required*: No
*Type*: Array of [KeyValuePair](aws-properties-apprunner-service-keyvaluepair.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RuntimeEnvironmentVariables`  <a name="cfn-apprunner-service-imageconfiguration-runtimeenvironmentvariables"></a>
Environment variables that are available to your running App Runner service. An array of key-value pairs.
*Required*: No
*Type*: Array of [KeyValuePair](aws-properties-apprunner-service-keyvaluepair.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StartCommand`  <a name="cfn-apprunner-service-imageconfiguration-startcommand"></a>
An optional command that App Runner runs to start the application in the source image. If specified, this command overrides the Docker image’s default start command.
*Required*: No
*Type*: String
*Pattern*: `[^\x0a\x0d]+`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
