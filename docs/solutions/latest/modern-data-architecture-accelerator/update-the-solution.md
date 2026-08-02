---
source_url: https://docs.aws.amazon.com/solutions/latest/modern-data-architecture-accelerator/update-the-solution.html
---

# Update the solution
<a name="update-the-solution"></a>

MDAA follows semantic versioning. Minor releases (for example, 1.6.0 to 1.7.0) are generally backward compatible with existing configurations. However, upgrades may include underlying CDK version changes and new module behaviors, so reviewing changes before deploying is recommended.

## Before you upgrade
<a name="before-you-upgrade"></a>

1. Review the [CHANGELOG](https://github.com/aws/modern-data-architecture-accelerator/blob/main/CHANGELOG.md) for the target version to understand new features, bug fixes, and dependency updates.

1. Run `diff` to preview the CloudFormation changes the upgrade will introduce. To diff against the latest published version:

   ```
   npx @aws-mdaa/cli diff -c ./mdaa.yaml
   ```

   To diff against a specific version:

   ```
   npx @aws-mdaa/cli@1.7.0 --mdaa-version 1.7.0 diff -c ./mdaa.yaml
   ```

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

To upgrade to the latest published version, simply run the CLI without specifying a version or `--mdaa-version`:

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
