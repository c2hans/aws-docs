---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-service-serviceconnectaccesslogconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::Service ServiceConnectAccessLogConfiguration
<a name="aws-properties-ecs-service-serviceconnectaccesslogconfiguration"></a>

Configuration for Service Connect access logging. Access logs provide detailed information about requests made to your service, including request patterns, response codes, and timing data for debugging and monitoring purposes.

**Note**
To enable access logs, you must also specify a `logConfiguration` in the `serviceConnectConfiguration`.

## Syntax
<a name="aws-properties-ecs-service-serviceconnectaccesslogconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ecs-service-serviceconnectaccesslogconfiguration-syntax.json"></a>

```
{
  "[Format](#cfn-ecs-service-serviceconnectaccesslogconfiguration-format)" : {{String}},
  "[IncludeQueryParameters](#cfn-ecs-service-serviceconnectaccesslogconfiguration-includequeryparameters)" : {{String}}
}
```

### YAML
<a name="aws-properties-ecs-service-serviceconnectaccesslogconfiguration-syntax.yaml"></a>

```
  [Format](#cfn-ecs-service-serviceconnectaccesslogconfiguration-format): {{String}}
  [IncludeQueryParameters](#cfn-ecs-service-serviceconnectaccesslogconfiguration-includequeryparameters): {{String}}
```

## Properties
<a name="aws-properties-ecs-service-serviceconnectaccesslogconfiguration-properties"></a>

`Format`  <a name="cfn-ecs-service-serviceconnectaccesslogconfiguration-format"></a>
The format for Service Connect access log output. Choose TEXT for human-readable logs or JSON for structured data that integrates well with log analysis tools.
*Required*: Yes
*Type*: String
*Allowed values*: `TEXT | JSON`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IncludeQueryParameters`  <a name="cfn-ecs-service-serviceconnectaccesslogconfiguration-includequeryparameters"></a>
Specifies whether to include query parameters in Service Connect access logs.
When enabled, query parameters from HTTP requests are included in the access logs. Consider security and privacy implications when enabling this feature, as query parameters may contain sensitive information such as request IDs and tokens. By default, this parameter is `DISABLED`.
*Required*: No
*Type*: String
*Allowed values*: `DISABLED | ENABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
