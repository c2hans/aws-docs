---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-service-serviceconnectconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::Service ServiceConnectConfiguration
<a name="aws-properties-ecs-service-serviceconnectconfiguration"></a>

The Service Connect configuration of your Amazon ECS service. The configuration for this service to discover and connect to services, and be discovered by, and connected from, other services within a namespace.

Tasks that run in a namespace can use short names to connect to services in the namespace. Tasks can connect to services across all of the clusters in the namespace. Tasks connect through a managed proxy container that collects logs and metrics for increased visibility. Only the tasks that Amazon ECS services create are supported with Service Connect. For more information, see [Service Connect](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-connect.html) in the *Amazon Elastic Container Service Developer Guide*.

## Syntax
<a name="aws-properties-ecs-service-serviceconnectconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ecs-service-serviceconnectconfiguration-syntax.json"></a>

```
{
  "[AccessLogConfiguration](#cfn-ecs-service-serviceconnectconfiguration-accesslogconfiguration)" : {{ServiceConnectAccessLogConfiguration}},
  "[Enabled](#cfn-ecs-service-serviceconnectconfiguration-enabled)" : {{Boolean}},
  "[LogConfiguration](#cfn-ecs-service-serviceconnectconfiguration-logconfiguration)" : {{LogConfiguration}},
  "[Namespace](#cfn-ecs-service-serviceconnectconfiguration-namespace)" : {{String}},
  "[Services](#cfn-ecs-service-serviceconnectconfiguration-services)" : {{[ ServiceConnectService, ... ]}}
}
```

### YAML
<a name="aws-properties-ecs-service-serviceconnectconfiguration-syntax.yaml"></a>

```
  [AccessLogConfiguration](#cfn-ecs-service-serviceconnectconfiguration-accesslogconfiguration): {{
    ServiceConnectAccessLogConfiguration}}
  [Enabled](#cfn-ecs-service-serviceconnectconfiguration-enabled): {{Boolean}}
  [LogConfiguration](#cfn-ecs-service-serviceconnectconfiguration-logconfiguration): {{
    LogConfiguration}}
  [Namespace](#cfn-ecs-service-serviceconnectconfiguration-namespace): {{String}}
  [Services](#cfn-ecs-service-serviceconnectconfiguration-services): {{
    - ServiceConnectService}}
```

## Properties
<a name="aws-properties-ecs-service-serviceconnectconfiguration-properties"></a>

`AccessLogConfiguration`  <a name="cfn-ecs-service-serviceconnectconfiguration-accesslogconfiguration"></a>
The configuration for Service Connect access logging. Access logs capture detailed information about requests made to your service, including request patterns, response codes, and timing data. They can be useful for debugging connectivity issues, monitoring service performance, and auditing service-to-service communication for security and compliance purposes.
To enable access logs, you must also specify a `logConfiguration` in the `serviceConnectConfiguration`.
*Required*: No
*Type*: [ServiceConnectAccessLogConfiguration](aws-properties-ecs-service-serviceconnectaccesslogconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Enabled`  <a name="cfn-ecs-service-serviceconnectconfiguration-enabled"></a>
Specifies whether to use Service Connect with this service.
*Required*: Yes
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LogConfiguration`  <a name="cfn-ecs-service-serviceconnectconfiguration-logconfiguration"></a>
The log configuration for the container. This parameter maps to `LogConfig` in the docker container create command and the `--log-driver` option to docker run.
By default, containers use the same logging driver that the Docker daemon uses. However, the container might use a different logging driver than the Docker daemon by specifying a log driver configuration in the container definition.
Understand the following when specifying a log configuration for your containers.
+ Amazon ECS currently supports a subset of the logging drivers available to the Docker daemon. Additional log drivers may be available in future releases of the Amazon ECS container agent.

  For tasks on AWS Fargate, the supported log drivers are `awslogs`, `splunk`, and `awsfirelens`.

  For tasks hosted on Amazon EC2 instances, the supported log drivers are `awslogs`, `fluentd`, `gelf`, `json-file`, `journald`,`syslog`, `splunk`, and `awsfirelens`.
+ This parameter requires version 1.18 of the Docker Remote API or greater on your container instance.
+ For tasks that are hosted on Amazon EC2 instances, the Amazon ECS container agent must register the available logging drivers with the `ECS_AVAILABLE_LOGGING_DRIVERS` environment variable before containers placed on that instance can use these log configuration options. For more information, see [Amazon ECS container agent configuration](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-agent-config.html) in the *Amazon Elastic Container Service Developer Guide*.
+ For tasks that are on AWS Fargate, because you don't have access to the underlying infrastructure your tasks are hosted on, any additional software needed must be installed outside of the task. For example, the Fluentd output aggregators or a remote host running Logstash to send Gelf logs to.
*Required*: No
*Type*: [LogConfiguration](aws-properties-ecs-service-logconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Namespace`  <a name="cfn-ecs-service-serviceconnectconfiguration-namespace"></a>
The namespace name or full Amazon Resource Name (ARN) of the AWS Cloud Map namespace for use with Service Connect. The namespace must be in the same AWS Region as the Amazon ECS service and cluster. The type of namespace doesn't affect Service Connect. For more information about AWS Cloud Map, see [Working with Services](https://docs.aws.amazon.com/cloud-map/latest/dg/working-with-services.html) in the *AWS Cloud Map Developer Guide*.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Services`  <a name="cfn-ecs-service-serviceconnectconfiguration-services"></a>
The list of Service Connect service objects. These are names and aliases (also known as endpoints) that are used by other Amazon ECS services to connect to this service.
This field is not required for a "client" Amazon ECS service that's a member of a namespace only to connect to other services within the namespace. An example of this would be a frontend application that accepts incoming requests from either a load balancer that's attached to the service or by other means.
An object selects a port from the task definition, assigns a name for the AWS Cloud Map service, and a list of aliases (endpoints) and ports for client applications to refer to this service.
*Required*: No
*Type*: Array of [ServiceConnectService](aws-properties-ecs-service-serviceconnectservice.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also
<a name="aws-properties-ecs-service-serviceconnectconfiguration--seealso"></a>
+  [Associate an Application Load Balancer with a service](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#aws-resource-ecs-service--examples--Associate_an_Application_Load_Balancer_with_a_service)
