---
source_url: https://docs.aws.amazon.com/linux/al2023/ug/dnf-supportinfo-user-guide.html
---

# Using the dnf supportinfo Plugin
<a name="dnf-supportinfo-user-guide"></a>

The dnf-plugin-support-info package provides the `dnf supportinfo` command for AL2023. Use this command to query lifecycle and support information for packages: find out whether a package is currently supported, what severity levels receive patches, and when support status changes.

For a summary view of all package support statements, see [AL2023 Support Statements](https://docs.aws.amazon.com/linux/al2023/release-notes/support-information.html) in the *AL2023 Release Notes*.

**Important**
The v2 plugin ships with `legacy = 1` in `/etc/dnf/plugins/supportinfo.conf`. In this mode, output uses the v1 field names and format. In a future AL2023 quarterly release, the default changes to `legacy = 0`, switching to the v2 output format documented on this page. To start using v2 output now, set `legacy = 0` in your configuration. For details on what changes, see [Migrating from dnf-plugin-support-info v1 to v2](dnf-supportinfo-migrate-v1-v2.md).

**Topics**
+ [Prerequisites](#dnf-supportinfo-prerequisites)
+ [Getting Started](#dnf-supportinfo-getting-started)
+ [Query Packages](#dnf-supportinfo-query-packages)
+ [Filter Packages](#dnf-supportinfo-filter-packages)
+ [Structured Output](#dnf-supportinfo-structured-output)
+ [Manage the Cache](#dnf-supportinfo-manage-cache)
+ [Non-root Usage](#dnf-supportinfo-non-root)
+ [Configuration Reference](#dnf-supportinfo-configuration-reference)
+ [Output Fields Reference](#dnf-supportinfo-output-fields)
+ [Schema](#dnf-supportinfo-schema)
+ [Migration from Legacy Plugin](#dnf-supportinfo-migration-from-legacy)
+ [Troubleshooting](#dnf-supportinfo-troubleshooting)
+ [Additional Resources](#dnf-supportinfo-additional-resources)

## Prerequisites
<a name="dnf-supportinfo-prerequisites"></a>
+ AL2023 instance
+ The dnf-plugin-support-info package (available from default AL2023 repositories)
+ No root privileges required (except for `--sync` in [legacy mode](#dnf-supportinfo-migration-from-legacy))

## Getting Started
<a name="dnf-supportinfo-getting-started"></a>

1. Install the plugin.

   ```
   sudo dnf install dnf-plugin-support-info
   ```

1. Query a package to verify the installation.

   ```
   dnf supportinfo --pkg glibc
   ```

   The output shows the package's support status and timeline:

   ```
   Name                         : glibc
   Version                      : 2.34-231.amzn2023.0.4
   State                        : installed
   Current Status               : Supported
   Patch Priority               : Full Support
   Support Level Description    : Full security and bug fix support for all severities
   Covered Severities           : Low, Medium, Important, Critical
   Origin                       : Amazon Linux 2023 Core
   Support Timeline             : from 2023-03-15     : supported
                                : from 2029-06-30     : unsupported
   ```

## Query Packages
<a name="dnf-supportinfo-query-packages"></a>

Pass `--pkg` with one or more package names to display their support information.

```
dnf supportinfo --pkg {{PACKAGE}} [{{PACKAGE}} ...]
```

### To Query a Specific Package
<a name="dnf-supportinfo-query-specific"></a>

The following `dnf supportinfo` example queries a package that has reached end of life:

```
dnf supportinfo --pkg php8.1
```

```
Name                         : php8.1
Version                      : 8.1.34-1.amzn2023.0.1
State                        : available
Current Status               : End of Life
Patch Priority               : End of Support
Support Level Description    : End of support - no further updates
Origin                       : Amazon Linux 2023 Core
Support Timeline             : from 2023-03-15     : supported
                             : from 2025-12-31     : unsupported
Package Note                 : Upstream end-of-life for PHP 8.1 (php8.1) is 2025-12-31
```

### To Query Multiple Packages
<a name="dnf-supportinfo-query-multiple"></a>

```
dnf supportinfo --pkg glibc bash openssl
```

## Filter Packages
<a name="dnf-supportinfo-filter-packages"></a>

The `--show` flag filters packages by state, support level, or both.

```
dnf supportinfo --show {{FILTER}} [{{FILTER}} ...]
```

### Filter Types
<a name="dnf-supportinfo-filter-types"></a>

| Category | Values | Source |
| --- | --- | --- |
| State filters (fixed) | installed, available, unavailable, all | Built into the plugin |
| Support level filters (dynamic) | Varies. For example, full\_support, eos | Loaded from <support\_level> entries in the support info XML |

**Note**
Support level filters are dynamic. They come directly from the support info XML data defined by the OS vendor. The available values depend on what AL2023 currently defines. Run `--list-filters` to see the current set of valid filter values. For information about how these levels are declared, see [SupportInfo XML Structure](dnf-supportinfo-xml-structure.md).

### Filter Logic
<a name="dnf-supportinfo-filter-logic"></a>
+ Multiple state filters combine with OR: `--show installed available` matches packages that are installed OR available.
+ Multiple support level filters combine with OR: `--show full_support eos` matches packages at the `full_support` OR `eos` support level.
+ When you combine both types, they combine with AND: `--show installed eos` matches packages that are installed AND at the `eos` support level.

**Note**
If a filter name exists in both state and support level categories, the plugin matches against both. Use prefix syntax to disambiguate: `state:{{NAME}}` or `support:{{NAME}}`.

### To List Available Filters
<a name="dnf-supportinfo-list-filters"></a>

Run `--list-filters` to see all valid filter values grouped by category:

```
dnf supportinfo --list-filters
```

Example output:

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

### To Filter Installed Packages
<a name="dnf-supportinfo-filter-installed"></a>

```
dnf supportinfo --show installed
```

The output lists each package in a table with its support level and current status:

```
Package                          Version                            State        Support Level    Current Status         Until (Next Phase)           Note
redis6                           6.2.20-2.amzn2023.0.1              installed    End of Support   End of Life                                         Upstream end-of-life for Redis 6 (redis6) is 2026-01-31
bash                             5.2.15-1.amzn2023.0.2              installed    Full Support     Supported              2029-06-30 (unsupported)
glibc                            2.34-231.amzn2023.0.1              installed    Full Support     Supported              2029-06-30 (unsupported)
...
```

### To Filter Installed Packages at a Specific Support Level
<a name="dnf-supportinfo-filter-installed-level"></a>

```
dnf supportinfo --show installed eos
```

### To Use Prefix Syntax for Disambiguation
<a name="dnf-supportinfo-filter-prefix"></a>

```
dnf supportinfo --show state:installed support:full_support
```

## Structured Output
<a name="dnf-supportinfo-structured-output"></a>

For scripting and automation, `--showjson` and `--showxml` produce machine-readable output.

### To Get JSON Output
<a name="dnf-supportinfo-json-output"></a>

```
dnf supportinfo --pkg nodejs20 --showjson
```

The output contains the package's current phase, origin, and full timeline with support level details:

```
{
  "name": "nodejs20",
  "version": "20.20.2-1.amzn2023.0.2",
  "state": "available",
  "current_phase": "unsupported",
  "origin": "Amazon Linux 2023 Core",
  "phases": [
    {
      "name": "supported",
      "start_date": "2023-10-24",
      "patch_priority": "Full Support",
      "support_level_description": "Full security and bug fix support for all severities",
      "covered_severities": "Low, Medium, Important, Critical"
    },
    {
      "name": "unsupported",
      "start_date": "2026-04-30",
      "patch_priority": "End of Support",
      "support_level_description": "End of support - no further updates"
    }
  ],
  "note": "Upstream end-of-life for Node.js 20 (nodejs20) is 2026-04-30"
}
```

### To Get XML Output
<a name="dnf-supportinfo-xml-output"></a>

```
dnf supportinfo --pkg nodejs20 --showxml
```

The output is an XML document with a `<package_support>` root containing one `<statement>` element per lifecycle, each with its phases, start dates, and support level details. For the full schema reference, see [SupportInfo XML Structure](dnf-supportinfo-xml-structure.md).

## Manage the Cache
<a name="dnf-supportinfo-manage-cache"></a>

The plugin caches the support info XML locally to reduce network requests.

### Cache Behavior
<a name="dnf-supportinfo-cache-behavior"></a>

When the cache expires:

1. The plugin checks whether the remote file has changed (using HTTP ETag).

1. If unchanged, it extends the cache without re-downloading.

1. If changed, it downloads the updated file.

1. On network errors, it falls back to the cached file if one exists.

### To Sync the Cache
<a name="dnf-supportinfo-sync-cache"></a>

Download and cache the latest support info data:

```
dnf supportinfo --sync
```

Use this for automation and cron jobs that need up-to-date support data without running a full query.

### To Clear the Cache
<a name="dnf-supportinfo-clean-cache"></a>

```
dnf supportinfo --clean-cache
```

## Non-root Usage
<a name="dnf-supportinfo-non-root"></a>

All commands work without root privileges. When run as root, the cache is stored at `/var/cache/dnf/support-info/`. When run as a non-root user, the cache goes to `/var/tmp/dnf-{{username}}-*/support-info/`. This follows DNF's standard convention for per-user temporary directories.

**Note**
If you enable [legacy mode](#dnf-supportinfo-migration-from-legacy), run `sudo dnf supportinfo --sync` once to create the legacy file. After that, non-root queries work normally.

## Configuration Reference
<a name="dnf-supportinfo-configuration-reference"></a>

The plugin reads configuration from `/etc/dnf/plugins/supportinfo.conf`. The following example shows the recommended configuration with legacy mode disabled:

```
[main]
# Required: URL to support info XML (DNF variables like $awsregion are resolved)
baseurl = https://cdn.amazonlinux.com/al2023/core/AL2023-supportinfo-1.0.xml

# Optional: XSD schema for validation
templateurl = https://cdn.amazonlinux.com/al2023/core/supportinfo-1.0.xsd

# Optional: Cache duration in seconds (default: 1800 = 30 minutes)
metadata_expire = 1800

# Legacy mode (default: 1). Set to 0 to use v2 format.
legacy = 0
```

| Option | Description | Default |
| --- | --- | --- |
| baseurl | URL to the support info XML file. Supports DNF variables such as $awsregion. | Required |
| templateurl | URL to the XSD schema for validation. | None |
| metadata\_expire | Cache duration in seconds. Use -1 for infinite, 0 to always check. | 1800 |
| legacy | Enable v1-compatible output. Set to 1 or 0. See [Migration from Legacy Plugin](#dnf-supportinfo-migration-from-legacy). | 1 |

## Output Fields Reference
<a name="dnf-supportinfo-output-fields"></a>

| Field | Description |
| --- | --- |
| Name | Package name |
| Version | Installed or available version |
| State | installed, available, or unavailable |
| Current Status | Current lifecycle phase, such as Supported or End of Life |
| Patch Priority | Support level name |
| Support Level Description | Human-readable description of the support level |
| Covered Severities | Security severity levels that receive patches |
| Origin | Repository providing the package |
| Support Timeline | Chronological list of lifecycle phases with dates |
| Package Note | Additional context, such as upstream EOL dates |

## Schema
<a name="dnf-supportinfo-schema"></a>

The support info data format is defined by an XSD schema. Use this schema to validate custom tooling that consumes the support info XML directly:

```
https://cdn.amazonlinux.com/al2023/core/supportinfo-1.0.xsd
```

## Migration from Legacy Plugin
<a name="dnf-supportinfo-migration-from-legacy"></a>

If you previously used an earlier version of the dnf-plugin-support-info package, the new v2 plugin ships with `legacy = 1` by default to maintain backward compatibility. In a future AL2023 quarterly release, the default changes to `legacy = 0` and output switches to the v2 format documented on this page.

If you have scripts or tooling that parse plugin output or read the legacy XML file directly, see [Migrating from dnf-plugin-support-info v1 to v2](dnf-supportinfo-migrate-v1-v2.md) for a complete list of differences, before/after examples, and a step-by-step migration checklist.

To keep legacy behavior after the transition, set `legacy = 1` in `/etc/dnf/plugins/supportinfo.conf`. This is a temporary measure. Legacy mode requires root privileges for `--sync` and will be removed in a future release.

## Troubleshooting
<a name="dnf-supportinfo-troubleshooting"></a>

### Stale Cache Data
<a name="dnf-supportinfo-troubleshooting-stale-cache"></a>

**Symptom:** Query results show outdated support information.

**Resolution:** Sync the cache manually:

```
dnf supportinfo --sync
```

If the issue persists, clear and re-sync:

```
dnf supportinfo --clean-cache
dnf supportinfo --sync
```

### Legacy File Not Found
<a name="dnf-supportinfo-troubleshooting-legacy-file"></a>

**Symptom:** Scripts that read `/usr/lib/python*/site-packages/dnf-plugins/support_info.xml` fail with "file not found."

**Resolution:** The plugin creates the legacy file only when you set `legacy = 1` and run `--sync` at least once:

```
sudo dnf supportinfo --sync
```

If `legacy = 0`, the file is no longer maintained. Migrate your scripts to use `--showjson` or `--showxml` output instead. For migration steps, see [Migrating from dnf-plugin-support-info v1 to v2](dnf-supportinfo-migrate-v1-v2.md).

## Additional Resources
<a name="dnf-supportinfo-additional-resources"></a>
+ [AL2023 Support Statements (human-readable)](https://docs.aws.amazon.com/linux/al2023/release-notes/support-information.html)
+ [DNF Support Info plugin on GitHub](https://github.com/amazonlinux/dnf-plugin-support-info)
+ [amazon-linux-supportinfo parsing library on GitHub](https://github.com/amazonlinux/amazon-linux-supportinfo)
