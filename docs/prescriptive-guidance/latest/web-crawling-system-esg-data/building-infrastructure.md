---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/web-crawling-system-esg-data/building-infrastructure.html
---

# Building the AWS infrastructure
<a name="building-infrastructure"></a>

There are many AWS services that you can use to build the web crawling infrastructure. The [Architecture](architecture.md) section of this guide includes one proposed solution. We recommend that you consider using the following AWS services to build the supporting infrastructure for your web crawler:
+ Use Amazon Virtual Private Cloud (Amazon VPC) to create the [VPC](https://docs.aws.amazon.com/vpc/latest/userguide/configure-your-vpc.html) and [subnets](https://docs.aws.amazon.com/vpc/latest/userguide/configure-subnets.html).
+ Initiate the crawling process by using [Amazon EventBridge Scheduler](https://docs.aws.amazon.com/eventbridge/latest/userguide/using-eventbridge-scheduler.html).
+ Manage the web crawler jobs by using AWS Batch [jobs](https://docs.aws.amazon.com/batch/latest/userguide/jobs.html) and [job queues](https://docs.aws.amazon.com/batch/latest/userguide/job_queues.html).
+ Use one of the following solutions to run the web crawler jobs:
  + Amazon Elastic Container Service (Amazon ECS) containers on [AWS Fargate](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html)
  + Amazon Elastic Compute Cloud (Amazon EC2) [instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Instances.html)
**Note**
If your application can handle disruptions, consider using Amazon EC2 [Spot Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances.html) through [Spot Fleet](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/work-with-spot-fleets.html). Fleets of Spot Instances can help you save significantly on compute costs.
  + AWS Lambda [functions](https://docs.aws.amazon.com/lambda/latest/dg/lambda-functions.html)
+ Store the retrieved data and raw files in an Amazon Simple Storage Service (Amazon S3) [bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-buckets-s3.html).
