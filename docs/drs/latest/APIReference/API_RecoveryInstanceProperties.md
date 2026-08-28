---
source_url: https://docs.aws.amazon.com/drs/latest/APIReference/API_RecoveryInstanceProperties.html
---

# RecoveryInstanceProperties
<a name="API_RecoveryInstanceProperties"></a>

Properties of the Recovery Instance machine.

## Contents
<a name="API_RecoveryInstanceProperties_Contents"></a>

 ** cpus **   <a name="drs-Type-RecoveryInstanceProperties-cpus"></a>
An array of CPUs.
Type: Array of [CPU](API_CPU.md) objects
Array Members: Minimum number of 0 items. Maximum number of 256 items.
Required: No

 ** disks **   <a name="drs-Type-RecoveryInstanceProperties-disks"></a>
An array of disks.
Type: Array of [RecoveryInstanceDisk](API_RecoveryInstanceDisk.md) objects
Array Members: Minimum number of 0 items. Maximum number of 1000 items.
Required: No

 ** identificationHints **   <a name="drs-Type-RecoveryInstanceProperties-identificationHints"></a>
Hints used to uniquely identify a machine.
Type: [IdentificationHints](API_IdentificationHints.md) object
Required: No

 ** lastUpdatedDateTime **   <a name="drs-Type-RecoveryInstanceProperties-lastUpdatedDateTime"></a>
The date and time the Recovery Instance properties were last updated on.
Type: String
Length Constraints: Minimum length of 19. Maximum length of 32.
Pattern: `[1-9][0-9]*-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])T([0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9](\.[0-9]+)?Z`
Required: No

 ** networkInterfaces **   <a name="drs-Type-RecoveryInstanceProperties-networkInterfaces"></a>
An array of network interfaces.
Type: Array of [NetworkInterface](API_NetworkInterface.md) objects
Array Members: Minimum number of 0 items. Maximum number of 32 items.
Required: No

 ** os **   <a name="drs-Type-RecoveryInstanceProperties-os"></a>
Operating system.
Type: [OS](API_OS.md) object
Required: No

 ** ramBytes **   <a name="drs-Type-RecoveryInstanceProperties-ramBytes"></a>
The amount of RAM in bytes.
Type: Long
Valid Range: Minimum value of 0.
Required: No

## See Also
<a name="API_RecoveryInstanceProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/drs-2020-02-26/RecoveryInstanceProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/drs-2020-02-26/RecoveryInstanceProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/drs-2020-02-26/RecoveryInstanceProperties)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elastic Disaster Recovery. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query drs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
