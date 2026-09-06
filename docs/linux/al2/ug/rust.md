---
source_url: https://docs.aws.amazon.com/linux/al2/ug/rust.html
---

# Rust in AL2
<a name="rust"></a>

 You might want to build your own code written in [Rust](https://www.rust-lang.org/) on AL2 using a toolchain provided with AL2.

 The Rust toolchain will be updated throughout the life of AL2. This might be in response to a CVE in the toolchain we ship, or as prerequisite for a CVE update in another package.

 [Rust](https://www.rust-lang.org/) is a relatively fast moving language, with new releases at approximately a six-week cadence. The new releases might add new language or standard library features. Although AL2 will incorporate new versions of the Rust toolchain during its life, this will not be in lockstep with the upstream Rust releases. Therefore, using the Rust toolchain provided in AL2 might not be suitable if you want to build Rust code using cutting-edge features of the Rust language.

 During the lifetime of AL2, previous package versions are not removed from the repositories. If a previous Rust toolchain is required, you can choose to forgo bug and security fixes of newer  Rust toolchains and install a previous version from the repositories using the same processes available for any RPM.

 To build your own Rust code on AL2, use the Rust toolchain included in AL2 with the knowledge that this toolchain might move forward throughout the lifetime of AL2.
