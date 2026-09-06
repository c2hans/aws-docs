---
source_url: https://docs.aws.amazon.com/linux/al2023/release-notes/support-information.html
---

# Package support information
<a name="support-information"></a>

This page describes the support lifecycle for the packages included in Amazon Linux 2023 (AL2023). Use it to find out the support level of a package, when its support level is scheduled to change, and the date on which it reaches end of support. Packages move through a series of lifecycle phases, each with a defined support level that determines the severity of issues addressed during that phase.

Packages are distributed from two repositories, and each one has its own support model. The sections below cover AL2023 core packages and Supplementary Packages for Amazon Linux (SPAL) separately, and link to the package lists that carry the support statement for each package.

To query support information for the packages installed on a running instance, use the `dnf supportinfo` command. For more information, see the following pages in the *AL2023 User Guide*:
+  [Query package support with the AL2023 support info plugin](https://docs.aws.amazon.com/linux/al2023/ug/dnf-supportinfo-plugin.html)
+  [Using the dnf supportinfo plugin](https://docs.aws.amazon.com/linux/al2023/ug/dnf-supportinfo-user-guide.html)
+  [Migrating from dnf-plugin-support-info v1 to v2](https://docs.aws.amazon.com/linux/al2023/ug/dnf-supportinfo-migrate-v1-v2.html)
+  [SupportInfo XML structure](https://docs.aws.amazon.com/linux/al2023/ug/dnf-supportinfo-xml-structure.html)

**Topics**
+ [Amazon Linux 2023 (AL2023) core packages](#support-information-al2023)
+ [Supplementary Packages for Amazon Linux (SPAL)](#support-information-spal)

## Amazon Linux 2023 (AL2023) core packages
<a name="support-information-al2023"></a>

Core packages are supported by AWS for the life of Amazon Linux 2023 (AL2023), except where a package follows its own upstream support model and reaches end of support earlier.

### Support milestones
<a name="support-information-milestones"></a>

Key dates for Amazon Linux 2023 (AL2023) support.

| Milestone | Date | Description |
| --- | --- | --- |
| AL2023 General Availability | 2023-03-15 | Amazon Linux 2023 general availability date |
| AL2023 End of Support | 2029-06-30 | End of all support for Amazon Linux 2023 |

### Support levels
<a name="support-information-levels"></a>

The following support levels define what severity of issues are addressed.

| Support level | Description | Severities addressed |
| --- | --- | --- |
| Full Support | Full security and bug fix support for all severities | Low, Medium, Important, Critical |
| End of Support | End of support - no further updates | None |

### Package origins
<a name="support-information-origins"></a>

Repository sources from which packages are distributed.

| Origin | Description |
| --- | --- |
| Amazon Linux 2023 Core | Core Amazon Linux 2023 repository containing base OS packages |

### Core package support status
<a name="support-information-al2023-packages"></a>

For the support status of an individual core package, see [Amazon Linux 2023 RPM packages as of the 2023.12.20260817 release](all-packages-AL2023.12.md).

## Supplementary Packages for Amazon Linux (SPAL)
<a name="support-information-spal"></a>

SPAL is a separate AL2023 repository derived from [Extra Packages for Enterprise Linux 9 (EPEL9)](https://docs.fedoraproject.org/en-US/epel/epel-about/). SPAL packages are not covered by the same level of support as core AL2023 packages, and the support milestones and support levels described in the previous section do not apply to them.

**Important**
Prior to using SPAL, customers must carefully evaluate the following considerations:
SPAL packages **are NOT covered** by AWS Support Plans.
SPAL packages **are provided 'as-is'** from upstream EPEL9.
SPAL packages **will NOT receive** AWS CVE security tracking.
SPAL packages receive security patches and bug fixes **exclusively from upstream EPEL9 when available**.

For more information about SPAL, see [Supplementary Packages for Amazon Linux](https://docs.aws.amazon.com/linux/al2023/ug/spal.html) in the *AL2023 User Guide*.
