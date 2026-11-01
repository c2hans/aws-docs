---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/terraform-aws-provider-best-practices/next-steps.html
---

# Next steps
<a name="next-steps"></a>

Consider the following next steps after reading this guide:
+ If you have an existing Terraform code base, review your configuration and identify areas for improvement based on the recommendations in this guide. For example, review best practices for implementing remote backends, separating code into modules, and using version pinning, and validate these in your configuration.
+ If you don't have an existing Terraform code base, use these best practices when you structure your new configuration. Apply the guidance on state management, authentication, and code structure from the beginning.
+ Explore the HashiCorp community modules referenced in this guide to determine whether they simplify your architecture patterns. The modules provide higher levels of abstraction, so you don't have to rewrite common resources.
+ Enable formatting, linting, security scans, policy checks, and automated tests to reinforce the best practices around security, compliance, and code quality. Tools such as TFLint, Trivy, Checkov, and `terraform test` can help.
+ Review the latest AWS Provider documentation and changelog to see if there are any new resources or functionality that could help optimize your Terraform usage. Stay up to date on new versions of the AWS Provider.
+ For additional guidance, see the [Terraform documentation](https://developer.hashicorp.com/terraform/language), [best practices guide](https://developer.hashicorp.com/terraform/cloud-docs/recommended-practices), and [style guide](https://developer.hashicorp.com/terraform/language/style) on the HashiCorp website.
