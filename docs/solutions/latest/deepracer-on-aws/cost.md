---
source_url: https://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/cost.html
---

# Cost
<a name="cost"></a>

You are responsible for the cost of AWS services that you use while operating this solution. As of this revision, the monthly cost of operating this solution for a small group of 25 users with limited model training and evaluation demand is about USD $7.71 for each user (or USD $192.70 total).

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

Total SageMaker cost = [(212.5 hours) \* ($0.714/instance hour)] \+ ($1.40 storage cost) = $153.13

## Training and evaluation cost examples
<a name="training-and-evaluation-cost-examples"></a>

### Example 1 (25 users)
<a name="example-1-25-users"></a>

For example, suppose you deploy DeepRacer on AWS for 25 users. Each user creates and trains 3 models, evaluates each model 3 times, and then submits the models to a race. With a training time of 90 minutes, the cost is USD $192.70, or USD $7.71 for each user.

 **Cost summary**

| AWS service | Dimensions | Cost per month (USD) |
| --- | --- | --- |
| Amazon SageMaker | [(212.5 hours) \* ($0.714/instance hour)] \+ ($1.40 storage cost) | $153.13 |
| AWS WAF | (1 Web ACL \* $5.00) \+ (10 rules and rule groups \* $1.00) \+ (1 Bot Control subscription \* $10.00) | $25.00 |
| Amazon S3 | (0.33GB average model size) \* (75 models) \* ($0.023/GB) | $0.57 |
| Other services | AWS Lambda, Amazon DynamoDB, Amazon CloudWatch, AWS CodeBuild, Amazon ECR | $14.00 |
|  **Monthly total**  |  **$7.71/user**  |  **$192.70**  |

### Example 2 (100 users)
<a name="example-2-100-users"></a>

For example, suppose you deploy DeepRacer on AWS for 100 users. Each user creates and trains 3 models, evaluates each model 3 times, and then submits the models to a race. With a training time of 90 minutes, the cost is USD $649.58, or USD $6.50 for each user.

 **Cost summary**

| AWS service | Dimensions | Cost per month (USD) |
| --- | --- | --- |
| Amazon SageMaker | [(850 hours) \* ($0.714/instance hour)] \+ ($1.40 storage cost) | $608.30 |
| AWS WAF | (1 Web ACL \* $5.00) \+ (10 rules and rule groups \* $1.00) \+ (1 Bot Control subscription \* $10.00) | $25.00 |
| Amazon S3 | (0.33GB average model size) \* (300 models) \* ($0.023/GB) | $2.28 |
| Other services | AWS Lambda, Amazon DynamoDB, Amazon CloudWatch, AWS CodeBuild, Amazon ECR | $14.00 |
|  **Monthly total**  |  **$6.50/user**  |  **$649.58**  |

### Example 3 (250 users)
<a name="example-3-250-users"></a>

For example, suppose you deploy DeepRacer on AWS for 250 users. Each user creates and trains 3 models, evaluates each model 3 times, and then submits the models to a race. With a training time of 90 minutes, the cost is USD $1,563.34, or USD $6.25 for each user.

 **Cost summary**

| AWS service | Dimensions | Cost per month (USD) |
| --- | --- | --- |
| Amazon SageMaker | [(2,125 hours) \* ($0.714/instance hour)] \+ ($1.40 storage cost) | $1,518.65 |
| AWS WAF | (1 Web ACL \* $5.00) \+ (10 rules and rule groups \* $1.00) \+ (1 Bot Control subscription \* $10.00) | $25.00 |
| Amazon S3 | (0.33GB average model size) \* (750 models) \* ($0.023/GB) | $5.69 |
| Other services | AWS Lambda, Amazon DynamoDB, Amazon CloudWatch, AWS CodeBuild, Amazon ECR | $14.00 |
|  **Monthly total**  |  **$6.25/user**  |  **$1,563.34**  |

## Fixed cost of AWS WAF
<a name="waf-fixed-cost"></a>

Most services that this solution uses, including Amazon CloudFront, Amazon API Gateway, AWS Lambda, and Amazon DynamoDB, cost little or nothing when the deployment is idle. AWS WAF does not. AWS WAF bills for the solution’s web access control list (Web ACL) every month, even if no one trains a model or runs a race.

The solution associates the Web ACL with its Amazon API Gateway REST API, not with the CloudFront distribution. The Web ACL contains 10 rules and rule groups:
+ Seven AWS managed rule groups: Bot Control, Known Bad Inputs, Core Rule Set, Anonymous IP List, Amazon IP Reputation List, SQL Database, and WordPress Application
+ The Admin Protection managed rule group, in count mode
+ A custom rule that enforces the request body size limit on all endpoints except the reward function endpoints
+ A rate-based rule that limits requests to `/admin/` paths to 100 per IP address

The following table shows the fixed monthly cost of AWS WAF in the US East (N. Virginia) AWS Region.

| AWS WAF component | Dimensions | Cost per month (USD) |
| --- | --- | --- |
| Web ACL | 1 Web ACL \* $5.00 | $5.00 |
| Rules and rule groups | 10 rules and rule groups \* $1.00 | $10.00 |
| Bot Control (Common) subscription | 1 subscription \* $10.00 | $10.00 |
|  **Fixed monthly total**  |  |  **$25.00**  |

AWS WAF also charges USD $0.60 per million requests inspected. Bot Control (Common) charges USD $1.00 per million requests, after the first 10 million requests each month, which are free. For idle or low-traffic deployments, these request charges are small. For current rates, refer to [AWS WAF pricing](https://aws.amazon.com/waf/pricing/).

You might use this solution as a development, evaluation, or occasional-use environment, and the AWS WAF cost can make up most of its idle cost. In that case, you can remove AWS WAF from your deployed resources. For instructions on removing AWS WAF and the related security considerations, refer to [Remove AWS WAF to reduce fixed costs](post-deployment-tasks.md#remove-waf).

## Live racing cost examples
<a name="live-racing-cost-examples"></a>

Live racing has no fixed monthly charge; cost is incurred only while a race is active. The following examples assume 5 laps per evaluation, \~7 minutes for the first evaluation (including instance warmup), and \~4 minutes per subsequent evaluation.

| Participants | Race duration | Cost per race (USD) |
| --- | --- | --- |
| 25 | \~103 minutes | $0.87 |
| 100 | \~403 minutes | $3.13 |
| 250 | \~1,003 minutes | $15.76 |
