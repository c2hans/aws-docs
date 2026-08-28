---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/implementing-logging-monitoring-cloudwatch/faq.html
---

# Designing and implementing logging and monitoring with CloudWatch FAQ
<a name="faq"></a>

This section provides answers to commonly raised questions about designing and implementing logging and monitoring solution with CloudWatch.

## Where do I store my CloudWatch configuration files?
<a name="where-do-i-store-my-cloudwatch-configuration-files-.a282966f-4705-599f-a1fe-fba454dd259d"></a>

The CloudWatch agent for Amazon EC2 can apply multiple configuration files that are stored in the CloudWatch configuration directory. Ideally, you should store your CloudWatch configuration as a set of files because you can version control and use them again across multiple accounts and environments. For more information about this, see the Storing CloudWatch configuration files in an S3 bucket section of this guide. Alternatively, you can store your configuration files in a repository on GitHub and automate the retrieval of the configuration files when a new EC2 instance is provisioned.

## How can I create a ticket in my service management solution when an alarm is raised?
<a name="how-can-i-create-a-ticket-in-my-service-management-solution-when-an-alarm-is-raised-.1d2cf27f-44c6-56d7-a7ad-251bb62842ce"></a>

You integrate your service management system with an Amazon Simple Notification Service (Amazon SNS) topic and configure the CloudWatch alarm to notify the SNS topic when an alarm is raised. Your integrated system receives the SNS message and can create a ticket using your service management systems APIs or SDKs. For example, [ServiceNow integrates with Amazon SNS as a feature of the IT Operations Module](https://docs.servicenow.com/bundle/kingston-it-operations-management/page/product/event-management/task/aws-events-transform-script.html).

## How do I use CloudWatch to capture log files in my containers?
<a name="how-do-i-use-cloudwatch-to-capture-log-files-in-my-containers-.1446e9ff-b111-5081-96b2-f3ff15221a20"></a>

Amazon ECS tasks and Amazon EKS pods can be configured to automatically send the STDOUT and STDERR output to CloudWatch. The recommended approach for logging containerized applications is to have containers send their output to STDOUT and STDERR. This is also covered in the [Twelve-Factor App manifesto](https://12factor.net/).

However, if you want to send specific log files to CloudWatch then you can mount a volume in your Amazon EKS pod or Amazon ECS task definition to where your application will write its lot files and use a sidecar container for Fluentd or Fluent Bit to send the logs to CloudWatch. You should consider symbolic linking a specific log file in your container to /dev/stdout and /dev/stderr. For more information about this, see [View logs for a container or service](https://docs.docker.com/config/containers/logging/) in the Docker documentation.

## How do I monitor health issues for AWS services?
<a name="how-do-i-monitor-health-issues-for-aws-services-.b5711f60-64ac-50e8-81d9-ef2c2effbd08"></a>

You can use the [ AWS Health Dashboard](https://docs.aws.amazon.com/health/latest/ug/getting-started-health-dashboard.html) to monitor AWS health events. You can also refer to the [aws-health-tools](https://github.com/aws/aws-health-tools) GitHub repository for sample automation solutions related to AWS health events.

## How can I create a custom CloudWatch metric when no agent support exists?
<a name="how-can-i-create-a-custom-cloudwatch-metric-when-no-agent-support-exists-.64d7ab53-5a57-5b5f-919e-6a11eec84e0f"></a>

You can use the embedded metric format to ingest metrics into CloudWatch. You can also use AWS SDK (for example, [put\_metric\_data](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch.html#CloudWatch.Client.put_metric_data)), AWS CLI (for example, [put-metric-data](https://docs.aws.amazon.com/cli/latest/reference/cloudwatch/put-metric-data.html)), or AWS API (for example, [PutMetricData](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_PutMetricData.html)) to create custom metrics. You should consider how any custom logic will be maintained long term. One approach would be to use Lambda with integrated embedded metric format support to create your metrics, along with an Amazon EventBridge event [schedule rule](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-create-rule-schedule.html) to establish the period for the metric.

## How do I integrate my existing logging and monitoring tools with AWS?
<a name="how-do-i-integrate-my-existing-logging-and-monitoring-tools-with-aws-.82ab7ecf-d489-51fa-b270-4bc5193ce069"></a>

You should refer to guidance provided by the software or service vendor for integrating with AWS. You might be able to use agent software, SDK, or an API provided to send logs and metrics to their solution. You might also be able to use an open-source solution, such as Fluentd or Fluent Bit, configured to the vendor's specifications. You can also use the AWS SDK and CloudWatch Logs subscription filters with Lambda and Kinesis Data Streams to create custom log processors and shippers. Finally, you should also consider how you will integrate the software if you are using multiple accounts and Regions.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
