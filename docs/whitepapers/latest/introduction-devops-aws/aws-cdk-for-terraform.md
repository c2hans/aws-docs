---
source_url: https://docs.aws.amazon.com/whitepapers/latest/introduction-devops-aws/aws-cdk-for-terraform.html
---

# AWS Cloud Development Kit for Terraform
<a name="aws-cdk-for-terraform"></a>

Built on top of the open source [JSII library](https://aws.github.io/jsii/), [CDK for Terraform](https://developer.hashicorp.com/terraform/cdktf) (CDKTF) allows you to write Terraform configurations in your choice of C\#, Python, TypeScript, Java, or Go and still benefit from the full ecosystem of Terraform providers and modules. You can import any existing provider or module from the Terraform Registry into your application, and CDKTF will generate resource classes for you to interact with in your target programming language.

With CDKTF, developers can set up their IaC without context switching from their familiar programming language, using the same tooling and syntax to provision infrastructure resources similar to the application business logic. Teams can collaborate in familiar syntax, while still using the power of the Terraform ecosystem and deploying their infrastructure configurations via established Terraform deployment pipelines.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
