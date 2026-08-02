---
source_url: https://docs.aws.amazon.com/linux/al2023/ug/minimized-pkg-dependencies.html
---

# Minimized package dependencies
<a name="minimized-pkg-dependencies"></a>

 Amazon Linux 2023 minimizes the dependency graph of many packages to provide a smaller footprint for applications. Notable changes from AL2 include the `curl-minimal` and `gnupg-minimal` packages, which siginicantly reduce the number of required packages while retaining commonly used functionality.

**Topics**
+ [Package changes for `curl` and `libcurl`](curl-minimal.md)
+ [GNU Privacy Guard (GNUPG)](gnupg-minimal.md)
