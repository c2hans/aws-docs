---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/create-an-api-driven-resource-orchestration-framework-using-github-actions-and-terragrunt.html
---

# Create an API-driven resource orchestration framework using GitHub Actions and Terragrunt
<a name="create-an-api-driven-resource-orchestration-framework-using-github-actions-and-terragrunt"></a>

*Tamilselvan P, Abhigyan Dandriyal, Sandeep Gawande, and Akash Kumar, Amazon Web Services*

## Summary
<a name="create-an-api-driven-resource-orchestration-framework-using-github-actions-and-terragrunt-summary"></a>

This pattern leverages GitHub Actions workflows to automate resource provisioning through standardized JSON payloads, eliminating the need for manual configuration. This automated pipeline manages the complete deployment lifecycle and can seamlessly integrate with various frontend systems, from custom UI components to ServiceNow. The solution’s flexibility allows users to interact with the system through their preferred interfaces while maintaining standardized processes.

The configurable pipeline architecture can be adapted to meet different organizational requirements. The example implementation focuses on Amazon Virtual Private Cloud (Amazon VPC) and Amazon Simple Storage Service (Amazon S3) provisioning. The pattern effectively addresses common cloud resources management challenges by standardizing requests across the organization and providing consistent integration points. This approach makes it easier for teams to request and manage resources while ensuring standardization.

## Prerequisites and limitations
<a name="create-an-api-driven-resource-orchestration-framework-using-github-actions-and-terragrunt-prereqs"></a>

**Prerequisites**
+ An active AWS account
+ An active GitHub account with access to the configured repository

**Limitations**
+ New resources require manual addition of `terragrunt.hcl` files to the repository configuration.
+ Some AWS services aren’t available in all AWS Regions. For Region availability, see [AWS Services by Region](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/). For specific endpoints, see [Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/aws-service-information.html), and choose the link for the service.

## Architecture
<a name="create-an-api-driven-resource-orchestration-framework-using-github-actions-and-terragrunt-architecture"></a>

The following diagram shows the components and workflow of this pattern.

![Workflow to automate resource provisioning with GitHub Actions and Terraform.](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/bff5d70e-e8f1-454a-94bc-60e8cc16e69f/images/d4a768c8-4e11-493c-85ed-f4bf7e76ce60.png)

The architecture diagram shows the following actions:

1. The user submits a JSON payload to GitHub Actions, triggering the automation pipeline.

1. The GitHub Actions pipeline retrieves the required resources code from the Terragrunt and Terraform repositories, based on the payload specifications.

1. The pipeline assumes the appropriate AWS Identity and Access Management (IAM) role using the specified AWS account ID. Then, the pipeline deploys the resources to the target AWS account and manages Terraform state using the account-specific Amazon S3 bucket and Amazon DynamoDB table.

Each AWS account contains IAM roles for secure access, an Amazon S3 bucket for Terraform state storage, and a DynamoDB table for state locking. This design enables controlled, automated resource deployment across AWS accounts. The deployment process maintains proper state management and access control through dedicated Amazon S3 buckets and IAM roles in each account.

## Tools
<a name="create-an-api-driven-resource-orchestration-framework-using-github-actions-and-terragrunt-tools"></a>

**AWS services**
+ [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html) is a fully managed NoSQL database service that provides fast, predictable, and scalable performance.
+ [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) helps you securely manage access to your AWS resources by controlling who is authenticated and authorized to use them.
+ [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) is a cloud-based object storage service that helps you store, protect, and retrieve any amount of data.
+ [Amazon Virtual Private Cloud (Amazon VPC)](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html) helps you launch AWS resources into a virtual network that you’ve defined. This virtual network resembles a traditional network that you’d operate in your own data center, with the benefits of using the scalable infrastructure of AWS.

**Other tools**
+ [GitHub Actions](https://docs.github.com/en/actions) is a continuous integration and continuous delivery (CI/CD) platform that’s tightly integrated with GitHub repositories. You can use GitHub Actions to automate your build, test, and deployment pipeline.
+ [Terraform](https://www.terraform.io/) is an infrastructure as code (IaC) tool from HashiCorp that helps you create and manage cloud and on-premises resources.
+ [Terragrunt](https://terragrunt.gruntwork.io/docs/getting-started/overview/) is an orchestration tool that extends both OpenTofu and Terraform capabilities. It manages how generic infrastructure patterns are applied, making it easier to scale and maintain large infrastructure estates.

**Code repository**

The code for this pattern is available in the GitHub [sample-aws-orchestration-pipeline-terraform](https://github.com/aws-samples/sample-aws-orchestration-pipeline-terraform) repository.

## Best practices
<a name="create-an-api-driven-resource-orchestration-framework-using-github-actions-and-terragrunt-best-practices"></a>
+ Store AWS credentials and sensitive data using GitHub repository secrets for secure access.
+ Configure the OpenID Connect (OIDC) provider for GitHub Actions to assume the IAM role, avoiding static credentials.
+ Follow the principle of least privilege and grant the minimum permissions required to perform a task. For more information, see [Grant least privilege](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#grant-least-priv) and [Security best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) in the IAM documentation.

## Epics
<a name="create-an-api-driven-resource-orchestration-framework-using-github-actions-and-terragrunt-epics"></a>

### Create and configure repository
<a name="create-and-configure-repository"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Initialize the GitHub repository. | To initialize the GitHub repository, use the following steps:1. Create a new [GitHub repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/quickstart-for-repositories) to host the pipeline code.<br />2. Import the `deployment.yml` and `workflow-trigger.yml` files that are located in the [.github/workflows](https://github.com/aws-samples/sample-aws-orchestration-pipeline-terraform/tree/main/.github/workflows) folder of the source repository. | DevOps engineer |
| Configure the IAM roles and permissions. | To configure the IAM roles and permissions, use the following steps:1. [Create an IAM role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create.html) with the trust relationships necessary for [GitHub Actions to connect to actions in AWS](https://aws.amazon.com/blogs/security/use-iam-roles-to-connect-github-actions-to-actions-in-aws/) using an [OpenID Connect (OIDC)](https://openid.net/connect/) identity provider (IdP).<br />2. Attach the required permissions to the IAM role to create the backend and the desired resources. For more information, see a [sample policy](https://github.com/aws-samples/sample-aws-orchestration-pipeline-terraform/blob/main/README.md) to create a VPC with Amazon VPC along with the backend Amazon S3 bucket and DynamoDB table. | DevOps engineer |
| Set up GitHub secrets and variables. | For instructions about how to set up repository secrets and variables in the GitHub repository, see [Creating configuration variables for a repository](https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/use-variables#creating-configuration-variables-for-a-repository) in the GitHub documentation. Configure the following variables:+ Repository secrets`PAT_TOKEN` – Your personal access token with the [permissions](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) to perform GitHub operations<br />+ Repository variables`aws_role` – The IAM role Amazon Resource Name (ARN) with appropriate permissions to deploy the required resources and [connect GitHub actions to actions in AWS](https://aws.amazon.com/blogs/security/use-iam-roles-to-connect-github-actions-to-actions-in-aws/) | DevOps engineer |
| Create the repository structure. | To create the repository structure, use the following steps:1. Create a new folder in the `main` branch to store the `terragrunt.hcl` file, as well as the outputs and changelogs after resource creation.<br />2. Name the folder using lowercase according to the resource type that you want to provision through it. The folder is used as-is later in the payload. For more information, see a [sample structure](https://github.com/aws-samples/sample-aws-orchestration-pipeline-terraform/tree/main/sample-payload) for Amazon S3 and Amazon VPC in the repository. | DevOps engineer |

### Trigger the pipeline and validate results
<a name="trigger-the-pipeline-and-validate-results"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Execute the pipeline using curl.  | To execute the pipeline by using [curl](https://curl.se/), use the following steps:1. Create a payload.json file in your local directory. Follow the defined structure for the payload file, and stringify it before submitting the request. For more information, see the [sample payloads](https://github.com/aws-samples/sample-aws-orchestration-pipeline-terraform/tree/main/sample-payload) in the repository.<br />2. Submit the request on your terminal by using the GitHub API as shown in the following example:<pre>curl -X POST \<br />  -H "Accept: application/vnd.github.v3+json" \<br />  -H "Authorization: token YOUR_GITHUB_TOKEN" \<br />  -d @payload.json \<br />  https://api.github.com/repos/OWNER/REPO/actions/workflows/workflow-trigger.yml/dispatches</pre><br />In the example, provide your own values for the following:`YOUR_GITHUB_TOKEN` with your GitHub personal access token`OWNER` with the name of the repository owner`REPO` with repository name<br />For more information about the pipeline execution process, see [Additional information](#create-an-api-driven-resource-orchestration-framework-using-github-actions-and-terragrunt-additional). | DevOps engineer |
| Validate results of the pipeline execution | To validate the results, use the following steps:1. Monitor the GitHub Actions workflow execution in your repository's **Actions** tab.<br />2. After the successful execution of the workflows, verify resource creation by using the AWS Management Console as follows:For Amazon VPC:Navigate to the Amazon VPC service in the specified AWS Region.Check for a new VPC with tags that match your request parameters.Verify CIDR block and other configurations.For Amazon S3:Navigate to Amazon S3 buckets.In **General purpose buckets**, check for a new bucket that matches your request parameters.Verify the S3 bucket name and other configurations.<br />You can also cross-verify the created resources by using the `output.json` file created in the repository that’s inside the same resource as the `terragrunt.hcl` file. | DevOps engineer |

### Clean up resources
<a name="clean-up-resources"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Submit a cleanup request. | To delete resources that are no longer required, use the following steps:1. Submit the deletion request by using the same API endpoint but modify the payload as follows:Change `RequestType` to `delete` in the `RequestParameters`.Keep all other parameters identical to the `create` request.<br />2. Monitor the deletion process in GitHub Actions.<br />3. After workflow completion, verify that the `changelog.json` file inside the resource folder shows the status of `deleted`.<br />4. Verify resource removal by using the AWS Management Console. | DevOps engineer |

## Related resources
<a name="create-an-api-driven-resource-orchestration-framework-using-github-actions-and-terragrunt-resources"></a>

**AWS Blogs**
+ [Use IAM roles to connect GitHub Actions to actions in AWS](https://aws.amazon.com/blogs/security/use-iam-roles-to-connect-github-actions-to-actions-in-aws/)

**AWS service documentation**
+ [IAM role creation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create.html)
+ [Monitoring CloudTrail log files with Amazon CloudWatch Logs](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/monitor-cloudtrail-log-files-with-cloudwatch-logs.html)
+ [Security best practices for Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/security-best-practices.html)

**GitHub resources**
+ [Create a repository dispatch event](https://docs.github.com/en/rest/repos/repos?apiVersion=2022-11-28#create-a-repository-dispatch-event)
+ [Creating webhooks](https://docs.github.com/en/webhooks/using-webhooks/creating-webhooks#payload)
+ [Implement strong access controls on the GitHub repository](https://docs.github.com/en/get-started/learning-about-github/access-permissions-on-github)
+ [Regularly audit repository access](https://docs.github.com/en/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization)
+ [Security checks in the CI/CD pipeline](https://github.com/marketplace/actions/checkov-github-action)
+ [Use multi-factor authentication for GitHub accounts](https://docs.github.com/en/authentication/securing-your-account-with-two-factor-authentication-2fa/configuring-two-factor-authentication)

## Additional information
<a name="create-an-api-driven-resource-orchestration-framework-using-github-actions-and-terragrunt-additional"></a>

**Pipeline execution process**

Following are the steps of the pipeline execution:

1. **Validates JSON payload format** - Ensures that the incoming JSON configuration is properly structured and contains all required parameters

1. **Assumes specified IAM role** - Authenticates and assumes the required IAM role for AWS operations

1. **Downloads required Terraform and Terragrunt code** - Retrieves the specified version of resource code and dependencies

1. **Executes resource deployment** - Applies the configuration to deploy or update AWS resources in the target environment

**Sample payload used for VPC creation**

Following is example code for Terraform backend state bucket creation:

```
state_bucket_name = "${local.payload.ApplicationName}-${local.payload.EnvironmentId}-tfstate"
```

```
lock_table_name = "${local.payload.ApplicationName}-${local.payload.EnvironmentId}-tfstate-lock"
```

Following is an example payload for creating a VPC with Amazon VPC, where `vpc_cidr` defines the [CIDR block](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-cidr-blocks.html) specifications for the VPC. The Terraform state bucket is mapped to a variable defined in the `terraform` files. The `ref` parameter contains the branch name of the code to execute.

```
{
    "ref": "main",
    "inputs": {
        "RequestParameters": {
            "RequestId": "1111111",
            "RequestType": "create",
            "ResourceType": "vpc",
            "AccountId": "1234567890",
            "AccountAlias": "account-alias",
            "RegionId": "us-west-2",
            "ApplicationName": "myapp",
            "DivisionName": "division-name",
            "EnvironmentId": "dev",
            "Suffix": "poc"
        },
        "ResourceParameters": [
            {
                "VPC": {
                    "vpc_cidr": "10.0.0.0/16"
                }
            }
        ]
    }
}
```

`RequestParameters` are used to track the request status in the pipeline section and `tfstate` is created based on this information. The following parameters contain metadata and control information:
+ `RequestId` – Unique identifier for the request
+ `RequestType` – Type of operation (create, update, or delete)
+ `ResourceType` – Type of resource to be provisioned
+ `AccountId` – Target AWS account for deployment
+ `AccountAlias` – Friendly name for the AWS account
+ `RegionId` – AWS Region for resource deployment
+ `ApplicationName` – Name of the application
+ `DivisionName` – Organization division
+ `EnvironmentId` – Environment (for example, dev and prod)
+ `Suffix` – Additional identifier for the resources

`ResourceParameters` contain resource-specific configuration that maps to variables defined in the Terraform files. Any custom variables that need to be passed to the Terraform modules should be included in `ResourceParameters`. The parameter `vpc_cidr` is mandatory for Amazon VPC.
