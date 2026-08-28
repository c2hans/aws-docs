---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/terraform-aws-provider-best-practices/version.html
---

# Best practices for AWS Provider version management
<a name="version"></a>

Carefully managing versions of the AWS Provider and associated Terraform modules is critical for stability. This section outlines best practices around version constraints and upgrades.

## Add automated version checks
<a name="version-check"></a>

Add version checks for Terraform providers in your CI/CD pipelines to validate version pinning, and fail builds if the version is undefined.
+ Add [TFLint](https://github.com/terraform-linters/tflint) checks in CI/CD pipelines to scan for provider versions that don't have pinned major/minor version constraints defined. Use the [TFLint ruleset plugin for Terraform AWS Provider](https://github.com/terraform-linters/tflint-ruleset-aws), which provides rules for detecting possible errors and checks for best practices about AWS resources.
+ Fail CI runs that detect unpinned provider versions to prevent implicit upgrades from reaching production.

## Monitor new releases
<a name="new-releases"></a>
+ Monitor provider release notes and changelog feeds. Get notifications on new major/minor releases.
+ Assess release notes for potentially breaking changes and evaluate their impact on your existing infrastructure.
+ Upgrade minor versions in non-production environments first to validate them before updating the production environment.

By automating version checks in pipelines and monitoring new releases, you can catch unsupported upgrades early and give your teams time to evaluate the impact of new major/minor releases before you update production environments.

## Contribute to providers
<a name="contribute-providers"></a>

Actively contribute to HashiCorp AWS Provider by reporting defects or requesting features in GitHub issues:
+ Open well-documented issues on the AWS Provider repository to detail any bugs you encountered or functionality that is missing. Provide reproducible steps.
+ Request and vote on enhancements to expand the capabilities of the AWS Provider for managing new services.
+ Reference issued pull requests when you contribute proposed fixes for provider defects or enhancements. Link to related issues.
+ Follow the contribution guidelines in the repository for coding conventions, testing standards, and documentation.

By giving back to the providers you use, you can provide direct input into their roadmap and help improve their quality and capabilities for all users.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
