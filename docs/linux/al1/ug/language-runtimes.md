---
source_url: https://docs.aws.amazon.com/linux/al1/ug/language-runtimes.html
---

# Programming languages and runtimes on AL1
<a name="language-runtimes"></a>

**Warning**
 Amazon Linux 1 (AL1, formerly Amazon Linux AMI) is no longer supported. This guide is available only for reference purposes.

**Note**
 AL1 is no longer the current version of Amazon Linux. AL2023 is the successor to AL1 and AL2. For more information about what's new in AL2023, see [Comparing AL1 and AL2023](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al1.html) section in the [AL2023 User Guide](https://docs.aws.amazon.com/linux/al2023/ug/) and the list of [Package changes in AL2023](https://docs.aws.amazon.com/linux/al2023/release-notes/compare-packages.html).

 AL1 provides different versions of some language runtimes. We work with upstream projects that support multiple versions at the same time. To find information about how to install and manage these name-versioned packages, use the `yum` command to search and install these packages.

The following topics outline how each language ecosystem exists in AL1.

**Topics**
+ [C, C\+\+, and Fortran in AL1](#c-cplusplus)
+ [Golang in AL1](#go)
+ [Java in AL1](#java)
+ [Perl in AL1](#perl)
+ [PHP in AL1](#php)
+ [Python in AL1](#python)
+ [Rust in AL1](#rust)

## C, C\+\+, and Fortran in AL1
<a name="c-cplusplus"></a>

AL1 includes both the GNU Compiler Collection (GCC) and the Clang frontend for LLVM (Low Level Virtual Machine).

## Golang in AL1
<a name="go"></a>

 AL1 updated the Go toolchain throughout the life of the operating system. This might have been be in response to a CVE in the toolchain or an emerging requirement needed to update another package.

## Java in AL1
<a name="java"></a>

 AL1 provided several versions of Java. The `java-1.6.0-openjdk` package was deprecated with the initial 2018.03 release, with `java-1.7.0-openjdk` and `java-1.8.0-openjdk` being available. For more information on the support for each version of Java in AL1, see [AL1 package support status](support-info-by-package.md).

## Perl in AL1
<a name="perl"></a>

AL1 provides version 5.16 of the [Perl](https://www.perl.org/) programming language.

## PHP in AL1
<a name="php"></a>

 AL1 provided several versions of the [PHP](https://www.php.net/) programming language, each supported for same period of time as upstream PHP. For more information on the length of support for each PHP version, see [AL1 package support status](support-info-by-package.md).

## Python in AL1
<a name="python"></a>

 With the 2018.03 release of AL1, Python 2.6 was deprecated. Python 2.6 continued to be available in the package repositories for backwards compatibility as customers finished their migration to Python 2.7 or 3.

 The system Python is 2.7, with various Python 3 versions available as options. For more information, see [AL1 package support status](support-info-by-package.md).

## Rust in AL1
<a name="rust"></a>

 There were updates to the Rust toolchain throughout the life of AL1.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Linux. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query linux` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
