---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/bare-metal-hardware-monitoring/best-practices.html
---

# Best practices
<a name="best-practices"></a>

Monitoring the health and performance of bare-metal hardware is critical, especially in multi-vendor environments where consistency can be a challenge. This section provides guidance for using the open source Telegraf agent and the industry-standard Redfish API to implement an effective and scalable hardware monitoring solution in the AWS Cloud. It explores key considerations, configuration steps, and best practices that help you get the most out of your hardware monitoring efforts on AWS.

**Topics in this section:**
+ [Standardized data collection](#best-practices-data)
+ [Scalability and high performance](#best-practices-performance)
+ [Authentication and authorization](#best-practices-access)
+ [Monitoring and alerting](#best-practices-alerting)

## Standardized data collection
<a name="best-practices-data"></a>

Standardized data collection is a crucial aspect of managing bare-metal hardware. Without standardization, it becomes difficult to compare, scale, and manage, and ensure the consistency of metrics. The following tools and AWS services can help you consistently and reliably ingest, store, and visualize data across your infrastructure:
+ [Telegraf](https://docs.influxdata.com/telegraf/v1/) is an open source agent for collecting and reporting metrics from various sources, including bare-metal hardware. It is designed to be lightweight and highly configurable, which makes it suitable for monitoring a wide range of system metrics, such as CPU, memory, disk, and network. For consistent data collection across your infrastructure, you can deploy Telegraf on each bare-metal server.
+ [Amazon Managed Service for Prometheus](https://docs.aws.amazon.com/prometheus/latest/userguide/what-is-Amazon-Managed-Service-Prometheus.html) is a serverless, Prometheus-compatible service that helps you securely monitor container environments at scale. It helps you run and manage Prometheus instances by handling tasks such as provisioning, scaling, and updating the service. This service provides reliable and scalable storage for the bare-metal hardware monitoring data that Telegraf collects.
+ [Amazon Managed Grafana](https://docs.aws.amazon.com/grafana/latest/userguide/what-is-Amazon-Managed-Service-Grafana.html) is a fully managed data visualization service that you can use to query, correlate, and visualize operational metrics, logs, and traces from multiple sources. [Grafana](https://grafana.com/docs/grafana/latest/) is an open source visualization tool that helps you create dashboards and visualizations for your monitoring data. Amazon Managed Grafana integrates seamlessly with Amazon Managed Service for Prometheus. You can use Amazon Managed Grafana to visualize and analyze the bare-metal hardware monitoring data that you store in Amazon Managed Service for Prometheus.

The following image shows a sample architecture. In an on-premises Amazon Elastic Kubernetes Service (Amazon EKS) Anywhere container, you deploy Telegraf to monitor the worker nodes and control plane nodes. Telegraf sends the monitoring data to Amazon Managed Service for Prometheus in the AWS Cloud. Amazon Managed Grafana retrieves the data from Amazon Managed Service for Prometheus. You can query, correlate, and visualize the data in Amazon Managed Grafana.

![Telegraf is deployed in an Amazon EKS Anywhere container and sends the data to the AWS Cloud.](http://docs.aws.amazon.com/prescriptive-guidance/latest/bare-metal-hardware-monitoring/images/guide-img/3b77512c-41d5-48a8-b53e-f2ea827bdbc5/images/91f47cd8-5540-4b45-b0c7-ddecf4f07ee0.png)

In Telegraf, you use a [configuration file](https://docs.influxdata.com/telegraf/v1/configuration/) to define what plugins to enable and what settings to use when Telegraf starts. Each plugin has different configuration options. The following is a sample Telegraf configuration file. The Telegraf agent sends the collected data to an Amazon Managed Service for Prometheus endpoint (`amp_remote_write_url`) in the target AWS Region (`region_name`):

```
telegraf.conf: |+
    [global_tags]
    [agent]
      interval = "60s"
      round_interval = true
      metric_batch_size = 1000
      metric_buffer_limit = 10000
      hostname = ""
      omit_hostname = true
    [[outputs.http]]
      url = "<amp_remote_write_url>"
      data_format = "prometheusremotewrite"
      region = "<region_name>"
      aws_service = "aps"
```

## Scalability and high performance
<a name="best-practices-performance"></a>

Scalability and high performance are crucial requirements for bare-metal hardware monitoring and management systems. As bare-metal infrastructures grow in size and complexity, the monitoring solution needs to handle the increasing volume and diversity of generated data. The solutions must support real-time monitoring, capacity planning, troubleshooting, and compliance reporting. Scalable and high-performance monitoring systems are essential to maintain visibility, responsiveness, and optimization.

We recommend the following best practices to help you scale and improve the performance of the Telegraf deployment:
+ **Cluster deployment** – Deploy Telegraf in a clustered configuration to distribute the load across multiple instances. This can improve scalability and performance by distributing the data collection and processing tasks across multiple nodes.
+ **Load balancing** – Use a load balancer or a service discovery mechanism to distribute the incoming Redfish API requests across multiple Telegraf instances. This can help balance the load and prevent any single instance from becoming a bottleneck.
+ **Parallel data collection** – If you have multiple Redfish-enabled systems to monitor, consider using the parallel data collection feature in Telegraf. Telegraf can collect data from multiple sources concurrently. This improves performance and reduces the overall data collection time.
+ **Vertical scaling** – Make sure that your Telegraf instances and the systems running them have sufficient compute resources (such as CPU, memory, and network bandwidth) to handle the anticipated load. Vertical scaling by increasing the resources of individual nodes can improve performance and scalability.
+ **Horizontal scaling** – If vertical scaling is not sufficient or cost-effective, consider horizontal scaling by adding more Telegraf instances or nodes to your cluster. This can distribute the load across a larger number of resources, which improves overall scalability.

The following is a sample YAML file that you can use during deployment. It deploys and configures Telegraf on Kubernetes. It creates a replica deployment across three nodes, which improves availability and scalability:

```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: telegraf-deployment
  namespace: monitoring
spec:
  replica: 3
  selector:
    matchLabels:
      app: telegraf
  minReadySeconds: 5
  template:
    metadata:
      labels:
        app: telegraf
    spec:
      containers:
        - image: telegraf:latest
          name: telegraf
```

## Authentication and authorization
<a name="best-practices-access"></a>

Robust authentication and authorization are critical requirements for bare-metal hardware monitoring and management systems. These controls restrict access to only authorized personnel. Authentication and authorization mechanisms helps you meet regulatory and compliance standards and help you maintain detailed logs for accountability and auditing purposes. You can integrate the authentication and authorization mechanisms with your organization's enterprise identity management system. This can enhance security, streamline user access, and make it easier to manage users and permissions.

We recommend the following security best practices:
+ **Authentication** – Consider the following when setting up access to the following tools and services:
  + **Redfish API** – Redfish supports various authentication methods, such as Basic Authentication, session-based authentication, and vendor-specific methods. Choose the appropriate method based on your security requirements and vendor recommendations.
  + **Telegraf** – Telegraf itself does not handle authentication. It relies on the authentication mechanisms provided by the data sources that it connects to, such as the Redfish API or other services.
  + **Amazon Managed Service for Prometheus and Amazon Managed Grafana** – Permissions to use AWS services is managed through [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) identities and policies. Follow the [security best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) for IAM.
+ **Credentials management** – Store credentials securely, such as in secure vaults or encrypted configuration files. Avoid hard-coding credentials in plaintext. Rotate credentials periodically to reduce the risk of credential exposure.
+ **Role-based access control (RBAC)** – Implement [RBAC](https://docs.aws.amazon.com/cognito/latest/developerguide/role-based-access-control.html) to restrict access to Redfish API resources and actions based on predefined roles and permissions. Define granular roles that follow the [principle of least privilege](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege), granting each role only the necessary permissions. Review and update roles and permissions regularly to align with changing requirements and personnel changes.
+ **Secure communication** – Use secure communication protocols, such as HTTPS, for all interactions with the Redfish API. Configure and maintain up-to-date TLS or SSL certificates for secure communication. Use HTTPS or encrypted connections to secure the communication between Telegraf and the monitoring or data storage services, such as [InfluxDB](https://www.influxdata.com/influxdb-cloud-on-aws/) or Amazon Managed Service for Prometheus.
+ **Security updates and patches** – Keep all components (such as Telegraf, Redfish-enabled systems, operating systems, and the monitoring infrastructure) up-to-date with the latest security patches and updates. Establish a regular patching and update process to promptly address known vulnerabilities.

## Monitoring and alerting
<a name="best-practices-alerting"></a>

Comprehensive monitoring and alerting capabilities are essential for effective bare-metal hardware management. These capabilities provide real-time visibility into infrastructure health. They also help you proactively detect anomalies, generate alerts, support accurate capacity planning, facilitate thorough troubleshooting, and comply with regulations. Effective monitoring and alerting are crucial for maintaining reliability, performance, and optimal utilization.

We recommend the following best practices when configuring monitoring and alerting in Amazon Managed Service for Prometheus:
+ **Alert notifications** – Set up alert rules in Amazon Managed Service for Prometheus to notify you if predefined conditions are met, such as high CPU or memory utilization, node failures, or critical hardware events. You can use [alert manager](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-alert-manager.html) to handle alert routing and notifications. Alert manager in Amazon Managed Service for Prometheus provides similar functionality to [Alertmanager](https://prometheus.io/docs/alerting/latest/alertmanager/) in Prometheus. You can configure alerts to be sent to a variety of notification channels, such as email, Slack, or PagerDuty.
+ **Persistent storage for metrics** – For long-term analysis and debugging, make sure that Prometheus has persistent storage configured to store historical metrics. For example, you can use [Amazon Elastic Block Store (Amazon EBS)](https://docs.aws.amazon.com/ebs/latest/userguide/what-is-ebs.html) volumes or [Amazon Elastic File System (Amazon EFS)](https://docs.aws.amazon.com/efs/latest/ug/whatisefs.html) file systems. Implement data retention policies and regular backups for persistent storage. This helps you manage storage consumption and protect against data loss.

  If you plan to run Prometheus on a single instance and require the highest possible performance, we recommend Amazon EBS. However, we recommend Amazon EFS if you anticipate scaling Prometheus horizontally across multiple instances or if you prioritize high availability, easier backup management, and simplified data sharing.
+ **Alert prioritization and thresholds** – Implement monitoring and alerting best practices, such as setting appropriate alert thresholds, avoiding alert fatigue, and prioritizing critical alerts. Regularly review and update monitoring and alerting configurations to align with changing requirements and infrastructure changes.

The following is a sample configuration for an alert rule in Amazon Managed Service for Prometheus:

```
groups:
- name:  Hardware Alerts
  rules:
    - alert: ServerOverAllHealth
      expr: 'OverallServerHealth == 0'
      for: 2m
      labels:
        severity: critical
      annotations:
        summary: Hardware health is not good (instance {{ $labels.hostname }})
        description: |
          **Alert Details:**
          - **Description:** Hardware overall health is not in the right status. Needs to be checked.
```
