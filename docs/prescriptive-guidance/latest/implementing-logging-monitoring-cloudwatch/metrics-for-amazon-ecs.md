---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/implementing-logging-monitoring-cloudwatch/metrics-for-amazon-ecs.html
---

# Metrics for Amazon ECS
<a name="metrics-for-amazon-ecs"></a>

[Amazon ECS provides standard CloudWatch metrics](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/cloudwatch-metrics.html) (for example, CPU and memory utilization) for the EC2 and Fargate launch types at the cluster and service level with the Amazon ECS container agent. You can also capture metrics for your services, tasks, and containers by using CloudWatch Container Insights, or capture your own custom container metrics by using the embedded metric format.

Container Insights is a CloudWatch feature that provides metrics such as CPU utilization, memory utilization, network traffic, and storage at the cluster, container instance, service, and task levels. Container Insights also creates automatic dashboards that help you analyze services and tasks, and see the average memory or CPU utilization at the container level. Container Insights publishes custom metrics to the ECS/ContainerInsights[ custom namespace](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/cloudwatch-metrics.html) that you can use for graphing, alarming, and dashboarding.

You can turn on Container Insight metrics by enabling Container Insights for each individual Amazon ECS cluster. If you also want to see metrics at the container instance level, you can [launch the CloudWatch agent as a daemon container on your Amazon ECS cluster](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/deploy-container-insights-ECS-instancelevel.html). You can use the [cwagent-ecs-instancemetric-cfn.yaml](https://github.com/aws-samples/logging-monitoring-apg-guide-examples/blob/main/examples/ecs/cwagent-ecs-instance-metric-cfn.yaml) AWS CloudFormation template to deploy the CloudWatch agent as an Amazon ECS service. Importantly, this example assumes that you created an appropriate custom CloudWatch agent configuration and stored it in Parameter Store with the key ecs-cwagent-daemon-service.

The [CloudWatch agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Container-Insights-metrics-ECS.html) deployed as a daemon container for CloudWatch Container Insights includes additional disk, memory, and CPU metrics such as instance\_cpu\_reserved\_capacity and instance\_memory\_reserved\_capacity with the ClusterName, ContainerInstanceId, InstanceId dimensions. Metrics at the container instance level are implemented by Container Insights by using the CloudWatch embedded metric format. You can configure additional system-level metrics for your Amazon ECS container instances by using the approach from from the Set up State Manager and Distributor for CloudWatch agent deployment and configuration (p. 21) section of this guide.

## Creating custom application metrics in Amazon ECS
<a name="creating-custom-application-metrics-in-amazon-ecs"></a>

You can create custom metrics for your applications by using the [CloudWatch embedded metric format](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Embedded_Metric_Format.html). The `awslogs` log driver can interpret CloudWatch embedded metric format statements.

The CW\_CONFIG\_CONTENT environment variable in the following example is set to the contents of the cwagentconfig Systems Manager Parameter Store parameter. You can run the agent with this basic configuration to configure it as an embedded metric format endpoint. However, it is no longer necessary.

```
  {
  "logs": {
    "metrics_collected": {
      "emf": { }
    }
  }
}
```

If you have Amazon ECS deployments across multiple accounts and Regions, you can use an AWS Secrets Manager secret to store your CloudWatch configuration and configure the secret policy to share it with your organization. You can use the secrets option in your task definition to set the CW\_CONFIG\_CONTENT variable.

You can use the AWS provided [open-source embedded metric format libraries](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Embedded_Metric_Format_Libraries.html) in your application and specify the AWS\_EMF\_AGENT\_ENDPOINT environment variable to connect to your CloudWatch agent sidecar container acting as an embedded metric format endpoint. For example, you can use the [ecs\_cw\_emf\_example](https://github.com/aws-samples/logging-monitoring-apg-guide-examples/tree/main/examples/ecs/ecs_cw_emf_example) sample Python application to send metrics in embedded metric format to a CloudWatch agent sidecar container configured as an embedded metric format endpoint.

The [Fluent Bit plugin](https://github.com/aws/amazon-cloudwatch-logs-for-fluent-bit) for CloudWatch can also be used to send embedded metric format messages. You can also use the [ecs\_firelense\_emf\_example](https://github.com/aws-samples/logging-monitoring-apg-guide-examples/tree/main/examples/ecs/ecs_firelense_emf_example) sample Python application to send metrics in embedded metric format to a Firelens for Amazon ECS sidecar container.

If you don't want to use embedded metric format, you can create and update CloudWatch metrics through the [AWS API](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/Welcome.html) or [AWS SDK](https://aws.amazon.com/developer/tools/). We don't recommend this approach unless you have a specific use case, because it adds maintenance and management overhead to your code.
