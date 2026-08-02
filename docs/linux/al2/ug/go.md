---
source_url: https://docs.aws.amazon.com/linux/al2/ug/go.html
---

# Go in AL2
<a name="go"></a>

 You might want to build your own code written in [https://go.dev/](https://go.dev/) on Amazon Linux using a toolchain provided with AL2.

 The Go toolchain will be updated throughout the life of AL2. This might be in response to any CVE in the toolchain we ship, or as a prerequisite of addressing a CVE in another package.

 Go is a relatively fast moving programming language. There might be a situation where existing applications written in Go have to adapt to new versions of the Go toolchain. For more information about Go, see [Go 1 and the Future of Go Programs](https://go.dev/doc/go1compat).

 Although AL2 will incorporate new versions of the Go toolchain during its life, this will not be in lockstep with the upstream Go releases. Therefore, using the Go toolchain provided in AL2 might not be suitable if you want to build Go code using cutting-edge features of the Go language and standard library.

 During the lifetime of AL2, earlier package versions are not removed from the repositories. If an earlier Go toolchain is required, you can choose to forgo bug and security fixes of newer Go toolchains and install an earlier version from the repositories using the same mechanisms available for any RPM.

 If you want to build your own Go code on AL2 you can use the Go toolchain included in AL2 with the knowledge that this toolchain might move forward through the lifetime of AL2.
