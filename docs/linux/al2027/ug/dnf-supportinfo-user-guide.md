---
source_url: https://docs.aws.amazon.com/linux/al2027/ug/dnf-supportinfo-user-guide.html
---

# Using the `dnf supportinfo` plugin
<a name="dnf-supportinfo-user-guide"></a>

**AL2027 Preview**
AL2027 is currently available for preview. It is intended for evaluation and testing only and is not recommended for production workloads.

Before you apply updates or plan a maintenance window, you can check whether a package stays supported for the period you need. Use the `dnf supportinfo` command, from the `dnf-plugin-support-info` package, to check the support status of an AL2027 package: whether it is supported now, what severity levels receive patches, and when its support status changes.

For more information about package support statements, see [Package support information](https://docs.aws.amazon.com/linux/al2027/release-notes/support-information.html) in the *AL2027 Release Notes*.

**Note**
During the preview, the reported support timeline for each package ends with the preview period. Support timelines for the AL2027 releases will be published with the public releases.

**Topics**
+ [Prerequisites](#dnf-supportinfo-prerequisites)
+ [Getting started](#dnf-supportinfo-getting-started)
+ [Query packages](#dnf-supportinfo-query-packages)
+ [Filter packages](#dnf-supportinfo-filter-packages)
+ [Structured output](#dnf-supportinfo-structured-output)
+ [Manage the cache](#dnf-supportinfo-manage-cache)
+ [Non-root usage](#dnf-supportinfo-non-root)
+ [Configuration reference](#dnf-supportinfo-configuration-reference)
+ [Output fields reference](#dnf-supportinfo-output-fields)
+ [Troubleshooting](#dnf-supportinfo-troubleshooting)
+ [Additional resources](#dnf-supportinfo-additional-resources)

## Prerequisites
<a name="dnf-supportinfo-prerequisites"></a>

Before you begin, make sure that you have the following:
+ An AL2027 instance
+ The `dnf-plugin-support-info` package, available from the default AL2027 repositories

No root privileges are required to run queries.

## Getting started
<a name="dnf-supportinfo-getting-started"></a>

Install the plugin.

```
$ sudo dnf install dnf-plugin-support-info
```

Query a package to verify the installation.

```
$ dnf supportinfo --pkg glibc
```

The output shows the package's support status and timeline:

```
Name                         : glibc
Version                      : 2.44-2.amzn2027
State                        : installed
Origin                       : Amazon Linux 2027 Core
Support Timeline             : from 2026-09-03     : supported (Low, Medium, Important, Critical)
                             : from 2027-03-31     : unsupported
Package Note                 : Amazon Linux will support this package until the end of the AL2027 public preview period
```

## Query packages
<a name="dnf-supportinfo-query-packages"></a>

Pass `--pkg` with one or more package names to show their support details.

```
$ dnf supportinfo --pkg {{package}} [{{package}} ...]
```

To query multiple packages in one command:

```
$ dnf supportinfo --pkg glibc bash openssl-libs
```

## Filter packages
<a name="dnf-supportinfo-filter-packages"></a>

The `--show` flag filters packages by state, support level, or both.

```
$ dnf supportinfo --show {{filter}} [{{filter}} ...]
```

There are two filter types:

| Category | Values | Source |
| --- | --- | --- |
| State filters (fixed) | installed, available, unavailable, all | Built into the plugin |
| Support level filters (dynamic) | Varies. For example, full\_support and eos | Loaded from the support data, so the values depend on what AL2027 defines |

Multiple filters of the same type combine with OR. Filters of different types combine with AND. For example, `--show installed eos` matches packages that are installed and at the `eos` support level. If a filter name exists in both categories, use the prefix syntax: `state:{{name}}` or `support:{{name}}`.

Run `--list-filters` to see all valid filter values grouped by category:

```
$ dnf supportinfo --list-filters
```

```
State filters:
  all                  - All packages (installed, available, and unavailable)
  available            - Packages available in repositories but not installed
  installed            - Packages currently installed on the system
  unavailable          - Packages in support info but not in any repository

Support level filters:
  eos                  - End of support - no further updates
  full_support         - Full security and bug fix support for all severities
```

To list the support information for all installed packages:

```
$ dnf supportinfo --show installed
```

The output lists each package in a table:

```
Package                          Version                            State        Support Level    Current Status         Until (Next Phase)           Note
alternatives                     1.33-3.amzn2027.0.2                installed                                                                         Amazon Linux will support this package until the end of the AL2027 public preview period
audit-libs                       4.1.3-1.amzn2027.0.1               installed                                                                         Amazon Linux will support this package until the end of the AL2027 public preview period
# Output truncated for brevity
```

To use the prefix syntax:

```
$ dnf supportinfo --show state:installed support:full_support
```

## Structured output
<a name="dnf-supportinfo-structured-output"></a>

For scripts and automation, `--showjson` and `--showxml` produce machine-readable output.

To get JSON output:

```
$ dnf supportinfo --pkg bash --showjson
```

The output contains the package's phases, origin, and timeline with support level details:

```
{
  "name": "bash",
  "version": "5.3.0-2.amzn2027",
  "state": "installed",
  "origin": "Amazon Linux 2027 Core",
  "phases": [
    {
      "name": "supported",
      "start_date": "2026-09-03",
      "patch_priority": "Full Support",
      "support_level_description": "Full security and bug fix support for all severities",
      "covered_severities": "Low, Medium, Important, Critical"
    },
    {
      "name": "unsupported",
      "start_date": "2027-03-31",
      "patch_priority": "End of Support",
      "support_level_description": "End of support - no further updates"
    }
  ],
  "note": "Amazon Linux will support this package until the end of the AL2027 public preview period"
}
```

To get XML output:

```
$ dnf supportinfo --pkg bash --showxml
```

The output is an XML document with a `package_support` root element containing the package's phases, start dates, and support level details. For the schema reference, see [SupportInfo XML structure](dnf-supportinfo-xml-structure.md).

## Manage the cache
<a name="dnf-supportinfo-manage-cache"></a>

Your queries use a local cache of the support data, which avoids unnecessary network requests. When the cache expires, the plugin checks for changes to the remote file. If the file is unchanged, the cache refreshes without downloading. If it changed, the plugin downloads the updated file. On network errors, the plugin uses the cached file if one is available.

To download and cache the latest support data, for example in automation that needs fresh data without a full query:

```
$ dnf supportinfo --sync
```

```
Support info sync complete
```

To clear the cache:

```
$ dnf supportinfo --clean-cache
```

```
Cleaned support info cache.
```

## Non-root usage
<a name="dnf-supportinfo-non-root"></a>

All commands work without root privileges. When run as root, the cache is stored at `/var/cache/libdnf5/support-info/`. When run as a non-root user, the cache goes to `~/.cache/libdnf5/support-info/` in the user's home directory.

## Configuration reference
<a name="dnf-supportinfo-configuration-reference"></a>

The plugin reads configuration from `/etc/dnf/plugins/supportinfo.conf`. The following is the configuration shipped with AL2027:

```
[main]
baseurl = https://cdn-al2027.amazonlinux.com/core/AL2027-supportinfo-1.0.xml
templateurl = https://cdn-al2027.amazonlinux.com/core/supportinfo-1.0.xsd
```

| Option | Description | Default |
| --- | --- | --- |
| baseurl | URL to the support info XML file. | Required |
| templateurl | URL to the XSD schema for validation. | None |
| metadata\_expire | Cache duration in seconds. | 1800 |

## Output fields reference
<a name="dnf-supportinfo-output-fields"></a>

The `--pkg` output contains the following fields:

| Field | Description |
| --- | --- |
| Name | Package name |
| Version | Installed or available version |
| State | installed, available, or unavailable |
| Origin | Repository providing the package |
| Support Timeline | Chronological list of lifecycle phases with dates and the severities covered in each phase |
| Package Note | Additional context, such as support period notes |

## Troubleshooting
<a name="dnf-supportinfo-troubleshooting"></a>

If query results look stale, sync the cache manually:

```
$ dnf supportinfo --sync
```

If the issue persists, clear the cache and sync again:

```
$ dnf supportinfo --clean-cache
dnf supportinfo --sync
```

## Additional resources
<a name="dnf-supportinfo-additional-resources"></a>
+ [DNF support info plugin](https://github.com/amazonlinux/dnf-plugin-support-info) on the GitHub website
+ [amazon-linux-supportinfo parsing library](https://github.com/amazonlinux/amazon-linux-supportinfo) on the GitHub website
