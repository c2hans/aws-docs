---
source_url: https://docs.aws.amazon.com/mgn/latest/APIReference/API_VcenterClient.html
---

# VcenterClient
<a name="API_VcenterClient"></a>

vCenter client.

## Contents
<a name="API_VcenterClient_Contents"></a>

 ** arn **   <a name="mgn-Type-VcenterClient-arn"></a>
Arn of vCenter client.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: No

 ** datacenterName **   <a name="mgn-Type-VcenterClient-datacenterName"></a>
Datacenter name of vCenter client.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** hostname **   <a name="mgn-Type-VcenterClient-hostname"></a>
Hostname of vCenter client .
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** lastSeenDatetime **   <a name="mgn-Type-VcenterClient-lastSeenDatetime"></a>
Last seen time of vCenter client.
Type: String
Length Constraints: Minimum length of 19. Maximum length of 32.
Pattern: `[1-9][0-9]*-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])T([0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9](\.[0-9]+)?Z`
Required: No

 ** sourceServerTags **   <a name="mgn-Type-VcenterClient-sourceServerTags"></a>
Tags for Source Server of vCenter client.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 0. Maximum length of 256.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** tags **   <a name="mgn-Type-VcenterClient-tags"></a>
Tags for vCenter client.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 0. Maximum length of 256.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** vcenterClientID **   <a name="mgn-Type-VcenterClient-vcenterClientID"></a>
ID of vCenter client.
Type: String
Length Constraints: Fixed length of 21.
Pattern: `vcc-[0-9a-zA-Z]{17}`
Required: No

 ** vcenterUUID **   <a name="mgn-Type-VcenterClient-vcenterUUID"></a>
Vcenter UUID of vCenter client.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## See Also
<a name="API_VcenterClient_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mgn-2020-02-26/VcenterClient)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mgn-2020-02-26/VcenterClient)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mgn-2020-02-26/VcenterClient)
