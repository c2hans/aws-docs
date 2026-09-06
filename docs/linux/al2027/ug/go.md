---
source_url: https://docs.aws.amazon.com/linux/al2027/ug/go.html
---

# Go in AL2027
<a name="go"></a>

**AL2027 Preview**
AL2027 is currently available for preview. It is intended for evaluation and testing only and is not recommended for production workloads.

 Go is a relatively fast-moving language. Existing applications written in Go might need to adapt to new versions of the Go toolchain.

 Although AL2027 will incorporate new versions of the Go toolchain during its lifetime, this will not be in lockstep with the upstream Go releases. If you want to build Go code that uses the latest features of the Go language or standard library, the Go toolchain provided in AL2027 might not be suitable.

 The package name is golang. Amazon Linux does not remove previous package versions from the repositories. If you need a previous Go toolchain, you can install an earlier version from the repositories using the same mechanisms available for any RPM. Note that an earlier version does not include the bug fixes and security fixes of newer Go toolchains.
