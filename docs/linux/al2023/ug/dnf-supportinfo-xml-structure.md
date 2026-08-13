---
source_url: https://docs.aws.amazon.com/linux/al2023/ug/dnf-supportinfo-xml-structure.html
---

# SupportInfo XML Structure
<a name="dnf-supportinfo-xml-structure"></a>

This page documents the v1.0 XML schema used to define package support lifecycles, timelines, and classifications for Linux distributions. The schema is independent of DNF and not specific to any single distribution. You can consume it directly from any tool. The `dnf supportinfo` plugin is one such consumer.
+ **Schema definition (XSD):** `https://cdn.amazonlinux.com/al2023/core/supportinfo-1.0.xsd`
+ **Support data (XML):** `https://cdn.amazonlinux.com/al2023/core/AL2023-supportinfo-1.0.xml`

To parse this XML directly, use the open-source [amazon-linux-supportinfo](https://github.com/amazonlinux/amazon-linux-supportinfo) library, which implements the schema described on this page, instead of writing a custom parser.

**Topics**
+ [How the Plugin Uses This File](#dnf-supportinfo-xml-how-plugin-uses)
+ [Complete Minimal Example](#dnf-supportinfo-xml-minimal-example)
+ [Element Reference](#dnf-supportinfo-xml-element-reference)
+ [Referential Integrity](#dnf-supportinfo-xml-referential-integrity)

## How the Plugin Uses This File
<a name="dnf-supportinfo-xml-how-plugin-uses"></a>

From this file, the plugin reports:
+ Which support level a package is at (these values populate the `--show` filter options)
+ When lifecycle phases change (displayed in `--pkg` output and the timeline)
+ Patch priority and severity coverage for each support level
+ Where the package comes from (origin and classification)

## Complete Minimal Example
<a name="dnf-supportinfo-xml-minimal-example"></a>

This example shows the minimum structure with all required sections and one package:

```
<package_support schema_version="1.0" current_as="2025-08-21T22:41:55.575196">
  <lifecycles>
    <lifecycle name="default_lc"
               display_name="AL2023 Standard Lifecycle"
               description="Standard support lifecycle for Amazon Linux 2023 packages">
      <phase name="full_support"
             support_level="default"
             start_milestone="AL2023_GA"
             display_name="Full Support"/>
      <phase name="end_of_support"
             support_level="eos"
             start_milestone="AL2023_EOS"
             display_name="End of Support"/>
    </lifecycle>
  </lifecycles>

  <support_milestones>
    <milestone name="AL2023_GA" date="2023-03-15"
               display_name="AL2023 General Availability"
               description="Amazon Linux 2023 general availability date"/>
    <milestone name="AL2023_EOS" date="2029-06-30"
               display_name="AL2023 End of Support"
               description="End of all support for Amazon Linux 2023"/>
  </support_milestones>

  <support_levels>
    <support_level name="default"
                   severities="Low,Medium,Important,Critical"
                   description="Full security and bug fix support for all severities"
                   display_name="Default Support" />
    <support_level name="eos"
                   severities=""
                   description="End of support - no further updates"
                   display_name="End of Support" />
  </support_levels>

  <packages>
    <package name="curl" lifecycle="default_lc" origin="al2023_core" package_class="default"/>
  </packages>

  <package_classes>
    <package_class name="default">
      <summary>Default class for Amazon Linux packages</summary>
      <text></text>
    </package_class>
  </package_classes>

  <package_origins>
    <package_origin name="al2023_core"
                    repo_id="amazonlinux"
                    dist="amzn2023"
                    vendor="amazonlinux"
                    display_name="Amazon Linux 2023 Core"
                    description="Core Amazon Linux 2023 repository" />
  </package_origins>

  <notes>
    <note name="eol_redis6">Upstream end-of-life for Redis 6 (redis6) is 2025-08-31</note>
  </notes>
</package_support>
```

## Element Reference
<a name="dnf-supportinfo-xml-element-reference"></a>

### `package_support` (Root Element)
<a name="dnf-supportinfo-xml-package-support"></a>

The root element that contains all support metadata.

| Attribute | Required | Description |
| --- | --- | --- |
| schema\_version | Yes | Schema format version (currently 1.0) |
| current\_as | Yes | ISO timestamp when the support data was last generated |

```
<package_support schema_version="1.0" current_as="2025-08-21T22:41:55.575196">
```

The `current_as` timestamp appears in output to indicate data freshness.

### `lifecycle`
<a name="dnf-supportinfo-xml-lifecycle"></a>

Defines a sequence of phases that a package transitions through over time.

| Attribute | Required | Description |
| --- | --- | --- |
| name | Yes | Unique identifier referenced by package@lifecycle |
| note | No | References a note@name for additional context |
| display\_name | No | Customer-facing label |
| description | No | Human-readable description |

```
<lifecycle name="redis6_lc" note="eol_redis6"
           display_name="Redis 6 Lifecycle"
           description="Support lifecycle for Redis 6 packages">
  <phase .../>
</lifecycle>
```

The plugin walks the phases in order, finds the one currently active, and reports that phase's support level in output.

### `phase`
<a name="dnf-supportinfo-xml-phase"></a>

Defines one stage within a lifecycle. Each phase continues until the next phase starts (or indefinitely if it is the last phase).

| Attribute | Required | Description |
| --- | --- | --- |
| name | Yes | Phase identifier (unique within its lifecycle) |
| support\_level | Yes | References a support\_level@name |
| start\_date | Conditional | Fixed ISO date (YYYY-MM-DD). Use this or start\_milestone |
| start\_milestone | Conditional | References a milestone@name. Use this or start\_date |
| display\_name | No | Customer-facing label |

**Note**
Specify exactly one of `start_date` or `start_milestone`, not both.

```
<phase name="limited_support"
       support_level="limited"
       start_milestone="AL2023_6months"
       display_name="Limited Support"/>
```

Each phase is active from its start date until the next phase begins. The last phase in a lifecycle remains active indefinitely.

### `milestone`
<a name="dnf-supportinfo-xml-milestone"></a>

Defines a reusable date marker that lifecycle phases reference.

| Attribute | Required | Description |
| --- | --- | --- |
| name | Yes | Unique identifier referenced by phase@start\_milestone |
| date | Yes | ISO date (YYYY-MM-DD) |
| display\_name | No | Customer-facing label |
| description | No | Human-readable description |

```
<milestone name="AL2023_GA" date="2023-03-15"
           display_name="AL2023 General Availability"
           description="Amazon Linux 2023 general availability date"/>
```

Milestones let phases share dates. When a milestone date changes, every phase referencing it updates automatically.

### `support_level`
<a name="dnf-supportinfo-xml-support-level"></a>

Defines a support tier and the severities it covers. Each `name` becomes a valid `--show` filter value.

| Attribute | Required | Description |
| --- | --- | --- |
| name | Yes | Unique identifier. Used as the --show filter value |
| severities | Yes | Comma-separated severity levels covered (empty string = no patches) |
| description | Yes | Human-readable description shown in --list-filters output |
| display\_name | No | Customer-facing label |

```
<support_level name="limited"
               severities="Important,Critical"
               description="Security fixes for Important and Critical severities only"
               display_name="Limited Support" />
```

Running `dnf supportinfo --show limited` lists all packages currently at this support level. The `--list-filters` command displays each level's `name` and `description`.

### `package`
<a name="dnf-supportinfo-xml-package"></a>

Maps an RPM package name to its lifecycle, origin, and class.

| Attribute | Required | Description |
| --- | --- | --- |
| name | Yes | RPM package name |
| lifecycle | Yes | References a lifecycle@name |
| origin | Yes | References a package\_origin@name |
| package\_class | No | References a package\_class@name |

```
<package name="curl" lifecycle="default_lc" origin="al2023_core" package_class="default"/>
```

**Note**
A package can appear multiple times with different `origin` values (for example, the same package in core and SPAL repos). The combination of `name` \+ `origin` must be unique.

Each installed RPM is matched against this list to determine its lifecycle and current support status.

### `package_class`
<a name="dnf-supportinfo-xml-package-class"></a>

Categorizes packages by their role in the system. The class name and summary appear in plugin output.

| Attribute/Element | Required | Description |
| --- | --- | --- |
| @name | Yes | Unique identifier referenced by package@package\_class |
| summary (child) | Yes | Short description of the category |
| text (child) | Yes | Extended description. The element must be present but may be empty |

```
<package_class name="os_dependency">
  <summary>Packages supported only as dependencies of the operating system</summary>
  <text></text>
</package_class>
```

The class name appears in output to indicate a package's role on the system.

### `package_origin`
<a name="dnf-supportinfo-xml-package-origin"></a>

Identifies the repository source of a package. The `origin` value appears in `dnf supportinfo --pkg` output.

| Attribute | Required | Description |
| --- | --- | --- |
| name | Yes | Unique identifier referenced by package@origin |
| repo\_id | Yes | DNF repository ID |
| dist | Yes | Distribution identifier |
| vendor | Yes | Package vendor |
| signing\_key | No | GPG signing key identifier |
| display\_name | No | Customer-facing label |
| description | No | Human-readable description |

```
<package_origin name="al2023_core"
                repo_id="amazonlinux"
                dist="amzn2023"
                vendor="amazonlinux"
                display_name="Amazon Linux 2023 Core"
                description="Core Amazon Linux 2023 repository" />
```

The `display_name` appears as the "Origin" field in `--pkg` output.

### `note`
<a name="dnf-supportinfo-xml-note"></a>

Provides freeform text that a lifecycle can reference for additional context.

| Attribute | Required | Description |
| --- | --- | --- |
| name | Yes | Unique identifier referenced by lifecycle@note |

The element's text content contains the note message.

```
<note name="eol_redis6">Upstream end-of-life for Redis 6 (redis6) is 2025-08-31</note>
```

When a package's lifecycle references a note, the note text appears as "Package Note" in `--pkg` output.

## Referential Integrity
<a name="dnf-supportinfo-xml-referential-integrity"></a>

The schema links elements together through `name` references. Each source attribute must match the `name` of an existing target element:

| Source attribute | References |
| --- | --- |
| package@lifecycle | lifecycle@name |
| package@origin | package\_origin@name |
| package@package\_class | package\_class@name |
| phase@support\_level | support\_level@name |
| phase@start\_milestone | milestone@name |
| lifecycle@note | note@name |

In addition, the combination of `package@name` and `package@origin` must be unique across all `package` elements.
