---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/implementing-logging-monitoring-cloudwatch/amazon-ecs-container-logs-for-ec2-and-fargate-launch-types.html
---

# Amazon ECS container logs for EC2 and Fargate launch types
<a name="amazon-ecs-container-logs-for-ec2-and-fargate-launch-types"></a>

Amazon ECS uses a task definition to deploys and manage containers as tasks and services. You configure the containers that you want to launch into your Amazon ECS cluster within a task definition. Logging is configured with a log driver at the container level. Multiple log driver options provide your containers with different logging systems (for example, awslogs,fluentd,gelf,jsonfile,journald,logentries,splunk,syslog, or awsfirelens) depending on whether you use the EC2 or Fargate launch type. The Fargate launch type provides a subset of the following log driver options: awslogs, splunk, and awsfirelens. AWS provides the awslogs log driver to capture and transmit container output to CloudWatch Logs. Log driver settings enable you to customize the log group, Region, and log stream prefix along with many other options.

The default naming for log groups and the option used by the **Auto-configure CloudWatch Logs** option on the AWS Management Console is /ecs/<task\_name>. The log stream name used by Amazon ECS has the <awslogs-stream-prefix>/<container\_name>/<task\_id> format. We recommend that you use a group name that groups your logs based on your organization's requirements. In the following table, the image\_name and image\_tag are included in the log stream's name.

|  |
| --- |
| Log group name | /<Business unit>/<Project or application name>/<Environment>/<Cluster name>/<Task name> |
| --- |--- |
| **Log stream name prefix** | /<image\_name>/<image\_tag> |

This information is also available in the task definition. However, tasks are regularly updated with new revisions, which means that the task definition might have used a different image\_name and image\_tag than those that the task definition is currently using. For more information and naming suggestions, see the Planning your CloudWatch deployment section of this guide.

If you use a continuous integration and continuous delivery (CI/CD) pipeline or automated process, you can create a new task definition revision for your application with each new Docker image build. For example, you can include the Docker image name, image tag, GitHub revision, or other important information in your task definition revision and logging configuration as a part of your CI/CD process.
