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
