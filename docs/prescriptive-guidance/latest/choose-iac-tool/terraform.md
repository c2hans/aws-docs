---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/choose-iac-tool/terraform.html
---

# Terraform
<a name="terraform"></a>

[HashiCorp Terraform](https://developer.hashicorp.com/terraform) is an infrastructure as code (IaC) tool that help you manage your cloud infrastructure. Using Terraform, you can define both cloud and on-premises resources in configuration files that you can version, reuse, and share. You can then use a consistent workflow to provision and manage all of your infrastructure throughout its lifecycle.

Developers use a high-level configuration language called [Terraform language](https://developer.hashicorp.com/terraform/language). The native, low-level syntax of Terraform language is [HashiCorp Configuration Language (HCL)](https://developer.hashicorp.com/terraform/language/syntax/configuration). Terraform language is designed to be easy for humans to read and write. You use Terraform language to describe the desired end state of the cloud or on-premises infrastructure. Terraform then generates a plan for reaching that end state, and you execute the plan to provision the infrastructure.

**Advantages of using Terraform:**
+ Terraform is platform agnostic. You can use it with any cloud services provider. You can configure, test, and deploy infrastructure across AWS and many other cloud providers. If your organization uses multiple cloud providers, Terraform can be a single, unified, consistent solution to manage cloud infrastructure. For more information about multi-cloud support, see [Multi-cloud provisioning](https://www.terraform.io/use-cases/multi-cloud-deployment) on the Terraform website.
+ Terraform is agentless. It doesn't require any software to be installed on the managed infrastructure.
+ Terraform modules are a powerful way to reuse code and stick to the *Don't Repeat Yourself (DRY)* principle. For example, you might have a specific configuration for an application which contains an Amazon Elastic Compute Cloud (Amazon EC2) instance, Amazon Elastic Block Store (Amazon EBS) volumes, and other resources that are logically grouped. If you need to create multiple copies of this configuration or application, you can package the resources into a Terraform module and create multiple instances of the module rather than copying the entire code multiple times. These modules can help you to organize, encapsulate, and reuse configurations. They also provide consistency and ensure best practices.
+ Terraform is able to [detect and manage drift](https://www.hashicorp.com/blog/detecting-and-managing-drift-with-terraform) (Terraform blog post) in your infrastructure. For example, if resources managed by Terraform are modified outside of Terraform, you can detect the drift and restore them to the desired state by using the Terraform CLI.

**Disadvantages of using Terraform:**
+ Support for new features or new resources related to any cloud provider might not be available.
+ Terraform does not automatically manage your state like AWS CloudFormation. It is stored by default in a local file, but you can also store it remotely in an [Amazon S3 bucket](https://developer.hashicorp.com/terraform/language/settings/backends/s3)  or through [Terraform Enterprise](https://developer.hashicorp.com/terraform/enterprise).
+ The Terraform state can contain sensitive data, such as database passwords, which can pose security concerns. It's best practice to encrypt your state file, store it remotely, enable file versioning on it, and use least privileges for read and write operations on it. For more information, see [Securing sensitive data by using AWS Secrets Manager and HashiCorp Terraform](https://docs.aws.amazon.com/prescriptive-guidance/latest/secure-sensitive-data-secrets-manager-terraform/introduction.html).
+ In August 2023, Hashicorp made an announcement that it would no longer be licensed as open source under the [Mozilla Public License](https://www.mozilla.org/en-US/MPL/). Instead, it is now licensed under the [Business Source License](https://github.com/hashicorp/terraform/blob/b145fbcaadf0fa7d0e7040eac641d9aef2a26433/LICENSE).
