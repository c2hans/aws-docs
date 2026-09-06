---
source_url: https://docs.aws.amazon.com/linux/al2027/ug/alas.html
---

# Amazon Linux Security advisories for AL2027
<a name="alas"></a>

**AL2027 Preview**
AL2027 is currently available for preview. It is intended for evaluation and testing only and is not recommended for production workloads.

 Although we work hard to make Amazon Linux secure, at times there will be security issues that require fixing. An *advisory* is issued when a fix is available. The primary location where we publish advisories is the Amazon Linux Security Center (ALAS). For more information, see [Amazon Linux Security Center](https://alas.aws.amazon.com/).

**Important**
 If you want to report a vulnerability or have a security concern regarding AWS cloud services or open source projects, contact AWS Security using the [Vulnerability Reporting page](https://aws.amazon.com/security/vulnerability-reporting/)

 Information on issues and the relevant updates that affect AL2027 are published by the Amazon Linux team in several locations. It's common for security tooling to fetch information from these primary sources and present the results to you. As such, you might not directly interact with the primary sources that Amazon Linux publishes, but instead the interface provided by your preferred tooling, such as [Amazon Inspector](https://docs.aws.amazon.com/inspector/latest/user/what-is-inspector.html).

## Amazon Linux Security Center announcements
<a name="alas-announcements"></a>

 Amazon Linux *announcements* are provided for items that do not fit into an advisory. This section contains announcements about ALAS itself, along with information that does not fit in an advisory. For more information, see [Amazon Linux Security Center (ALAS) Announcements](https://alas.aws.amazon.com/announcements.html)

## Amazon Linux Security Center Frequently Asked Questions
<a name="alas-faqs"></a>

 For answers to some frequently asked questions about ALAS and how Amazon Linux evaluates CVEs, see [Amazon Linux Security Center (ALAS) Frequently Asked Questions (FAQs)](https://alas.aws.amazon.com/faqs.html).

## ALAS Advisories
<a name="alas-advisories"></a>

 An Amazon Linux Advisory contains important information relevant to Amazon Linux users, typically information about security updates. The [Amazon Linux Security Center](https://alas.aws.amazon.com/) is where Advisories are visible on the web. Advisory information is also part of the RPM package repository metadata.

## Advisories and RPM repositories
<a name="advisory-and-repos"></a>

 An Amazon Linux 2027 package repository may contain metadata describing zero or more updates. The `dnf updateinfo` command is named after the repository metadata filename which contains this information, `updateinfo.xml`. While the command is named `updateinfo`, and the metadata file refers to an `update`, these all refer to package updates which are part of an Advisory.

 Amazon Linux Advisories are published on the [Amazon Linux Security Center](https://alas.aws.amazon.com/) web site, along with information being present in the RPM repository metadata that the `dnf` package manager refers to. The web site and repository metadata are eventually consistent, and there may be inconsistencies in the information on the web site and in repository metadata. This will typically occur when a new release of AL2027 is in the process of being released, there has been an update to an Advisory after the most recent AL2027 release.

 While it is typical for a new Advisory to be issued alongside the package update which addresses the issue, this is not always the case. An Advisory can be created for a new issue which is addressed in already released packages. An existing Advisory may also be updated with new CVEs which are addressed by the existing update.

 The [Deterministic upgrades through versioned repositories on AL2027](deterministic-upgrades.md) feature of Amazon Linux 2027 means that the RPM repository for a particular AL2027 version contains a snapshot of the RPM repository metadata as of that version. This *includes* the metadata describing security updates. The RPM repository for particular AL2027 version *is not updated* after release. New or updated security advisories *will not be visible when looking at an older version of the AL2027 RPM repositories*. Refer to the [Listing applicable advisories](security-dnf-updateinfo.md) section for how to use the `dnf` package manager to look at either the `latest` repository version, or a specific AL2027 release.

## Advisory IDs
<a name="advisory-ids"></a>

 Each Advisory is referred to by an `id`. It is currently a quirk of Amazon Linux where the [Amazon Linux Security Center](https://alas.aws.amazon.com/) web site will list an Advisory as [ALAS-2024-581](https://alas.aws.amazon.com/AL2023/ALAS-2024-581.html), while the `dnf` package manager will [list that advisory as having the ID of ALAS2023-2024-581](security-dnf-updateinfo.md). When [Applying security updates in-place](security-update-advisory.md) the package manager ID needs to be used if referring to a specific Advisory.

 For Amazon Linux, each major version of the OS has its own namespace of Advisory IDs. There should be no assumptions made as to the format of Amazon Linux Advisory IDs. Historically, Amazon Linux Advisory IDs have followed the pattern of `NAMESPACE-YEAR-NUMBER`. The full range of possible values for `NAMESPACE` is not defined, but has included `ALAS`, `ALASCORRETTO8`, `ALAS2023`, `ALAS2`, `ALASPYTHON3.8`, and `ALASUNBOUND-1.17`. The `YEAR` has been the year in which the advisory was created, and `NUMBER` being a unique integer within the namespace.

 While Advisory IDs will *typically* be sequential and in the order the updates are released, there are many reasons why this could not be the case, so this should not be assumed.

 Treat the Advisory ID as an opaque string which is unique to each major version of Amazon Linux.

 In Amazon Linux 2, each Extra was in a separate RPM repository, and the Advisory metadata is contained only within the repository to which it is relevant. An Advisory for one repository *is not applicable* to another repository. On the [Amazon Linux Security Center](https://alas.aws.amazon.com/alas2.html) web site, there is currently one list of Advisories for each major Amazon Linux version, and it is not separated out into per-repository lists.

## Advisory Released Date and Advisory Updated Date
<a name="advisory-dates"></a>

 The Advisory Released Date for Amazon Linux Advisories indicates when the security update was first made publicly available in the RPM repository. Advisories are posted on the [Amazon Linux Security Center](https://alas.aws.amazon.com/) web site immediately after fixes are made available for installation through the RPM repository.

 The Advisory Updated Date indicates when new information was added to an advisory after it was previously published.

 There should not be any assumptions made between the AL2027 version number and the Advisory Released Date of Advisories published alongside that release.

## Advisory Types
<a name="advisory-types"></a>

 The RPM repository metadata supports Advisories of different types. While Amazon Linux has near universally only issued Advisories which are security updates, this should not be assumed. It is possible that Advisories for events such as bug fixes, enhancements, and new packages could be issued, and the Advisory be marked as containing that type of update.

## Advisory Severities
<a name="advisory-severities"></a>

 Each Advisory has its own Severity as each issue is evaluated separately. Multiple CVEs may be addressed in a single Advisory, and each CVE may have a different evaluation, but the Advisory itself has one Severity. There can be multiple Advisories referring to a single package update, thus there can be multiple Severities for a particular package update (one per Advisory).

 In order of decreasing Severity, Amazon Linux has used Critical, Important, Moderate, and Low to indicate the Severity of an Advisory. Amazon Linux Advisories may also *not have a Severity*, although this is exceedingly rare.

 Amazon Linux is one of the RPM based Linux distributions that uses the term Moderate, while some other RPM based Linux distributions use the equivalent term Medium. The Amazon Linux package manager treats both terms as equivalent, and third party package repositories may use the term Medium.

 Amazon Linux Advisories can *change Severity* over time as more is learned about the relevant issues addressed in the Advisory.

 The Severity of an Advisory will *typically* track the highest Amazon Linux evaluated CVSS score for the CVEs referenced by the Advisory. There may be cases where this is not the case. One example would be where there is an issue which is addressed for which there is not a CVE assigned.

 See the [ALAS FAQ](https://alas.aws.amazon.com/faqs.html) for more information about how Amazon Linux uses Advisory severity ratings.

## Advisories and Packages
<a name="advisory-packages"></a>

 There can be many Advisories for a single package, and not all packages will ever have an Advisory published for them. A particular package version can be referenced in multiple Advisories, each with its own Severity and CVEs.

 It is possible for multiple Advisories for the same package update to be issued simultaneously in one new AL2027 release, or in rapid succession.

 Like other Linux distributions, there can be one to many different binary packages built from the same source package. For example, [ALAS-2024-698](https://alas.aws.amazon.com/AL2023/ALAS-2024-698.html) is an Advisory listed on the AL2027 section of the [Security Center web site](https://alas.aws.amazon.com/) as applying to the `mariadb105` package. This is the *source* package name, and the Advisory itself refers to the *binary* packages alongside the source package. In this case, over a dozen binary packages are built from the one `mariadb105` source package. While it is extremely common for there to be a binary package with the same name as the source package, this is not universal.

 While Amazon Linux Advisories have typically listed all binary packages built from the updated source package, this should not be assumed. The package manager and RPM repository metadata format allows for Advisories that list a subset of the updated binary packages.

 A particular Advisory may also only apply to a particular CPU Architecture. There can be packages that are not built for all architectures, or issues that do not affect all architectures. In the case where a package is available on all architectures but an issue applies only to one, Amazon Linux has typically not issued an Advisory only referencing only the affected architecture, although this should not be assumed.

 Due to the nature of package dependencies, it is common that an Advisory references one package, but installing that update will require other package updates, including packages that are not listed in the Advisory. The `dnf` package manager will handle installing the required dependencies.

## Advisories and CVEs
<a name="advisory-cves"></a>

 An Advisory may address zero or more CVEs, and there may be multiple Advisories referencing the same CVE. An example of when an Advisory may reference zero CVEs is when a CVE is not yet (or ever) assigned to the issue.

 An example of where multiple Advisories may reference the same CVE when (for example) the CVE is applicable to multiple packages. For example, [CVE-2024-21208](https://alas.aws.amazon.com/cve/html/CVE-2024-21208.html) applies to Corretto 8, 11, 17, and 21. Each of these Corretto versions is a separate package in Amazon Linux, and there is an Advisory for each of these packages: [ALAS-2024-754](https://alas.aws.amazon.com/AL2023/ALAS-2024-754.html) for Corretto 8, [ALAS-2024-753](https://alas.aws.amazon.com/AL2023/ALAS-2024-753.html) for Corretto 11, [ALAS-2024-752](https://alas.aws.amazon.com/AL2023/ALAS-2024-752.html) for Corretto 17, and [ALAS-2024-752](https://alas.aws.amazon.com/AL2023/ALAS-2024-751.html) for Corretto 21. While these Corretto releases all have the same list of CVEs, this should not be assumed.

 A particular CVE can be evaluated differently for different packages. For example, if a particular CVE is referenced in an Advisory with a Severity of Important, it is possible that another Advisory is issued referencing the same CVE with a different Severity.

 The RPM repository metadata allows for a list of References for each Advisory. While Amazon Linux has typically only referenced CVEs, the metadata format does allow for other reference types.

 The RPM package repository metadata will only refer to CVEs with a fix available. The [Explore section of the Amazon Linux Security Center](https://explore.alas.aws.amazon.com) web site contains information on CVEs that Amazon Linux has evaluated. This evaluation may result in a CVSS base score, Severity, and status for various Amazon Linux releases and packages. The status for a CVE for a particular Amazon Linux release or package may be Not Affected, Pending Fix, or No Fix Planned. The status and evaluation of CVEs may change many times and *in any way* prior to an Advisory being issued. This includes re-evaluation of the applicability of a CVE to Amazon Linux.

 The list of CVEs referenced by an Advisory can change after initial publication of that Advisory.

## Advisory Text
<a name="advisory-text"></a>

 An Advisory will also contain text describing the issue or issues that were the reason for creating the Advisory. It is common that this text will be the unmodified CVE text. This text may refer to upstream version numbers where a fix is available which are different from the package version that Amazon Linux has applied a fix to. It is common that Amazon Linux will back-port fixes from newer upstream releases. In the case where the Advisory text mentions an upstream release which is different than the version shipped in an Amazon Linux version, the Amazon Linux package versions in the Advisory will be accurate for Amazon Linux.

 It is possible for the Advisory text in the RPM repository metadata to be placeholder text simply referring to the [Amazon Linux Security Center](https://alas.aws.amazon.com/alas2027.html) web site for details.

## Kernel Live Patch Advisories
<a name="livepatch-advisories"></a>

 Advisories for live patches are unique in that they refer to a different package (the Linux kernel) than the package the Advisory is against (e.g. `kernel-livepatch-6.1.15-28.43`).

 An Advisory for a Kernel Live Patch will reference the issues (such as CVEs) which the particular Live Patch package can address for the *specific* kernel version to which the live patch package applies.

 Each live patch is for a *specific* kernel version. In order to apply a live patch for a CVE, the right live patch package for your kernel version needs to be installed, and the live patch applied.

 For example, [CVE-2023-6111](https://alas.aws.amazon.com/cve/html/CVE-2023-6111.html) can be live patched for AL2023 kernel versions `6.1.56-82.125`, `6.1.59-84.139`, and `6.1.61-85.141`. A new kernel version with a fix for this CVE was also released, and has [a separate advisory](https://alas.aws.amazon.com/AL2023/ALAS-2023-461.html). In order for [CVE-2023-6111](https://alas.aws.amazon.com/cve/html/CVE-2023-6111.html) to be addressed on AL2023 either a kernel version equal to or later than what [ALAS2023-2023-461](https://alas.aws.amazon.com/AL2023/ALAS-2023-461.html) specifies needs to be *running*, or one of the kernel versions with a live patch for this CVE needs to be running with the applicable livepatch applied.

 When there are new live patches available for a specific kernel version which already has a live patch available, a new version of the `kernel-livepatch-KERNEL_VERSION` package is released. For example, the [ALASLIVEPATCH-2023-003](https://alas.aws.amazon.com/AL2023/ALASLIVEPATCH-2023-003.html) Advisory was issued with the `kernel-livepatch-6.1.15-28.43-1.0-1.amzn2023` package which contained live patches for the `6.1.15-28.43` kernel covering three CVEs. Later, the [ALASLIVEPATCH-2023-009](https://alas.aws.amazon.com/AL2023/ALASLIVEPATCH-2023-009.html) Advisory was issued with the `kernel-livepatch-6.1.15-28.43-1.0-2.amzn2023` package; an update to the previous live patch package for the `6.1.15-28.43` kernel containing live patches for another three CVEs. There were also other live patch Advisories issues for other kernel versions, with packages containing live patches for those specific kernel versions.

 For anyone developing tools around security advisories, it is also recommended to look at the [XML Schema for Advisories and `updateinfo.xml`](#advisory-schema) section for more information.

## XML Schema for Advisories and `updateinfo.xml`
<a name="advisory-schema"></a>

 The `updateinfo.xml` file is part of the package repository format. It is the metadata that the `dnf` package manager parses to implement functionality such as [Listing applicable advisories](security-dnf-updateinfo.md) and [Applying security updates in-place](security-update-advisory.md).

 We recommended that the API of the `dnf` package manager is used rather than writing custom code to parse the repository metadata formats.

 The [RPM Software Management](https://github.com/rpm-software-management/) project documents the RPM metadata formats in the [rpm-metadata](https://github.com/rpm-software-management/rpm-metadata) repository on GitHub.

 For those developing tools to directly parse the `updateinfo.xml` metadata, paying careful attention to the [rpm-metadata documentation](https://github.com/rpm-software-management/rpm-metadata) is strongly advised. The documentation covers what has been seen in the wild, which includes many exceptions to what you may reasonably interpret as a rule for the metadata format.

 There is also a growing set of real-world examples of `updateinfo.xml` files in the [raw-historical-rpm-repository-examples](https://github.com/rpm-software-management/raw-historical-rpm-repository-examples) repository on GitHub.

 In case anything is unclear in the documentation, you can open an issue on the GitHub project so that we can answer the question and update the documentation appropriately. As Open Source projects, pull requests updating documentation are also welcome.
