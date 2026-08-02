---
source_url: https://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/quotas.html
---

# Service quotas
<a name="quotas"></a>

Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account.

## Request a service quota increase based on anticipated usage
<a name="request-a-service-increase"></a>

DeepRacer on AWS uses a combination of Amazon SageMaker AI training jobs and AWS Lambda functions for servicing compute-related tasks, including but not limited to creating, training, and evaluating models. AWS Lambda functions are also used for servicing general requests, such as creating a new account, making changes to account settings, and running/participating in races.

Considering your anticipated usage in advance and right-sizing your service quotas can improve user experience by reducing the amount of time it takes for training and evaluation jobs to be run. If your deployment is expected to serve consistently high demand (i.e. large number of users) or is subject to burst traffic (i.e. used for events, classes, workshops etc.), training and evaluation jobs will be constrained by the service quota that is in place, and those jobs will remain in the queue until capacity is available to run them.

**Note**
If you are operating or plan to operate multiple deployments of DeepRacer on AWS in the same account or same region (within the same account), it is important to consider the total anticipated usage across all deployments when evaluating the amount to increase the service quota by.

**Note**
For some services, smaller increases are automatically approved, while larger requests are submitted to AWS Support. AWS Support can approve, deny, or partially approve your requests. Larger increase requests take more time to process.

### Amazon SageMaker AI training jobs
<a name="amazon-sagemaker-ai-training-jobs"></a>

Amazon SageMaker AI training jobs are responsible for running training and evaluation jobs, and also support community and live races. At the time of writing, the default applied account-level quota value is 8. This means that DeepRacer on AWS can dispatch up to 8 training jobs, evaluation jobs, or race submissions (i.e. evaluating one model in a given race) at a time. If demand exceeds this limit at any point, jobs will remain queued until an actively-running job is completed and capacity becomes available. The queue for jobs in DeepRacer on AWS is managed in FIFO (first-in-first-out) order, and the amount of time that a job spends in the queue depends on the number of jobs that can be processed currently (i.e. the service quota), and the number of jobs that have entered the queue ahead of it.

As a result, it is recommended to consider in advance the number of jobs that may need to be run concurrently at any given point in time in order to deliver preferable throughput. If you decide that you would like to request a service quota increase, you may do so by:

1. Accessing the **AWS Management Console**

1. Searching for and selecting **Service Quotas** from the search bar at the top

1. Selecting **Amazon SageMaker** from the list of services

1. Searching for and selecting **ml.c7i.4xlarge for training job usage** in the Service quotas table, and clicking **Request increase at account level**

1. Enter the number of jobs that you would like to be able to service concurrently into the **Increase quota value** box, and, if applicable, review it against the value provided for **Utilization**. If you are working with a new deployment, this value will most likely appear as 0.

1. When you are ready to submit the request, click **Request**.

#### SageMaker managed warm pools (live race events)
<a name="sagemaker-managed-warm-pools-live-race-events"></a>

If you plan to host live race events and want to reduce per-evaluation startup latency, requesting an increase for the SageMaker managed warm pool quota is recommended. The default quota is 0, meaning every evaluation incurs a cold start without an increase. If you decide that you would like to request a service quota increase, you may do so by:

1. Accessing the **AWS Management Console**

1. Searching for and selecting **Service Quotas** from the search bar at the top

1. Selecting **Amazon SageMaker** from the list of services

1. Searching for and selecting **ml.c7i.4xlarge for training warm pool usage** in the Service quotas table, and clicking **Request increase at account level**

1. Enter the desired warm pool capacity into the **Increase quota value** box. For most live race events, a value of 1–2 is sufficient.

1. When you are ready to submit the request, click **Request**.

**Note**
Warm pool instances remain allocated for up to 1 hour after the last evaluation completes. If another evaluation starts within that window, the warm pool is reused and the timer resets. Standard SageMaker instance pricing applies while the warm pool is active.

### AWS Lambda functions
<a name="aws-lambda-functions-2"></a>

AWS Lambda functions are the primary compute resource used for servicing requests in DeepRacer on AWS, including dispatching and monitoring training and evaluation jobs. Similar to that of the Amazon SageMaker AI training jobs noted in the previous section, AWS Lambda functions have an applied account-level quota of 1,000 concurrent executions. This represents the maximum number of events that functions can process simultaneously in the current region. In the event that this limit is reached, requests will be queued and serviced once capacity becomes available.

If you anticipate needing to be able to service more than 1,000 requests concurrently, requesting a service quota increase for the number of requests that you would like to be able to handle at any given point is recommended. This will allow requests to be serviced as soon as they are received, or with minimal wait time in the queue. If you decide that you would like to request a service quota increase, you may do so by:

1. Accessing the **AWS Management Console**

1. Searching for and selecting **Service Quotas** from the search bar at the top

1. Selecting **AWS Lambda** from the list of services

1. Searching for and selecting **Concurrent executions** in the Service quotas table, and clicking **Request increase at account level**

1. Enter the number of requests that you would like to be able to service concurrently into the **Increase quota value** box, and, if applicable, review it against the value provided for **Utilization**. If you are working with a new deployment, this value will most likely appear as 0.

1. When you are ready to submit the request, click **Request**.

### Amazon Virtual Private Cloud (VPC)
<a name="amazon-virtual-private-cloud-vpc"></a>

DeepRacer on AWS configures one Amazon Virtual Private Cloud (VPC) per deployment to provide network isolation for functions that handle imported models and other user-supplied artifacts. At the time of writing, the default account-level quota is 5 VPCs per region. If you plan to host more than 5 deployments of DeepRacer on AWS in a single region, requesting a service quota increase for at least the number of deployments you expect to host is recommended.

1. Accessing the **AWS Management Console**

1. Searching for and selecting **Service Quotas** from the search bar at the top

1. Selecting **Amazon Virtual Private Cloud (VPC)** from the list of services

1. Searching for and selecting **VPCs per Region** in the Service quotas table, and clicking **Request increase at account level**

1. Enter the number of VPCs that you would like to be able to deploy into the **Increase quota value** box, and, if applicable, review it against the value provided for **Utilization**. If you are working with a new deployment, this value will most likely appear as 0.

1. When you are ready to submit the request, click **Request**.

## Quotas for AWS services in this solution
<a name="quotas-for-aws-services-in-this-solution"></a>

Make sure you have sufficient quota for each of the [services implemented in this solution](architecture-overview.md#aws-services-in-this-solution). For more information, see [AWS service quotas](https://docs.aws.amazon.com/general/latest/gr/aws-service-limits.html).

Use the following links to go to the page for that service. To view the service quotas for all AWS services in the documentation without switching pages, view the information in the [Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/aws-general.pdf) page in the PDF instead.

| AWS Service | Documentation Link |
| --- | --- |
| AWS Lambda |  [AWS Lambda service quotas](https://docs.aws.amazon.com/general/latest/gr/lambda-service.html)  |
| Amazon S3 |  [Amazon S3 service quotas](https://docs.aws.amazon.com/general/latest/gr/s3.html)  |
| Amazon SageMaker |  [Amazon SageMaker service quotas](https://docs.aws.amazon.com/general/latest/gr/sagemaker.html)  |
| Amazon DynamoDB |  [Amazon DynamoDB service quotas](https://docs.aws.amazon.com/general/latest/gr/ddb.html)  |
| Amazon API Gateway |  [Amazon API Gateway service quotas](https://docs.aws.amazon.com/general/latest/gr/apigateway.html)  |
| Amazon CloudFront |  [Amazon CloudFront service quotas](https://docs.aws.amazon.com/general/latest/gr/cloudfront.html)  |
| Amazon Cognito |  [Amazon Cognito service quotas](https://docs.aws.amazon.com/general/latest/gr/cognito_identity.html)  |
| AWS Step Functions |  [AWS Step Functions service quotas](https://docs.aws.amazon.com/general/latest/gr/step-functions.html)  |
| Amazon SQS |  [Amazon SQS service quotas](https://docs.aws.amazon.com/general/latest/gr/sqs-service.html)  |
| Amazon Kinesis Video Streams |  [Amazon Kinesis Video Streams service quotas](https://docs.aws.amazon.com/general/latest/gr/kinesisvideo.html)  |

## Service quota increase guidance by event size
<a name="quota-increase-by-event-size"></a>

The following guide is intended to help you right-size your service quotas in advance of deploying the solution or hosting a first event. The default account-level quota for Amazon SageMaker AI training jobs that use `ml.c7i.4xlarge` instance types is `0`. Depending on your activity and service usage, a service quota increase may be required before deploying the solution or hosting an event.

**Note**
It is important to plan ahead when considering a service quota increase request. Depending on the size of the increase, requests may either be approved automatically or referred to AWS Support for review. If the request is referred for review, additional processing time should be expected.

### Per-user compute assumptions
<a name="per-user-compute-assumptions"></a>

The recommendations in this section are based on hosting an event with the following characteristics:
+ Each user creates and trains one model
+ Each user evaluates that model one time
+ Each user submits their trained model to a community race

These characteristics result in the following per-user assumptions:
+ Training hours per user = (1 model/user) \* (1.5 hrs/training) = 1.5 hours
+ Evaluation hours per user = (1 model) \* (1 evaluation/model) \* (20 mins/evaluation) = 0.33 hours
+ Submission hours per user = (1 submission) \* (20 mins/submission) = 0.33 hours
+ Total per user = (training hours) \+ (evaluation hours) \+ (submission hours) = 2.17 hours/month

### Example 1 (100 users)
<a name="example-1-100-users"></a>

You are planning a deployment of DeepRacer on AWS that will serve 100 users. Based on the per-user compute assumptions above, this deployment will require approximately 217 compute hours per month. The estimated monthly cost for Amazon SageMaker AI training job usage will be (217 hrs × $0.714/hr) \+ $1.40 ≈ $156. This cost only accounts for Amazon SageMaker AI training job usage, and does not include other fixed and variable costs, which can be found in the [Cost](cost.md) section of this guide.

 **Recommended quotas**

| Resource | Default Quota | Recommended Quota | Rationale |
| --- | --- | --- | --- |
| SageMaker `ml.c7i.4xlarge` training jobs | 0 | 20–25 | Supports concurrent training for a small event with moderate wait times |
| Lambda concurrent executions | 1,000 | No change | Default quota is sufficient for 100 users |
| VPCs per region | 5 | No change | Single deployment requires only 1 VPC |

 **Queue times**

If all 100 users submit jobs simultaneously, queue times depend on the job type:
+  **Training jobs (90 min each):** 100 jobs across 25 slots are processed in 4 batches. All jobs complete after approximately 6 hours.
+  **Evaluations and race submissions (20 min each):** 100 jobs across 25 slots are processed in 4 batches. All jobs complete after approximately 80 minutes.

If jobs arrive gradually (approximately one per minute), training jobs still queue because the slot count (25) is less than the job duration (90 min). The last training job may wait up to 65 minutes. Evaluations and race submissions (20 min each) do not queue under gradual arrival because the slot count exceeds the job duration.

**Note**
For an event of this size, consider requesting your quota increase 1–2 weeks in advance.

### Example 2 (1,000 users)
<a name="example-2-1000-users"></a>

You are planning a deployment of DeepRacer on AWS that will serve 1,000 users. Based on the per-user compute assumptions above, this deployment will require approximately 2,167 compute hours per month. The estimated monthly cost for Amazon SageMaker AI training job usage will be (2,167 hrs × $0.714/hr) \+ $1.40 ≈ $1,548. This cost only accounts for Amazon SageMaker AI training job usage, and does not include other fixed and variable costs, which can be found in the [Cost](cost.md) section of this guide.

 **Recommended quotas**

| Resource | Default Quota | Recommended Quota | Rationale |
| --- | --- | --- | --- |
| SageMaker `ml.c7i.4xlarge` training jobs | 0 | 100–150 | Supports concurrent training for a medium-scale event |
| Lambda concurrent executions | 1,000 | 3,000–5,000 | Higher concurrency needed for API and job orchestration at scale |
| VPCs per region | 5 | No change | Single deployment requires only 1 VPC |

 **Queue times**

If all 1,000 users submit jobs simultaneously, queue times depend on the job type:
+  **Training jobs (90 min each):** 1,000 jobs across 150 slots are processed in 7 batches. All jobs complete after approximately 10.5 hours.
+  **Evaluations and race submissions (20 min each):** 1,000 jobs across 150 slots are processed in 7 batches. All jobs complete after approximately 2.3 hours.

If jobs arrive gradually (approximately one per minute), neither job type experiences queuing. Peak concurrency never exceeds 90 concurrent jobs, well within the 150-slot quota.

 **Additional considerations**
+  **DynamoDB consumed capacity** — Verify that on-demand capacity can handle the read/write throughput from 1,000 concurrent users.
+  **SQS FIFO throughput** — The default limit is 300 messages/sec. Monitor queue depth and consider requesting an increase if jobs accumulate.
+  **Kinesis Video Streams** — Monitor concurrent stream limits if video-based evaluation is enabled.

**Note**
Consider requesting your quota increase 2–3 weeks in advance. Increases of 100\+ instances may require AWS Support review.

### Example 3 (10,000 users)
<a name="example-3-10000-users"></a>

You are planning a deployment of DeepRacer on AWS that will serve 10,000 users. Based on the per-user compute assumptions above, this deployment will require approximately 21,667 compute hours per month. The estimated monthly cost for Amazon SageMaker AI training job usage will be (21,667 hrs × $0.714/hr) \+ $1.40 ≈ $15,472. This cost only accounts for Amazon SageMaker AI training job usage, and does not include other fixed and variable costs, which can be found in the [Cost](cost.md) section of this guide.

 **Recommended quotas**

| Resource | Default Quota | Recommended Quota | Rationale |
| --- | --- | --- | --- |
| SageMaker `ml.c7i.4xlarge` training jobs | 0 | 500–1,000 | Supports concurrent training for a large-scale event |
| Lambda concurrent executions | 1,000 | 10,000–20,000 | Required to handle API, orchestration, and monitoring at scale |
| VPCs per region | 5 | No change | Single deployment requires only 1 VPC |
| API Gateway throttling | 10,000 req/sec | Review and increase if needed | At 10,000 users, burst API traffic may exceed the default throttle limit |

 **Queue times**

If all 10,000 users submit jobs simultaneously, queue times depend on the job type:
+  **Training jobs (90 min each):** 10,000 jobs across 1,000 slots are processed in 10 batches. All jobs complete after approximately 15 hours.
+  **Evaluations and race submissions (20 min each):** 10,000 jobs across 1,000 slots are processed in 10 batches. All jobs complete after approximately 3.3 hours.

If jobs arrive gradually (approximately one per minute), neither job type experiences queuing. Peak concurrency never exceeds 90 concurrent jobs, well within the 1,000-slot quota. At this scale, the constraint shifts from slot availability to the total calendar time needed for all users to complete their work.

 **Additional considerations**
+  **DynamoDB capacity** — Monitor closely and consider switching to provisioned capacity with auto-scaling to manage costs and ensure consistent throughput.
+  **Kinesis Video Streams** — Review concurrent stream limits and request increases as needed.

**Note**
Consider requesting your quota increase 3–4 weeks in advance. Increases of 500\+ instances may require manual approval and capacity verification by AWS Support.

### Additional considerations for live race events
<a name="additional-considerations-for-live-race-events"></a>

Live races introduce real-time streaming and WebSocket connections on top of the standard SageMaker evaluation workload. The following guidance applies when you are planning a live race event in addition to, or instead of, standard model training and evaluation.

 **Concurrent viewers (AWS IoT Core WebSocket connections)**

Each user watching a live race holds one persistent WebSocket connection to AWS IoT Core. AWS IoT Core has a default account-level quota of 500,000 concurrent connections, which is unlikely to be a constraint for typical event sizes. However, if your deployment is in a region where a lower limit applies, verify the quota in the [AWS IoT Core service quotas](https://docs.aws.amazon.com/general/latest/gr/iot-core.html) page.

 **Video stream (Amazon Kinesis Video Streams)**

The live race video stream is delivered via Amazon Kinesis Video Streams as an HLS stream. Each live race uses one active stream. The number of concurrent viewers that a single stream can support is governed by the fragment-metadata and fragment-media quotas, which are soft limits that can be increased via a support request. Review the [Fragment-metadata and fragment-media quotas](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/limits.html#fragment_based_throttling) to understand the limits and worked examples for your stream configuration before hosting a large event.

 **SageMaker evaluation slots for live races**

Live race model evaluations use the same SageMaker `ml.c7i.4xlarge` instance quota as training and community race submissions. However, live races run evaluations sequentially (one at a time), so only one SageMaker slot is consumed at any given moment during a live race. The queue size is not constrained by a separate service quota — it is bounded by the number of submitted models.

For planning purposes, assume approximately 20 minutes per model evaluation. A live race with 30 participants will take roughly 10 hours to complete if run sequentially without pauses.

 **Recommended pre-event checklist**
+ Verify IoT Core concurrent connection quota (especially in opt-in regions).
+ Verify Kinesis Video Streams quota if running more than one simultaneous live race.
+ Confirm your SageMaker training job quota is sufficient to handle any concurrent training and community race activity alongside the live race.
+ Open the submission period well before the event to allow participants to queue models in advance, then close submissions once the event begins.

### How to request a quota increase
<a name="how-to-request-a-quota-increase"></a>

To request a service quota increase for SageMaker training instances, you may do so by:

1. Accessing the **AWS Management Console**

1. Searching for and selecting **Service Quotas** from the search bar at the top

1. Selecting **Amazon SageMaker** from the list of services

1. Searching for and selecting **ml.c7i.4xlarge for training job usage** in the Service quotas table, and clicking **Request increase at account level**

1. Enter the desired concurrent instance count into the **Increase quota value** box, and, if applicable, review it against the value provided for **Utilization**.

1. When you are ready to submit the request, click **Request**.
