---
source_url: https://docs.aws.amazon.com/linux/al2027/ug/security-update-advisory.html
---

# Applying security updates in-place
<a name="security-update-advisory"></a>

**AL2027 Preview**
AL2027 is currently available for preview. It is intended for evaluation and testing only and is not recommended for production workloads.

**Note**
We recommend applying *all* updates available in a new AL2027 release. Picking only security updates, or only specific updates, should be the exception rather than the rule. For an overview of applying all updates, see [Applying updates using DNF and repository versions](manage-updates.md#apply-security-updates).

To restrict an upgrade to packages that have a security advisory, use the `--security` option:

```
sudo dnf upgrade --security --releasever=latest
```

To apply only the updates from specific advisories, name them with the `--advisories` option. The advisory identifier in this example follows the Amazon Linux Security Advisory (ALAS) format:

```
sudo dnf upgrade --releasever=latest --advisories=ALAS2027-2026-001
```

This updates the packages mentioned in the advisory to the latest version available in the selected release, which might be newer than the version the advisory introduced. To update the affected packages only up to the lowest versions that fix the advisory, use `dnf upgrade-minimal` instead:

```
sudo dnf upgrade-minimal --releasever=latest --advisories=ALAS2027-2026-001
```

In the following example, the advisory is fixed by `zsh-5.9-21` and the repository also carries the newer `zsh-5.9-22`. The `upgrade-minimal` command selects the lowest version that fixes the advisory:

```
Updating and loading repositories:
Repositories loaded.
Package          Arch   Version           Repository       Size
Upgrading:
 zsh             x86_64 0:5.9-21.amzn2027 example       0.0   B
   replacing zsh x86_64 0:5.9-20.amzn2027 amazonlinux   7.9 MiB

Transaction Summary:
 Upgrading:          1 package
 Replacing:          1 package
```

If the fixed versions are already installed, both commands make no changes. You can also filter by severity with `--advisory-severities={{severity}}`, or by CVE with `--cves={{cve-id}}`.

**Note**
In DNF5, the DNF (version 4) option `--advisory` was renamed to `--advisories`. The old spelling is kept as a compatibility alias in AL2027.

**Note**
Unless the `system-release` package is updated, the release version that DNF is locked to *does not change*.

**Warning**
When installing updates from a newer release without changing the version that DNF is locked to, take care with subsequent mutating DNF operations. Package dependencies might have changed in the newer release, and the older release that you remain locked to might not be able to satisfy the new dependencies.

Advisory publication for AL2027 begins with the public preview. Until then, advisory-filtered commands find no matching updates. The preceding example was captured with example advisories, so the advisory identifier and package versions are examples. For listing the advisories that apply to a system, see [Listing applicable advisories](security-dnf-updateinfo.md).
