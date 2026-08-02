---
source_url: https://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/cost.html
---

# Cost
<a name="cost"></a>

You are responsible for the cost of AWS services that are used while operating this solution. As of this revision, the monthly cost of operating this solution for a small group of 25 users with limited model training and evaluation demand is about $7.78 per user (or $194.37 total).

**Note**
The cost of operating DeepRacer on AWS depends on how you choose to use the solution. The following examples provide cost breakdown for single instance and multiple instances deployment configurations in the US East (N. Virginia) Region. AWS services listed in the example tables below are billed on a monthly basis.

The cost of operating the solution is dependent on the number of users registered to the system, the number of models they train, the number of evaluations they run, and the number of race submissions they perform. The cost of the solution is also dependent on the amount of time each model is trained for and the underlying instance type that is used for these jobs. The solution is configured to use an instance of type `ml.c7i.4xlarge` by default. However, you may choose to change this based on your desired performance profile by updating the appropriate field in the solution’s CloudFormation template or CDK project and deploying that configuration.

Operating cost is figured and expressed on a monthly basis. The estimates provided in this section are only accurate for use cases in which all training jobs, evaluations, and submissions occur within the same month. This is an important consideration to account for when planning usage over the course of a quarter, semester, or other longer timeframe.

We recommend creating a [budget](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-create.html) through [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/) to help manage costs. Prices are subject to change. For full details, refer to the pricing webpage for each AWS service used in this solution.

## Compute usage formula
<a name="compute-usage-formula"></a>

The training job compute usage for the examples in this section is figured using the following formula:
+ Training hours per month = (25 users) \* (3 models/user) \* (1.5 hrs/training) = 112.5 hours
+ Evaluation hours per month = [(25 users) \* (3 models/user) \* (3 evaluations/model)] \* (20 mins/evaluation) = 75 hours
+ Submission hours per month = [(25 users) \* (3 submissions/user)] \* (20 mins/submission) = 25 hours
+ Total hours = (training hours) \+ (evaluation hours) \+ (submission hours) = 212.5 hours

Total SageMaker cost = [(212.5 hours) \* ($0.714/instance hour)] \+ ($1.40 storage cost) = $174.80

## Training and evaluation cost examples
<a name="training-and-evaluation-cost-examples"></a>

### Example 1 (25 users)
<a name="example-1-25-users"></a>

You are planning a deployment of DeepRacer on AWS that will serve 25 users, with each user creating and training 3 models. Each user will then evaluate each of their models 3 times, before submitting them to a race. With a training time of 90 minutes, the cost will be $172.69, or $6.91 per user.

 **Cost summary**

| AWS service | Dimensions | Cost per month (USD) |
| --- | --- | --- |
| Amazon SageMaker | [(212.5 hours) \* ($0.714/instance hour)] \+ ($1.40 storage cost) | $153.13 |
| AWS WAF | 1 Web ACL | $5.00 |
| Amazon S3 | (0.33GB average model size) \* (75 models) \* ($0.023/GB) | $0.57 |
| Other services | AWS Lambda, Amazon DynamoDB, Amazon CloudWatch, AWS CodeBuild, Amazon ECR | $14.00 |
|  **Monthly total**  |  **$6.91/user**  |  **$172.69**  |

### Example 2 (100 users)
<a name="example-2-100-users"></a>

You are planning a deployment of DeepRacer on AWS that will serve 100 users, with each user creating and training 3 models. Each user will then evaluate each of their models 3 times, before submitting them to a race. With a training time of 90 minutes, the cost will be $629.58, or $6.30 per user.

 **Cost summary**

| AWS service | Dimensions | Cost per month (USD) |
| --- | --- | --- |
| Amazon SageMaker | [(850 hours) \* ($0.714/instance hour)] \+ ($1.40 storage cost) | $608.30 |
| AWS WAF | 1 Web ACL | $5.00 |
| Amazon S3 | (0.33GB average model size) \* (300 models) \* ($0.023/GB) | $2.28 |
| Other services | AWS Lambda, Amazon DynamoDB, Amazon CloudWatch, AWS CodeBuild, Amazon ECR | $14.00 |
|  **Monthly total**  |  **$6.30/user**  |  **$629.58**  |

### Example 3 (250 users)
<a name="example-3-250-users"></a>

You are planning a deployment of DeepRacer on AWS that will serve 250 users, with each user creating and training 3 models. Each user will then evaluate each of their models 3 times, before submitting them to a race. With a training time of 90 minutes, the cost will be $1,543.34, or $6.17 per user.

 **Cost summary**

| AWS service | Dimensions | Cost per month (USD) |
| --- | --- | --- |
| Amazon SageMaker | [(2,125 hours) \* ($0.714/instance hour)] \+ ($1.40 storage cost) | $1,518.65 |
| AWS WAF | 1 Web ACL | $5.00 |
| Amazon S3 | (0.33GB average model size) \* (750 models) \* ($0.023/GB) | $5.69 |
| Other services | AWS Lambda, Amazon DynamoDB, Amazon CloudWatch, AWS CodeBuild, Amazon ECR | $14.00 |
|  **Monthly total**  |  **$6.17/user**  |  **$1,543.34**  |

## Live racing cost examples
<a name="live-racing-cost-examples"></a>

Live racing has no fixed monthly charge; cost is incurred only while a race is active. The following examples assume 5 laps per evaluation, \~7 minutes for the first evaluation (including instance warmup), and \~4 minutes per subsequent evaluation.

| Participants | Race duration | Cost per race (USD) |
| --- | --- | --- |
| 25 | \~103 minutes | $0.87 |
| 100 | \~403 minutes | $3.13 |
| 250 | \~1,003 minutes | $15.76 |
