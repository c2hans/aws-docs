---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/terraform-aws-provider-best-practices/next-steps.html
---

# Next steps
<a name="next-steps"></a>

Here are some potential next steps after reading this guide:
+ If you have an existing Terraform code base, review your configuration and identify areas that could be improved based on the recommendations that are provided in this guide. For example, review best practices for implementing remote backends, separating code into modules, using version pinning, and so on, and validate these in your configuration.
+ If you don't have an existing Terraform code base, use these best practices when you structure your new configuration. Follow the advice around state management, authentication, code structure, and so on from the beginning.
+ Try using some of the HashiCorp community modules referenced in this guide to see if they simplify your architecture patterns. The modules allow higher levels of abstraction, so you don't have to rewrite common resources.
+ Enable linting, security scans, policy checks, and automated testing tools to reinforce some of the best practices around security, compliance, and code quality. Tools such as TFLint, tfsec, and Checkov can help.
+ Review the latest AWS Provider documentation to see if there are any new resources or functionality that could help optimize your Terraform usage. Stay up to date on new versions of the AWS Provider.
+ For additional guidance, see the [Terraform documentation](https://developer.hashicorp.com/terraform/language), [best practices guide](https://developer.hashicorp.com/terraform/cloud-docs/recommended-practices), and [style guide](https://developer.hashicorp.com/terraform/language/style) on the HashiCorp website.
