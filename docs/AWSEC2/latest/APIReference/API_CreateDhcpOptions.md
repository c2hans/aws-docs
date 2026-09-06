---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateDhcpOptions.html
---

# CreateDhcpOptions
<a name="API_CreateDhcpOptions"></a>

Creates a custom set of DHCP options. After you create a DHCP option set, you associate it with a VPC. After you associate a DHCP option set with a VPC, all existing and newly launched instances in the VPC use this set of DHCP options.

The following are the individual DHCP options you can specify. For more information, see [DHCP option sets](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_DHCP_Options.html) in the *Amazon VPC User Guide*.
+  `domain-name` - If you're using AmazonProvidedDNS in `us-east-1`, specify `ec2.internal`. If you're using AmazonProvidedDNS in any other Region, specify `region.compute.internal`. Otherwise, specify a custom domain name. This value is used to complete unqualified DNS hostnames.

  Some Linux operating systems accept multiple domain names separated by spaces. However, Windows and other Linux operating systems treat the value as a single domain, which results in unexpected behavior. If your DHCP option set is associated with a VPC that has instances running operating systems that treat the value as a single domain, specify only one domain name.
+  `domain-name-servers` - The IP addresses of up to four DNS servers, or AmazonProvidedDNS. To specify multiple domain name servers in a single parameter, separate the IP addresses using commas. To have your instances receive custom DNS hostnames as specified in `domain-name`, you must specify a custom DNS server.
+  `ntp-servers` - The IP addresses of up to eight Network Time Protocol (NTP) servers (four IPv4 addresses and four IPv6 addresses).
+  `netbios-name-servers` - The IP addresses of up to four NetBIOS name servers.
+  `netbios-node-type` - The NetBIOS node type (1, 2, 4, or 8). We recommend that you specify 2. Broadcast and multicast are not supported. For more information about NetBIOS node types, see [RFC 2132](https://www.ietf.org/rfc/rfc2132.txt).
+  `ipv6-address-preferred-lease-time` - A value (in seconds, minutes, hours, or years) for how frequently a running instance with an IPv6 assigned to it goes through DHCPv6 lease renewal. Acceptable values are between 140 and 2147483647 seconds (approximately 68 years). If no value is entered, the default lease time is 140 seconds. If you use long-term addressing for EC2 instances, you can increase the lease time and avoid frequent lease renewal requests. Lease renewal typically occurs when half of the lease time has elapsed.

## Request Parameters
<a name="API_CreateDhcpOptions_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DhcpConfiguration.N**
A DHCP configuration option.
Type: Array of [NewDhcpConfiguration](API_NewDhcpConfiguration.md) objects
Required: Yes

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **TagSpecification.N**
The tags to assign to the DHCP option.
Type: Array of [TagSpecification](API_TagSpecification.md) objects
Required: No

## Response Elements
<a name="API_CreateDhcpOptions_ResponseElements"></a>

The following elements are returned by the service.

 **dhcpOptions**
A set of DHCP options.
Type: [DhcpOptions](API_DhcpOptions.md) object

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_CreateDhcpOptions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_CreateDhcpOptions_Examples"></a>

### Example
<a name="API_CreateDhcpOptions_Example_1"></a>

This example creates a set of DHCP options with a domain name `example.com` and two DNS servers (`10.2.5.1` and `10.2.5.2`). The DNS servers' IP addresses are specified in a single parameter, separated by commas, to preserve the order in which they are specified.

#### Sample Request
<a name="API_CreateDhcpOptions_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=CreateDhcpOptions
&DhcpConfiguration.1.Key=domain-name
&DhcpConfiguration.1.Value.1=example.com
&DhcpConfiguration.2.Key=domain-name-servers
&DhcpConfiguration.2.Value.1=10.2.5.1,10.2.5.2
&DhcpConfiguration.3.Key=ipv6-address-preferred-lease-time
&DhcpConfiguration.3.Value.1=140
&AUTHPARAMS
```

#### Sample Response
<a name="API_CreateDhcpOptions_Example_1_Response"></a>

```
<CreateDhcpOptionsResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
  <requestId>7a62c49f-347e-4fc4-9331-6e8eEXAMPLE</requestId>
  <dhcpOptions>
      <dhcpOptionsId>dopt-096c1234cade2dabc</dhcpOptionsId>
      <dhcpConfigurationSet>
        <item>
          <key>domain-name</key>
          <valueSet>
            <item>
              <value>example.com</value>
            </item>
          </valueSet>
        </item>
        <item>
          <key>domain-name-servers</key>
          <valueSet>
            <item>
              <value>10.2.5.1</value>
            </item>
            <item>
              <value>10.2.5.2</value>
            </item>
          </valueSet>
        </item>
        <item>
          <key>ipv6-address-preferred-lease-time</key>
          <valueSet>
            <item>
              <value>140</value>
            </item>
          </valueSet>
        </item>
      </dhcpConfigurationSet>
      <tagSet/>
  </dhcpOptions>
</CreateDhcpOptionsResponse>
```

## See Also
<a name="API_CreateDhcpOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/CreateDhcpOptions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/CreateDhcpOptions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CreateDhcpOptions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/CreateDhcpOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CreateDhcpOptions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/CreateDhcpOptions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/CreateDhcpOptions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/CreateDhcpOptions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/CreateDhcpOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CreateDhcpOptions)
