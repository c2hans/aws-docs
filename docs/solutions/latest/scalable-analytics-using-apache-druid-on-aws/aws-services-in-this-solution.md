---
source_url: https://docs.aws.amazon.com/solutions/latest/scalable-analytics-using-apache-druid-on-aws/aws-services-in-this-solution.html
---

# AWS services in this guidance
<a name="aws-services-in-this-solution"></a>

| AWS service | Description |
| --- | --- |
|  [Amazon S3](https://aws.amazon.com/s3/)  |  **Core**.<br />The guidance provisions the following S3 buckets:<br />\* Deep storage bucket to store the segments.<br />\* Installation bucket to store the installation files as needed by the guidance.<br />\* Access logging bucket to store the access logs from ALB, and S3 buckets. |
|  [Amazon Elastic Compute Cloud](https://aws.amazon.com/ec2/)  |  **Core**. The guidance provisions EC2 instances to run Apache Druid and Apache ZooKeeper. |
|  [Amazon Aurora](https://aws.amazon.com/rds/aurora/)  |  **Core**. The guidance provisions an Aurora PostgreSQL cluster to serve as the metadata storage. |
|  [Amazon Elastic Load Balancer](https://aws.amazon.com/elasticloadbalancing/)  |  **Core**. Application load balancer to distribute the incoming traffic among the Druid query nodes. |
|  [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/)  |  **Core** Secrets to store master user credentials for Aurora DB cluster, and credentials of the users `admin` and `druid_system`. |
|  [AWS Key Management System](https://aws.amazon.com/kms/)  |  **Core** KMS keys used to encrypt the data in S3 buckets, Aurora cluster, SNS topic, and EFS. |
|  [Amazon Elastic Block Store](https://aws.amazon.com/ebs/)  |  **Core** EBS volumes to serve as segment cache for historical nodes. |
|  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)  |  **Supporting** The guidance uses CloudWatch for logs, metrics, alarms, and dashboard. |
|  [Amazon Simple Notification Service](https://aws.amazon.com/sns/)  |  **Supporting** Topics to receive CloudWatch alarm notifications and auto scaling group scaling event notifications. |
|  [AWS WAF](https://aws.amazon.com/waf/)  |  **Supporting** Protect Druid web console and API endpoints from common application-layer exploits that can affect availability or consume excessive resources. |
|  [AWS Systems Manager](https://aws.amazon.com/systems-manager/)  |  **Supporting** Provides application-level resource monitoring and visualization of resource operations and cost data. |
|  [Amazon EventBridge](https://aws.amazon.com/eventbridge/)  |  **Supporting** The guidance creates an EventBridge rule to receive the event from auto scaling group. |
|  [Amazon Elastic Kubernetes Service](https://aws.amazon.com/eks/)  |  **Optional** When opting for EKS deployment, the guidance initializes an EKS cluster to execute the Apache Druid workload. |
|  [Amazon Elastic File System](https://aws.amazon.com/efs/)  |  **Optional** When opting for EKS Fargate deployment, the guidance creates an EFS filesystem to provide storage to Fargate workloads. |
|  [Amazon Route 53](https://aws.amazon.com/route53/)  |  **Optional** The guidance provides the option for integration with Rout 53 to manage the domain for accessing the Druid cluster. |
