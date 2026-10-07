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

## Notable changes by release
<a name="notable-changes-by-release"></a>

For breaking changes, deprecations, and other notable behavior changes in each release, refer to the [CHANGELOG](https://github.com/aws/modern-data-architecture-accelerator/blob/main/CHANGELOG.md) in the GitHub repository.

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
