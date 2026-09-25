---
source_url: https://docs.aws.amazon.com/drs/latest/APIReference/API_SourceProperties.html
---

# SourceProperties
<a name="API_SourceProperties"></a>

Properties of the Source Server machine.

## Contents
<a name="API_SourceProperties_Contents"></a>

 ** architecture **   <a name="drs-Type-SourceProperties-architecture"></a>
The architecture of the Source Server.
Type: String
Valid Values: `x86_64 | arm64`
Required: No

 ** cpus **   <a name="drs-Type-SourceProperties-cpus"></a>
An array of CPUs.
Type: Array of [CPU](API_CPU.md) objects
Array Members: Minimum number of 0 items. Maximum number of 256 items.
Required: No

 ** disks **   <a name="drs-Type-SourceProperties-disks"></a>
An array of disks.
Type: Array of [Disk](API_Disk.md) objects
Array Members: Minimum number of 0 items. Maximum number of 1000 items.
Required: No

 ** identificationHints **   <a name="drs-Type-SourceProperties-identificationHints"></a>
Hints used to uniquely identify a machine.
Type: [IdentificationHints](API_IdentificationHints.md) object
Required: No

 ** lastUpdatedDateTime **   <a name="drs-Type-SourceProperties-lastUpdatedDateTime"></a>
The date and time the Source Properties were last updated on.
Type: String
Length Constraints: Minimum length of 19. Maximum length of 32.
Pattern: `[1-9][0-9]*-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])T([0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9](\.[0-9]+)?Z`
Required: No

 ** networkInterfaces **   <a name="drs-Type-SourceProperties-networkInterfaces"></a>
An array of network interfaces.
Type: Array of [NetworkInterface](API_NetworkInterface.md) objects
Array Members: Minimum number of 0 items. Maximum number of 32 items.
Required: No

 ** os **   <a name="drs-Type-SourceProperties-os"></a>
Operating system.
Type: [OS](API_OS.md) object
Required: No

 ** ramBytes **   <a name="drs-Type-SourceProperties-ramBytes"></a>
The amount of RAM in bytes.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** recommendedInstanceType **   <a name="drs-Type-SourceProperties-recommendedInstanceType"></a>
The recommended EC2 instance type that will be used when recovering the Source Server.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Required: No

 ** supportsNitroInstances **   <a name="drs-Type-SourceProperties-supportsNitroInstances"></a>
Are EC2 nitro instance types supported when recovering the Source Server.
Type: Boolean
Required: No

## See Also
<a name="API_SourceProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/drs-2020-02-26/SourceProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/drs-2020-02-26/SourceProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/drs-2020-02-26/SourceProperties)
