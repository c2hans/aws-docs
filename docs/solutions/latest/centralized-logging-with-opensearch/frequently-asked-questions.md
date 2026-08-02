---
source_url: https://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/frequently-asked-questions.html
---

# Frequently asked questions
<a name="frequently-asked-questions"></a>

## General
<a name="general"></a>

 **Q: What is Centralized Logging with OpenSearch solution?**

Centralized Logging with OpenSearch is an AWS Solution that simplifies the building of log analytics pipelines. It provides to customers, as complementary of Amazon OpenSearch Service, capabilities to ingest and process both application logs and AWS service logs without writing code, and create visualization dashboards from templates. Centralized Logging with OpenSearch automatically assembles the underlying AWS services, and provides you with a web console to manage log analytics pipelines.

 **Q: What are the supported logs in this solution?**

Centralized Logging with OpenSearch supports both AWS service logs and EC2/EKS application logs. Refer to the [supported AWS services](supported-aws-services.md), and the [supported application log formats and sources](supported-log-formats-and-log-sources.md) for more details.

 **Q: Does Centralized Logging with OpenSearch support ingesting logs from multiple AWS accounts?**

Yes. Centralized Logging with OpenSearch supports ingesting AWS service logs and application logs from a different AWS account in the same Region. For more information, see [cross-account ingestion](cross-account-ingestion.md).

 **Q: Does Centralized Logging with OpenSearch support ingesting logs from multiple AWS Regions?**

Currently, Centralized Logging with OpenSearch does not automate the log ingestion from a different AWS Region. You must ingest logs from other Regions into pipelines provisioned by Centralized Logging with OpenSearch. For AWS services that store the logs in S3 bucket, you can use the [S3 Cross-Region Replication](https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication.html) to copy the logs to the Centralized Logging with OpenSearch deployed Region, and import incremental logs using the [manual mode](access-proxy-1.md#option-1using-the-centralized-logging-with-opensearch-console) by specifying the log location in the S3 bucket. For application logs on EC2 and EKS, you must set up the networking (for example, Kinesis VPC endpoint, VPC Peering), install agents, and configure the agents to ingest logs to Centralized Logging with OpenSearch pipelines.

 **Q: What is the license of this solution?**

This solution is provided under the [Apache-2.0 license](https://www.apache.org/licenses/LICENSE-2.0). It is a permissive free software license written by the Apache Software Foundation. It allows users to use the software for any purpose, to distribute it, to modify it, and to distribute modified versions of the software under the terms of the license, without concern for royalties.

 **Q: How can I find the roadmap of this solution?**

This solution uses a GitHub project to manage the roadmap. You can find the roadmap [here](https://github.com/orgs/aws-solutions/projects/17).

 **Q: How can I submit a feature request or bug report?** You can submit feature requests and bug reports through the GitHub issues. Here are the templates for [feature request](https://github.com/aws-solutions/centralized-logging-with-opensearch/issues/new?assignees=&labels=feature-request%2Cneeds-triage&template=feature-request.yml&title=%28module+name%29%3A+%28short+issue+description%29), [bug report](https://github.com/aws-solutions/centralized-logging-with-opensearch/issues/new?assignees=&labels=bug%2Cneeds-triage&template=bug-report.yml&title=%28module+name%29%3A+%28short+issue+description%29).

## Setup and configuration
<a name="setup-and-configuration"></a>

 **Q: Can I deploy Centralized Logging with OpenSearch on AWS in any AWS Region?**

Centralized Logging with OpenSearch provides two deployment options: option 1 with Amazon Cognito User Pool, and option 2 with OpenID Connect. For option 1, customers can deploy the solution in AWS Regions where Amazon Cognito User Pool, AWS AppSync, Amazon Data Firehose (optional) are available. For option 2, customers can deploy the solution in AWS Regions where AWS AppSync, Amazon Data Firehose (optional) are available. Refer to [supported Regions for deployment](plan-your-deployment.md#supported-aws-regions) for more information.

 **Q: What are the prerequisites of deploying this solution?**

Centralized Logging with OpenSearch does not provision Amazon OpenSearch Service clusters, and you must import existing OpenSearch clusters through the web console. The clusters must meet the requirements specified in the [prerequisites](launch-with-openid-connect-oidc.md#prerequisites).

 **Q: Why do I need a domain name with ICP recordal when deploying the solution in AWS China Regions?**

The Centralized Logging with OpenSearch console is served via the CloudFront distribution, which is considered as an internet information service. According to the local regulations, any internet information service must bind to a domain name with [ICP recordal](https://www.amazonaws.cn/en/support/icp/?nc2=h_l2_su).

 **Q: What versions of OpenSearch does the solution work with?**

Centralized Logging with OpenSearch supports Amazon OpenSearch Service, with OpenSearch 1.3 or later.

 **Q: What is the index name rules for OpenSearch created by the Log Analytics Pipeline?**

You can change the index name if needed when using the Centralized Logging with OpenSearch console to create a log analytics pipeline.

If the log analytics pipeline is created for service logs, the index name is composed of <Index Prefix>-<service-type>-<Index Suffix>-<00000x>, where you can define a name for Index Prefix and service-type is automatically generated by the solution according to the service type you have chosen. Moreover, you can choose different index suffix types to adjust the index rollover time window.
+ YYYY-MM-DD-HH: Amazon OpenSearch Service will roll the index by the hour.
+ YYYY-MM-DD: Amazon OpenSearch Service will roll the index by 24 hours.
+ YYYY-MM: Amazon OpenSearch Service will roll the index by 30 days.
+ YYYY: Amazon OpenSearch Service will roll the index by 365 days.

It should be noted that in OpenSearch, the time is in the UTC 0 time zone.

Regarding the 00000x part, Amazon OpenSearch Service will automatically append a 6-digit suffix to the index name, where the first index rule is 000001, rollover according to the index, and increment backwards, such as 000002, 000003.

If the log analytics pipeline is created for application log, the index name is composed of <Index Prefix>-<Index Suffix>-<00000x>. The rules for index prefix and index suffix, 00000x are the same as those for service logs.

 **Q: What is the index rollover rules for OpenSearch created by the Log Analytics Pipeline?**

Index rollover is determined by two factors. One is the Index Suffix in the index name. If you enable the index rollover by capacity, Amazon OpenSearch Service will roll your index when the index capacity equals or exceeds the specified size, regardless of the rollover time window. Note that if one of these two factors matches, index rollover can be triggered.

For example, we created an application log pipeline on January 1, 2023, deleted the application log pipeline at 9:00 on January 4, 2023, and the index name is nginx-YYYY-MM-DD-<00000x>. At the same time, we enabled the index rollover by capacity and entered 300GB. If the log data volume increases suddenly after creation, it can reach 300GB every hour, and the duration is 2 hours and 10 minutes. After that, it returns to normal, and the daily data volume is 90GB. Then OpenSearch creates three indexes on January 1, the index names are nginx-2023-01-01-000001, nginx-2023-01-01-000002, nginx-2023-01-01-000003, and then creates one every day Indexes respectively: nginx-2023-01-02-000004, nginx-2023-01-03-000005, nginx-2023-01-04-000006.

 **Q: Can I deploy the solution in an existing VPC?**

Yes. You can either launch the solution with a new VPC or launch the solution with an existing VPC. When using an existing VPC, you must select the VPC and the corresponding subnets. Refer to [launch with Amazon Cognito User Pool](launch-with-amazon-cognito-user-pool.md) or [launch with OpenID Connect](launch-with-openid-connect-oidc.md) for more details.

 **Q: How can I change the default CIDR of the solution?**

To change the default CIDR of the solution, you must first create a custom CIDR VPC and then deploy CLO using the 'Existing VPC' template.

You may use the following AWS CloudFormation templates to do so. First, deploy this [CloudFormation template](https://github.com/aws-solutions/centralized-logging-with-opensearch/files/13974602/3-layer-subnets.template.json) and when prompted, enter the CIDR prefix you want for your VPC. After the CloudFormation stack has finished deploying, continue with the deployment of the CLO solution using the [Launch with an existing VPC](https://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/launch-with-amazon-cognito-user-pool.html#step-1.-launch-the-stack) option.

 **Q: I did not receive the email containing the temporary password when launching the solution with Amazon Cognito User Pool. How can I resend the password?**

Your account is managed by the Amazon Cognito User Pool. To resend the temporary password, you can find the user pool created by the solution, and delete and recreate the user using the same email address. If you still have the same issue, try with another email address.

 **Q: How can I create more users for this solution?**

If you launched the solution with Amazon Cognito User Pool, go to the AWS Management Console, find the user pool created by the solution, and you can create more users. If you launched the solution with OpenID Connect (OIDC), you should add more users in the user pool managed by the OIDC provider. Note that all users have the same permissions.

## Pricing
<a name="pricing"></a>

 **Q: How will I be charged and billed for the use of this solution?**

You are responsible for the cost of AWS services used while running this solution. You pay only for what you use, and there are no minimum or setup fees. Refer to the Centralized Logging with OpenSearch [Cost](cost.md) section for detailed cost estimation.

 **Q: Will there be additional costs for cross-account ingestion?**

No. The cost will be the same as ingesting logs within the same AWS account.

## Log Ingestion
<a name="log-ingestion"></a>

 **Q: What is the log agent used in the Centralized Logging with OpenSearch solution?** Centralized Logging with OpenSearch uses [AWS for Fluent Bit](https://github.com/aws/aws-for-fluent-bit), a distribution of [Fluent Bit](https://fluentbit.io/) maintained by AWS. The solution uses this distribution to ingest logs from Amazon EC2 and Amazon EKS.

 **Q: I have already stored the AWS service logs of member accounts in a centralized logging account. How should I create service log ingestion for member accounts?**

In this case, you must deploy the Centralized Logging with OpenSearch solution in the centralized logging account, and ingest AWS service logs using the *Manual* mode from the logging account. Refer to this [guide](application-load-balancer-application-load-balancer-logs.md) for ingesting Application Load Balancer logs with *Manual* mode. You can do the same with other supported AWS services that output logs to Amazon S3.

 **Q: Why are there some duplicated records in OpenSearch when ingesting logs via Kinesis Data Streams?**

This is usually because there is no enough Kinesis Shards to handle the incoming requests. When a threshold error occurs in Kinesis, the Fluent Bit agent will [retry](https://docs.fluentbit.io/manual/administration/scheduling-and-retries) that [chunk](https://docs.fluentbit.io/manual/administration/buffering-and-storage). To avoid this issue, you must estimate your log throughput, and set a proper Kinesis shard number. Refer to the [Kinesis Data Streams quotas and limits](https://docs.aws.amazon.com/streams/latest/dev/service-sizes-and-limits.html). Centralized Logging with OpenSearch provides a built-in feature to scale-out and scale-in the Kinesis shards, and it would take a couple of minutes to scale out to the desired number.

 **Q: How to install a log agent on CentOS 7?**

Refer to [Create Instance Group for CentOS 7](additional-resources.md#create-instance-group-for-centos-7).

## Log Visualization
<a name="log-visualization"></a>

 **Q: How can I find the built-in dashboards in OpenSearch?**

Refer to the [AWS Service Logs](aws-service-logs.md) and [Application Logs](application-logs.md) to find out if there is a built-in dashboard supported. You also must turn on the *Sample Dashboard* option when creating a log analytics pipeline. The dashboard will be inserted into the Amazon OpenSearch Service under **Global Tenant**. You can switch to the Global Tenant from the top right coder of the OpenSearch Dashboards.
