---
source_url: https://docs.aws.amazon.com/linux/al2027/ug/dnf-supportinfo-xml-structure.html
---

# SupportInfo XML structure
<a name="dnf-supportinfo-xml-structure"></a>

**AL2027 Preview**
AL2027 is currently available for preview. It is intended for evaluation and testing only and is not recommended for production workloads.

Use this reference to understand the v1.0 XML schema that defines package support lifecycles, timelines, and classifications. The schema is independent of DNF. You can consume the data directly from any tool; the `dnf supportinfo` plugin is one such consumer. On AL2027, the schema definition (XSD) is published at `https://cdn-al2027.amazonlinux.com/core/supportinfo-1.0.xsd` and the support data (XML) at `https://cdn-al2027.amazonlinux.com/core/AL2027-supportinfo-1.0.xml`.

To parse this XML directly, use the open-source [amazon-linux-supportinfo](https://github.com/amazonlinux/amazon-linux-supportinfo) library on the GitHub website, which implements the schema described on this page, instead of writing a custom parser.

**Topics**
+ [How the plugin uses this file](#dnf-supportinfo-xml-how-plugin-uses)
+ [Example](#dnf-supportinfo-xml-example)
+ [Element reference](#dnf-supportinfo-xml-element-reference)
+ [Referential integrity](#dnf-supportinfo-xml-referential-integrity)

## How the plugin uses this file
<a name="dnf-supportinfo-xml-how-plugin-uses"></a>

From this file, the plugin reports which support level a package is at (these values populate the `--show` filter options), when lifecycle phases change (displayed in the `--pkg` timeline), the severity coverage for each support level, and where the package comes from (origin).

## Example
<a name="dnf-supportinfo-xml-example"></a>

The following example shows the structure with all sections, taken from the AL2027 support data published during the preview:

```
<?xml version='1.0' encoding='UTF-8'?>
<package_support current_as="2026-08-11T00:42:30.979109+00:00" schema_version="1.0">
  <lifecycles>
    <lifecycle name="eol_lc" note="al2027_public_preview"
               display_name="AL2027 Public Preview Lifecycle"
               description="Support timeline for Amazon Linux 2027 public preview packages">
      <phase name="supported" support_level="full_support"
             start_milestone="AL2027_PUBLIC_PREVIEW" display_name="Supported"/>
      <phase name="unsupported" support_level="eos" start_date="2027-03-31"
             display_name="End of Life"/>
    </lifecycle>
  </lifecycles>
  <support_milestones>
    <milestone name="AL2027_PUBLIC_PREVIEW" date="2026-09-03"
               display_name="AL2027 Public Preview"
               description="Amazon Linux 2027 public preview date"/>
  </support_milestones>
  <support_levels>
    <support_level name="full_support" severities="Low, Medium, Important, Critical"
                   description="Full security and bug fix support for all severities"
                   display_name="Full Support"/>
    <support_level name="eos" severities=""
                   description="End of support - no further updates"
                   display_name="End of Support"/>
  </support_levels>
  <packages>
    <package lifecycle="eol_lc" name="7zip" origin="al2027_core"/>
  </packages>
  <package_origins>
    <package_origin dist="amzn2027" name="al2027_core" repo_id="amazonlinux"
                    vendor="amazonlinux" display_name="Amazon Linux 2027 Core"
                    description="Core Amazon Linux 2027 repository containing base OS packages"/>
  </package_origins>
  <package_classes>
    <package_class name="default">
      <summary>Default class for Amazon Linux packages</summary>
      <text/>
    </package_class>
  </package_classes>
  <notes>
    <note name="al2027_public_preview">Amazon Linux will support this package until the end
of the AL2027 public preview period</note>
  </notes>
</package_support>
```

## Element reference
<a name="dnf-supportinfo-xml-element-reference"></a>

The root element, `package_support`, carries the schema format version in `schema_version` (currently `1.0`) and the generation timestamp in `current_as`. It contains the following element families.

| Element | Purpose | Key attributes |
| --- | --- | --- |
| lifecycle | A sequence of phases that a package transitions through over time. The plugin walks the phases in order, finds the active one, and reports its support level. | name (referenced by package@lifecycle), note, display\_name |
| phase | One stage within a lifecycle. Each phase is active from its start until the next phase begins. The last phase remains active indefinitely. | name, support\_level, and exactly one of start\_date (ISO date) or start\_milestone |
| milestone | A reusable date marker that phases reference. When a milestone date changes, every phase referencing it updates automatically. | name, date (ISO date) |
| support\_level | A support tier and the severities it covers. Each name becomes a valid --show filter value. | name, severities (comma-separated, empty means no patches), description |
| package | Maps an RPM package name to its lifecycle, origin, and optional class. The combination of name and origin must be unique. | name, lifecycle, origin, package\_class |
| package\_class | Categorizes packages by their role in the system, with a summary and text child element. | name (referenced by package@package\_class) |
| package\_origin | Identifies the repository source of a package. The display name appears as the Origin field in --pkg output. | name, repo\_id, dist, vendor |
| note | Freeform text that a lifecycle references for additional context. Appears as the Package Note field in --pkg output. | name (referenced by lifecycle@note) |

## Referential integrity
<a name="dnf-supportinfo-xml-referential-integrity"></a>

The schema links elements together through `name` references. Each source attribute must match the `name` of an existing target element:
+ `package@lifecycle` references `lifecycle@name`
+ `package@origin` references `package_origin@name`
+ `package@package_class` references `package_class@name`
+ `phase@support_level` references `support_level@name`
+ `phase@start_milestone` references `milestone@name`
+ `lifecycle@note` references `note@name`
