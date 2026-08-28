---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-control-tower/customizations.html
---

# Deploying the Customizations for AWS Control Tower solution
<a name="customizations"></a>

To deploy service control policies (SCPs), custom AWS CloudFormation templates, and baseline templates to your enrolled accounts, you can deploy the [Customizations for Control Tower solution](https://aws.amazon.com/solutions/implementations/customizations-for-aws-control-tower/).

The template launches the following:
+ An [AWS CodePipeline](https://aws.amazon.com/codepipeline/) pipeline
+ [AWS CodeBuild](https://aws.amazon.com/codebuild/) projects
+ [AWS Step Functions](https://aws.amazon.com/step-functions/) workflows
+ [AWS Lambda](https://aws.amazon.com/lambda/) functions
+ An [Amazon EventBridge](https://aws.amazon.com/eventbridge/) event rule
+ An [Amazon Simple Queue Service](https://aws.amazon.com/sqs/) (Amazon SQS) queue
+ An [Amazon Simple Storage Service](https://aws.amazon.com/s3/) (Amazon S3) bucket that contains a sample configuration package

The solution can also create an [AWS CodeCommit](https://aws.amazon.com/codecommit/) repository to contain the sample configuration package, instead of using the S3 bucket.

## Adding existing or new baselines to AWS Control Tower
<a name="baselines"></a>

In AWS Landing Zone, you could deploy resources using AWS CloudFormation stack sets on account creation. Those stack sets are also called baseline resources in the manifest.yaml file. They are deployed in AWS Control Tower as stack sets or service control policies (SCPs). To integrate these baseline resources with AWS Control Tower, see the following steps. You can also modify the baselines during the process.

1. Deploy the [Customizations for AWS Control Tower](https://aws.amazon.com/solutions/implementations/customizations-for-aws-control-tower/) solution in the management account of your AWS Control Tower setup in the AWS Regions where you deployed AWS Control Tower.

1. Download and unzip the custom-control-tower-configuration.zip file from the S3 bucket that was created as a part of solution that you deployed in step 1.

1. To add CloudFormation stack sets as baselines, open the manifest.yaml file, and in the cloudformation\_resourcessection, do the following:
   + Add the account name or account number of the account where you want to deploy the baselines. Or specify the organizational unit (OU) name to deploy the baselines to all the accounts under the OU.
   + Upload the CloudFormation templates to the templates folder in the main folder, and confirm that the correct path is mentioned in the manifest.yaml file.
   + If you have any parameters, add a parameter file, such as parameters.json, to the parameters folder.

1. To add service control policies as baselines, open the manifest.yaml file, and in the organization\_policiessection, do the following:
   + Add the organizational units that you want to apply the service control policy (SCP) to.
   + Make sure to upload the policies to the policies folder in the main folder, and confirm that the correct path is mentioned in the manifest file.

1. Zip the custom-control-tower-configuration folder, and upload it to the S3 bucket from which you downloaded it. This will start the pipeline and apply the baselines to the accounts or OUs that you specified.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
