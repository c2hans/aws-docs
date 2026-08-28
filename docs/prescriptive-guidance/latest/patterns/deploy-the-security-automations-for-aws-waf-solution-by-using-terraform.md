---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-the-security-automations-for-aws-waf-solution-by-using-terraform.html
---

# Deploy the Security Automations for AWS WAF solution by using Terraform
<a name="deploy-the-security-automations-for-aws-waf-solution-by-using-terraform"></a>

*Dr. Rahul Sharad Gaikwad and Tamilselvan P, Amazon Web Services*

## Summary
<a name="deploy-the-security-automations-for-aws-waf-solution-by-using-terraform-summary"></a>

AWS WAF is a web application firewall that helps protect applications from common exploits by using customizable rules, which you define and deploy in *web access control lists* (ACLs). Configuring AWS WAF rules can be challenging, especially for organizations that do not have dedicated security teams. To simplify this process, Amazon Web Services (AWS) offers the [Security Automations for AWS WAF](https://aws.amazon.com/solutions/implementations/security-automations-for-aws-waf/) solution, which automatically deploys a single web ACL with a set of AWS WAF rules that filters web-based attacks. During Terraform deployment, you can specify which protective features to include. After you deploy this solution, AWS WAF inspects web requests to existing Amazon CloudFront distributions or Application Load Balancers, and blocks any requests that don’t match the rules.

The Security Automations for AWS WAF solution can be deployed by using AWS CloudFormation according to the instructions in the [Security Automations for AWS WAF Implementation Guide](https://docs.aws.amazon.com/solutions/latest/security-automations-for-aws-waf/overview.html). This pattern provides an alternative deployment option for organizations that use HashiCorp Terraform as their preferred infrastructure as code (IaC) tool to provision and manage their cloud infrastructure. When you deploy this solution, Terraform automatically applies the changes in the cloud and deploys and configures the AWS WAF settings and protective features.

## Prerequisites and limitations
<a name="deploy-the-security-automations-for-aws-waf-solution-by-using-terraform-prereqs"></a>

**Prerequisites**
+ An active AWS account.
+ AWS Command Line Interface (AWS CLI) version 2.4.25 or later, installed and configured with necessary permissions. For more information, see [Getting started](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) (AWS CLI documentation).
+ Terraform version 1.1.9 or later, installed and configured. For more information, see [Install Terraform](https://learn.hashicorp.com/tutorials/terraform/install-cli) (Terraform documentation).

## Architecture
<a name="deploy-the-security-automations-for-aws-waf-solution-by-using-terraform-architecture"></a>

**Target architecture**

This pattern deploys the Security Automations for AWS WAF solution. For more information about the target architecture, see [Architecture overview](https://docs.aws.amazon.com/solutions/latest/security-automations-for-aws-waf/overview.html) in the *Security Automations for AWS WAF Implementation Guide*. For more information about the AWS Lambda automations in this deployment, the Application log parser, the AWS WAF log parser, the IP lists parser, and the Access handler, see [Component details](https://docs.aws.amazon.com/solutions/latest/security-automations-for-aws-waf/appendix-b.html) in the *Security Automations for AWS WAF Implementation Guide*.

**Terraform deployment**

When you run `terraform apply`, Terraform does the following:

1. Terraform creates AWS Identity and Access Management (IAM) roles and Lambda functions based on the inputs from the **testing.tfvars** file.

1. Terraform creates AWS WAF ACL rules and IP sets based on the inputs from the **testing.tfvars **file.

1. Terraform creates the Amazon Simple Storage Service (Amazon S3) buckets, Amazon EventBridge rules, AWS Glue database tables, and Amazon Athena work groups based on the inputs from the **testing.tfvars **file.

1. Terraform deploys the AWS CloudFormation stack to provision the custom resources.

1. Terraform creates the Amazon API Gateway resources based on the given inputs from **testing.tfvars **file.

**Automation and scale**

You can use this pattern to create AWS WAF rules for multiple AWS accounts and AWS Regions to deploy the Security Automations for AWS WAF solution throughout your AWS Cloud environment.

## Tools
<a name="deploy-the-security-automations-for-aws-waf-solution-by-using-terraform-tools"></a>

**AWS services**
+ [AWS Command Line Interface (AWS CLI)](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) is an open-source tool that helps you interact with AWS services through commands in your command-line shell.
+ [AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/what-is-aws-waf.html) is a web application firewall that helps you monitor HTTP and HTTPS requests that are forwarded to your protected web application resources.

**Other services**
+ [Git](https://git-scm.com/docs) is an open-source, distributed version control system.
+ [HashiCorp Terraform](https://www.terraform.io/docs) is a command-line interface application that helps you use code to provision and manage cloud infrastructure and resources.

**Code repository**

The code for this pattern is available in the GitHub [AWS WAF Automation Using Terraform](https://github.com/aws-samples/aws-waf-automation-terraform-samples) repository.

## Best practices
<a name="deploy-the-security-automations-for-aws-waf-solution-by-using-terraform-best-practices"></a>
+ Put static files in separate Amazon S3 buckets.
+ Avoid hardcoding variables.
+ Limit the use of custom scripts.
+ Adopt a naming convention.

## Epics
<a name="deploy-the-security-automations-for-aws-waf-solution-by-using-terraform-epics"></a>

### Set up your local workstation
<a name="set-up-your-local-workstation"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Install Git. | Follow the instructions in [Getting started](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) (Git website) to install Git on your local workstation. | DevOps engineer |
| Clone the repository. | On your local workstation, enter the following command to clone the code repository:<pre>git clone https://github.com/aws-samples/aws-waf-automation-terraform-samples.git</pre> | DevOps engineer |
| Update the variables. | 1. Navigate into the cloned directory by entering the following command:<pre>cd terraform-aws-waf-automation</pre><br />2. In any text editor, open the **testing.tfvars** file.<br />3. Update the values of the variables in the **testing.tfvars** file.<br />4. Save and close the file. | DevOps engineer |

### Provision the target architecture using Terraform
<a name="provision-the-target-architecture-using-terraform"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Initialize the Terraform configuration. | Enter the following command to initialize your working directory that contains the Terraform configuration files:<pre>terraform init</pre> | DevOps engineer |
| Preview the Terraform plan. | Enter the following command. Terraform evaluates the configuration files to determine the target state for the declared resources. It then compares the target state against the current state and creates a plan:<pre>terraform plan -var-file="testing.tfvars"</pre> | DevOps engineer |
| Verify the plan. | Review the plan and confirm that it configures the required architecture in your target AWS account. | DevOps engineer |
| Deploy the solution. | 1. Enter the following command to apply the plan:<pre>terraform apply -var-file="testing.tfvars"</pre><br />2. Enter `yes` to confirm. Terraform creates, updates, or destroys infrastructure to achieve the target state declared in the configuration files. For more information about the sequence, see *Terraform deployment* in the [Architecture](#deploy-the-security-automations-for-aws-waf-solution-by-using-terraform-architecture) section of this pattern. | DevOps engineer |

### Validate and clean up
<a name="validate-and-clean-up"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Verify the changes. | 1. In the Terraform console, verify that the outputs match the expected results.<br />2. Sign in to the AWS Management Console.<br />3. Verify the outputs in the Terraform console have been successfully deployed in your AWS account. | DevOps engineer |
| (Optional) Clean up the infrastructure. | If you want to remove all resources and configuration changes made by this solution, do the following:1. In the Terraform console, enter the following command:<pre>terraform destroy -var-file="testing.tfvars"</pre><br />2. Enter `yes` to confirm. | DevOps engineer |

## Troubleshooting
<a name="deploy-the-security-automations-for-aws-waf-solution-by-using-terraform-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| `WAFV2 IPSet: WAFOptimisticLockException` error | If you** **receive this error when you run the `terraform destroy` command, you must manually delete the IP sets. For instructions, see [Deleting an IP set](https://docs.aws.amazon.com/waf/latest/developerguide/waf-ip-set-deleting.html) (AWS WAF documentation). |

## Related resources
<a name="deploy-the-security-automations-for-aws-waf-solution-by-using-terraform-resources"></a>

**AWS references**
+ [Security Automations for AWS WAF Implementation Guide](https://docs.aws.amazon.com/solutions/latest/security-automations-for-aws-waf/welcome.html)
+ [Security Automations for AWS WAF](https://aws.amazon.com/solutions/implementations/security-automations-for-aws-waf/) (AWS Solutions Library)
+ [Security Automations for AWS WAF FAQ](https://aws.amazon.com/solutions/implementations/security-automations-for-aws-waf/resources/#FAQ)

**Terraform references**
+ [Terraform backend configuration](https://developer.hashicorp.com/terraform/language/backend)
+ [Terraform AWS Provider - Documentation and Usage](https://registry.terraform.io/providers/hashicorp/aws/latest/docs)
+ [Terraform AWS Provider](https://github.com/hashicorp/terraform-provider-aws) (GitHub repository)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
