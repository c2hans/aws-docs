---
source_url: https://docs.aws.amazon.com/linux/al2027/ug/package-management.html
---

# Package management tool
<a name="package-management"></a>

**AL2027 Preview**
AL2027 is currently available for preview. It is intended for evaluation and testing only and is not recommended for production workloads.

The default software package management tool in AL2027 is DNF5. DNF5 is the successor to DNF (version 4), the package management tool in AL2023. DNF5 is faster, uses less memory, and is where upstream package management development now happens.

Both the `dnf` and `yum` commands run DNF5 in AL2027. Day-to-day commands are unchanged from AL2023:

```
sudo dnf install packagename
sudo dnf search packagename
sudo dnf remove packagename
sudo dnf upgrade
```

For a complete command reference, run `man dnf5` or see the [DNF5 documentation](https://dnf5.readthedocs.io/en/latest/index.html) on the dnf5.readthedocs.io website.

**Topics**
+ [Compatibility with AL2023 commands](#package-management-compatibility)
+ [Migrating to DNF5](package-management-migration.md)
+ [RPM 6.0](#package-management-rpm)

## Compatibility with AL2023 commands
<a name="package-management-compatibility"></a>

AL2027 ships compatibility aliases so that common DNF (version 4) command spellings continue to work. This includes commands such as `dnf check-update`, `dnf updateinfo`, `dnf list installed`, `dnf groupinstall`, and `dnf erase`. Existing scripts that use these spellings run unchanged. The aliases are a standard part of AL2027, not a temporary migration aid.

Common DNF (version 4) option spellings also continue to work, such as `--sec-severity`, `--skip-broken`, and `--downloaddir`. A `--setopt` option that DNF5 does not recognize prints a warning instead of stopping the command. Scripts that pass settings specific to DNF (version 4) keep running.

AL2027 includes the command-line tools from the AL2023 `yum-utils` package. They run the equivalent DNF5 commands:
+ `repoquery`
+ `yumdownloader`
+ `yum-builddep`
+ `needs-restarting`
+ `reposync`
+ `repoclosure`
+ `repomanage`
+ `repotrack`
+ `package-cleanup`
+ `debuginfo-install`
+ `yum-config-manager`
+ `find-repos-of-install`

Installing the `yum-utils` or `dnf-utils` package name resolves to the `dnf5-plugins` package, which provides these tools.

Some differences remain. Command output formats differ. DNF5 renamed some options. For example, `--advisory` is now `--advisories`, with the old spelling kept as an alias. Options that took values in DNF (version 4) often became subcommands. For example, `dnf updateinfo --list` is now `dnf advisory list`. For the complete list, see [Changes in DNF5 compared to DNF](https://dnf5.readthedocs.io/en/latest/changes_from_dnf4.7.html) on the dnf5.readthedocs.io website.

Configuration carries over. DNF5 reads settings from `/etc/dnf/dnf.conf` and repository definitions from `/etc/yum.repos.d/`. The Amazon Linux defaults ship in a separate vendor file, so `/etc/dnf/dnf.conf` starts empty.

To define your own command aliases, add drop-in files under `/etc/dnf/dnf5-aliases.d/`.

For the changes that can break scripts and the steps to move, see [Migrating to DNF5](package-management-migration.md).

## RPM 6.0
<a name="package-management-rpm"></a>

AL2027 uses RPM 6.0, upgraded from RPM 4.16 in AL2023. Package signature verification uses the `rpm-sequoia` OpenPGP implementation. If you build and distribute your own RPM packages, test your spec files and package signing against RPM 6.0.
