---
source_url: https://docs.aws.amazon.com/linux/al2027/ug/spal.html
---

# Supplementary Packages for Amazon Linux

**AL2027 Preview**
AL2027 is currently available for preview. It is intended for evaluation and testing only and is not recommended for production workloads.

 This section introduces Supplementary Packages for Amazon Linux (SPAL) and outlines its benefits and limitations, along with guidelines for reporting package-related issues and requesting new packages.

**Topics**
+ [What is Supplementary Packages for Amazon Linux (or SPAL)?](#spal-what-is)
+ [Benefits](#spal-benefits)
+ [Support of SPAL packages](#spal-support)
+ [Reporting package-related issues](#spal-reporting)
+ [Requesting new packages](#spal-requesting)
+ [Related topics](#spal-more-info)
+ [Tutorial: Configure SPAL repository on AL2027](configure-spal-repository.md)

## What is Supplementary Packages for Amazon Linux (or SPAL)?
<a name="spal-what-is"></a>

 Supplementary Packages for Amazon Linux (SPAL) is a dedicated package repository that provides access to additional packages derived from [Fedora 44](https://fedoraproject.org/). These packages complement the existing software available in core Amazon Linux 2027. The Fedora release that SPAL is derived from tracks AL2027 and advances as AL2027 moves to a newer Fedora release.

 SPAL simplifies software deployment by providing pre-built packages that are compatible with AL2027, eliminating the need for customers to build packages from source code themselves. This saves time and effort in the software installation process.

 We made an initial set of packages available in SPAL for AL2027, and will expand it before the general availability (GA) of AL2027.

**Note**
 SPAL is available for AL2027 instances with a release version of ` 2027.0.20261112` or later.

## Benefits
<a name="spal-benefits"></a>

 SPAL provides several key advantages to Amazon Linux 2027 users:
+  **Expanding AL2027 use cases ** — Access to popular additional packages beyond the core AL2027 repository, such as `fish`, ` fzf` or `mosh`, enables customers to support multiple business and development needs.
+  **Simplifying AL2027 package management** — By providing packages pre-built for AL2027, the process of building additional packages from source is eliminated, saving time and reducing the risk of compilation errors.

## Support of SPAL packages
<a name="spal-support"></a>

 SPAL packages are not covered by the same level of support as core AL2027 packages, which receive support for the entire life of Amazon Linux 2027.

**Important**
 Prior to using SPAL, customers must carefully evaluate the following considerations:
SPAL packages **are NOT covered** by AWS Support Plans.
SPAL packages **are provided 'as-is'** from the upstream Fedora release that SPAL is derived from.
SPAL packages **will NOT receive** AWS CVE security tracking.
SPAL packages receive security patches and bug fixes **exclusively from the upstream Fedora release when available**.

## Reporting package-related issues
<a name="spal-reporting"></a>

 If you encounter an issue with an SPAL package, we recommend that you first check whether the same issue occurs with the corresponding package in the upstream Fedora. For this, please consult the [list of issues](https://bugzilla.redhat.com/buglist.cgi?product=Fedora) on the upstream Fedora bug tracker.

 If the issue is not present in Fedora, create an issue in the [Amazon Linux 2027 GitHub repository](https://github.com/amazonlinux/amazon-linux-2027/issues), as this indicates the problem is specific to the SPAL package build or configuration.

 This approach ensures issues are addressed by the appropriate maintainers and contributes to the overall quality of both SPAL and upstream Fedora packages.

**Note**
 The reported issues will be handled on a best-effort basis.

## Requesting new packages
<a name="spal-requesting"></a>

 To request that a package is added to SPAL, create an issue in the [Amazon Linux 2027 GitHub repository](https://github.com/amazonlinux/amazon-linux-2027/issues). Include the package name and a short description of your use case.

**Note**
 Package requests will be handled on a best-effort basis.

## Related topics
<a name="spal-more-info"></a>

For information on configuring SPAL on your system, consult the following documentation page:
+  [Tutorial: Configure SPAL repository on AL2027](configure-spal-repository.md)
