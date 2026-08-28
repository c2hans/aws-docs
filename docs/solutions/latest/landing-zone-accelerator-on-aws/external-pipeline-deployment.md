---
source_url: https://docs.aws.amazon.com/solutions/latest/landing-zone-accelerator-on-aws/external-pipeline-deployment.html
---

# External pipeline deployment
<a name="external-pipeline-deployment"></a>

In a default Landing Zone Accelerator on AWS installation, the CodePipeline and S3 bucket deploys into the AWS Organizations management account. You may want to deploy and operate these components in a member AWS account to limit access to the management account. This solution supports this model with an optional pipeline deployment account. In this model, the solution assumes a role in the AWS Organizations management account to deploy resources to workload accounts.

 **External pipeline deployment**

![external pipeline deployment](http://docs.aws.amazon.com/solutions/latest/landing-zone-accelerator-on-aws/images/external-pipeline-deployment.png)

Follow these instructions to implement this pattern:

1. Select an AWS account for the pipeline deployment account. We recommend having the account as a member of the AWS Organizations environment.

1. Create a new IAM role in the AWS Organizations management account that allows access from the pipeline deployment account. `AcceleratorPipelineDeploymentRole` is the preferred name for this role.

1. Update the trust policy of the `AcceleratorPipelineDeploymentRole` to allow access from the pipeline deployment account:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::${PIPELINE_DEPLOYMENT_ACCOUNT_ID}:root"
      },
      "Action": "sts:AssumeRole",
      "Condition": {
        "StringLike": {
          "aws:PrincipalArn": "arn:aws:iam::${PIPELINE_DEPLOYMENT_ACCOUNT_ID}:role/${AcceleratorQualifier}-*"
        }
      }
    }
  ]
}
```

1. Attach the `AdministratorAccess` AWS managed IAM policy to the role.

**Note**
By default, AWS IAM roles with prefix AcceleratorQualifier in the pipeline account are used by AWS CodeBuild to assume role in the management account and deploy resources. To protect these roles, you should implement additional security measures, such as Service control policies (SCPs).

After you create the IAM role in the management account, synthesize the Landing Zone Accelerator on AWS installer template configured for external deployments by following these instructions:

1. Clone or download the latest release of the Landing Zone Accelerator on AWS [source code](https://github.com/awslabs/landing-zone-accelerator-on-aws/tree/main/source).

1. Navigate to the `source` folder:

   ```
   cd landing-zone-accelerator-on-aws/source
   ```

1. Install dependencies and build the source code:

   ```
   yarn install && yarn build
   ```

1. Navigate to the installer folder:

   ```
   cd packages/\@aws-accelerator/installer/
   ```

1. Synthesize the installer template by running:

   ```
   cdk synth --context use-external-pipeline-account=true
   ```

1. Retrieve the synthesize template named `AWSAccelerator-InstallerStack.template.json` from the `cdk.out` directory.

1. Use this template to create the `AWSAccelerator-Installer` CloudFormation stack in the external deployment account.

1. The deployment now follows the same process as the [standard deployment process](https://docs.aws.amazon.com/solutions/latest/landing-zone-accelerator-on-aws/deployment-overview.html) with the addition of the following parameters:

   1.  **AcceleratorQualifier** - Names the resources in the external deployment account. This must be unique for each Landing Zone Accelerator on AWS pipeline created in a single external deployment account, for example "env2" or "app1." Do not use "aws-accelerator" or a similar value that could be confused with the prefix.

   1.  **ManagementAccountId** - This is the AWS account ID of the AWS Organizations management account.

   1.  **ManagementAccountRoleName** - This is the name of the IAM role used to access the management account from the external deployment account.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Landing Zone Accelerator on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
