---
source_url: https://docs.aws.amazon.com/linux/al2023/ug/minimized-pkg-dependencies.html
---

# Minimized package dependencies
<a name="minimized-pkg-dependencies"></a>

 Amazon Linux 2023 minimizes the dependency graph of many packages to provide a smaller footprint for applications. Notable changes from AL2 include the `curl-minimal` and `gnupg-minimal` packages, which siginicantly reduce the number of required packages while retaining commonly used functionality.

**Topics**
+ [Package changes for `curl` and `libcurl`](curl-minimal.md)
+ [GNU Privacy Guard (GNUPG)](gnupg-minimal.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Linux. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query linux` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
