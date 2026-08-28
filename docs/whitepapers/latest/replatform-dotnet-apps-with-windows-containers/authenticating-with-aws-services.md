---
source_url: https://docs.aws.amazon.com/whitepapers/latest/replatform-dotnet-apps-with-windows-containers/authenticating-with-aws-services.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Authenticating with AWS services
<a name="authenticating-with-aws-services"></a>

 Amazon ECS provides multiple levels to secure your applications and clusters using IAM while containerized applications interact with other AWS services. The following diagram depicts the types of roles Amazon ECS supports when using the EC2 launch type.

![Types of roles Amazon ECS supports when using the EC2 launch type](http://docs.aws.amazon.com/whitepapers/latest/replatform-dotnet-apps-with-windows-containers/images/ecs-roles.png)

## Service-linked role
<a name="service-linked-role"></a>

 There are multiple activities that the Amazon ECS runs while it orchestrates your container workloads. Amazon ECS uses a service-linked role for the permissions it requires to call other AWS services on your behalf. These include services such as Amazon EC2 to manage elastic network interfaces, ELB to manage targets, and [Amazon Route 53](https://aws.amazon.com/route53/) for creating health checks. A more detailed list can be found on the [Service-linked role for Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/using-service-linked-roles.html) page.

![Amazon ECS service-linked role architecture](http://docs.aws.amazon.com/whitepapers/latest/replatform-dotnet-apps-with-windows-containers/images/ecs-service-linked-role.png)

## Container instance role
<a name="container-instance-role"></a>

 The [container instance role](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/instance_IAM_role.html) is the IAM role used as the Instance role by EC2 instances running your containers. This role is also used by the Amazon ECS container agent to make calls to AWS services and connect with the Amazon ECS to register container instances, report status, and get commands. Other examples include the agent starting a telemetry session, or creating the Amazon ECS cluster if one does not already exist. A more detailed list can be found on the [Amazon ECS container instance IAM role](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/instance_IAM_role.html) page.

![Container instance role architecture](http://docs.aws.amazon.com/whitepapers/latest/replatform-dotnet-apps-with-windows-containers/images/container-instance-role.png)

## Task execution role
<a name="task-execution-role"></a>

 The [task execution role](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_execution_IAM_role.html) grants the Amazon ECS container agent permission to make AWS API calls on your behalf when an [Amazon ECS task](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html#welcome-task-sched) is started. An example of an activity that the Amazon ECS Agent runs during this time is pulling container images from a private repository, and [private registry authentication](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/private-auth.html) needs to be configured.

 Another use case where this role is required is [injecting sensitive data into your containers](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_execution_IAM_role.html#task-execution-secrets). You might choose to store sensitive data (such as database connection strings) in either [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/) or [AWS Systems Manager Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html), and reference them in your container definition. Sensitive data is injected into your container as environment variables when the container is initially started without having to write code to retrieve the values.

 If the secret or Parameter Store parameter is subsequently updated or rotated, the container will not receive the updated value automatically. Either launch a new task, or if your task is part of a service, you can update the service and use the **Force new deployment** option to force the service to launch a fresh task.

 For Windows tasks that are configured to use the `awslogs` logging driver, set the `ECS_ENABLE_AWSLOGS_EXECUTIONROLE_OVERRIDE` environment variable on your container instance. This can be done with user data using the following syntax:

```
<PowerShell>
[Environment]::SetEnvironmentVariable("ECS_ENABLE_AWSLOGS_EXECUTIONROLE_OVERRIDE", $TRUE, "Machine")
Initialize-ECSAgent -Cluster '<cluster name>' -LoggingDrivers '["json-file","awslogs"]' -EnableTaskIAMRole
</PowerShell>
```

![Task execution role architecture](http://docs.aws.amazon.com/whitepapers/latest/replatform-dotnet-apps-with-windows-containers/images/task-execution-role.png)

## Task role
<a name="task-role"></a>

 The [task role](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-iam-roles.html) is the IAM role assigned to the Containers instances created as part of the Amazon ECS task. This role provides applications using the AWS SDK or CLI the AWS credentials used to make API requests to authorized AWS services. For example, you can set the policy associated with the task role to allow your application to read/write items from or to DynamoDB, publish an event to an EventBridge bus, or start an [AWS Step Functions](https://aws.amazon.com/step-functions/) workflow.

 One of the requirements that must be met to enable [IAM roles for tasks on Windows](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/windows_task_IAM_roles.html) is that the `EnableTaskIAMRole` option be set when you launch an EC2 instance. This can be done by using a user data script. For example:

```
<PowerShell>
Import-Module ECSTools
Initialize-ECSAgent -Cluster '<cluster name>' -EnableTaskIAMRole
</PowerShell>
```

 Additionally, before containers can access the credential proxy on the container instance to get credentials, the container instance must be bootstrapped with the required networking commands. The following code example script should be run on your containers when they start.

```
$gateway = (Get-NetRoute | Where { $_.DestinationPrefix -eq '0.0.0.0/0' } | Sort-Object RouteMetric | Select NextHop).NextHop
$ifIndex = (Get-NetAdapter -InterfaceDescription "Hyper-V Virtual Ethernet*" | Sort-Object | Select ifIndex).ifIndex
New-NetRoute -DestinationPrefix 169.254.170.2/32 -InterfaceIndex $ifIndex -NextHop $gateway # credentials API
New-NetRoute -DestinationPrefix 169.254.169.254/32 -InterfaceIndex $ifIndex -NextHop $gateway # metadata API
```

 For a complete list of requirements, refer to the [Windows IAM roles for tasks](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/windows_task_IAM_roles.html) page on the Amazon ECS Developer Guide.

 Now that you know how to enable IAM roles for Amazon ECS Tasks on Windows, learn how your application code can assume the role.

![Task role architecture](http://docs.aws.amazon.com/whitepapers/latest/replatform-dotnet-apps-with-windows-containers/images/task-role-arch.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
