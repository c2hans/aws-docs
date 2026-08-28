---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/terraform-data-limitations/best-practices.html
---

# Best practices
<a name="best-practices"></a>

Follow these guidelines when you use Terraform to automate your DevOps tasks on AWS.

Do's:
+ Use `terraform_data` for custom scripts and provisioners.
+ Use triggers to control resource recreation.
+ Implement a `local-exec` provisioner for complex setup tasks.
+ Use `depends_on` for explicit dependency management.
+ Store state for idempotent operations.
+ Implement proper error handling in scripts.
+ Validate and sanitize inputs for security.
+ Log output for troubleshooting.
+ Use connection blocks for remote execution.
+ When you implement features with `terraform_data`, consider it a temporary solution. Regularly check if the provider has added native support for that functionality. When the provider introduces native capability for your `terraform_data` implementation, switch to the provider's official solution.

Don'ts:
+ Don't overuse `terraform_data` as a primary resource management tool.
+ Avoid storing sensitive information directly in scripts.
+ Don't ignore error handling in provisioners.
+ Avoid complex, long-running scripts. Don't create null resources with multiple responsibilities and excessively complex workflows.
+ Don't create unnecessary dependencies. Follow state management principles and add only necessary triggers and `depends_on` conditions in your code.
+ Don't use `terraform_data` for core infrastructure management. Don't replace your standard resource management with custom resources.
+ Don't hardcode credentials or sensitive data.
+ Don't ignore security best practices.
+ Don't skip input validation.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
