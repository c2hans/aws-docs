---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/terraform-aws-provider-best-practices/structure.html
---

# Best practices for code base structure and organization
<a name="structure"></a>

Proper code base structure and organization becomes increasingly important as Terraform usage grows across large teams and organizations. A structured, maintainable code base enables collaboration at scale. This section provides recommendations on Terraform modularity, naming conventions, documentation, and coding standards that support quality and consistency.

Guidance includes breaking configuration into reusable modules by environment and components, establishing naming conventions by using prefixes and suffixes, documenting modules and clearly explaining inputs and outputs, and applying consistent formatting rules by using automated style checks.

Additional best practices cover logically organizing modules and resources in a structured hierarchy, cataloging public and private modules in documentation, and abstracting unnecessary implementation details in modules to simplify usage.

Applying these guidelines helps teams scale Terraform usage consistently and reduces the long-term cost of maintaining a growing infrastructure code base.

## Implement a standard repository structure
<a name="repo-structure"></a>

We recommend that you implement the following repository layout. Standardizing on these practices across modules improves discoverability, transparency, organization, and reliability while enabling reuse across many Terraform configurations.
+ **Root directory:** In a root module, this is where you run `terraform plan` and `terraform apply`. In a [reusable module](https://developer.hashicorp.com/terraform/language/modules/develop), it's what callers point their `source` at. Split a large design into nested modules that match parts of the architecture, such as the network or the data tier, instead of one module for each resource type.
+ **README.md:** Every module needs one, including nested modules that other teams use. Say what the module is for, what it creates, and what it expects from the caller. A diagram of the resources helps reviewers. [terraform-docs](https://github.com/terraform-docs/terraform-docs) can generate the inputs and outputs tables from the code, so they don't drift from it.
+ **main.tf:** Resources and calls to nested modules. A small module needs no other resource files.
+ **variables.tf** and **outputs.tf:** Inputs and outputs, each with a short `description`, because the description becomes the module's documentation. For details, see [variable blocks](https://developer.hashicorp.com/terraform/language/values/variables) and [output blocks](https://developer.hashicorp.com/terraform/language/values/outputs) in the HashiCorp documentation.
+ Give every variable a `type`.
+ A variable with a `default` is optional. The default must be a literal value; it can't refer to other objects in the configuration. To make a variable required, leave out the default, and consider setting `nullable = false`.
+ Set a default when one value suits every environment, such as `log_retention_days = 30`. Leave out the default when the right value depends on the environment, such as `vpc_id` or `account_id`, so that each caller has to set it.
+ Use an empty string or an empty list as a default only when the AWS API accepts an empty value for that setting.
+ Expose a variable only when callers have a concrete reason to change the value. You can add an optional variable later without breaking callers, but removing a variable breaks every caller that sets it. For a literal that you repeat inside the module, use a local value instead of a variable.
+ Build outputs from resource attributes, not from input variables. An output such as `value = aws_s3_bucket.this.id` makes the caller's resources depend on the bucket, so Terraform creates the bucket first. An output that returns `var.bucket_name` carries no dependency, so a caller's resources can be created before the bucket exists. For more information, see [Create resource dependencies](https://developer.hashicorp.com/terraform/tutorials/configuration-language/dependencies).
+ **locals.tf:** Local values give a name to an expression that the module uses more than once, such as a common name prefix built from `var.environment`. Unlike variables, callers can't set them.
+ **providers.tf:** The [terraform block](https://developer.hashicorp.com/terraform/language/block/terraform) and [provider blocks](https://developer.hashicorp.com/terraform/language/block/provider). Only root modules declare `provider` blocks. If you're using HCP Terraform, also add an empty [cloud block](https://developer.hashicorp.com/terraform/language/block/terraform#cloud), and let your CI/CD pipeline set the organization, workspace, and token through [environment variables](https://developer.hashicorp.com/terraform/language/block/terraform#environment-variables-for-the-cloud-block) and [environment variable credentials](https://developer.hashicorp.com/terraform/cli/config/config-file#environment-variable-credentials).
+ **versions.tf:** The `required_version` setting and the [required\_providers](https://developer.hashicorp.com/terraform/language/providers/requirements#require-providers) block. Every module declares the providers that it uses.
+ **.terraform.lock.hcl:** The [dependency lock file](https://developer.hashicorp.com/terraform/language/files/dependency-lock) records the exact provider versions and checksums that `terraform init` selected. Commit it in root modules. Terraform reads the lock file only from the root module, so reusable modules don't need one. For more information, see [Version management](https://docs.aws.amazon.com/prescriptive-guidance/latest/terraform-aws-provider-best-practices/version.html).
+ **Data sources:** Declare each data source in the file that uses its result, for example the `aws_ami` lookup next to the `aws_instance` that launches from it. Move data sources to a `data.tf` file only when there are enough of them to make the main file hard to read.
+ **.tfvars files:** Keep non-sensitive inputs for a root module in `.tfvars` files: values that every environment shares in `terraform.tfvars` at the repository root, and the rest in `envs/<environment>/terraform.tfvars`. Don't put secrets in `.tfvars` files that you commit. Pass them from your pipeline's secret store as ephemeral variables.
+ **tests/:** Put Terraform test files (`*.tftest.hcl`) in a `tests/` directory. For more information, see [Best practices for testing](https://docs.aws.amazon.com/prescriptive-guidance/latest/terraform-aws-provider-best-practices/best-practices-for-testing.html).
+ **modules/:** Put nested modules in `modules/<name>/`. A nested module with a `README.md` is one that other teams can call, and one without is internal to the repository. Call nested modules with relative paths, such as `./modules/network`, so that Terraform loads them from the same repository instead of downloading them. Have the root module wire nested modules together, instead of having nested modules call each other several levels deep.
+ **examples/:** Put usage examples for a reusable module in `examples/<name>/`, each with a short README. People copy examples into their own repositories, so set each example's module `source` to the registry or Git address that a caller would use, not to a relative path.
+ **Splitting files:** Keep resources in `main.tf` until the file gets hard to review, and then split by purpose, such as `iam.tf` for the module's roles and policies. Avoid a file for every AWS service by default, because a reader then has to open several files to follow one feature.
+ **scripts/:** Terraform doesn't track what a script creates or changes, so prefer resources and data sources. When no resource can do what you need, put the script that Terraform runs, for example through the `external` data source or a `local-exec` provisioner, in `scripts/`.
+ **helpers/:** Put scripts that people run by hand and Terraform never calls, such as a one-time bootstrap or a cleanup script, in `helpers/`. Document each one in `README.md` with an example command.

### Root module structure
<a name="root-module-structure.00e8a549-7371-599d-9727-81656e8f813d"></a>

Terraform always runs in the context of a single root module. A complete Terraform configuration consists of a root module and the tree of child modules (which includes the modules that the root module calls, any modules that those modules call, and so on).

Terraform root module layout basic example:

```
.
├── .terraform.lock.hcl
├── data.tf
├── envs
│   ├── dev
│   │   └── terraform.tfvars
│   ├── prod
│   │   └── terraform.tfvars
│   └── test
│       └── terraform.tfvars
├── locals.tf
├── main.tf
├── outputs.tf
├── providers.tf
├── README.md
├── terraform.tfvars
├── tests
│   └── main.tftest.hcl
├── variables.tf
└── versions.tf
```

### Reusable module structure
<a name="reusable-module-structure.9a29332b-3fba-5824-b0f1-41ad55e25bda"></a>

Reusable modules follow the same concepts as root modules. To define a module, create a new directory for it and place the `.tf` files inside, just as you would define a root module. Terraform can load modules either from local relative paths or from remote repositories. If you expect a module to be reused by many configurations, place it in its own version control repository. Keep the module tree relatively flat to make it easier to reuse modules in different combinations.

Terraform reusable module layout basic example:

```
.
├── data.tf
├── examples
│   ├── multi-az-new-vpc
│   │   ├── data.tf
│   │   ├── locals.tf
│   │   ├── main.tf
│   │   ├── outputs.tf
│   │   ├── providers.tf
│   │   ├── README.md
│   │   ├── terraform.tfvars
│   │   ├── variables.tf
│   │   ├── versions.tf
│   │   └── vpc.tf
│   └── single-az-existing-vpc
│       ├── data.tf
│       ├── locals.tf
│       ├── main.tf
│       ├── outputs.tf
│       ├── providers.tf
│       ├── README.md
│       ├── terraform.tfvars
│       ├── variables.tf
│       └── versions.tf
├── iam.tf
├── locals.tf
├── main.tf
├── outputs.tf
├── README.md
├── tests
│   ├── integration.tftest.hcl
│   └── unit.tftest.hcl
├── variables.tf
└── versions.tf
```

## Structure for modularity
<a name="modularity"></a>

A module is worth its cost when it gives a name to something that your architecture talks about, such as a VPC network baseline, a data tier, or an application service. Each module adds an interface to maintain, versions to manage, and one more place to look during an incident. Split a configuration into reusable modules when several teams or environments need the same set of resources, not for every group of resources.

Size each module around one capability. A module for each resource type leaves callers to wire everything together, and a module that builds a whole application stack is hard to reuse and slow to plan.

### Don't wrap single resources
<a name="don-t-wrap-single-resources.e1469e63-331f-5b02-a582-9ab7c5a9f011"></a>

A module that contains one resource, and passes every argument of that resource through as a variable, adds a layer without adding a concept. A useful test is the module's name: if the best name you can find is the resource type, such as `s3-bucket`, use the resource directly, or design a module around what the bucket is for, such as `log-archive`.

### Encapsulate logical relationships
<a name="encapsulate-logical-relationships.3f6fb397-42a0-5a1d-983e-fac4bb74cb35"></a>

Group sets of related resources such as networking foundations, data tiers, security controls, and applications. A reusable module should encapsulate infrastructure pieces that work together to enable a capability.

### Keep inheritance flat
<a name="keep-inheritance-flat.1f27fe93-c1c2-57f4-a429-d04bc41b0cdc"></a>

When you nest modules in subdirectories, avoid going more than one or two levels deep. Deeply nested inheritance structures complicate configurations and troubleshooting. Modules should build on other modules, not pass through them as intermediaries.

By focusing modules on logical resource groupings that represent architecture patterns, teams can configure reliable infrastructure foundations. Aim for the right level of abstraction: avoid both excessive complexity and oversimplification.

### Reference resources in outputs
<a name="reference-resources-in-outputs.a1b75758-bc8e-509c-8111-ef9593b1c6cb"></a>

For every resource that a reusable module defines, include at least one output that references the resource. Variables and outputs let you infer dependencies between modules and resources. Without any outputs, users cannot properly order your module in relation to their Terraform configurations.

Well-structured modules that provide environment consistency, purpose-driven groupings, and exported resource references enable organization-wide Terraform collaboration at scale. Teams can assemble infrastructure from reusable building blocks.

### Don't configure providers
<a name="don-t-configure-providers.96a7e473-9959-5a1e-8f8a-5c0cebb555dd"></a>

Although shared modules inherit providers from calling modules, modules should not configure provider settings themselves. Avoid specifying provider configuration blocks in modules. This configuration should only be declared once globally.

### Declare required providers
<a name="declare-required-providers.a2e17fbf-80a1-51b6-9617-b8a1df8b9f10"></a>

Although provider configurations are shared between modules, shared modules must also declare their own [provider requirements](https://developer.hashicorp.com/terraform/language/providers/requirements). This practice enables Terraform to ensure that there is a single version of the provider that's compatible with all modules in the configuration, and to specify the source address that serves as the global (module-agnostic) identifier for the provider. However, module-specific provider requirements don't specify any of the configuration settings that determine what remote endpoints the provider will access, such as an AWS Region.

By declaring version requirements and avoiding hardcoded provider configuration, modules provide portability and reusability across Terraform configurations using shared providers.

Declare version requirements differently in reusable modules and in root modules:
+ **Reusable modules** declare the oldest Terraform and provider versions that they work with, by using `>=`. A lower bound lets the root module choose any newer version.
+ **Root modules** also set an upper bound, usually with the *pessimistic constraint operator* (`~>`), so that a new major version isn't installed without review. The dependency lock file then pins the exact version.

For example, both set `required_version = ">= 1.11"` in the `terraform` block. In `required_providers`, a reusable module declares the AWS Provider with `version = ">= 6.0"`, and a root module declares it with `version = "~> 6.0"`.

`~> 6.0` allows any 6.x version, such as `6.70.0`, but not `7.0.0`. To allow only patch releases of one minor version, use three components, such as `~> 6.70.0`. For more information, see [Version constraints](https://developer.hashicorp.com/terraform/language/expressions/version-constraints) and [Provider requirements](https://developer.hashicorp.com/terraform/language/providers/requirements) in the HashiCorp documentation.

### Configure providers for Regions and accounts
<a name="configure-providers-for-regions-and-accounts.f28c5615-a94e-505d-a58a-5da827f86c81"></a>

Configure providers in the root module. Each provider configuration works in one AWS account, the account of the credentials or role that it uses, and has a default AWS Region. In AWS Provider 6.x, most resources also accept a top-level `region` argument, so one provider configuration can manage resources in several Regions of the same account. To manage resources in another account, add a provider configuration with an alias that assumes a role in that account.

The following example sets the default Region and limits the configuration to one account. It then creates an Amazon Relational Database Service (Amazon RDS) read replica in a second Region of the same account, from a primary DB instance that is defined elsewhere in the configuration:

```
provider "aws" {
  region              = "us-west-2"
  allowed_account_ids = ["111122223333"]
}

resource "aws_db_instance" "read_replica" {
  region              = "us-east-1"
  replicate_source_db = aws_db_instance.primary.arn
  instance_class      = "db.t4g.medium"
}
```

In this example:
+ The `provider` block manages resources in account 111122223333, with `us-west-2` as the default Region. `allowed_account_ids` stops any run whose credentials belong to a different account, before Terraform changes anything.
+ The replica sets `region = "us-east-1"`, so the same provider configuration creates it in that Region. A cross-Region replica refers to its source by Amazon Resource Name (ARN) in `replicate_source_db`. The source needs automated backups (`backup_retention_period` greater than 0), and an encrypted replica needs a key in its own Region in `kms_key_id`. Changing a resource's `region` value replaces the resource.
+ To manage resources in another account, such as a DNS record in a shared networking account, add a second `provider` block with an `alias` and an [assume\_role](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#assuming-an-iam-role) block, and set `provider = aws.<alias>` on those resources.

Amazon RDS creates a read replica in the same account as its source DB instance. To copy data to a database in another account, use AWS Database Migration Service (AWS DMS) or the database engine's own replication.

## Follow naming conventions
<a name="naming-conventions"></a>

Clear, descriptive names simplify your understanding of relationships between resources in the module and the purpose of configuration values. Consistency with style guidelines enhances readability for both module users and maintainers.

### Follow guidelines for resource naming
<a name="follow-guidelines-for-resource-naming.ce985823-2c6b-5023-961a-36da7af1778b"></a>
+ Use *snake\_case* (where lowercase terms are separated by underscores) for all resource names to match Terraform style standards. This practice ensures consistency with the naming convention for resource types, data source types, and other predefined values. This convention doesn't apply to [name arguments](https://developer.hashicorp.com/terraform/docs/glossary#argument).
+ To simplify references to a resource that is the only one of its type (for example, a single load balancer for an entire module), name the resource `main` or `this` for clarity.
+ Use meaningful names that describe the purpose and context of the resource, and that help differentiate between similar resources (for example, `primary` for the main database and `read_replica` for a read replica of the database).
+ Use singular, not plural names.
+ Don't repeat the resource type in the resource name.

### Follow guidelines for variable naming
<a name="follow-guidelines-for-variable-naming.49afde7f-d58c-58cb-8704-9e73ae66c64c"></a>
+ Add units to the names of inputs, local variables, and outputs that represent numeric values such as disk size or RAM size (for example, `ram_size_gb` for RAM size in gigabytes). This practice makes the expected input unit clear for configuration maintainers.
+ Use binary units such as MiB and GiB for storage sizes, and decimal units such as MB or GB for other metrics.
+ Give Boolean variables positive names such as `enable_external_access`.

## Use attachment resources
<a name="attachment-resources"></a>

Some resources can manage related objects in two ways: as nested blocks inside the parent resource, or as separate resources that attach to it. Prefer the separate resources. When the same objects are managed in both places, or by two resource types, each one overwrites the other's changes, and Terraform shows a difference on every plan. Separate resources also give each object its own ID and tags.

For security groups, use one `aws_vpc_security_group_ingress_rule` or `aws_vpc_security_group_egress_rule` resource for each rule. The [AWS Provider documentation](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/vpc_security_group_ingress_rule) recommends these resources over the `ingress` and `egress` blocks of `aws_security_group`, and over the `aws_security_group_rule` resource. Each rule resource takes one CIDR block, prefix list, or referenced security group.

For example, a web server security group that allows HTTPS from the load balancer's security group becomes an `aws_security_group` with no `ingress` or `egress` blocks, plus an `aws_vpc_security_group_ingress_rule` with `security_group_id`, `referenced_security_group_id`, `ip_protocol = "tcp"`, and `from_port` and `to_port` set to `443`.

Scope egress rules to the destinations that the workload needs, such as the security group of the VPC endpoints, instead of `0.0.0.0/0`. Scanners such as Trivy rate unrestricted egress as critical.

Other resources follow the same rule. For example, use `aws_iam_role_policy_attachment` instead of `managed_policy_arns` on `aws_iam_role`, and `aws_s3_bucket_versioning` and the other `aws_s3_bucket_*` resources instead of the deprecated arguments of `aws_s3_bucket`.

## Use default tags
<a name="default-tags"></a>

Assign tags to all resources that can accept tags. Set the tags that every resource in a configuration shares in the provider's `default_tags` block. The provider adds them to every resource that it creates, and a resource's own `tags` argument adds to them or overrides them. The `tags_all` attribute of each resource shows the combined result. For example, set `Environment`, `Owner`, and `CostCenter` in `default_tags`, and set only `Name` on each resource.

`aws_autoscaling_group` doesn't receive default tags. Read them with the [aws\_default\_tags](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/data-sources/default_tags) data source, and pass them to the group's `tag` blocks with a `dynamic "tag"` block that sets `propagate_at_launch = true`, so that they're also applied to the instances that it launches.

Add the following tags to all resources that a Terraform module creates:
+ **Name**: Human-readable resource name
+ **AppId**: The ID for the application that uses the resource
+ **AppRole**: The resource's technical function; for example, "webserver" or "database"
+ **AppPurpose**: The resource's business purpose; for example, "frontend ui" or "payment processor"
+ **Environment**: The software environment, such as dev, test, or prod
+ **Project**: The projects that use the resource
+ **CostCenter**: Who to bill for resource usage

## Meet Terraform registry requirements
<a name="registry-reqs"></a>

Structure each reusable module so that you can publish it to a registry, even if you don't plan to publish it soon. You can then publish it later without changing its configuration or repository layout.

Requirements for the public [Terraform Registry](https://developer.hashicorp.com/terraform/registry/modules/publish):
+ **Repository:** A public GitHub repository named `terraform-aws-<NAME>`, where `<NAME>` reflects the type of infrastructure the module manages. The `<NAME>` segment can contain additional hyphens (for example, `terraform-aws-iam-terraform-roles`).
+ **Standard module structure:** The module files are at the root of the repository, following the standard structure. The registry uses this structure to generate documentation, track resource usage, and more.
+ **Release tags:** At least one tag that uses [semantic versioning](https://semver.org/), optionally prefixed with `v` (for example, `v1.1.0` or `1.1.0`). The registry ignores tags that don't look like version numbers.

Requirements for an HCP Terraform [private registry](https://developer.hashicorp.com/terraform/cloud-docs/registry/publish-modules):
+ **Repository:** The repository is in one of your organization's configured [version control system (VCS) providers](https://developer.hashicorp.com/terraform/cloud-docs/vcs), and the HCP Terraform VCS user account has administrator access to it. The registry needs administrator access to create the webhooks that import new module versions.
+ **Release tags:** Semantic version tags, as for the public registry, unless you publish with branch-based publishing.
+ **Access:** The registry handles downloads and controls access with HCP Terraform API tokens, so consumers don't need access to the module's source repository, even when they run Terraform from the command line.

Place each module that is intended to be reusable in the root of its own repository, but you can also reference modules from subdirectories.

## Use recommended module sources
<a name="module-sources"></a>

Terraform uses the `source` argument in a module block to find and download the source code for a child module.

Use local paths for closely related modules that have the primary purpose of factoring out repeated code elements, and a module registry or a VCS provider for modules that are intended to be shared by multiple configurations.

The most common [source types](https://developer.hashicorp.com/terraform/language/modules/configuration) for sharing modules are registries and version control systems. Choose based on how much control you need over the code that runs:
+ **Public Terraform Registry:** set `source` to the module address, such as `terraform-aws-modules/lambda/aws`, and set `version` to an exact version, such as `8.12.0`. Change the version deliberately, after you review the release. This is the simplest option, and tools such as Dependabot and Renovate can propose upgrades. The trade-off is that the publisher controls what a version number points to, and the dependency lock file covers providers, not modules.
+ **Git repository pinned to a commit:** set `source` to the module's repository with `?ref=` and a full commit SHA, and record the matching release in a comment. The code that runs is always the code that you reviewed. The trade-off is that upgrades mean finding and reviewing a new SHA, and Terraform downloads the whole repository.
+ **Private registry in HCP Terraform or Terraform Enterprise:** set `source` to `<hostname>/<organization>/<name>/<provider>`, such as `app.terraform.io/example-org/eks/aws`, and set `version`. Your organization controls the published versions, and teams can discover approved modules in one place. The trade-off is that you depend on HCP Terraform or Terraform Enterprise for every `terraform init`.
+ **Other VCS providers:** for repositories in other Git services, use a `git::` source with the repository URL and a `?ref=` tag or commit SHA. Prefer SSH or HTTPS URLs that use the credentials your CI/CD pipeline already has.

Some modules have inputs that change their behavior in ways that matter at scale. For example, set `trigger_on_package_timestamp = false` in `terraform-aws-modules/lambda/aws`. Its default, `true`, plans a new deployment package on every run, even when the source hasn't changed.

## Follow coding standards
<a name="coding-standards"></a>

Apply consistent Terraform formatting rules and styles across all configuration files. Enforce standards by using automated style checks in CI/CD pipelines. When you embed coding best practices into team workflows, configurations remain readable, maintainable, and collaborative across your organization.

### Follow style guidelines
<a name="follow-style-guidelines.8361ae48-67ee-52a4-ba22-481be2b0e993"></a>
+ Format all Terraform files (`.tf` files) with the [terraform fmt](https://developer.hashicorp.com/terraform/cli/commands/fmt) command to match HashiCorp style standards.
+ Use the [terraform validate](https://developer.hashicorp.com/terraform/cli/commands/validate) command to verify the syntax and structure of your configuration.
+ Statically analyze code quality by using [TFLint](https://github.com/terraform-linters/tflint). This linter checks for Terraform best practices beyond just formatting and fails builds when it encounters errors.

### Configure pre-commit hooks
<a name="configure-pre-commit-hooks.e41824da-c229-56b2-bac3-9ad8a11ce957"></a>

Configure client-side pre-commit hooks that run `terraform fmt`, `terraform validate`, `tflint`, a security scanner such as `trivy config` or `checkov`, and `terraform-docs` before you allow commits. This practice helps you validate standards conformance earlier in developer workflows.

Use pre-commit frameworks such as [pre-commit](https://pre-commit.com/) to add Terraform linting, formatting, and code scanning as hooks on your local machine. Hooks run on each Git commit and fail the commit if checks don't pass.

Moving style and quality checks to local pre-commit hooks provides rapid feedback to developers before they introduce changes. Standards become part of the coding workflow.

## Refactor and import without re-creating resources
<a name="refactor-and-import-without-re-creating-resources"></a>

Use configuration blocks instead of `terraform state` commands to change what Terraform manages. The blocks are reviewed in a pull request like any other change, and `terraform plan` shows their effect before anything happens.
+ **moved** (Terraform 1.1 and later): Rename a resource, or move it into or out of a module, without destroying and re-creating it.
+ **removed** (Terraform 1.7 and later): Stop managing a resource. With `destroy = false`, Terraform removes the resource from state and leaves it running.
+ **import** (Terraform 1.5 and later): Bring an existing resource under management. Add `-generate-config-out=<file>` to `terraform plan` to have Terraform write the resource configuration for you.

For example, a `moved` block with `from = aws_ssm_parameter.old_name` and `to = aws_ssm_parameter.feature_flag` renames the resource in state when you rename it in the configuration. Run `terraform plan` to confirm that the plan shows a move and no destroy.

To find existing resources to import, use `terraform query` (Terraform 1.14 and later) with `list` blocks in a `.tfquery.hcl` file. `terraform query -generate-config-out=<file>` writes an `import` block and a `resource` block for each result. A `list` block covers the whole account and Region for its resource type, so set a `limit`, and review and filter the results before you import them.

For more information, see [Refactoring](https://developer.hashicorp.com/terraform/language/modules/develop/refactoring) and [Import](https://developer.hashicorp.com/terraform/language/import) in the HashiCorp documentation.
