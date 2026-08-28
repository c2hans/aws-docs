---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-service-serviceconnectservice.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::Service ServiceConnectService
<a name="aws-properties-ecs-service-serviceconnectservice"></a>

The Service Connect service object configuration. For more information, see [Service Connect](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-connect.html) in the *Amazon Elastic Container Service Developer Guide*.

## Syntax
<a name="aws-properties-ecs-service-serviceconnectservice-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ecs-service-serviceconnectservice-syntax.json"></a>

```
{
  "[ClientAliases](#cfn-ecs-service-serviceconnectservice-clientaliases)" : {{[ ServiceConnectClientAlias, ... ]}},
  "[DiscoveryName](#cfn-ecs-service-serviceconnectservice-discoveryname)" : {{String}},
  "[IngressPortOverride](#cfn-ecs-service-serviceconnectservice-ingressportoverride)" : {{Integer}},
  "[PortName](#cfn-ecs-service-serviceconnectservice-portname)" : {{String}},
  "[Timeout](#cfn-ecs-service-serviceconnectservice-timeout)" : {{TimeoutConfiguration}},
  "[Tls](#cfn-ecs-service-serviceconnectservice-tls)" : {{ServiceConnectTlsConfiguration}}
}
```

### YAML
<a name="aws-properties-ecs-service-serviceconnectservice-syntax.yaml"></a>

```
  [ClientAliases](#cfn-ecs-service-serviceconnectservice-clientaliases): {{
    - ServiceConnectClientAlias}}
  [DiscoveryName](#cfn-ecs-service-serviceconnectservice-discoveryname): {{String}}
  [IngressPortOverride](#cfn-ecs-service-serviceconnectservice-ingressportoverride): {{Integer}}
  [PortName](#cfn-ecs-service-serviceconnectservice-portname): {{String}}
  [Timeout](#cfn-ecs-service-serviceconnectservice-timeout): {{
    TimeoutConfiguration}}
  [Tls](#cfn-ecs-service-serviceconnectservice-tls): {{
    ServiceConnectTlsConfiguration}}
```

## Properties
<a name="aws-properties-ecs-service-serviceconnectservice-properties"></a>

`ClientAliases`  <a name="cfn-ecs-service-serviceconnectservice-clientaliases"></a>
The list of client aliases for this Service Connect service. You use these to assign names that can be used by client applications. The maximum number of client aliases that you can have in this list is 1.
Each alias ("endpoint") is a fully-qualified name and port number that other Amazon ECS tasks ("clients") can use to connect to this service.
Each name and port mapping must be unique within the namespace.
For each `ServiceConnectService`, you must provide at least one `clientAlias` with one `port`.
*Required*: No
*Type*: Array of [ServiceConnectClientAlias](aws-properties-ecs-service-serviceconnectclientalias.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DiscoveryName`  <a name="cfn-ecs-service-serviceconnectservice-discoveryname"></a>
The `discoveryName` is the name of the new AWS Cloud Map service that Amazon ECS creates for this Amazon ECS service. This must be unique within the AWS Cloud Map namespace. The name can contain up to 64 characters. The name can include lowercase letters, numbers, underscores (\_), and hyphens (-). The name can't start with a hyphen.
If the `discoveryName` isn't specified, the port mapping name from the task definition is used in `portName.namespace`.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IngressPortOverride`  <a name="cfn-ecs-service-serviceconnectservice-ingressportoverride"></a>
The port number for the Service Connect proxy to listen on.
Use the value of this field to bypass the proxy for traffic on the port number specified in the named `portMapping` in the task definition of this application, and then use it in your VPC security groups to allow traffic into the proxy for this Amazon ECS service.
In `awsvpc` mode and Fargate, the default value is the container port number. The container port number is in the `portMapping` in the task definition. In bridge mode, the default value is the ephemeral port of the Service Connect proxy.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `65535`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PortName`  <a name="cfn-ecs-service-serviceconnectservice-portname"></a>
The `portName` must match the name of one of the `portMappings` from all the containers in the task definition of this Amazon ECS service.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Timeout`  <a name="cfn-ecs-service-serviceconnectservice-timeout"></a>
A reference to an object that represents the configured timeouts for Service Connect.
*Required*: No
*Type*: [TimeoutConfiguration](aws-properties-ecs-service-timeoutconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tls`  <a name="cfn-ecs-service-serviceconnectservice-tls"></a>
A reference to an object that represents a Transport Layer Security (TLS) configuration.
*Required*: No
*Type*: [ServiceConnectTlsConfiguration](aws-properties-ecs-service-serviceconnecttlsconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also
<a name="aws-properties-ecs-service-serviceconnectservice--seealso"></a>
+  [Associate an Application Load Balancer with a service](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#aws-resource-ecs-service--examples--Associate_an_Application_Load_Balancer_with_a_service)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
