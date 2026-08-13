---
source_url: https://docs.aws.amazon.com/linux/al2023/ug/go.html
---

# Go in AL2023
<a name="go"></a>

 You might want to build your own code written in [Go](https://go.dev/) on Amazon Linux, and might want to use a toolchain provided with AL2023. Similar to AL2, AL2023 will update the Go toolchain throughout the life of the operating system. This might be in response to any CVE in the toolchain we ship, or as part of a quarterly release.

 Go is a relatively fast moving language. There might be a situation where existing applications written in Go have to adapt to new versions of the Go toolchain. For more information about Go, see [Go 1 and the Future of Go Programs](https://go.dev/doc/go1compat).

 Although AL2023 will incorporate new versions of the Go toolchain during its life, this will not be in lockstep with the upstream Go releases. Therefore, using the Go toolchain provided in AL2023 might not be suitable if you want to build Go code using cutting-edge features of the Go language and standard library.

 During the lifetime of AL2023, previous package versions are not removed from the repositories. If a previous Go toolchain is required, you can choose to forgo the bug and security fixes of newer Go toolchains and install an previous version from the repositories using the same mechanisms available for any RPM.

 If you want to build your own Go code on AL2023, you can use the Go toolchain included in AL2023 with the knowledge that this toolchain might move forward through the lifetime of AL2023.

## AL2023 Lambda functions written in Go
<a name="lambda-go"></a>

 As Go compiles to native code, Lambda treats Go as a custom runtime. You can use the `provided.al2023` runtime to deploy Go functions on AL2023 to Lambda.

 For more information, see [Building Lambda functions with Go](https://docs.aws.amazon.com/lambda/latest/dg/lambda-golang.html) in the *AWS Lambda Developer Guide*.
