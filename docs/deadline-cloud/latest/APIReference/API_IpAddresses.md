---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_IpAddresses.html
---

# IpAddresses
<a name="API_IpAddresses"></a>

The IP addresses for a host.

## Contents
<a name="API_IpAddresses_Contents"></a>

 ** ipV4Addresses **   <a name="deadlinecloud-Type-IpAddresses-ipV4Addresses"></a>
The IpV4 address of the network.
Type: Array of strings
Pattern: `(?:[0-9]{1,3}\.){3}[0-9]{1,3}`
Required: No

 ** ipV6Addresses **   <a name="deadlinecloud-Type-IpAddresses-ipV6Addresses"></a>
The IpV6 address for the network and node component.
Type: Array of strings
Pattern: `(?:[A-F0-9]{1,4}:){7}[A-F0-9]{1,4}`
Required: No

## See Also
<a name="API_IpAddresses_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/IpAddresses)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/IpAddresses)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/IpAddresses)
