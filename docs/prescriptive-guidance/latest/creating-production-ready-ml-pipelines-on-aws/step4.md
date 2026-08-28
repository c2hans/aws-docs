---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/creating-production-ready-ml-pipelines-on-aws/step4.html
---

# Step 4. Create the pipeline
<a name="step4"></a>

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/creating-production-ready-ml-pipelines-on-aws/images/guide-img/38c6f8a0-9908-46ce-9db4-ad6b4c4bc218/images/8e062f26-a42c-4552-9a3e-9e66c772a3cf.png)

After you define the pipeline logically, it's time to create the infrastructure to support the pipeline. This step requires the following  capabilities, at a minimum:
+ Storage, to host and manage pipeline inputs and outputs, including code, model artifacts, and data used in training and inference runs.
+ Compute (GPU or CPU), for modeling and inference as well as data preprocessing and postprocessing.
+ Orchestration, to manage the resources being used and to schedule any regular runs. For example, the model might be retrained on a periodic basis as new data becomes available.
+ Logging and alerting, to monitor the pipeline model accuracy, for resource utilization, and for troubleshooting.

## Implementation with AWS CloudFormation
<a name="cfn"></a>

To create the pipeline we used AWS CloudFormation, which is an AWS service for deploying and managing infrastructure as code. The AWS CloudFormation templates include the Step Functions definition that was created in the previous step with the Step Functions SDK. This step includes the creation of the AWS-managed Step Functions instance, which is called the *Step Functions state machine*. No resources for training and inference are created at this stage, because training and and inference jobs run on demand, only when they're needed, as Amazon SageMaker jobs. This step also includes creating AWS Identity and Access Management (IAM) roles to run the Step Functions, run SageMaker, and read and write from Amazon S3.

## Modifying the output from the Step Functions SDK
<a name="modify-output"></a>

We had to make some minor modifications to the AWS CloudFormation output from the previous section. We used simple Python string matching to do the following:
+ We added logic for creating the Parameters section of the AWS CloudFormation template. This is because we want to create two roles and define the pipeline name as a parameter along with the deployment environment. This step also covers any additional resources and roles that you might want to create, as discussed in step 6.
+ We reformatted three fields to have the required `!Sub` prefix and quotation marks so that they can be updated dynamically as a part of the deployment process:
  + The `StateMachineName` property, which names the state machine.
  + The `DefinitionString` property, which defines the state machine.
  + The `RoleArn` property, which is returned by the state machine.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
