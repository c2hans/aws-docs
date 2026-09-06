---
source_url: https://docs.aws.amazon.com/linux/al2027/ug/rust.html
---

# Rust in AL2027
<a name="rust"></a>

**AL2027 Preview**
AL2027 is currently available for preview. It is intended for evaluation and testing only and is not recommended for production workloads.

 AL2027 includes a Rust toolchain for building Rust applications. Because Rust releases far more often than AL2027 does, the toolchain is not always the newest release available upstream. For more information about the language, see [Learn Rust](https://www.rust-lang.org/learn) on the Rust website.

 The compiler package is named `rust`. The toolchain also includes `cargo`, `clippy`, `rustfmt`, and `rust-analyzer`. We do not namespace these packages. Because the package names do not include a version, you can install only one Rust toolchain at a time.

## Rust toolchain versions
<a name="rust-versions"></a>

 Rust is a fast-moving language. The Rust project publishes a new stable release about every six weeks. AL2027 publishes releases on a two-week cadence, and each new Rust release requires packaging and validation first.

 The two cadences do not align. You can therefore expect the Rust toolchain in AL2027 to be either the current stable release or the release immediately before it.

 The toolchain moves forward during the life of AL2027. We do not remove previous package versions from the repositories. If you need an earlier toolchain, you can install it using the same mechanisms available for any RPM. An earlier toolchain does not include the bug fixes and security fixes of newer Rust releases.
