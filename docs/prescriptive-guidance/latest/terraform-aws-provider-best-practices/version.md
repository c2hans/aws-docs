---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/terraform-aws-provider-best-practices/version.html
---

# Best practices for AWS Provider version management
<a name="version"></a>

Managing versions of the AWS Provider and associated Terraform modules carefully helps maintain stability. This section outlines best practices around version constraints, locking, and upgrades.

## Commit the dependency lock file
<a name="commit-the-dependency-lock-file.fe6307de-9178-544e-b113-96011faf3de3"></a>

`terraform init` writes the exact provider versions it selects, and their checksums, to the [dependency lock file](https://developer.hashicorp.com/terraform/language/files/dependency-lock), `.terraform.lock.hcl`. Commit this file in every root module. Later runs, on any machine, install the same versions until you deliberately upgrade:
+ To move to a newer version that the constraints allow, run `terraform init -upgrade`, review the change to the lock file, and commit it.
+ If you change a version constraint so that it excludes the locked version, `terraform init` fails until you run it with `-upgrade`.
+ In CI, run `terraform init -lockfile=readonly` so that a job fails instead of changing the lock file.
+ The lock file records checksums for the platforms where `init` ran. If developers and CI use different operating systems, add the other platforms' checksums: `terraform providers lock -platform=linux_amd64 -platform=linux_arm64 -platform=darwin_arm64`.

### Add automated version checks
<a name="version-check"></a>

Add version checks for Terraform providers in your CI/CD pipelines to validate version pinning, and fail builds if the version is undefined.
+ Add [TFLint](https://github.com/terraform-linters/tflint) checks in CI/CD pipelines. The `terraform_required_version` and `terraform_required_providers` rules report modules that don't declare their Terraform version or provider versions. The [TFLint ruleset for the AWS Provider](https://github.com/terraform-linters/tflint-ruleset-aws) adds rules that detect possible errors and check for best practices about AWS resources.
+ Fail CI runs that detect unpinned provider versions to prevent implicit upgrades from reaching production.

#### Automate upgrade proposals
<a name="automate-upgrade-proposals.5ffd751d-247f-555c-b714-236abdc7c586"></a>

Use a dependency update tool such as [Dependabot](https://docs.github.com/en/code-security/concepts/supply-chain-security/dependabot-version-updates) or [Renovate](https://docs.renovatebot.com/) to open pull requests when new provider or module versions are released. Each pull request then runs your normal checks and tests. Before you merge one, check that the updated lock file has checksums for every platform that runs Terraform. If it doesn't, add them with `terraform providers lock`.

#### Upgrade major versions in steps
<a name="upgrade-major-versions-in-steps.10e39eb8-02d4-5d94-abe9-0517d6e4e369"></a>

Major versions of the AWS Provider remove deprecated arguments and resources. For each major upgrade, follow the provider's upgrade guide, such as the [version 6 upgrade guide](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/guides/version-6-upgrade), in this order:

1. Upgrade to the latest release of your current major version.

1. Run `terraform plan`, and fix every deprecation warning until the plan is clean.

1. Change the version constraint, for example from `~> 5.0` to `~> 6.0`, and run `terraform init -upgrade`.

1. Run `terraform plan` again. Fix any differences, and any deprecation warnings that only the new version reports.

1. Apply in non-production environments first, and then in production.

### Monitor new releases
<a name="new-releases"></a>
+ Monitor provider release notes and changelog feeds. Get notifications on new major/minor releases.
+ Assess release notes for potentially breaking changes and evaluate their impact on your existing infrastructure.
+ Upgrade minor versions in non-production environments first to validate them before updating the production environment.

By automating version checks in pipelines and monitoring new releases, you can catch unsupported upgrades early and give your teams time to evaluate the impact of new major/minor releases before you update production environments.

### Contribute to providers
<a name="contribute-providers"></a>

Actively contribute to the HashiCorp AWS Provider by reporting defects or requesting features in GitHub issues:
+ Open well-documented issues on the AWS Provider repository to detail any bugs you encountered or functionality that is missing. Provide reproducible steps.
+ Request and vote on enhancements to expand the capabilities of the AWS Provider for managing new services.
+ When you contribute a fix or an enhancement, link your pull request to the issue that it addresses.
+ Follow the contribution guidelines in the repository for coding conventions, testing standards, and documentation.

By contributing to the providers you use, you can provide direct input into their roadmap and help improve their quality and capabilities for all users.
