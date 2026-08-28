---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/getting-started-terraform/introduction.html
---

# Getting started with Terraform: Guidance for AWS CDK and AWS CloudFormation experts
<a name="introduction"></a>

*Steven Guggenheimer, Amazon Web Services*

If your experience with provisioning cloud resources exclusively lies within the realm of AWS, you might have limited experience with infrastructure as code (IaC) tools beyond the [AWS Cloud Development Kit (AWS CDK)](https://docs.aws.amazon.com/cdk/v2/guide/home.html) and [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html). In fact, similar tools, such as Hashicorp Terraform, might be completely unfamiliar to you. However, the deeper you get into your cloud journey, the more inevitable it becomes that you'll encounter Terraform. It will be decidedly to your advantage to be familiar with its core concepts.

While Terraform, the AWS CDK, and CloudFormation achieve similar goals and share many core concepts, there are quite a few differences. You might not be prepared for these differences if you're approaching Terraform for the first time. After all, AWS CDK and CloudFormation stacks are all based within AWS accounts, so in that way, they have a direct relationship with most of the resources that they maintain. Terraform is not based within any single cloud provider's environment. This gives it the flexibility to support various different providers, but it must maintain resources from what amounts to a remote location.

This guide helps demystify the core concepts behind Terraform to help you handle any IaC challenge that comes your way. It focuses on how Terraform uses concepts, such as providers, modules, and state files, to provision resources. It also contrasts Terraform concepts with how the AWS CDK and CloudFormation perform similar operations.

**Note**
The AWS CDK helps developers deploy CloudFormation stacks by using programmatic coding languages. After you run `cdk synth`, your code is converted into CloudFormation templates. From that point forward, the process is identical between the AWS CDK and CloudFormation. For the sake of brevity, this guide usually refers to the AWS IaC process in CloudFormation terms, but the comparisons are just as apt for the AWS CDK.

## CloudFormation and Terraform terminology
<a name="cf-nshort-and-terraform-terminology"></a>

When comparing Terraform with the AWS CDK and CloudFormation, reconciling the IaC core concepts can be difficult because of the inconsistent terminology used to describe them. The following are these terms and how this guide will refer to them:
+ **Stack*** – *A *stack* is IaC that is deployed into a CI/CD pipeline and trackable as a single unit*. *Although this term is common in CloudFormation, Terraform does not really use this term. A Terraform stack is a deployed root module with all of its child modules. However, in order to avoid confusion with the term *module*, this guide uses the term *stack* to describe a single deployment for both tools.
+ **State** - The *state* is all currently tracked resources and their current configurations within an IaC deployment stack*.* As described in the [Understanding Terraform states and backends](states-and-backends.md) section, Terraform uses the term *state* more than CloudFormation. This is because maintaining state is more visible in Terraform, but tracking and updating the state is equally important for CloudFormation.
+ **IaC file – **An *IaC file* is a single file that contains infrastructure as code (IaC) language*.* CloudFormation refers to a single CloudFormation file as a *template*. However [templates ](https://developer.hashicorp.com/terraform/language/expressions/strings#string-templates)and [template files](https://developer.hashicorp.com/terraform/language/functions/templatefile) in Terraform are something completely different. The equivalent to a CloudFormation template in Terraform is called a *configuration file*. To minimize confusion in this guide, the term *file *or *IaC file* is used to refer to both CloudFormation templates and Terraform configuration files.

The following table compares the terminology used for CloudFormation and Terraform. The intent of this table is to show similarities. These are not one-to-one comparisons. Each concept differs at least slightly between CloudFormation and Terraform. Concepts are explained in depth in relevant sections of this guide.

|
|
| CloudFormation term | Terraform term | Section of this guide |
| --- |--- |--- |
| CDK interfaces (such as *IBucket)* | Data source | [Understanding Terraform data sources](data-sources.md) |
| Change set | Plan | [Understanding Terraform modules](modules.md) |
| Condition functions | Conditional expressions | [Understanding Terraform functions, expressions, and meta-arguments](functions-expressions.md#functions) |
| `DependsOn` attribute | `depends_on` meta-argument | [Understanding Terraform functions, expressions, and meta-arguments](functions-expressions.md#functions) |
| Intrinsic functions | Functions | [Understanding Terraform functions, expressions, and meta-arguments](functions-expressions.md#functions) |
| Modules | Modules | [Understanding Terraform modules](modules.md) |
| Outputs | Output values | [Understanding Terraform variables, local values, and outputs](variables-locals-outputs.md#variables) |
| Parameters | Variables | [Understanding Terraform variables, local values, and outputs](variables-locals-outputs.md#variables) |
| Registry | Providers | [Understanding Terraform providers](providers.md) |
| Template | Configuration file | All |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
