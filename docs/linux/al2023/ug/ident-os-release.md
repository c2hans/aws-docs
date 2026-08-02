---
source_url: https://docs.aws.amazon.com/linux/al2023/ug/ident-os-release.html
---

# Using the `os-release` standard
<a name="ident-os-release"></a>

 Amazon Linux complies with the [`os-release` standard](https://www.freedesktop.org/software/systemd/man/latest/os-release.html) for identifying Linux distributions. This file provides machine-readable information about the operating system identification and version information.

**Note**
 The standard dictates that `/etc/os-release` is attempted to be parsed first, followed by `/usr/lib/os-release`. Care should be taken to follow the standard around file names and paths.

**Topics**
+ [Key identification differences](#ident-key-differences)
+ [Field types: Machine-readable vs. Human-readable](#ident-os-release-field-types)
+ [`/etc/os-release` examples](#ident-os-release-examples)
+ [Comparison with other distributions](#ident-other-distributions-comparison)

## Key identification differences
<a name="ident-key-differences"></a>

 The `os-release` is found at `/etc/os-release`, and if that is not present, at `/usr/lib/os-release`. Consult the [`os-release` standard](https://www.freedesktop.org/software/systemd/man/latest/os-release.html) for complete information.

 The most reliable way to determine an instance is running Amazon Linux is to check the `ID` field in `os-release`.

 The most reliable way to determine distinguish between versions is to check the `VERSION_ID` field in `os-release`:
+ Amazon Linux AMI: `VERSION_ID` contains a date-based version (e.g., `2018.03`)
+ AL2: `VERSION_ID="2"`
+ AL2023: `VERSION_ID="2023"`

**Note**
 Remember that `VERSION_ID` is a machine-readable field intended for programmatic use, while `PRETTY_NAME` is designed for display to users. See [Field types: Machine-readable vs. Human-readable](#ident-os-release-field-types) for more information about field types.

## Field types: Machine-readable vs. Human-readable
<a name="ident-os-release-field-types"></a>

 The `/etc/os-release` file (or `/usr/lib/os-release` if `/etc/os-release` does not exist) contains two types of fields: machine-readable fields intended for programmatic use, and human-readable fields intended for presentation to users.

### Machine-readable fields
<a name="ident-machine-readable-fields"></a>

 These fields use standardized formats and are intended for processing by scripts, package managers, and other automated tools. They contain only lowercase letters, numbers, and limited punctuation (periods, underscores, and hyphens).
+ `ID` – Operating system identifier. Amazon Linux uses `amzn` across all versions, distinguishing it from other distributions like Debian (`debian`), Ubuntu (`ubuntu`), or Fedora (`fedora`)
+ `VERSION_ID` – Operating system version for programmatic use (e.g., `2023`)
+ `ID_LIKE` – Space-separated list of related distributions (e.g., `fedora`)
+ `VERSION_CODENAME` – Release codename for scripts (e.g., `karoo`)
+ `VARIANT_ID` – Variant identifier for programmatic decisions
+ `BUILD_ID` – Build identifier for system images
+ `IMAGE_ID` – Image identifier for containerized environments
+ `PLATFORM_ID` – Platform identifier (e.g., `platform:al2023`)

### Human-readable fields
<a name="ident-human-readable-fields"></a>

 These fields are intended for display to users and may contain spaces, mixed case, and descriptive text. They should be used when presenting operating system information in user interfaces.
+ `NAME` – Operating system name for display (e.g., `Amazon Linux`)
+ `PRETTY_NAME` – Full operating system name with version for display (e.g., `Amazon Linux 2023.8.20250721`)
+ `VERSION` – Version information suitable for user presentation
+ `VARIANT` – Variant or edition name for display (e.g., `Server Edition`)

### Other informational fields
<a name="ident-other-fields"></a>

 These fields provide additional metadata about the operating system:
+ `HOME_URL` – Project homepage URL
+ `DOCUMENTATION_URL` – Documentation URL
+ `SUPPORT_URL` – Support information URL
+ `BUG_REPORT_URL` – Bug reporting URL
+ `VENDOR_NAME` – Vendor name
+ `VENDOR_URL` – Vendor URL
+ `SUPPORT_END` – End-of-support date in YYYY-MM-DD format
+ `CPE_NAME` – Common Platform Enumeration identifier
+ `ANSI_COLOR` – ANSI color code for terminal display

 When writing scripts or applications that need to identify Amazon Linux programmatically, use the machine-readable fields like `ID` and `VERSION_ID`. When displaying operating system information to users, use the human-readable fields like `PRETTY_NAME`.

## `/etc/os-release` examples
<a name="ident-os-release-examples"></a>

 The `/etc/os-release` file content varies between Amazon Linux versions:

------
#### [ AL2023 ]

```
[ec2-user ~]$ cat /etc/os-release
```

```
NAME="Amazon Linux"
VERSION="2023"
ID="amzn"
ID_LIKE="fedora"
VERSION_ID="2023"
PLATFORM_ID="platform:al2023"
PRETTY_NAME="Amazon Linux 2023.8.20250721"
ANSI_COLOR="0;33"
CPE_NAME="cpe:2.3:o:amazon:amazon_linux:2023"
HOME_URL="https://aws.amazon.com/linux/amazon-linux-2023/"
DOCUMENTATION_URL="https://docs.aws.amazon.com/linux/"
SUPPORT_URL="https://aws.amazon.com/premiumsupport/"
BUG_REPORT_URL="https://github.com/amazonlinux/amazon-linux-2023"
VENDOR_NAME="AWS"
VENDOR_URL="https://aws.amazon.com/"
SUPPORT_END="2029-06-30"
```

------
#### [ AL2 ]

```
[ec2-user ~]$ cat /etc/os-release
```

```
NAME="Amazon Linux"
VERSION="2"
ID="amzn"
ID_LIKE="centos rhel fedora"
VERSION_ID="2"
PRETTY_NAME="Amazon Linux 2"
ANSI_COLOR="0;33"
CPE_NAME="cpe:2.3:o:amazon:amazon_linux:2"
HOME_URL="https://amazonlinux.com/"
SUPPORT_END="2026-06-30"
```

------
#### [ Amazon Linux AMI ]

```
[ec2-user ~]$ cat /etc/os-release
```

```
NAME="Amazon Linux AMI"
VERSION="2018.03"
ID="amzn"
ID_LIKE="rhel fedora"
VERSION_ID="2018.03"
PRETTY_NAME="Amazon Linux AMI 2018.03"
ANSI_COLOR="0;33"
CPE_NAME="cpe:/o:amazon:linux:2018.03:ga"
HOME_URL="http://aws.amazon.com/amazon-linux-ami/"
```

------

## Comparison with other distributions
<a name="ident-other-distributions-comparison"></a>

 To understand how Amazon Linux fits within the broader Linux ecosystem, compare its `/etc/os-release` format with other major distributions:

------
#### [ Fedora ]

```
[ec2-user ~]$ cat /etc/os-release
```

```
NAME="Fedora Linux"
VERSION="42 (Container Image)"
RELEASE_TYPE=stable
ID=fedora
VERSION_ID=42
VERSION_CODENAME=""
PLATFORM_ID="platform:f42"
PRETTY_NAME="Fedora Linux 42 (Container Image)"
ANSI_COLOR="0;38;2;60;110;180"
LOGO=fedora-logo-icon
CPE_NAME="cpe:/o:fedoraproject:fedora:42"
DEFAULT_HOSTNAME="fedora"
HOME_URL="https://fedoraproject.org/"
DOCUMENTATION_URL="https://docs.fedoraproject.org/en-US/fedora/f42/system-administrators-guide/"
SUPPORT_URL="https://ask.fedoraproject.org/"
BUG_REPORT_URL="https://bugzilla.redhat.com/"
REDHAT_BUGZILLA_PRODUCT="Fedora"
REDHAT_BUGZILLA_PRODUCT_VERSION=42
REDHAT_SUPPORT_PRODUCT="Fedora"
REDHAT_SUPPORT_PRODUCT_VERSION=42
SUPPORT_END=2026-05-13
VARIANT="Container Image"
VARIANT_ID=container
```

------
#### [ Debian ]

```
[ec2-user ~]$ cat /etc/os-release
```

```
PRETTY_NAME="Debian GNU/Linux 12 (bookworm)"
NAME="Debian GNU/Linux"
VERSION_ID="12"
VERSION="12 (bookworm)"
VERSION_CODENAME=bookworm
ID=debian
HOME_URL="https://www.debian.org/"
SUPPORT_URL="https://www.debian.org/support"
BUG_REPORT_URL="https://bugs.debian.org/"
```

------
#### [ Ubuntu ]

```
[ec2-user ~]$ cat /etc/os-release
```

```
PRETTY_NAME="Ubuntu 24.04.2 LTS"
NAME="Ubuntu"
VERSION_ID="24.04"
VERSION="24.04.2 LTS (Noble Numbat)"
VERSION_CODENAME=noble
ID=ubuntu
ID_LIKE=debian
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
UBUNTU_CODENAME=noble
LOGO=ubuntu-logo
```

------

 Notice how the machine-readable fields provide consistent identification across distributions:
+ `ID` – Uniquely identifies the operating system: `amzn` for Amazon Linux, `fedora` for Fedora, `debian` for Debian, `ubuntu` for Ubuntu
+ `ID_LIKE` – Shows distribution relationships: Amazon Linux uses `fedora` (AL2023) or `centos rhel fedora` (AL2), while Ubuntu shows `debian` to indicate its Debian heritage
+ `VERSION_ID` – Provides machine-parseable version information: `2023` for AL2023, `42` for Fedora, `12` for Debian, `24.04` for Ubuntu

 In contrast, the human-readable fields are designed for display to users:
+ `NAME` – User-friendly OS name: `Amazon Linux`, `Fedora Linux`, `Debian GNU/Linux`, `Ubuntu`
+ `PRETTY_NAME` – Complete display name with version: `Amazon Linux 2023.8.20250721`, `Fedora Linux 42 (Container Image)`, `Debian GNU/Linux 12 (bookworm)`, `Ubuntu 24.04.2 LTS`
+ `VERSION` – Human-readable version with additional context like codenames or release types

 When writing cross-platform scripts, always use the machine-readable fields (`ID`, `VERSION_ID`, `ID_LIKE`) for logic and decisions, and use the human-readable fields (`PRETTY_NAME`, `NAME`) only for displaying information to users.
