---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/implementing-logging-monitoring-cloudwatch/resources.html
---

# Resources
<a name="resources"></a>

## Introduction
<a name="introduction.efa42a0e-4510-54ac-a7c0-effb0914f4bf"></a>
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected/)

## Targeted business outcomes
<a name="targeted-business-outcomes.01ac6a0c-9c25-55a9-bdef-b5bf7bf1d6dc"></a>
+ [logging-monitoring-apg-guide-examples](https://github.com/aws-samples/logging-monitoring-apg-guide-examples)
+ [Six advantages of cloud computing](https://docs.aws.amazon.com/whitepapers/latest/aws-overview/six-advantages-of-cloud-computing.html)

## Planning your CloudWatch deployment
<a name="planning-your-cloudwatch-deployment.7e14b9c4-5ec7-5eae-8cc1-92f8f9ed5c93"></a>
+ [AWS Organizations terminology and concepts](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html)
+ [AWS Systems Manager Quick Setup](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-quick-setup.html)
+ [Collecting metrics and logs from Amazon EC2 instances and on-premises servers with the CloudWatch agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.html)
+ [cloudwatch-config-s3-bucket.yaml](https://github.com/aws-samples/logging-monitoring-apg-guide-examples/blob/main/cloudwatch-config-s3-bucket.yaml)
+ [Create the CloudWatch agent configuration file with the wizard](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/create-cloudwatch-agent-configuration-file-wizard.html)
+ [Enterprise DevOps: Why you should run what you build](https://aws.amazon.com/blogs/enterprise-strategy/enterprise-devops-why-you-should-run-what-you-build/)
+ [Exporting log data to Amazon S3](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/S3Export.html)
+ [Fine-grained access control in Amazon ES](https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/fgac.html)
+ [Lambda quotas](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html)
+ [Manually create or edit the CloudWatch agent configuration file](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Agent-Configuration-File-Details.html#CloudWatch-Agent-Configuration-File-Agentsection)
+ [Real-time processing of log data with subscriptions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Subscriptions.html)
+ [Tools to build on AWS](https://aws.amazon.com/developer/tools/)

## Configuring the CloudWatch agent for EC2 instances and on-premises servers
<a name="configuring-the-cloudwatch-agent-for-ec2-instances-and-on-premises-servers.e6f7a187-7918-5f7f-aebb-cb4146ac854e"></a>
+ [Amazon EC2 metric dimensions](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/viewing_metrics_with_cloudwatch.html#ec2-cloudwatch-dimensions)
+ [Burstable performance instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/burstable-performance-instances.html)
+ [CloudWatch agent predefined metric sets](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/create-cloudwatch-agent-configuration-file-wizard.html#cloudwatch-agent-preset-metrics)
+ [Collect process metrics with the procstat plugin](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Agent-procstat-process-metrics.html)
+ [Configuring the CloudWatch agent for procstat](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Agent-procstat-process-metrics.html#CloudWatch-Agent-procstat-configuration)
+ [Manage detailed monitoring for your EC2 instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/manage-detailed-monitoring.html)
+ [Ingesting high-cardinality logs and generating metrics with CloudWatch embedded metric format](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Embedded_Metric_Format.html)
+ [Working with log groups and log streams](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html)
+ [List the available CloudWatch metrics for your instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/viewing_metrics_with_cloudwatch.html)
+ [PutLogEvents](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutLogEvents.html)
+ [Retrieve custom metrics with collectd](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Agent-custom-metrics-collectd.html)
+ [Retrieve custom metrics with StatsD](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Agent-custom-metrics-statsd.html)

## CloudWatch agent installation approaches for Amazon EC2 and on-premises servers
<a name="cloudwatch-agent-installation-approaches-for-amazon-ec2-and-on-premises-servers.c5c532d5-cc60-50b3-b8eb-6d2dbc060892"></a>
+ [Create the IAM service role required for Systems Manager in hybrid and multicloud environments](https://docs.aws.amazon.com/systems-manager/latest/userguide/hybrid-multicloud-service-role.html)
+ [Create a managed-instance activation for a hybrid environment](https://docs.aws.amazon.com/systems-manager/latest/userguide/hybrid-activation-managed-nodes.html)
+ [Create IAM roles and users for use with the CloudWatch agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/create-iam-roles-for-cloudwatch-agent.html)
+ [Download and configure the CloudWatch agent using the command line](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/download-cloudwatch-agent-commandline.html)
+ [How can I configure on-premises servers that use Systems Manager agent and the unified CloudWatch agent to use only temporary credentials?](https://repost.aws/knowledge-center/cloudwatch-on-premises-temp-credentials)
+ [Prerequisites for stack set operations](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-prereqs.html)
+ [Using spot instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances.html)

## Logging and monitoring on Amazon ECS
<a name="logging-and-monitoring-on-amazon-ecs.a7e027d7-bd2e-52b3-9249-4b105e785e0b"></a>
+ [amazon-cloudwatch-logs-for-fluent-bit](https://github.com/aws/amazon-cloudwatch-logs-for-fluent-bit)
+ [Amazon ECS CloudWatch metrics](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/cloudwatch-metrics.html)
+ [Amazon ECS Container Insights metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Container-Insights-metrics-ECS.html)
+ [Amazon ECS container agent](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-agent-versions.html)
+ [Amazon ECS launch types](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/launch_types.html)
+ [Deploying the CloudWatch agent to collect EC2 instance-level metrics on Amazon ECS](https://github.com/aws-samples/logging-monitoring-apg-guide-examples/blob/main/examples/ecs/cwagent-ecs-instance-metric-cfn.yaml)
+ [ecs\_cluster\_with\_cloudwatch\_linux.yaml](https://github.com/aws-samples/logging-monitoring-apg-guide-examples/blob/main/examples/ecs/ecs_cluster_with_cloudwatch_linux.yaml)
+ [ecs\_cw\_emf\_example](https://github.com/aws-samples/logging-monitoring-apg-guide-examples/tree/main/examples/ecs/ecs_cw_emf_example)
+ [ecs\_firelense\_emf\_example](https://github.com/aws-samples/logging-monitoring-apg-guide-examples/tree/main/examples/ecs/ecs_firelense_emf_example)
+ [ecs-task-nginx-firelense.json](https://github.com/aws-samples/logging-monitoring-apg-guide-examples/blob/main/examples/ecs/ecs-task-nginx-firelense.json)
+ [Retrieving Amazon ECS optimized AMI metadata](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/retrieve-ecs-optimized_AMI.html)
+ [Using the awslogs log driver](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/using_awslogs.html)
+ [Using the client libraries to generate embedded metric format logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Embedded_Metric_Format_Libraries.html)

## Logging and monitoring on Amazon EKS
<a name="logging-and-monitoring-on-amazon-eks.4b028175-1073-59d3-80a0-ec8f4312cf73"></a>
+ [Amazon EKS control plane logging](https://docs.aws.amazon.com/eks/latest/userguide/control-plane-logs.html)
+ [amazon\_eks\_managed\_node\_group\_launch\_config.yaml](https://github.com/aws-samples/logging-monitoring-apg-guide-examples/blob/main/examples/eks/amazon_eks_managed_node_group_launch_config.yaml)
+ [Amazon EKS nodes](https://docs.aws.amazon.com/eks/latest/userguide/eks-compute.html)
+ [amazon-eks-nodegroup.yaml](https://github.com/aws-samples/logging-monitoring-apg-guide-examples/blob/main/examples/eks/amazon-eks-nodegroup.yaml)
+ [Amazon EKS Service Level Agreement](https://aws.amazon.com/eks/sla/)
+ [Container Insights Prometheus metrics monitoring](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContainerInsights-Prometheus.html)
+ [Control plane metrics with Prometheus](https://docs.aws.amazon.com/eks/latest/userguide/prometheus.html)
+ [Fargate logging](https://docs.aws.amazon.com/eks/latest/userguide/fargate-logging.html)
+ [Fluent Bit for Amazon EKS on Fargate](https://aws.amazon.com/blogs/containers/fluent-bit-for-amazon-eks-on-aws-fargate-is-here/)
+ [How to capture application logs when using Amazon EKS on Fargate](https://aws.amazon.com/blogs/containers/how-to-capture-application-logs-when-using-amazon-eks-on-aws-fargate/)
+ [Installing the CloudWatch agent to collect Prometheus metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContainerInsights-Prometheus-Setup.html#ContainerInsights-Prometheus-Setup-install-agent)
+ [Installing the Kubernetes Metrics Server](https://docs.aws.amazon.com/eks/latest/userguide/metrics-server.html)
+ [kubernetes / dashboard](https://github.com/kubernetes/dashboard)
+ [Kubernetes Horizontal Pod Autoscaler](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/)
+ [Kubernetes Control Plane components](https://kubernetes.io/docs/concepts/overview/components/#control-plane-components)
+ [Kubernetes pods](https://kubernetes.io/docs/concepts/workloads/pods/)
+ [Launch template support](https://docs.aws.amazon.com/eks/latest/userguide/launch-templates.html)
+ [Managed node groups](https://docs.aws.amazon.com/eks/latest/userguide/managed-node-groups.html)
+ [Managed node update behavior](https://docs.aws.amazon.com/eks/latest/userguide/managed-node-update-behavior.html)
+ [metrics-server](https://github.com/kubernetes-sigs/metrics-server)
+ [Monitoring Amazon EKS on Fargate using Prometheus and Grafana](https://aws.amazon.com/blogs/containers/monitoring-amazon-eks-on-aws-fargate-using-prometheus-and-grafana/)
+ [prometheus\_jmx](https://github.com/aws-samples/logging-monitoring-apg-guide-examples/tree/main/examples/eks/prometheus_jmx)
+ [prometheus / jmx\_exporter](https://github.com/prometheus/jmx_exporter)
+ [Scraping additional Prometheus sources and importing those metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContainerInsights-Prometheus-Setup-configure.html)
+ [Self-managed nodes](https://docs.aws.amazon.com/eks/latest/userguide/worker.html)
+ [Send logs to CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Container-Insights-EKS-logs.html)
+ [Set up FluentD as a DaemonSet to send logs to CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Container-Insights-setup-logs.html)
+ [Set up Java/JMX sample workload on Amazon EKS and Kubernetes](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContainerInsights-Prometheus-Sample-Workloads-javajmx.html)
+ [Tutorial for adding a new Prometheus scrape target: Prometheus API Server metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContainerInsights-Prometheus-Setup-configure.html#ContainerInsights-Prometheus-Setup-new-exporters)
+ [Vertical Pod Autoscaler](https://docs.aws.amazon.com/eks/latest/userguide/vertical-pod-autoscaler.html)

## Logging and metrics for AWS Lambda
<a name="logging-and-metrics-for-aws-lambda.a1173d03-4ad7-5e98-91a1-c8a5d18da235"></a>
+ [Lambda invocation errors](https://docs.aws.amazon.com/lambda/latest/api/API_Invoke.html)
+ [logging – Logging facility for Python](https://docs.python.org/3/library/logging.html)
+ [Using the client libraries to generate embedded metric format logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Embedded_Metric_Format_Libraries.html)
+ [Working with Lambda function metrics](https://docs.aws.amazon.com/lambda/latest/dg/monitoring-metrics.html)

## Searching and analyzing logs in CloudWatch
<a name="searching-and-analyzing-logs-in-cloudwatch.604c43ec-11c2-5d3e-b238-1baf7e51dc2f"></a>
+ [The Beats family](https://www.elastic.co/beats)
+ [Elastic Logstash](https://www.elastic.co/logstash)
+ [Elastic Stack](https://www.elastic.co/elastic-stack?ultron=B-Stack-Trials-AMER-US-W-Exact&gambit=Elasticsearch-ELK&blade=adwords-s&hulk=cpc&Device=c&thor=elk%20elasticsearch%20logstash%20kibana&gclid=EAIaIQobChMI3raE5vWK8AIVTT6tBh2idgBbEAAYASAAEgKsoPD_BwE)
+ [Streaming CloudWatch Logs data to Amazon OpenSearch Service](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_OpenSearch_Stream.html)

## Alarming options with CloudWatch
<a name="alarming-options-with-cloudwatch.7ff64408-c445-5b8e-af49-3561a5e0bcbb"></a>
+ [amazon-cloudwatch-auto-alarms](https://github.com/aws-samples/amazon-cloudwatch-auto-alarms)
+ [AWS Service Management Connector for Jira Service Management Cloud](https://docs.aws.amazon.com/smc/latest/ag/integrations-jsmcloud.html)
+ [AWS Service Management Connector for Jira Service Management Data Center](https://docs.aws.amazon.com/smc/latest/ag/integrations-jiraservicedesk.html)
+ [AWS Service Management Connector for ServiceNow](https://docs.aws.amazon.com/smc/latest/ag/sn-what-is.html)

## Monitoring application and service availability
<a name="monitoring-application-and-service-availability.750e0ff0-225f-5c48-9a68-d78c63958098"></a>
+ [Configuring DNS failover](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-configuring.html)

## Tracing applications with AWS X-Ray
<a name="tracing-applications-with-aws-x-ray.e16796a2-e1b4-5062-8624-ec4d842cfcd7"></a>
+ [Amazon ECS task networking](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-networking.html)
+ [Configuring sampling rules in the X-Ray console](https://docs.aws.amazon.com/xray/latest/devguide/xray-console-sampling.html?icmpid=docs_xray_console)
+ [Run Windows PowerShell commands or scripts](https://docs.aws.amazon.com/systems-manager/latest/userguide/walkthrough-powershell.html#walkthrough-powershell-run-script)
+ [Running the X-Ray daemon on Amazon EC2](https://docs.aws.amazon.com/xray/latest/devguide/xray-daemon-ec2.html)
+ [Sending trace data to X-Ray](https://docs.aws.amazon.com/xray/latest/devguide/xray-api-sendingdata.html)
+ [Service graph in X-Ray](https://docs.aws.amazon.com/xray/latest/devguide/xray-concepts.html#xray-concepts-servicegraph)

## Dashboards and visualizations with CloudWatch
<a name="dashboards-and-visualizations-with-cloudwatch.3dd84956-e004-530f-8cd8-d387728fb0d9"></a>
+ [Amazon CloudWatch Metric Math simplifies near real-time monitoring of your Amazon EFS file systems](https://aws.amazon.com/blogs/mt/amazon-cloudwatch-metric-math-simplifies-near-real-time-monitoring-of-your-amazon-efs-file-systems-and-more/)
+ [Setting up CloudWatch Container Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/deploy-container-insights.html)
+ [Using metric math](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/using-metric-math.html)

## CloudWatch integration with AWS services
<a name="cloudwatch-integration-with-aws-services.f42d7696-3f54-5524-a110-19eab86dd69d"></a>
+ [AWS CloudTrail supported services and integrations](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.html)
+ [Events from AWS services in Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event.html)
+ [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html)
+ [Monitoring CloudTrail log files with CloudWatch Logs](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/monitor-cloudtrail-log-files-with-cloudwatch-logs.html)
+ [Publishing database logs to CloudWatch Logs](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_LogAccess.Procedural.UploadtoCloudWatch.html)
+ [Publishing flow logs to CloudWatch Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs-cwl.html)

## Amazon Managed Service for Grafana for dashboarding and visualization
<a name="amazon-managed-service-for-grafana-for-dashboarding-and-visualization.041fc404-0d75-56bb-ae65-b39fb823a24d"></a>
+ [Best practices for the management account in AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_best-practices_mgmt-acct.html)
+ [Built-in data sources for AMG](https://docs.aws.amazon.com/grafana/latest/userguide/AMG-data-sources-builtin.html)
+ [Cross-account and cross-Region dashboards in CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/create_xaxr_dashboard.html)
+ [Grafana plugins](https://grafana.com/grafana/plugins/)
