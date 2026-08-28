---
source_url: https://docs.aws.amazon.com/solutions/latest/landing-zone-accelerator-on-aws/awsaccelerator-pipeline.html
---

# Core pipeline
<a name="awsaccelerator-pipeline"></a>

The solution uses CodeBuild as an orchestration engine for each action completed after the **Source** stage in this pipeline. These actions run a CDK application, which deploys CloudFormation stacks across each of the Landing Zone Accelerator on AWS solution-managed AWS accounts and Regions, unless otherwise specified:

1.  **Source** - There are two source actions in this stage:
   +  **Source** - The Landing Zone Accelerator on AWS source code from the AWS Solutions [GitHub](https://github.com/awslabs/landing-zone-accelerator-on-aws) repository.
   +  **Configuration** - The Landing Zone Accelerator on AWS configuration repository, named `aws-accelerator-config`.

1.  **Build** - In this stage, the Landing Zone Accelerator on AWS source code is transpiled, including input and type validation for the configuration files.

1.  **Prepare** - Any AWS accounts that are defined in the configuration are created and/or validated as necessary. If using [AWS Control Tower](https://aws.amazon.com/controltower/), new AWS accounts are generated using the Control Tower Account Factory and enrolled into the proper [AWS Organizations](https://aws.amazon.com/organizations/) Organizational Unit (OU). We highly recommend that you use AWS Control Tower to generate and enroll new OUs. However, if you’re deploying the solution in an AWS Region that isn’t yet supported by AWS Control Tower, any OUs that are defined in the configuration are created and/or validated as necessary.

1.  **Accounts** - Additional account validation occurs across the environment. All accounts in the configuration are checked to verify if they’re part of the AWS Organization. Any configured AWS Organization Service Control Policies (SCPs) are also created and attached to configuration-specified deployment targets in this stage.

1.  **Bootstrap** - AWS CDK bootstrap is run; this initializes the environment for CDK. A solution-specific CDK toolkit CloudFormation template (`AWS Accelerator-CDKToolkit`) is deployed to any AWS accounts and Regions that haven’t been previously bootstrapped. If you want to deploy additional CDK applications, we recommend that you deploy your own CDK bootstrap template to avoid collisions with the Landing Zone Accelerator on AWS usage of CDK.

1.  **Review (optional)** - An optional stage that can be turned on and off using the **EnableApprovalStage** configuration parameter on the `AWSAccelerator-InstallerStack` CloudFormation template. Turning on this option adds this stage to the pipeline, which includes the following actions:
   +  **Diff** - AWS CDK diff is run on the synthesized CloudFormation templates against each target account and Region. The result of the diff can be reviewed in the build logs of the CodeBuild project.
   +  **Approve** - A manual approval action. This is meant as a gate to review and approve/deny the changes represented in the **Diff** action. This action publishes to an SNS topic to notify configured email list(s) of the pending approval.

1.  **Logging** - There are two actions in this stage:
   +  **Key** - The solution deploys two stacks during this stage:
     +  **KeyStack** - Deploys a centralized AWS KMS key to the AWS account designated as the audit account in the configuration. This key is used in subsequent deployments to activate encryption at-rest for applicable resources. The solution also deploys Systems Manager Parameter Store parameters containing the value of the key Amazon Resource Names (ARNs) along with an IAM role that allows cross-account read access for the parameters.
     +  **DependenciesStack** - Deploys resources that are required by the solution in subsequent pipeline stages, such as IAM roles for custom resources.
   +  **Logging** - This solution deploys a centralized logging Amazon S3 bucket, an Amazon Kinesis Data Stream, and Amazon Data Firehose in the AWS account designated as `LogArchive` in the configuration. The solution uses the Kinesis Data Stream as a destination for CloudWatch Logs groups in member accounts so that logs can be streamed to the central logs bucket via Firehose. Optionally, you can specify a dynamic partitioning configuration to map specific CloudWatch Log groups to specific Amazon S3 bucket prefixes.

     The solution creates Amazon S3 buckets for Amazon S3 server access logging in each AWS account and Region activated in the configuration. Optionally, you can activate the Amazon S3 Block Public Access feature at the account level and activate Systems Manager Session Manager logging for each configured account and Region.

     The solution also deploys AWS KMS keys for Amazon S3, [AWS Lambda](https://aws.amazon.com/lambda/), and CloudWatch Logs. These keys deploy in each AWS account and Region activated in the configuration. A solution-deployed Systems Manager automation document named `Accelerator-Put-S3-Encryption` uses the AWS KMS key for Amazon S3 to encrypt any Amazon S3 buckets that were created without encryption. The solution uses the AWS KMS key for Lambda to invoke Lambda environment variable encryption, and it uses the AWS KMS key for CloudWatch Logs to encrypt solution-created CloudWatch Logs groups.

1.  **Organization** - Deployment of AWS Organization-wide resources. These resources are deployed in the Region designated as the organization’s home Region in the organization’s management account. This includes actions such as activating trusted services, creating AWS Organizations tagging and backup policies, creating report definitions for [AWS Cost and Usage Report](https://aws.amazon.com/aws-cost-management/aws-cost-and-usage-reporting/), and [AWS Budgets](https://aws.amazon.com/aws-cost-management/aws-budgets/).

1.  **Security\_Audit** - Deployment of resource dependencies for centralized security services in the AWS account designated as the audit account in the configuration. This includes S3 buckets and/or configurations for [Amazon Macie](https://aws.amazon.com/macie/), [Amazon GuardDuty](https://aws.amazon.com/guardduty/), [AWS Security Hub](https://aws.amazon.com/security-hub/), and Systems Manager automation documents.

1.  **Deploy** - The following actions are completed in this stage to deploy the remaining architecture as defined in the configuration files. Refer to our [sample configuration](https://github.com/awslabs/landing-zone-accelerator-on-aws/tree/main/reference/sample-configurations) as a reference to get started:
   +  **Network\_Prepare** - Network resources that subsequent networking stacks must reference are created in this action. This includes AWS Transit Gateway and AWS Resource Access Manager (AWS RAM) shares, if configured.
   +  **Security** - Member account security services are configured.
   +  **Operations** - Users, groups, and roles are deployed. IAM [Security Assertion Markup Language](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_create_saml.html) (SAML) identity provider configuration is also deployed, if configured.
   +  **Network\_VPCs** - Three stacks are deployed during this stage, each related to VPC networking:
     +  **NetworkVpcStack** - VPCs, subnets, route tables, security groups and other associated resources are deployed. AWS Transit Gateway attachments are created, if configured.
     +  **NetworkVpcEndpointsStack** - VPC endpoints, including Route 53 resolver endpoints and AWS Network Firewall endpoints are deployed.
     +  **NetworkVpcDnsStack** - Route 53 private hosted zones and resolver rules are deployed.
   +  **Security\_Resources** - Additional member account security services such as AWS Config, CloudWatch metrics, and alarms are deployed.
   +  **Network\_Associations** - The solution deploys two stacks during this stage, each related to network associations that depend on resources created in the **Network\_VPCs** stage:
     +  **NetworkAssociationsStack** - Network associations that depend on Amazon VPC resources to be created, such as AWS Transit Gateway VPC associations, are deployed.
     +  **NetworkAssociationsGwlbStack** - Network associations that depend on Gateway Load Balancers to be created, such as Gateway Load Balancer VPC endpoints, are deployed.
   +  **Customizations (optional)** - The solution deploys custom applications, CloudFormation stacks, and CloudFormation stacksets that are configured in the `customizations-config.yaml` file.
   +  **Finalize** - If using the account quarantine feature for new account creation, the quarantine SCP is removed during this action.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Landing Zone Accelerator on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
