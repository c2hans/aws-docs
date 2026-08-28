---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AssignPrivateIpAddresses.html
---

# AssignPrivateIpAddresses
<a name="API_AssignPrivateIpAddresses"></a>

Assigns the specified secondary private IP addresses to the specified network interface.

You can specify specific secondary IP addresses, or you can specify the number of secondary IP addresses to be automatically assigned from the subnet's CIDR block range. The number of secondary IP addresses that you can assign to an instance varies by instance type. For more information about Elastic IP addresses, see [Elastic IP Addresses](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html) in the *Amazon EC2 User Guide*.

When you move a secondary private IP address to another network interface, any Elastic IP address that is associated with the IP address is also moved.

Remapping an IP address is an asynchronous operation. When you move an IP address from one network interface to another, check `network/interfaces/macs/mac/local-ipv4s` in the instance metadata to confirm that the remapping is complete.

You must specify either the IP addresses or the IP address count in the request.

You can optionally use Prefix Delegation on the network interface. You must specify either the IPv4 Prefix Delegation prefixes, or the IPv4 Prefix Delegation count. For information, see [ Assigning prefixes to network interfaces](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-prefix-eni.html) in the *Amazon EC2 User Guide*.

## Request Parameters
<a name="API_AssignPrivateIpAddresses_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **AllowReassignment**
Indicates whether to allow an IP address that is already assigned to another network interface or instance to be reassigned to the specified network interface.
Type: Boolean
Required: No

 **Ipv4Prefix.N**
One or more IPv4 prefixes assigned to the network interface. You can't use this option if you use the `Ipv4PrefixCount` option.
Type: Array of strings
Required: No

 **Ipv4PrefixCount**
The number of IPv4 prefixes that AWS automatically assigns to the network interface. You can't use this option if you use the `Ipv4 Prefixes` option.
Type: Integer
Required: No

 **NetworkInterfaceId**
The ID of the network interface.
Type: String
Required: Yes

 **PrivateIpAddress.N**
The IP addresses to be assigned as a secondary private IP address to the network interface. You can't specify this parameter when also specifying a number of secondary IP addresses.
If you don't specify an IP address, Amazon EC2 automatically selects an IP address within the subnet range.
Type: Array of strings
Required: No

 **SecondaryPrivateIpAddressCount**
The number of secondary IP addresses to assign to the network interface. You can't specify this parameter when also specifying private IP addresses.
Type: Integer
Required: No

## Response Elements
<a name="API_AssignPrivateIpAddresses_ResponseElements"></a>

The following elements are returned by the service.

 **assignedIpv4PrefixSet**
The IPv4 prefixes that are assigned to the network interface.
Type: Array of [Ipv4PrefixSpecification](API_Ipv4PrefixSpecification.md) objects

 **assignedPrivateIpAddressesSet**
The private IP addresses assigned to the network interface.
Type: Array of [AssignedPrivateIpAddress](API_AssignedPrivateIpAddress.md) objects

 **networkInterfaceId**
The ID of the network interface.
Type: String

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_AssignPrivateIpAddresses_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_AssignPrivateIpAddresses_Examples"></a>

### Example 1
<a name="API_AssignPrivateIpAddresses_Example_1"></a>

This example assigns two secondary private IP addresses (`10.0.2.1` and `10.0.2.11`) to the specified network interface.

#### Sample Request
<a name="API_AssignPrivateIpAddresses_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=AssignPrivateIpAddresses
&NetworkInterfaceId=eni-d83388b1
&PrivateIpAddress.1=10.0.2.1
&PrivateIpAddress.2=10.0.2.11
&AUTHPARAMS
```

#### Sample Response
<a name="API_AssignPrivateIpAddresses_Example_1_Response"></a>

```
<AssignPrivateIpAddressesResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
  <requestId>3fb591ba-558c-48f8-ae6b-c2f9d6d06425</requestId>
  <networkInterfaceId>eni-01d32da61c165ac3e</networkInterfaceId>
  <assignedPrivateIpAddressesSet>
    <item>
      <privateIpAddress>10.2.2.1</privateIpAddress>
    </item>
    <item>
      <privateIpAddress>10.2.2.11</privateIpAddress>
    </item>
  </assignedPrivateIpAddressesSet>
  <return>true</return>
</AssignPrivateIpAddressesResponse>
```

### Example 2
<a name="API_AssignPrivateIpAddresses_Example_2"></a>

This example assigns two secondary private IP addresses to the specified network interface. Amazon EC2 automatically assigns these IP addresses from the available IP addresses within the subnet's CIDR block range.

#### Sample Request
<a name="API_AssignPrivateIpAddresses_Example_2_Request"></a>

```
https://ec2.amazonaws.com/?Action=AssignPrivateIpAddresses
&NetworkInterfaceId=eni-d83388b1
&SecondaryPrivateIpAddressCount=2
&AUTHPARAMS
```

#### Sample Response
<a name="API_AssignPrivateIpAddresses_Example_2_Response"></a>

```
<AssignPrivateIpAddressesResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
  <requestId>3fb591ba-558c-48f8-ae6b-c2f9d6d06425</requestId>
  <networkInterfaceId>eni-01d32da61c165ac3e</networkInterfaceId>
  <assignedPrivateIpAddressesSet>
    <item>
      <privateIpAddress>10.2.2.7</privateIpAddress>
    </item>
    <item>
      <privateIpAddress>10.2.2.5</privateIpAddress>
    </item>
  </assignedPrivateIpAddressesSet>
  <return>true</return>
</AssignPrivateIpAddressesResponse>
```

## See Also
<a name="API_AssignPrivateIpAddresses_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/AssignPrivateIpAddresses)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/AssignPrivateIpAddresses)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/AssignPrivateIpAddresses)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/AssignPrivateIpAddresses)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/AssignPrivateIpAddresses)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/AssignPrivateIpAddresses)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/AssignPrivateIpAddresses)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/AssignPrivateIpAddresses)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/AssignPrivateIpAddresses)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/AssignPrivateIpAddresses)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
