---
source_url: https://docs.aws.amazon.com/linux/al2027/ug/compare-with-al2023.html
---

# Comparing AL2023 and AL2027
<a name="compare-with-al2023"></a>

**AL2027 Preview**
AL2027 is currently available for preview. It is intended for evaluation and testing only and is not recommended for production workloads.

The following table summarizes the major component changes between AL2023 and AL2027.

**Component changes from AL2023 to AL2027**

| Component | AL2023 | AL2027 | Notes |
| --- | --- | --- | --- |
| SELinux | Permissive | Enforcing | SELinux is now set to Enforcing mode by default. |
| Kernel | 6.1 (default); 6.12 and 6.18 available | 7.1 | Kernel packages use versioned names, such as kernel7.1. The current preview release ships kernel version 7.1. Amazon Linux adds newer kernel versions over time, as with AL2023. |
| GCC | 11.5 | 16.1 | Major toolchain upgrade from GCC 11 to 16. |
| glibc | 2.34 | 2.44 |  |
| binutils | 2.41 | 2.46 |  |
| LLVM/Clang | 15, 18, 19 (separate SRPMs) | 22 (unified SRPM) | clang, lld, lldb, and libomp are built from a single source package. |
| systemd | 252 | 260 | Support for System V service scripts has been removed. |
| RPM | 4.16 | 6.0 | OpenPGP signature verification uses the rpm-sequoia implementation. |
| DNF | DNF 4.14 | DNF5 5.4 | DNF5 replaces DNF. The dnf and yum commands run DNF5. The DNF (version 4) Python API (python3-dnf) is not available. Use python3-libdnf5 instead. See [Package management tool](package-management.md). |
| Python | 3.9 | 3.14 | The default python3 is Python 3.14. |
| zlib | 1.2.11 | zlib-ng 2.3 | Drop-in replacement through the zlib-ng-compat package. |
| PCRE | PCRE 8.x \+ PCRE2 | PCRE2 only | PCRE1 has been removed. |

## Toolchain considerations
<a name="key-changes-toolchain"></a>

The GCC 11 to 16 jump is the largest toolchain change. Code compiled on AL2023 generally runs on AL2027, but recompiling might expose new warnings or errors because of stricter defaults in GCC 16.

RPM 6.0 replaces 4.16. If you maintain custom spec files, test them against the new RPM version.

LLVM 22 is built from a single unified SRPM. The separate `clang`, `lld`, and `lldb` source packages no longer exist.

AL2027 turns on dependency cooldowns for *npm* and *pip* by default. Dependency cooldowns delay the installation of recently published packages, giving the security community time to detect and remove malicious packages before they reach your systems. The cooldowns were available in AL2023 (npm since release 2023.11, pip since 2023.12) but required manual configuration. For more information, see [Supply chain protection for package managers](security-features.md#supply-chain-protection).

## AWS-LC
<a name="key-changes-aws-lc"></a>

AL2027 adds [AWS-LC](https://github.com/aws/aws-lc), a general-purpose cryptographic library. AWS-LC emphasizes correctness: portions of the library are backed by [formal proofs](https://github.com/awslabs/aws-lc-verification) that mechanically verify the implementation of key algorithms against their specifications, in addition to extensive testing. It provides FIPS 140-validated cryptography and is optimized for the platforms and workloads that AWS and its customers run.

AWS-LC is maintained by AWS for AWS and its customers. It is derived from code that Google's BoringSSL project and the OpenSSL project released.

AWS-LC has recently added a stable shared library ABI, which makes it practical to ship as a system library that multiple packages can link against and to update independently of the applications that use it. AL2027 is leaning heavily into using the AWS-LC cryptographic library: a number of packages are currently built against AWS-LC instead of OpenSSL, and we expect this range to increase during the preview.

We encourage you to adopt AWS-LC for its many benefits. Beyond correctness, AWS-LC is focused on performance, with cryptographic operations optimized for the platforms and workloads that run on AWS. AWS-LC is proven through widespread use across Amazon: if you have used an AWS API, you have had AWS-LC on the other end. Building your own applications against AWS-LC gives you the same cryptography that AWS relies on in production.

AWS-LC is provided by the following packages:
+ `aws-lc` — command line tools.
+ `aws-lc-libs` — the shared libraries (`libcrypto` and `libssl`).
+ `aws-lc-devel` — headers and development files for building against AWS-LC.

AWS-LC does not replace OpenSSL. OpenSSL 3.5 remains the default system cryptographic library in AL2027, and most packages in the distribution continue to link against it. AWS-LC is installed alongside OpenSSL and is intended for applications that choose to build or link against it.

In the AL2027 preview, the following packages are built against AWS-LC instead of OpenSSL:
+ `coreutils` (used by `sort`)
+ `elinks`
+ `haproxy`
+ `httpd` and `mod_http2`
+ `libmemcached-awesome`
+ `libpq`
+ `nginx-awslc`
+ `python3-awscrt`
+ `python-cryptography`
+ `python3.14`
+ `rsync`
+ `socat`
+ `tpm2-tools`
+ `tpm2-tss`
+ `trousers`
+ `wget1`
+ More packages coming during the AL2027 preview.

We are introducing AWS-LC carefully to ensure that we maintain compatibility and correctness as each package moves to it. OpenSSL 3.5 is still available, so you can link your applications against it if you prefer. There are some feature gaps between the two libraries in both directions. AWS-LC offers some functionality that OpenSSL does not, and OpenSSL offers some functionality that AWS-LC does not. We are working to close the gaps in AWS-LC that matter for customer workloads.

`nginx-awslc` is a build of nginx that links against AWS-LC instead of OpenSSL. Install `nginx-awslc` in place of `nginx` to use it.

We want your feedback during the preview. To report issues or share feedback about AL2027, including which packages you would like to see built against AWS-LC, use the [AL2027 GitHub repository](https://github.com/amazonlinux/amazon-linux-2027/issues). For feedback about AWS-LC itself, use the [AWS-LC GitHub repository](https://github.com/aws/aws-lc/issues).
