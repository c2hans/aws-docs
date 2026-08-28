---
source_url: https://docs.aws.amazon.com/linux/al2023/ug/spal.html
---

# Supplementary Packages for Amazon Linux
<a name="spal"></a>

 This section introduces Supplementary Packages for Amazon Linux (SPAL) and outlines its benefits and limitations, along with guidelines for reporting package-related issues.

**Topics**
+ [What is Supplementary Packages for Amazon Linux (or SPAL)?](#spal-what-is)
+ [Benefits](#spal-benefits)
+ [Support of SPAL packages](#spal-support)
+ [Reporting package-related issues](#spal-reporting)
+ [Related topics](#spal-more-info)
+ [Tutorial: Configure SPAL repository on AL2023](configure-spal-repository.md)

## What is Supplementary Packages for Amazon Linux (or SPAL)?
<a name="spal-what-is"></a>

 Supplementary Packages for Amazon Linux (SPAL) is a dedicated package repository that provides access to thousands of additional packages derived from [Extra Packages for Enterprise Linux 9 (EPEL9)](https://docs.fedoraproject.org/en-US/epel/epel-about/). These packages complement the existing software available in core Amazon Linux 2023.

 SPAL simplifies software deployment by providing pre-built packages that are compatible with AL2023, eliminating the need for customers to build packages from source code themselves. This saves time and effort in the software installation process.

**Note**
 SPAL is available in all AWS Commercial Regions, including the AWS GovCloud (US) Regions and China, for AL2023 instances with a release version of ` 2023.9.20251117` or later.

## Benefits
<a name="spal-benefits"></a>

 SPAL provides several key advantages to Amazon Linux 2023 users:
+  **Expanding AL2023 use cases ** — Access to popular additional packages beyond the core AL2023 repository, such as `pandoc`, ` GDAL` or `drbd-utils`, enables customers to support multiple business and development needs.
+  **Simplifying AL2023 package management** — By providing packages pre-built for AL2023, the process of building additional packages from source is eliminated, saving time and reducing the risk of compilation errors.
+  **Streamlining AL2 to AL2023 migration** — SPAL repository enables seamless migration of workloads from AL2 to AL2023, including workloads that depend on EPEL7 packages.

## Support of SPAL packages
<a name="spal-support"></a>

 SPAL packages are not covered by the same level of support as core AL2023 packages, which receive support for the entire life of Amazon Linux 2023.

**Important**
 Prior to using SPAL, customers must carefully evaluate the following considerations:
SPAL packages **are NOT covered** by AWS Support Plans.
SPAL packages **are provided 'as-is'** from upstream EPEL9.
SPAL packages **will NOT receive** AWS CVE security tracking.
SPAL packages receive security patches and bug fixes **exclusively from upstream EPEL9 when available**.

## Reporting package-related issues
<a name="spal-reporting"></a>

 If you encounter an issue with an SPAL package, we recommend to first check if the same issue occurs with the corresponding package in the upstream EPEL9 repository. For this, please consult the [list of issues](https://pagure.io/epel/issues) on the upstream EPEL repository.

 If the issue is not present in EPEL9, create an issue in the [Amazon Linux 2023 GitHub repository](https://github.com/amazonlinux/amazon-linux-2023/issues), as this indicates the problem is specific to the SPAL package build or configuration.

 This approach ensures issues are addressed by the appropriate maintainers and contributes to the overall quality of both SPAL and upstream EPEL packages.

**Note**
 The reported issues will be handled on a best-effort basis.

## Related topics
<a name="spal-more-info"></a>

For information on configuring SPAL on your system, consult the following documentation page:
+  [Tutorial: Configure SPAL repository on AL2023](configure-spal-repository.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Linux. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query linux` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
