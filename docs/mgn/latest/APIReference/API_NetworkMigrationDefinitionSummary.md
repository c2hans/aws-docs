---
source_url: https://docs.aws.amazon.com/mgn/latest/APIReference/API_NetworkMigrationDefinitionSummary.html
---

# NetworkMigrationDefinitionSummary
<a name="API_NetworkMigrationDefinitionSummary"></a>

A summary of a network migration definition.

## Contents
<a name="API_NetworkMigrationDefinitionSummary_Contents"></a>

 ** arn **   <a name="mgn-Type-NetworkMigrationDefinitionSummary-arn"></a>
The Amazon Resource Name (ARN) of the network migration definition.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: No

 ** name **   <a name="mgn-Type-NetworkMigrationDefinitionSummary-name"></a>
The name of the network migration definition.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^\s\x00]( *[^\s\x00])*`
Required: No

 ** networkMigrationDefinitionID **   <a name="mgn-Type-NetworkMigrationDefinitionSummary-networkMigrationDefinitionID"></a>
The unique identifier of the network migration definition.
Type: String
Length Constraints: Fixed length of 21.
Pattern: `nmd-[0-9a-zA-Z]{17}`
Required: No

 ** scopeTags **   <a name="mgn-Type-NetworkMigrationDefinitionSummary-scopeTags"></a>
Scope tags for the network migration definition.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 40 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `(?!aws:)[a-zA-Z0-9\s+\-=._:/@]*`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `[a-zA-Z0-9\s+\-=._:/@]*`
Required: No

 ** sourceEnvironment **   <a name="mgn-Type-NetworkMigrationDefinitionSummary-sourceEnvironment"></a>
The source environment configuration.
Type: String
Valid Values: `NSX | VSPHERE | FORTIGATE_FIREWALL | PALO_ALTO_FIREWALL | CISCO_ACI | LOGICAL_MODEL | MODELIZE_IT | AWS_DISCOVERY_COLLECTOR | PRE_MAPPED_MODEL`
Required: No

 ** tags **   <a name="mgn-Type-NetworkMigrationDefinitionSummary-tags"></a>
Tags assigned to the network migration definition.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 0. Maximum length of 256.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## See Also
<a name="API_NetworkMigrationDefinitionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mgn-2020-02-26/NetworkMigrationDefinitionSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mgn-2020-02-26/NetworkMigrationDefinitionSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mgn-2020-02-26/NetworkMigrationDefinitionSummary)
