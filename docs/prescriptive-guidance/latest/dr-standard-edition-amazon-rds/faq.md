---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/dr-standard-edition-amazon-rds/faq.html
---

# FAQ
<a name="faq"></a>

Find answers to frequently raised questions about disaster recovery (DR) solutions for standard editions of Amazon RDS for Oracle and Amazon RDS for SQL Server.

## Do the DR solutions explained in this guide apply only to standard editions?
<a name="q1"></a>

The options given for standard editions can be used for enterprise editions as well if they meet your RTO and RPO requirements.

## After a primary site Multi-AZ failover, what will happen to the cross-Region automated backup replication?
<a name="q2"></a>

Cross-Region automated backup replication works fine after a Multi-AZ failover on the primary site. No manual intervention is needed.

## Does the native transaction logs solution work for Amazon RDS for Oracle as well?
<a name="q3"></a>

Amazon RDS for Oracle supports accessing the archived redo logs and copying to and from an S3 bucket, but RDS for Oracle can't perform manual recovery using these logs. So this solution applies only to Amazon RDS for SQL Server.

## What are the options for automating the failover process in a cross-Region DR setup with standard editions of Amazon RDS commercial DB engines?
<a name="q4"></a>

Automating the failover process often involves combining multiple AWS services, such as AWS Lambda, Amazon CloudWatch, Amazon EventBridge, and Amazon RDS APIs. You can use these services to initiate failover actions based on predefined criteria, and you can automate the process for minimal downtime.

## How can I achieve near real-time replication for cross-Region DR with standard editions of Amazon RDS commercial DB engines?
<a name="q5"></a>

Achieving near real-time replication requires careful consideration of factors such as network latency, workload complexity, and the chosen replication mechanism. Using services such as AWS DMS can help achieve this objective.

## Are there any architectural differences or restrictions when using third-party tools or services for cross-Region DR with standard editions of Amazon RDS commercial DB engines?
<a name="q6"></a>

Third-party tools or services might introduce specific architectural requirements or restrictions. It's crucial to review their documentation and ensure compatibility with standard editions of Amazon RDS commercial DB engines before implementation.

## What are the considerations for network connectivity when implementing cross-Region DR for standard editions of Amazon RDS commercial DB engines?
<a name="q7"></a>

Network connectivity between AWS Regions plays a critical role in cross-Region DR. To help ensure efficient and reliable data replication, it's important to evaluate network bandwidth, latency, and any limitations imposed by your network infrastructure.
