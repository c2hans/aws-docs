---
source_url: https://docs.aws.amazon.com/linux/al2027/release-notes/support-information.html
---

# Package support information
<a name="support-information"></a>

**AL2027 Preview**
AL2027 is currently available for preview. It is intended for evaluation and testing only and is not recommended for production workloads.

This page describes the support lifecycle for the packages included in Amazon Linux 2027 (AL2027). Use this page to find the support level of a package. You can also find out when a package's support level changes and when it reaches end of support. Packages move through a series of lifecycle phases. Each phase has a defined support level that determines the severity of issues addressed during that phase.

All AL2027 packages are distributed from a single core repository and share one support model. The following section describes that support model and links to the package list that carries the support statement for each package.

To query support information for the packages installed on a running instance, use the `dnf supportinfo` command. For more information, see the following pages in the *AL2027 User Guide*:
+  [Query package support with the AL2027 support info plugin](https://docs.aws.amazon.com/linux/al2027/ug/dnf-supportinfo-plugin.html)
+  [Using the dnf supportinfo plugin](https://docs.aws.amazon.com/linux/al2027/ug/dnf-supportinfo-user-guide.html)
+  [SupportInfo XML structure](https://docs.aws.amazon.com/linux/al2027/ug/dnf-supportinfo-xml-structure.html)

**Topics**
+ [Amazon Linux 2027 (AL2027) core packages](#support-information-al2027)

## Amazon Linux 2027 (AL2027) core packages
<a name="support-information-al2027"></a>

Core packages receive full support for the duration of the AL2027 public preview. Support timelines for the AL2027 releases will be published with the public releases.

### Support milestones
<a name="support-information-milestones"></a>

Key dates for Amazon Linux 2027 (AL2027) support.

| Milestone | Date | Description |
| --- | --- | --- |
| AL2027 Public Preview | 2026-09-03 | Amazon Linux 2027 public preview date |
| AL2027 Public Preview End of Support | 2027-03-31 | End of support for Amazon Linux 2027 public preview packages |

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
| Amazon Linux 2027 Core | Core Amazon Linux 2027 repository containing base OS packages |

### Core package support status
<a name="support-information-al2027-packages"></a>

For the support status of an individual core package, see [All Amazon Linux 2027 packages](all-packages.md).
