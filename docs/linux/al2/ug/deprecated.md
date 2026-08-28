---
source_url: https://docs.aws.amazon.com/linux/al2/ug/deprecated.html
---

# Deprecated functionality in AL2
<a name="deprecated"></a>

The following sections describe functionality supported in AL2 and not present in AL2023. This is functionality such as features and packages that are present in AL2, but not in AL2023 and will not be added to AL2023. See the AL2 documentation for how long this functionality is supported in AL2.

## `compat-` packages
<a name="deprecated-compat"></a>

 Any packages in AL2 with the prefix of `compat-` are provided for binary compatibility with older binaries that have not yet been rebuilt for modern versions of the package. Each new major version of Amazon Linux will not carry forward any `compat-` package from prior releases.

 All `compat-` packages in a release of Amazon Linux (such as AL2) are discontinued, and not present in the subsequent version (such as AL2023). We strongly recommend that software is rebuilt against updated versions of the libraries.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Linux. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query linux` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
