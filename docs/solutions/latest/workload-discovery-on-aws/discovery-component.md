---
source_url: https://docs.aws.amazon.com/solutions/latest/workload-discovery-on-aws/discovery-component.html
---

# Discovery component
<a name="discovery-component"></a>

The discovery component is the main data-gathering element of the Workload Discovery on AWS architecture. It is responsible for querying AWS Config and making * [describe](architecture-details.md#supported-resources) * API calls to maintain the inventory of resources and their relationships between one another.

 **Workload Discovery on AWS discovery component**

![workload discovery discovery component](http://docs.aws.amazon.com/solutions/latest/workload-discovery-on-aws/images/workload-discovery-discovery-component.png)

This solution configures Amazon ECS to run an AWS Fargate task using the container image downloaded from Amazon ECR. The AWS Fargate task is scheduled to run at 15-minute intervals. The resource relationship data that is collected is inserted into an Amazon Neptune graph database and Amazon OpenSearch Service.

The discovery component workflow consists of the following three steps:

1. Amazon ECS invokes an AWS Fargate task at 15-minute intervals.

1. The Fargate task gathers resource data from AWS Config, AWS API *describe* calls, and from the Amazon Neptune database.

1. The Fargate task calculates the difference between what is present in the Amazon Neptune database and what it has received from AWS Config and the *describe* calls.

1. The Fargate task sends requests to the AppSync API to persist the changes to resources and relationships discovered into Amazon Neptune and Amazon OpenSearch Service.
