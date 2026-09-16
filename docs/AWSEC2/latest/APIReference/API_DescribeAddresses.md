---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeAddresses.html
---

# DescribeAddresses
<a name="API_DescribeAddresses"></a>

Describes the specified Elastic IP addresses or all of your Elastic IP addresses.

## Request Parameters
<a name="API_DescribeAddresses_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **AllocationId.N**
Information about the allocation IDs.
Type: Array of strings
Required: No

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **Filter.N**
One or more filters. Filter names and values are case-sensitive.
+  `allocation-id` - The allocation ID for the address.
+  `association-id` - The association ID for the address.
+  `instance-id` - The ID of the instance the address is associated with, if any.
+  `network-border-group` - A unique set of Availability Zones, Local Zones, or Wavelength Zones from where AWS advertises IP addresses.
+  `network-interface-id` - The ID of the network interface that the address is associated with, if any.
+  `network-interface-owner-id` - The AWS account ID of the owner.
+  `private-ip-address` - The private IP address associated with the Elastic IP address.
+  `public-ip` - The Elastic IP address, or the carrier IP address.
+  `tag`:<key> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key `Owner` and the value `TeamA`, specify `tag:Owner` for the filter name and `TeamA` for the filter value.
+  `tag-key` - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value.
Type: Array of [Filter](API_Filter.md) objects
Required: No

 **PublicIp.N**
One or more Elastic IP addresses.
Default: Describes all your Elastic IP addresses.
Type: Array of strings
Required: No

## Response Elements
<a name="API_DescribeAddresses_ResponseElements"></a>

The following elements are returned by the service.

 **addressesSet**
Information about the Elastic IP addresses.
Type: Array of [Address](API_Address.md) objects

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_DescribeAddresses_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DescribeAddresses_Examples"></a>

### Example
<a name="API_DescribeAddresses_Example_1"></a>

This example request describes a specific Elastic IP address allocated to your account.

#### Sample Request
<a name="API_DescribeAddresses_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=DescribeAddresses
&AllocationId.1= eipalloc-08229861
&AUTHPARAMS
```

#### Sample Response
<a name="API_DescribeAddresses_Example_1_Response"></a>

```
<DescribeAddressesResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
   <requestId>f7de5e98-491a-4c19-a92d-908d6EXAMPLE</requestId>
   <addressesSet>
     <item>
       <publicIp>203.0.113.41</publicIp>
       <allocationId>eipalloc-08229861</allocationId>
       <domain>vpc</domain>
       <instanceId>i-0598c7d356eba48d7</instanceId>
       <associationId>eipassoc-f0229899</associationId>
       <networkInterfaceId>eni-ef229886</networkInterfaceId>
       <networkInterfaceOwnerId>053230519467</networkInterfaceOwnerId>
       <privateIpAddress>10.0.0.228</privateIpAddress>
     </item>
   </addressesSet>
</DescribeAddressesResponse>
```

## See Also
<a name="API_DescribeAddresses_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DescribeAddresses)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DescribeAddresses)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DescribeAddresses)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DescribeAddresses)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DescribeAddresses)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DescribeAddresses)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DescribeAddresses)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DescribeAddresses)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DescribeAddresses)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DescribeAddresses)
