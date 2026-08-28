---
source_url: https://docs.aws.amazon.com/cdk/v2/guide/security.html
---

This is the AWS CDK v2 Developer Guide. The older CDK v1 entered maintenance on June 1, 2022 and ended support on June 1, 2023.

# Security for the AWS Cloud Development Kit (AWS CDK)
<a name="security"></a>

## The AWS Shared Responsibility Model
<a name="the_shared_aws_shared_responsibility_model"></a>

Cloud security at Amazon Web Services (AWS) is the highest priority. As an AWS customer, you benefit from a data center and network architecture that is built to meet the requirements of the most security-sensitive organizations. Security is a shared responsibility between AWS and you. The [Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/) describes this as Security of the Cloud and Security in the Cloud.

 **Security of the Cloud** – AWS is responsible for protecting the infrastructure that runs all of the services offered in the AWS Cloud and providing you with services that you can use securely. Our security responsibility is the highest priority at AWS, and the effectiveness of our security is regularly tested and verified by third-party auditors as part of the [AWS Compliance Programs](https://aws.amazon.com/compliance/programs/).

 **Security in the Cloud** – Your responsibility is determined by the AWS service you are using, and other factors including the sensitivity of your data, your organization’s requirements, and applicable laws and regulations.

The AWS CDK follows the [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/) through the specific Amazon Web Services (AWS) services it supports. For AWS service security information, see the [AWS service security documentation page](https://docs.aws.amazon.com/security/?id=docs_gateway#aws-security) and [AWS services that are in scope of AWS compliance efforts by compliance program](https://aws.amazon.com/compliance/services-in-scope/).

## Security of the AWS CDK
<a name="security_of_the_shared_aws_cdk"></a>

Given a program written in a general purpose programming language that describes the shape of your desired infrastructure, the AWS CDK generates a set of deployable artifacts that will create that infrastructure.

### Security of default generated infrastructure
<a name="_security_of_default_generated_infrastructure"></a>

 *(AWS' responsibility)* Constructs in the AWS Construct Library are designed to generate infrastructure that does not allow data disclosure, data manipulation, elevation of privilege or other tampering by unauthorized third parties (unless explicitly configured otherwise, which is in line with the [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/)).

Any violation of this expectation can be reported [through the company-wide vulnerability reporting mechanisms](https://aws.amazon.com/security/vulnerability-reporting/).

### Execution in a trusted environment
<a name="_execution_in_a_trusted_environment"></a>

 *(Your responsibility)* CDK is designed to run in a *trusted environment* with *trusted inputs*. It is your responsibility to ensure user code, any libraries loaded into memory (including those downloaded from the Internet via a package manager like NPM or pip), or inputs into the CDK construct libraries are trustworthy. The CDK cannot protect you from malicious intent.

You should not use CDK in an environment where untrusted authors write parts of the code that drives a CDK application, or where untrusted parties control inputs to CDK constructs without validation.

### Compliance verification is an external process
<a name="_compliance_verification_is_an_external_process"></a>

 *(Your responsibility)* Because of the unlimited expressivity afforded by a general purpose programming language, custom CDK constructs cannot *guarantee* an unbypassable compliance with security policies. CDK has mechanisms to [shift left compliance checks](compliance-validation.md), and mechanisms that can [help developers meet compliance requirements with minimal effort](blueprints.md); but a determined enough developer will always be able to bypass the output of the specially designed constructs.

If you need compliance guarantees, impose them via a process external to the CDK application like [CloudFormation Hooks](https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/what-is-cloudformation-hooks.html), or a separate CloudFormation template validation step in the CI Pipeline.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Cloud Development Kit. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
