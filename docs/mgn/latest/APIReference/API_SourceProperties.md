---
source_url: https://docs.aws.amazon.com/mgn/latest/APIReference/API_SourceProperties.html
---

# SourceProperties
<a name="API_SourceProperties"></a>

Source server properties.

## Contents
<a name="API_SourceProperties_Contents"></a>

 ** cpus **   <a name="mgn-Type-SourceProperties-cpus"></a>
Source Server CPUs.
Type: Array of [CPU](API_CPU.md) objects
Array Members: Minimum number of 0 items. Maximum number of 256 items.
Required: No

 ** disks **   <a name="mgn-Type-SourceProperties-disks"></a>
Source Server disks.
Type: Array of [Disk](API_Disk.md) objects
Array Members: Minimum number of 0 items. Maximum number of 1000 items.
Required: No

 ** identificationHints **   <a name="mgn-Type-SourceProperties-identificationHints"></a>
Source server identification hints.
Type: [IdentificationHints](API_IdentificationHints.md) object
Required: No

 ** lastUpdatedDateTime **   <a name="mgn-Type-SourceProperties-lastUpdatedDateTime"></a>
Source server last update date and time.
Type: String
Length Constraints: Minimum length of 19. Maximum length of 32.
Pattern: `[1-9][0-9]*-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])T([0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9](\.[0-9]+)?Z`
Required: No

 ** networkInterfaces **   <a name="mgn-Type-SourceProperties-networkInterfaces"></a>
Source server network interfaces.
Type: Array of [NetworkInterface](API_NetworkInterface.md) objects
Array Members: Minimum number of 0 items. Maximum number of 32 items.
Required: No

 ** os **   <a name="mgn-Type-SourceProperties-os"></a>
Source server OS.
Type: [OS](API_OS.md) object
Required: No

 ** ramBytes **   <a name="mgn-Type-SourceProperties-ramBytes"></a>
Source server RAM in bytes.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** recommendedInstanceType **   <a name="mgn-Type-SourceProperties-recommendedInstanceType"></a>
Source server recommended instance type.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Required: No

## See Also
<a name="API_SourceProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mgn-2020-02-26/SourceProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mgn-2020-02-26/SourceProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mgn-2020-02-26/SourceProperties)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for ApplicationMigrationService. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mgn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
