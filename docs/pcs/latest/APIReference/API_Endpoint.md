---
source_url: https://docs.aws.amazon.com/pcs/latest/APIReference/API_Endpoint.html
---

# Endpoint
<a name="API_Endpoint"></a>

An endpoint available for interaction with the scheduler.

## Contents
<a name="API_Endpoint_Contents"></a>

 ** port **   <a name="PCS-Type-Endpoint-port"></a>
The endpoint's connection port number.
 Example: `1234`
Type: String
Required: Yes

 ** privateIpAddress **   <a name="PCS-Type-Endpoint-privateIpAddress"></a>
For clusters that use IPv4, this is the endpoint's private IP address.
Example: `10.1.2.3`
For clusters configured to use IPv6, this is an empty string.
Type: String
Required: Yes

 ** type **   <a name="PCS-Type-Endpoint-type"></a>
Indicates the type of endpoint running at the specific IP address.
Type: String
Valid Values: `SLURMCTLD | SLURMDBD | SLURMRESTD`
Required: Yes

 ** ipv6Address **   <a name="PCS-Type-Endpoint-ipv6Address"></a>
The endpoint's IPv6 address.
Example: `2001:db8::1`
Type: String
Required: No

 ** publicIpAddress **   <a name="PCS-Type-Endpoint-publicIpAddress"></a>
The endpoint's public IP address.
Example: `192.0.2.1`
Type: String
Required: No

## See Also
<a name="API_Endpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pcs-2023-02-10/Endpoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pcs-2023-02-10/Endpoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pcs-2023-02-10/Endpoint)
