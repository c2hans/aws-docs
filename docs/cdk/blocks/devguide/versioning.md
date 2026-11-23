---
source_url: https://docs.aws.amazon.com/cdk/blocks/devguide/versioning.html
---

# Versioning

This topic describes how AWS CDK Blocks handles versioning.

CDK Blocks version numbers have three numeric parts: `MAJOR.MINOR.PATCH`. They follow [Semantic Versioning](https://semver.org), with the exceptions described in [Exceptions](#versioning-exceptions). Breaking changes are limited to major releases.

Minor and patch releases are backward compatible. You can upgrade code written for an earlier version to a newer version with the same major version, and it continues to build and run.

## Version numbers
<a name="versioning-semver"></a>

The following list describes each part of a version number.
+  `MAJOR` (`1.2.3` to `2.0.0`): A major release can include changes that break existing code. Release notes describe what changed and how to update.
+  `MINOR` (`1.2.3` to `1.3.0`): A minor release adds new, backward-compatible features. Existing code continues to work.
+  `PATCH` (`1.2.3` to `1.2.4`): A patch release contains backward-compatible bug fixes.

Versions earlier than `1.0.0` are initial development releases. In these versions, a minor release can include breaking changes.

## Exceptions
<a name="versioning-exceptions"></a>

In rare cases, a patch or minor release can include a change that is not backward compatible. This happens only in the following situations:
+  **Security fixes:** A fix for a security issue can change behavior that your code relies on.
+  **Short-lived bugs:** A bug introduced in a recent release and fixed soon after can be corrected in a way that breaks code that depended on the faulty behavior.

Such changes are described in the release notes.

## Upgrade your packages
<a name="versioning-upgrading"></a>

You can avoid unexpected changes by committing your lock file and upgrading deliberately. For more information about changes in each release, see the [releases page](https://github.com/aws/cdk-blocks/releases) on the GitHub website.
