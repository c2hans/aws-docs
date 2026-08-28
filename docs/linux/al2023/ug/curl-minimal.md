---
source_url: https://docs.aws.amazon.com/linux/al2023/ug/curl-minimal.html
---

# Package changes for `curl` and `libcurl`
<a name="curl-minimal"></a>

 AL2023 separates out the common protocols and functionality of the `curl` and `libcurl` packages into `curl-minimal` and `libcurl-minimal`. This reduces the disk, memory, and dependency footprint for most users, and is the default package for AL2023 AMIs and containers.

If the full functionality of `curl` is required, for example for `gopher://` support, run the following commands to install the `curl-full` and `libcurl-full` packages.

```
$ dnf swap libcurl-minimal libcurl-full
```

```
$ dnf swap curl-minimal curl-full
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Linux. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query linux` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
