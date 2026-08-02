---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/addf-security-and-operations/built-in-security-features.html
---

# Built-in security features
<a name="built-in-security-features"></a>

Autonomous Driving Data Framework (ADDF) has various built-in security features. By default, these features are designed to help you set up a secure framework and help your organization meet common enterprise security requirements.

The following are the built-in security features:
+ [Least privilege for ADDF module code](#least-privilege-for-addf-module-code)
+ [Infrastructure as code](#infrastructure-as-code)
+ [Automated security checks for IaC](#automated-security-checks-for-iac)
+ [Custom least-privilege policy for the AWS CDK deployment role](#custom-least-privilege-policy-for-the-aws-cdk-deployment-role)
+ [Least-privilege policy for the module deployspec file](#least-privilege-policy-for-the-module-deployspec-file)
+ [Data encryption](#data-encryption)
+ [Credential storage using Secrets Manager](#credential-storage-using-secrets-manager)
+ [Security reviews of SeedFarmer and CodeSeeder](#security-reviews-of-seed-farmer-and-code-seeder)
+ [Permissions boundary support for the AWS CodeBuild role for CodeSeeder](#permissions-boundary-support-for-the-aws-code-build-role-for-code-seeder)
+ [AWS multi-account architecture](#aws-multi-account-architecture)
+ [Least-privilege permissions for multi-account deployments](#least-privilege-permissions-for-multi-account-deployments)

## Least privilege for ADDF module code
<a name="least-privilege-for-addf-module-code"></a>

*Least privilege* is the security best practice of granting the minimum permissions required to perform a task. For more information, see [Apply least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege). ADDF-provided modules strictly follow the principle of least privilege in their code and deployed resources, as follows:
+ All AWS Identity and Access Management (IAM) policies generated for an ADDF module have the minimum permissions needed for the use case.
+ AWS services are configured and deployed according to the principle of least privilege. ADDF-provided modules use only the services and service features that are required for the specific use case.

## Infrastructure as code
<a name="infrastructure-as-code"></a>

ADDF, as a framework, is designed to deploy ADDF modules as infrastructure as code (IaC). IaC eliminates manual deployment processes and helps prevent errors and misconfigurations, which can result from manual processes.

ADDF is designed to orchestrate and deploy modules by using any common IaC framework. This includes, but isn't limited to:
+ [AWS Cloud Development Kit (AWS CDK)](https://docs.aws.amazon.com/cdk/v2/guide/home.html)
+ [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html)
+ [Hashicorp Terraform](https://www.terraform.io/)

You can use different IaC frameworks to write different modules, and then you use ADDF to deploy them.

The default IaC framework used by ADDF modules is AWS CDK. AWS CDK is a high-level object-oriented abstraction that you can use to define AWS resources imperatively. AWS CDK already enforces security best practices by default for various services and scenarios. By using AWS CDK, the risk of security misconfigurations is reduced.

## Automated security checks for IaC
<a name="automated-security-checks-for-iac"></a>

The open-source [cdk-nag](https://github.com/cdklabs/cdk-nag/blob/main/README.md) utility (GitHub) is integrated into ADDF. This utility automatically checks ADDF modules that are based on AWS CDK for adherence to general and security best practices. The cdk-nag utility uses rules and rule packs to detect and report code that violates best practices. For more information about the rules and a comprehensive list, see [cdk-nag rules](https://github.com/cdklabs/cdk-nag/blob/main/RULES.md#awssolutions) (GitHub).

## Custom least-privilege policy for the AWS CDK deployment role
<a name="custom-least-privilege-policy-for-the-aws-cdk-deployment-role"></a>

ADDF makes extensive use of AWS CDK v2. It is required that you bootstrap all ADDF AWS accounts to AWS CDK. For more information, see [Bootstrapping](https://docs.aws.amazon.com/cdk/v2/guide/bootstrapping.html) (AWS CDK documentation).

By default, AWS CDK assigns the permissive [AdministratorAccess](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html#jf_administrator) AWS managed policy to the AWS CDK deployment role created in bootstrapped accounts. The complete name of this role is `cdk-[CDK_QUALIFIER]-cfn-exec-role-[AWS_ACCOUNT_ID]-[REGION]`. AWS CDK uses this role to deploy resources into the bootstrapped AWS account as part of the AWS CDK deployment process.

Depending on your organization's security requirements, the `AdministratorAccess` policy might be too permissive. As part of the AWS CDK bootstrap process, you can customize the policy and permissions according to your needs. You can change the policy can by re-bootstrapping the account with a newly defined policy by using the `--cloudformation-execution-policies` parameter. For more information, see [Customizing bootstrapping](https://docs.aws.amazon.com/cdk/v2/guide/bootstrapping.html#bootstrapping-customizing) (AWS CDK documentation).

**Note**
Although this security feature isn't specific to ADDF, it is listed in this section because it can increase the overall security of your ADDF deployment.

## Least-privilege policy for the module deployspec file
<a name="least-privilege-policy-for-the-module-deployspec-file"></a>

Each module contains a deployment specifications file that is called **deployspec.yaml**. This file defines the deployment instructions for the module. CodeSeeder uses it to deploy the defined module in the target account by using AWS CodeBuild. CodeSeeder assigns a default service role to CodeBuild to deploy the resources, as instructed in the deployment specifications file. This service role is designed according to the least-privilege principle. It includes all required permissions to deploy AWS CDK applications, because all ADDF-provided modules are created as AWS CDK applications.

However, if you need to run any stage commands outside of AWS CDK, you need to create a custom IAM policy instead of using the default service role for CodeBuild. For example, if you are using an IaC deployment framework other than AWS CDK, such as Terraform, you need to create an IAM policy that grants sufficient permissions for that specific framework to function. Another scenario that requires a dedicated IAM policy is when you include direct AWS Command Line Interface (AWS CLI) calls to other AWS services in the `install`, `pre_build`, `build`, or `post_build` stage commands. For example, you need a custom policy if your module includes an Amazon Simple Storage Service (Amazon S3) command to upload files to an S3 bucket. The custom IAM policy provides fine-grained control for any AWS command outside of the AWS CDK deployment. When creating a custom IAM policy for your ADDF module, make sure that you apply least-privilege permissions.

## Data encryption
<a name="data-encryption"></a>

ADDF stores and processes potentially sensitive data. To help protect this data, SeedFarmer, CodeSeeder, and ADDF-provided modules encrypt data at rest and in transit for all used AWS services (unless explicitly stated otherwise for modules in the `demo-only` folder).

## Credential storage using Secrets Manager
<a name="credential-storage-using-secrets-manager"></a>

ADDF handles various secrets for different services, such as Docker Hub, JupyterHub, and [Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/gsg/getting-started.html). ADDF uses [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html) to store any ADDF-related secrets. This helps you remove sensitive data from the source code.

AWS Secrets Manager secrets are stored only in the target accounts, as needed for that account to function properly. By default, the toolchain account doesn't contain any secrets.

## Security reviews of SeedFarmer and CodeSeeder
<a name="security-reviews-of-seed-farmer-and-code-seeder"></a>

[SeedFarmer](https://github.com/awslabs/seed-farmer) and [CodeSeeder](https://github.com/awslabs/aws-codeseeder) (GitHub repositories) are used to deploy ADDF and its ADDF modules. These open-source projects undergo the same regular AWS internal security review process as ADDF, as described in [ADDF security review process](addf-security-review-process.md).

## Permissions boundary support for the AWS CodeBuild role for CodeSeeder
<a name="permissions-boundary-support-for-the-aws-code-build-role-for-code-seeder"></a>

IAM *permissions boundaries* are a common security mechanism that defines the maximum permissions that an identity-based policy can grant to an IAM entity. SeedFarmer and CodeSeeder support an IAM permissions boundary attachment for each target account. The permissions boundary limits the maximum permissions of any service role used by CodeBuild when CodeSeeder deploys modules. IAM permissions boundaries must be created outside of ADDF by a security team. IAM permissions boundary policy attachments are accepted as an attribute within the ADDF deployment manifest file, **deployment.yaml**. For more information, see [Permissions boundaries](https://seed-farmer.readthedocs.io/en/latest/concepts/multi-account/#permissions-boundaries) (SeedFarmer documentation).

The workflow is as follows:

1. Your security team defines and creates an IAM permissions boundary according to your security requirements. The IAM permissions boundary must be individually created in each ADDF AWS account. The output is a permissions boundary policy Amazon Resource Name (ARN) list.

1. The security team shares the policy ARN list with your ADDF developer team.

1. The ADDF developer team integrates the policy ARN list into the manifest file. For an example of this integration, see [sample-permissionboundary.yaml](https://github.com/awslabs/autonomous-driving-data-framework/blob/d98e02f1a89d0029b35a56b93dd56c18c5cb2aa1/resources/sample-permissionboundary.yaml) (GitHub).

1. After successful deployment, the permissions boundary is attached to all service roles that CodeBuild uses to deploy modules.

1. The security team monitors that the permissions boundaries are applied as needed.

## AWS multi-account architecture
<a name="aws-multi-account-architecture"></a>

As defined in the security pillar of the AWS Well-Architected Framework, it is considered best practice to separate resources and workloads into multiple AWS accounts, based on your organization's requirements. This is because an AWS account acts as an isolation boundary. For more information, see [AWS account management and separation](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/aws-account-management-and-separation.html). The implementation of this concept is called a *multi-account architecture*. A properly designed AWS multi-account architecture provides workload categorization and reduces the scope of impact in the event of a security breach, as compared to a single-account architecture.

ADDF natively supports AWS multi-account architectures. You can distribute your ADDF modules across as many AWS accounts as needed for your organization's security and separation-of-duties requirements. You can deploy ADDF into a single AWS account, combining the toolchain and target account functions. Alternatively, you can create individual target accounts for ADDF modules or module groups.

The only restriction that you need to consider is that an ADDF module represents the smallest unit of deployment for each AWS account.

For production environments, it is recommended that you use a multi-account architecture consisting of a toolchain account and at least one target account. For more information, see [ADDF architecture](addf-architecture-terminology.md#addf-architecture).

## Least-privilege permissions for multi-account deployments
<a name="least-privilege-permissions-for-multi-account-deployments"></a>

If you use a multi-account architecture, SeedFarmer needs to access the target accounts to perform the following three actions:

1. Write the ADDF module metadata to the toolchain account and target accounts.

1. Read the current ADDF module metadata from the toolchain account and the target accounts.

1. Initiate AWS CodeBuild jobs in the target accounts, for the purpose of deploying or updating modules.

The following figure shows the cross-account relationships, including operations for assuming ADDF-specific AWS Identity and Access Management (IAM) roles.

![IAM roles in an AWS multi-account architecture that has a toolchain account and target accounts.](http://docs.aws.amazon.com/prescriptive-guidance/latest/addf-security-and-operations/images/guide-img/b7c99a03-2a36-4dc2-9b13-9b2a1cbf7eb9/images/724ea3a3-e810-4fca-ad1f-f0d12d1a7de9.png)

These cross-account actions are achieved by using well-defined assume-role operations.
+ The ADDF toolchain IAM role is deployed in the toolchain account. SeedFarmer assumes this role. This role has permissions to perform an `iam:AssumeRole` action and can assume the ADDF deployment IAM role in each target account. In addition, the ADDF toolchain IAM role can run local AWS Systems Manager Parameter Store operations.
+ The ADDF deployment IAM role is deployed in each target account. This role can be assumed only from the toolchain account by using the ADDF toolchain IAM role. This role has permissions to run local AWS Systems Manager Parameter Store operations and has permissions to run AWS CodeBuild actions that initiate and describe CodeBuild jobs through CodeSeeder.

These ADDF-specific IAM roles are created as part of the ADDF-bootstrapping process. For more information, see *Bootstrap AWS Account(s)* in the [ADDF Deployment Guide](https://github.com/awslabs/autonomous-driving-data-framework/blob/main/docs/deployment_guide.md) (GitHub).

All cross-account permissions are set up according to the principle of least privilege. If one target account is compromised, there is minimal or no impact to the other ADDF AWS accounts.

In the case of a single-account architecture for ADDF, the role relationships remain the same. They just collapse into a single AWS account.
