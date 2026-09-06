---
source_url: https://docs.aws.amazon.com/linux/al2027/ug/security-dnf-updateinfo.html
---

# Listing applicable advisories
<a name="security-dnf-updateinfo"></a>

**AL2027 Preview**
AL2027 is currently available for preview. It is intended for evaluation and testing only and is not recommended for production workloads.

The DNF package manager has access to metadata describing which advisories are fixed in which package versions. It can list the advisories that are applicable to an instance or container image. Tools such as [AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/) use this metadata to show relevant updates across a fleet rather than a single instance.

In AL2027, advisory information is queried with the `dnf advisory` command and its `summary`, `list`, and `info` subcommands:

```
# Summary of advisories applicable to this system
dnf advisory summary

# One line per applicable advisory and package
dnf advisory list

# Full details of one advisory
dnf advisory info <advisory-id>
```

Advisory publication for AL2027 begins with the public preview, using the same Amazon Linux Security Advisory (ALAS) model as AL2023. The following outputs show the format. They were captured with example advisories, so the advisory identifiers and CVE numbers are examples:

```
dnf advisory summary
```

```
Available advisory information summary:
Security    : 2
  Critical  : 0
  Important : 1
  Moderate  : 0
  Low       : 1
  Other     : 0
Bugfix      : 0
Enhancement : 0
Other       : 0
```

```
dnf advisory list
```

```
Name              Type     Severity                  Package                 Issued
ALAS2027-2026-001 security Important zsh-5.9-21.amzn2027.x86_64 2026-08-17 18:00:00
ALAS2027-2026-002 security Low       zsh-5.9-22.amzn2027.x86_64 2026-08-17 18:00:00
```

```
dnf advisory info ALAS2027-2026-001
```

```
Name        : ALAS2027-2026-001
Title       : Amazon Linux 2027 - ALAS2027-2026-001: Important priority package update: zsh
Severity    : Important
Type        : security
Status      : final
Vendor      : linux-security@amazon.com
Issued      : 2026-08-17 18:00:00
Description : Package updates are available for Amazon Linux 2027 that fix the following vulnerabilities:
            : CVE-2026-12345
Message     :
Rights      :
Reference   :
  Title     : CVE-2026-12345
  Id        : CVE-2026-12345
  Type      : cve
  Url       : https://alas.aws.amazon.com/cve/html/CVE-2026-12345.html
Collection  :
  Packages  : zsh-5.9-21.amzn2027.x86_64
```

By default, the commands consider advisories for available package upgrades. Use the `--installed`, `--updates`, or `--all` options to change the scope, and `--contains-pkgs={{name}}` to filter by package. As with other DNF commands, add `--releasever={{version}}` to evaluate the metadata of a newer release than the one the system is locked to:

```
dnf advisory summary --releasever=latest
```

**Note**
After an AL2027 release is made, it is immutable. New or updated advisories are only added to the metadata of *new* releases. To see the newest advisories, query with `--releasever=latest`.

If you are migrating from AL2023: DNF5 replaces the `dnf updateinfo --list` option style with subcommands, such as `dnf advisory list`. The `dnf updateinfo` spelling is kept as an alias for `dnf advisory`, so `dnf updateinfo list` also works.

To list advisories against a specific release, name it. To list against the newest release, use `latest`. Both forms report zero advisories until advisory publication begins with the public preview:

```
dnf advisory summary --releasever=2027.0.20260817
dnf advisory summary --releasever=latest
```

For the preview patching policy, see [Known issues and preview limitations](known-issues.md). For information about Amazon Linux Security Advisories, see [Amazon Linux Security advisories for AL2027](alas.md).
