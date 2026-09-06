---
source_url: https://docs.aws.amazon.com/solutions/latest/modern-data-architecture-accelerator/update-the-solution.html
---

# Update the solution
<a name="update-the-solution"></a>

MDAA follows semantic versioning. Minor releases (for example, 1.6.0 to 1.7.0) are generally backward compatible with existing configurations. However, upgrades may include underlying CDK version changes and new module behaviors, so reviewing changes before deploying is recommended.

## Before you upgrade
<a name="before-you-upgrade"></a>

1. Review the [release notes](https://github.com/aws/modern-data-architecture-accelerator/releases/) for the target version to understand new features, bug fixes, and dependency updates.

1. Run `diff` to preview the CloudFormation changes the upgrade will introduce. To diff against the latest published version:

   ```
   npx @aws-mdaa/cli diff -c ./mdaa.yaml
   ```

   To diff against a specific version:

   ```
   npx @aws-mdaa/cli@1.7.0 --mdaa-version 1.7.0 diff -c ./mdaa.yaml
   ```

## Notable changes in 1.8.0
<a name="notable-changes-in-1-8-0"></a>

Review the following before upgrading from 1.7.0 to 1.8.0:
+  **Terraform configuration now resolves child-over-parent (breaking change)**: when a `terraform` key is set at more than one level of the configuration hierarchy (global, domain, environment, module), the more specific level now takes effect. Previously the parent level took effect. This aligns `terraform` with every other cascaded field, including `context`, `tag_config_data`, `custom_aspects`, `custom_naming` and `permissions_boundary_arn`. A project that sets the same `terraform. ` key, for example `terraform.override.`, at both a parent and a child level resolves to the opposite value it did in 1.7.0, which can retarget Terraform state. Review those configurations before you deploy.
+  ** `@mdaaIncludeEnvInSsmPath` naming flag**: this new opt-in flag lets you deploy multiple MDAA environments into one AWS account by including `env` in SSM parameter paths and CloudFormation export names. It defaults to `false`, so existing deployments are unaffected. Enabling it on an existing deployment is not backward compatible, because the parameter paths and export names change. See the naming utility documentation for migration steps.
+  **AgentCore Runtime `enforceVpcOnly` now denies out-of-VPC IAM callers**: in 1.7.0 the VPC-only resource policy allowed rather than denied, so an IAM caller whose identity policy already authorized the action could invoke the runtime from outside the VPC. JWT and OAuth callers were correctly blocked. The policy now adds explicit deny statements and covers all invoke variants. Out-of-VPC IAM invocations that previously succeeded are now denied.
+  **AgentCore Runtime agent spans move to the runtime’s own log group**: agent spans now route to the runtime’s own CloudWatch log group instead of the account-shared `aws/spans` log group, so they inherit the module’s KMS encryption, retention, and PII masking. This is on by default. The destination takes effect only from `aws-opentelemetry-distro` 0.18.0, so raise that dependency in the runtime container image before upgrading; an earlier version silently keeps delivering to `aws/spans`. The change also creates a new runtime version on deploy. To opt out, set `UNIFIED_TRACES_DESTINATION_ENABLED` to `'false'` under `environmentVariables`.
+  ** `mdaa upgrade` CLI command**: the CLI gains an `upgrade` action that bumps `mdaa_version` in `mdaa.yaml` and regenerates the project’s `.mdaa/` assets — JSON schemas, module documentation, and AI steering files — pruning the directories for older versions as it goes. Use it in place of editing `mdaa_version` by hand, so that the schemas your editor validates against match the version you deploy.

## Notable changes in 1.7.0
<a name="notable-changes-in-1-7-0"></a>

Review the following before upgrading from 1.6.0 to 1.7.0:
+  **Lambda Python runtime**: `aws-cdk-lib` was upgraded from 2.192.0 to 2.258.0. Version 2.258.0 removes the `lambda.Runtime.PYTHON_3_13` enum value in favor of `Runtime.PYTHON_3_14`. Any MDAA config that specifies `python3.13` as a Lambda runtime must be changed to `python3.13t` (thread-based) or another supported runtime such as `python3.14`.
+  **AgentCore Runtime data protection (breaking change)**: The previous `dataProtection.enabled` / `dataProtection.identifiers` configuration has been replaced by a mandatory built-in baseline plus an additive `dataProtection.additionalIdentifiers` field. Data protection is no longer opt-in and the identifier list cannot be narrowed. Existing configs using the old keys are silently ignored — remove them to avoid confusion. On next deploy, existing AgentCore runtimes gain a new KMS key, a CloudWatch Data Protection policy, and a log-protection custom resource.
+  **Audit Trail `trail` → `trails` **: The existing `trail` property is deprecated in favor of a `trails` map that accepts multiple named trail configurations. Migrate by moving your existing trail configuration under `trails` with a key of `'s3-audit'` for equivalent behavior. Both properties can coexist during migration.
+  **GAIA v1 removal target**: `@aws-mdaa/gaia` and `@aws-mdaa/gaia-l3-construct` (GAIA v1) now have a firm removal target of **v1.9.0**. v1 remains published and functional until then. See `MIGRATION_TO_V2.md` in the `gaia-app` package for migration guidance to `@aws-mdaa/gaia-v2`.
+  **Lambda runtime for CDK managed resources**: Existing AgentCore runtimes migrated to the typed `CfnRuntime`/`CfnRuntimeEndpoint` constructs will gain standard MDAA stack tags on next deploy. Logical IDs are unchanged and no resource replacement occurs.

## Upgrading to the latest version
<a name="upgrading-to-the-latest-version"></a>

Starting with MDAA 1.8.0, the CLI has an `upgrade` action. Run it from the project root, the directory that holds `mdaa.yaml`:

```
npx @aws-mdaa/cli@1.8.0 upgrade
```

 `upgrade` updates `mdaa_version` in `mdaa.yaml`, regenerates `.mdaa/<version>/` with the schemas and module documentation for the new version, rewrites the `$schema` directives in your config files to point at it, prunes the directories for older versions, and refreshes the AI steering files. MDAA-owned files are always regenerated; a user-owned file such as `CLAUDE.md` that you have edited since MDAA generated it prompts first. Pass `--overwrite` to replace those files without prompting, or `--no-prompt` to leave them untouched.

The version argument has to match the CLI that runs, because the schemas and documentation are generated from the installed CLI. Omit it to upgrade the project to the CLI version already installed:

```
mdaa upgrade
```

Then deploy with the same version. To deploy the latest published version, run the CLI without specifying a version or `--mdaa-version`:

```
npx @aws-mdaa/cli deploy -c ./mdaa.yaml
```

## Upgrading to a specific version
<a name="upgrading-to-a-specific-version"></a>

To upgrade to a specific version, specify the target version when running the CLI:

```
npx @aws-mdaa/cli@1.7.0 --mdaa-version 1.7.0 deploy -c ./mdaa.yaml
```

The `--mdaa-version` flag controls which version of the MDAA module packages are installed during execution. The version after `@aws-mdaa/cli@` controls the CLI version itself. These should generally match.

## Gradual upgrade via version pinning
<a name="gradual-upgrade-via-version-pinning"></a>

For a more controlled rollout, you can pin specific MDAA versions at different levels in your `mdaa.yaml` configuration. This allows you to upgrade and validate modules individually before upgrading the rest.

```
# Pin version globally
mdaa_version: '1.6.0'

domains:
  my-domain:
    environments:
      dev:
        # Override version for a specific environment
        mdaa_version: '1.7.0'
        modules:
          audit:
            # Override version for a specific module
            mdaa_version: '1.7.0'
```

Version resolution follows a hierarchy: module overrides environment, environment overrides domain, and domain overrides the global setting.

You can also use the `-d`, `-e`, and `-m` CLI flags to target specific domains, environments, or modules during an upgrade:

```
npx @aws-mdaa/cli@1.7.0 --mdaa-version 1.7.0 deploy -c ./mdaa.yaml -m audit
```

## Validating with baseline diff
<a name="validating-with-baseline-diff"></a>

Starting with MDAA 1.5.0, you can compare synthesized templates against a stored baseline without requiring a deployed stack. This is useful for CI/CD pipelines or for validating upgrades in a non-deployed environment:

```
# Synthesize and store templates from the current version
npx @aws-mdaa/cli@1.6.0 --mdaa-version 1.6.0 synth -c ./mdaa.yaml --cdk-out ./baseline

# Compare against the new version
npx @aws-mdaa/cli@1.7.0 --mdaa-version 1.7.0 diff -c ./mdaa.yaml --baseline ./baseline --diff-out ./diff-results
```
