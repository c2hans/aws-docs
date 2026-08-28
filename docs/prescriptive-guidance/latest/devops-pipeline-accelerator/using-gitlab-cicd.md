---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/devops-pipeline-accelerator/using-gitlab-cicd.html
---

# Using GitLab CI/CD to deploy Terraform, AWS CDK, and CloudFormation templates
<a name="using-gitlab-cicd"></a>

DPA contains GitLab CI/CD templates that you use as building blocks for deploying Terraform, AWS Cloud Development Kit (AWS CDK), and CloudFormation IaC code. This section describes the following for this use case:
+ Standardized pipeline structure
+ Reusable stages and jobs
+ Pipeline structure rules
+ Integrated tools for security scans

## Prerequisites
<a name="prerequisites-gitlab-cicd"></a>
+ An active AWS account
+ Permissions to provision resources by using IaC templates
+ GitLab account with any type of license-free, premium, or enterprise version that supports GitLab CI/CD features
+ GitLab required runners configured to run jobs with specific Docker images

## Tools
<a name="tools-gitlab-cicd"></a>
+ [cdk\_nag](https://github.com/cdklabs/cdk-nag#readme) is an open source tool that uses a combination of rule packs to check AWS CDK applications for adherence to best practices.
+ [AWS CloudFormation Linter (cfn-lint)](https://github.com/aws-cloudformation/cfn-lint) is a linter that checks CloudFormation YAML or JSON templates against the [AWS CloudFormation resource specification](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-resource-specification.html). It also performs other checks, such as checking for valid values for resource properties and adherence to best practices.
+ [cfn\_nag](https://github.com/stelligent/cfn_nag) is an open source tool that identifies potential security issues in CloudFormation templates by searching for patterns.
+ [Checkov](https://www.checkov.io/1.Welcome/What%20is%20Checkov.html) is a static code-analysis tool that checks IaC for security and compliance misconfigurations.
+ [Keeping Infrastructure as Code Secure (KICS)](https://github.com/Checkmarx/kics) is an open source tool that identifies security vulnerabilities, compliance issues, and infrastructure misconfigurations early in the development cycle.
+ [tfsec](https://github.com/aquasecurity/tfsec) is a static code-analysis tool that checks Terraform code for potential misconfigurations.

## Instructions
<a name="instructions-gitlab-cicd"></a>

1. Copy the `gitlab-ci` directory and host it to your GitLab organization group.

1. Make sure that the applications can access the GitLab organization group that contains the DPA templates.

1. For the application, include the DPA-specific entry point for the pipeline as follows:
   + Terraform

     ```
       include:
           - project: <GITLAB_GROUP_PATH/<REPOSITORY_NAME>
             ref: main # best practise to create release tag and use the same
             file: gitlab-ci/entrypoints/gitlab/terraform-infrastructure.yml
     ```
   + AWS CDK

     ```
       include:
           - project: <GITLAB_GROUP_PATH/<REPOSITORY_NAME>
             ref: main # best practise to create release tag and use the same
             file: gitlab-ci/entrypoints/gitlab/cdk-infrastructure.yml
     ```
   + CloudFormation

     ```
       include:
           - project: <GITLAB_GROUP_PATH/<REPOSITORY_NAME>
             ref: main # best practise to create release tag and use the same
             file: gitlab-ci/entrypoints/gitlab/cf-infrastructure.yml
     ```

1. For the application, define the following variables in order to enable deployment on `DEV` and `INTEGRATION` environments.

   ```
     AWS_REGION: us-east-2 # region where deployment should happen
     DEV_AWS_ACCOUNT: 123456789012 # Dev environment AWS account number
     DEV_ARN_ROLE: arn:aws:iam::123456789012:role/dpa-gitlab-access-role # IAM role ARN that will be used to provision resources in Dev
     DEV_DEPLOY: "true" # true / false to enable deployment to DEV environment
     DEV_ENV: "dev" # Dev environment name
     INT_AWS_ACCOUNT: 123456789012 # Integration environment AWS account number
     INT_ARN_ROLE: arn:aws:iam::123456789012:role/dpa-gitlab-access-role # IAM role ARN that will be used to provision resources in Integration
     INT_DEPLOY: "true" # true / false to enable deployment to Integration environment
     INT_ENV: "int" # Integration environment name
   ```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
