---
source_url: https://docs.aws.amazon.com/linux/al2023/ug/rust.html
---

# Rust in AL2023
<a name="rust"></a>

 You might want to build code written in [Rust](https://www.rust-lang.org/) on Amazon Linux, and might want to use a toolchain provided with AL2023.

 Similar to AL2, AL2023 will update the Rust toolchain throughout the life of the operating system. This might be in response to any CVE in the toolchain we ship, or as part of a quarterly release.

 [Rust](https://www.rust-lang.org/) is a relatively fast moving language, with new releases on approximately a six-week cadence. These releases might add new language or standard library features. Although AL2023 will incorporate new versions of the Rust toolchain during its life, this will not be in lockstep with the upstream Rust releases. Therefore, using the Rust toolchain provided in AL2023 might not be suitable if you want to build Rust code using cutting-edge features of the Rust language.

 During the lifetime of AL2023, old package versions are not removed from the repositories. If an older Rust toolchain is required, you can choose to forgo bug and security fixes of newer Rust toolchains and install an older version from the repositories using the same mechanisms available for any RPM.

 If you want to build your own Rust code on AL2023, you can use the Rust toolchain included in AL2023 with the knowledge that this toolchain might move forward through the lifetime of AL2023.

## AL2023 Lambda functions written in Rust
<a name="lambda-rust"></a>

 Because Rust compiles to native code, Lambda treats Rust as a custom runtime. You can use the `provided.al2023` runtime to deploy Rust functions on AL2023 to Lambda.

 For more information, see [Building Lambda functions with Rust](https://docs.aws.amazon.com/lambda/latest/dg/lambda-rust.html) in the *AWS Lambda Developer Guide*.
