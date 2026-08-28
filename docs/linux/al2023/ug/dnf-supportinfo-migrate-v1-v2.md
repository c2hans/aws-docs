---
source_url: https://docs.aws.amazon.com/linux/al2023/ug/dnf-supportinfo-migrate-v1-v2.html
---

# Migrating from dnf-plugin-support-info v1 to v2
<a name="dnf-supportinfo-migrate-v1-v2"></a>

The dnf-plugin-support-info package has a new major version (v2) with a redesigned output format. This guide helps you update any scripts or tooling that parse `dnf supportinfo` output.

During the transition period, the v2 plugin ships with `legacy = 1` in `/etc/dnf/plugins/supportinfo.conf`, which preserves v1-compatible output. Once you have updated your scripts, set `legacy = 0` to switch to v2 output.

**Topics**
+ [Overview](#dnf-supportinfo-migrate-overview)
+ [Breaking Changes That Require Action](#dnf-supportinfo-migrate-breaking-changes)
+ [What Does Not Change](#dnf-supportinfo-migrate-unchanged)
+ [Transition Period](#dnf-supportinfo-migrate-transition-period)

## Overview
<a name="dnf-supportinfo-migrate-overview"></a>

### Timeline
<a name="dnf-supportinfo-migrate-timeline"></a>

| Event | Timing |
| --- | --- |
| v2 plugin (dnf-plugin-support-info 2.0) available | Now |
| Plugin ships with legacy = 1 (v1-compatible output) | Initial v2 release |
| Default changes to legacy = 0 | A future AL2023 quarterly release |
| v1 format no longer maintained | After transition period |

### What You Need to Do
<a name="dnf-supportinfo-migrate-what-to-do"></a>

If you have scripts that parse console output, XML output, or read the XML file from disk, update them to handle the new field names, structure, and file paths. If you use `--showjson`, your scripts need no changes, because the JSON output is identical between v1 and v2. If you read the XML file directly from disk, switch to downloading the XML from the configured `baseurl` or use `dnf supportinfo --show installed --showxml`.

## Breaking Changes That Require Action
<a name="dnf-supportinfo-migrate-breaking-changes"></a>

### If You Parse Console Output
<a name="dnf-supportinfo-migrate-console-output"></a>

#### Detail Fields
<a name="dnf-supportinfo-migrate-detail-fields"></a>

The plugin changed the field labels it displays when you query a specific package:

| v1 label | v2 label | Notes |
| --- | --- | --- |
| Support Status | Current Status | Renamed |
| Support Periods | Support Timeline | Renamed, moved to end of output |
| Support Statement | (removed) | No longer displayed |
| Link | Link | Unchanged (shown when available) |
| Other Info | Other Info | Unchanged (shown when available) |
| (not present) | Patch Priority | New field |
| (not present) | Support Level Description | New field |
| (not present) | Covered Severities | New field |
| (not present) | Origin | New field |

The field label column is now 28 characters wide (previously 20).

**v1:** `dnf supportinfo --pkg apr`

```
Name                 : apr
Version              : 1.7.5-1.amzn2023.0.4
State                : available
Support Status       : supported
Support Periods      : from 2023-03-15      : supported
                     : from 2029-06-30      : unsupported
Support Statement    : Amazon Linux 2023 end-of-life
Link                 : https://aws.amazon.com/amazon-linux-ami/faqs/
Other Info           : This is the support statement for AL2023. The end-of-life
                     : of Amazon Linux 2023 is June 2029. From this point, the
                     : Amazon Linux 2023 packages will no longer receive any
                     : updates from AWS.
```

**v2:** `dnf supportinfo --pkg apr`

```
Name                         : apr
Version                      : 1.7.5-1.amzn2023.0.4
State                        : available
Current Status               : Supported
Patch Priority               : Full Support
Support Level Description    : Full security and bug fix support for all severities
Covered Severities           : Low, Medium, Important, Critical
Origin                       : Amazon Linux 2023 Core
Support Timeline             : from 2023-03-15     : supported
                             : from 2029-06-30     : unsupported
```

#### Table Columns
<a name="dnf-supportinfo-migrate-table-columns"></a>

The summary table has changed from 6 columns to 7. The v2 table also displays a header row (v1 does not):

| v1 column | v2 column | Change |
| --- | --- | --- |
| Name | Package | Renamed |
| Version | Version | Unchanged |
| State | State | Unchanged |
| Support Status | Current Status | Renamed |
| (not present) | Support Level | New column |
| Date (such as 2029-06-30) | Until (Next Phase) (such as 2029-06-30 (end\_of\_support)) | Renamed, format changed |
| Note | Note | Unchanged |

**Important**
The date column now includes the next phase name in parentheses. If you parse this field, update your regex or delimiter logic.

**v1:** `dnf supportinfo --show installed`

```
iproute              6.10.0-319.amzn2023.0.1    installed    supported    2029-06-30    Kernel6.18 has security support until June 2029
kernel6.12           6.12.90-120.164.amzn2023   installed    supported    2029-06-30    Kernel6.12 has security support until June 2029
```

**v2:** `dnf supportinfo --show installed`

```
Package                          Version                            State        Support Level    Current Status         Until (Next Phase)           Note
alternatives                     1.15-2.amzn2023.0.2                installed    Full Support     Supported              2029-06-30 (unsupported)
amazon-linux-repo-cdn            2023.12.20260611-0.amzn2023        installed    Full Support     Supported              2029-06-30 (unsupported)
redis6                           6.2.20-2.amzn2023.0.1              installed    End of Support   End of Life                                         Upstream end-of-life for Redis 6 (redis6) is 2026-01-31
```

### If You Parse `--showxml` Output
<a name="dnf-supportinfo-migrate-xml-output"></a>

The v2 `--showxml` output uses a different XML structure than v1. The root `<package_support>` element is the same, but the child elements, attributes, and hierarchy have changed.

**v1:** `dnf supportinfo --pkg apr --showxml`

```
<?xml version="1.0" ?>
<package_support current_as="2026-06-18">
  <statements>
    <statement id="eol" marker="supported" start_date="2023-03-15" end_date="2029-06-30">
      <summary>Amazon Linux 2023 end-of-life</summary>
      <text>This is the support statement for AL2023. The end-of-life of Amazon
Linux 2023 is June 2029. From this point, the Amazon Linux 2023 packages will
no longer receive any updates from AWS.</text>
      <link>https://aws.amazon.com/amazon-linux-ami/faqs/</link>
      <packages>
        <package name="apr" nevra="1.7.5-1.amzn2023.0.4"/>
      </packages>
    </statement>
  </statements>
</package_support>
```

**v2:** `dnf supportinfo --pkg apr --showxml`

```
<?xml version='1.0' encoding='utf-8'?>
<package_support current_as="2026-06-18">
  <statements>
    <statement id="eol_lc" current_phase="supported">
      <phases>
        <phase name="supported" start_date="2023-03-15">
          <patch_priority>Full Support</patch_priority>
          <support_level_description>Full security and bug fix support for all severities</support_level_description>
          <covered_severities>Low, Medium, Important, Critical</covered_severities>
        </phase>
        <phase name="unsupported" start_date="2029-06-30">
          <patch_priority>End of Support</patch_priority>
          <support_level_description>End of support - no further updates</support_level_description>
        </phase>
      </phases>
      <packages>
        <package name="apr" nevra="1.7.5-1.amzn2023.0.4" state="available" origin="Amazon Linux 2023 Core"/>
      </packages>
    </statement>
  </statements>
</package_support>
```

Key structural differences:
+ v1 uses `marker`, `start_date`, `end_date` attributes on `<statement>` with `<summary>`, `<text>`, `<link>` children
+ v2 uses `current_phase` attribute and nested `<phases>` elements with support level details
+ v2 omits `<covered_severities>` entirely when empty (instead of an empty element)
+ v2 package elements include `state` and `origin` attributes
+ v2 does not include `<summary>`, `<text>`, or `<link>` elements

### If You Read the XML File Directly from Disk
<a name="dnf-supportinfo-migrate-xml-file"></a>

The v1 plugin bundled its data file at:

```
/usr/lib/python*/site-packages/dnf-plugins/support_info.xml
```

**Warning**
This file is no longer updated once `legacy = 0` takes effect. Do not rely on this path for current data.

The v2 plugin caches data at `/var/cache/dnf/support-info/` when run as root. When run as a non-root user, it uses `/var/tmp/dnf-{{username}}-*/support-info/`, following DNF's standard convention for per-user temporary directories. Files in these directories use content-addressed filenames and are not stable. Do not parse them directly.

**Recommended alternatives:**

1. Download the XML directly from the configured URL:

   ```
   https://cdn.amazonlinux.com/al2023/core/AL2023-supportinfo-1.0.xml
   ```

1. Use the CLI to get structured output for installed packages:

   ```
   dnf supportinfo --show installed --showxml
   ```

### If You Filter with `--show`
<a name="dnf-supportinfo-migrate-show-filter"></a>

The values accepted by the `--show` filter have changed:

| v1 filter values | v2 filter values |
| --- | --- |
| supported | full\_support |
| unsupported | eos |

v1 filters are **phase names** (`supported`, `unsupported`). v2 filters are **support level names** (`full_support`, `eos`, etc.).

Run `--list-filters` to discover available filter values on your system:

```
dnf supportinfo --list-filters
```

## What Does Not Change
<a name="dnf-supportinfo-migrate-unchanged"></a>

Once you install dnf-plugin-support-info v2, the following remain the same regardless of the `legacy` setting:
+ **`--showjson` output.** The JSON output is identical whether `legacy` is `0` or `1`, because the plugin normalizes to the v2 internal structure before formatting.
+ **CLI arguments.** All flags (`--pkg`, `--show`, `--showxml`, `--showjson`, `--clean-cache`, `--list-filters`, `--sync`) work in both modes.
+ **Command name.** You still run `dnf supportinfo`.

**Note**
The `--showjson`, `--clean-cache`, `--list-filters`, and `--sync` flags are new in v2 and are not available in v1.

## Transition Period
<a name="dnf-supportinfo-migrate-transition-period"></a>

The v2 plugin ships with `legacy = 1` in `/etc/dnf/plugins/supportinfo.conf`. During this period:

1. The plugin downloads v2 data from the configured URL.

1. Console output, XML output, and filter values continue to behave like v1.

1. The v1-format XML file remains available at the old path so existing scripts continue to work.

In a future AL2023 quarterly release, the default changes to `legacy = 0`. At that point:
+ Console output uses v2 field names and structure.
+ `--showxml` produces the new phases-based format.
+ `--show` filter values change to support level names.
+ The v1 XML file at the old path is no longer updated.

**To keep v1-compatible output temporarily**, set `legacy = 1` in `/etc/dnf/plugins/supportinfo.conf`:

```
[main]
legacy = 1
```

**Important**
The `legacy = 1` option is a temporary bridge. Plan to migrate your tooling to v2 output rather than relying on this setting indefinitely.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Linux. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query linux` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
