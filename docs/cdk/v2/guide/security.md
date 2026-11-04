---
source_url: https://docs.aws.amazon.com/cdk/v2/guide/security.html
---

# Security for the AWS Cloud Development Kit (AWS CDK)
<a name="security"></a>

## The AWS Shared Responsibility Model
<a name="the_shared_aws_shared_responsibility_model"></a>

Cloud security at Amazon Web Services (AWS) is the highest priority. As an AWS customer, you benefit from a data center and network architecture that is built to meet the requirements of the most security-sensitive organizations. Security is a shared responsibility between AWS and you. The [Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/) describes this as Security of the Cloud and Security in the Cloud.

 **Security of the Cloud** – AWS is responsible for protecting the infrastructure that runs all of the services offered in the AWS Cloud and providing you with services that you can use securely. Our security responsibility is the highest priority at AWS, and the effectiveness of our security is regularly tested and verified by third-party auditors as part of the [AWS Compliance Programs](https://aws.amazon.com/compliance/programs/).

 **Security in the Cloud** – Your responsibility is determined by the AWS service you are using, and other factors including the sensitivity of your data, your organization’s requirements, and applicable laws and regulations.

The AWS Cloud Development Kit (AWS CDK) follows the [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/) through the specific Amazon Web Services (AWS) services it supports. For AWS service security information, see the [AWS service security documentation page](https://docs.aws.amazon.com/security/?id=docs_gateway#aws-security) and [AWS services that are in scope of AWS compliance efforts by compliance program](https://aws.amazon.com/compliance/services-in-scope/).

Given a program written in a general purpose programming language that describes the shape of your desired infrastructure, the AWS CDK generates a set of deployable artifacts that will create that infrastructure.

## Security of default generated infrastructure
<a name="security-generated-infra"></a>

 *(AWS' responsibility)* Constructs in the AWS Construct Library are designed to generate infrastructure that does not allow data disclosure, data manipulation, elevation of privilege or other tampering by external parties (meaning unauthenticated identities or identities from different AWS Accounts; unless explicitly configured otherwise, which is in line with the [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/)).

Any violation of this expectation can be reported [through the company-wide vulnerability reporting mechanisms](https://aws.amazon.com/security/vulnerability-reporting/).

## Run CDK code in a trusted execution environment
<a name="security-execution-environment"></a>

 *(Your responsibility)* CDK is designed to run in a *trusted environment* with *trusted inputs*. It is your responsibility to ensure user code, any libraries loaded into memory (including those downloaded from the Internet via a package manager like NPM or pip), or inputs into the CDK construct libraries are trustworthy. The CDK cannot protect you from malicious intent.

You should not use CDK in an environment where untrusted authors write parts of the code that drives a CDK application, or where untrusted parties control inputs to CDK constructs without validation.

Similarly, you should not deploy cloud assemblies from sources that you do not trust. Synthesizing a CDK app produces a cloud assembly (the `cdk.out` directory by default). It’s possible to deploy a previously synthesized cloud assembly from a different source; for example, `cdk deploy --app /downloaded/file/path/cdk.out`. Only deploy a cloud assembly that you produced yourself or that comes from a trusted source.

## Deploy to a trusted environment
<a name="security-deployment-environment"></a>

 *(Your responsibility)* CDK treats the AWS [Account as the security boundary](https://docs.aws.amazon.com/accounts/latest/reference/accounts-welcome.html). This is consistent with the AWS [Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/aws-account-management-and-separation.html). CDK cannot guarantee that all synthesized infrastructure is secure against actors with permissions in the same Account. Some examples of scenarios that CDK cannot guard against include, but are not limited to, the following:
+ CDK may create AWS [Lambda-based CloudFormation Custom Resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-custom-resources.html) to perform actions at deployment time. Any identity with `lambda:InvokeFunction` permissions can trigger such a function and effectively assume the function’s execution role permissions;
+ CloudFormation Stack deployments can replace resource policies on resources owned by another Stack;
+  AWS Step Functions-backed Custom Resources hold a signed S3 URL secret in their State Machine State. Anyone with `stepfunctions:DescribeExecution` permissions can read this secret.

You should not use CDK in an environment where untrusted identities might perform AWS CloudFormation deployments, or where untrusted identities have AWS Identity and Access Management (IAM) permissions that might interact with resources created by CDK.

## Compliance verification is an external process
<a name="security-compliance-verification"></a>

 *(Your responsibility)* Because of the unlimited expressivity afforded by a general purpose programming language, custom CDK constructs cannot *guarantee* an unbypassable compliance with security policies. CDK has mechanisms to [shift left compliance checks](compliance-validation.md), and mechanisms that can [help developers meet compliance requirements with minimal effort](blueprints.md); but a determined enough developer will always be able to bypass the output of the specially designed constructs.

If you need compliance guarantees, impose them via a process external to the CDK application like [CloudFormation Hooks](https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/what-is-cloudformation-hooks.html), or a separate CloudFormation template validation step in the CI Pipeline.
