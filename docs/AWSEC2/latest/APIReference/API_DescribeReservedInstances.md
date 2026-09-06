---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeReservedInstances.html
---

# DescribeReservedInstances
<a name="API_DescribeReservedInstances"></a>

Describes one or more of the Reserved Instances that you purchased.

For more information about Reserved Instances, see [Reserved Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts-on-demand-reserved-instances.html) in the *Amazon EC2 User Guide*.

**Note**
The order of the elements in the response, including those within nested structures, might vary. Applications should not assume the elements appear in a particular order.

## Request Parameters
<a name="API_DescribeReservedInstances_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **Filter.N**
One or more filters.
+  `availability-zone` - The Availability Zone where the Reserved Instance can be used.
+  `availability-zone-id` - The ID of the Availability Zone where the Reserved Instance can be used.
+  `duration` - The duration of the Reserved Instance (one year or three years), in seconds (`31536000` \| `94608000`).
+  `end` - The time when the Reserved Instance expires (for example, 2015-08-07T11:54:42.000Z).
+  `fixed-price` - The purchase price of the Reserved Instance (for example, 9800.0).
+  `instance-type` - The instance type that is covered by the reservation.
+  `scope` - The scope of the Reserved Instance (`Region` or `Availability Zone`).
+  `product-description` - The Reserved Instance product platform description (`Linux/UNIX` \| `Linux with SQL Server Standard` \| `Linux with SQL Server Web` \| `Linux with SQL Server Enterprise` \| `SUSE Linux` \| `Red Hat Enterprise Linux` \| `Red Hat Enterprise Linux with HA` \| `Windows` \| `Windows with SQL Server Standard` \| `Windows with SQL Server Web` \| `Windows with SQL Server Enterprise`).
+  `reserved-instances-id` - The ID of the Reserved Instance.
+  `start` - The time at which the Reserved Instance purchase request was placed (for example, 2014-08-07T11:54:42.000Z).
+  `state` - The state of the Reserved Instance (`payment-pending` \| `active` \| `payment-failed` \| `retired`).
+  `tag:<key>` - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key `Owner` and the value `TeamA`, specify `tag:Owner` for the filter name and `TeamA` for the filter value.
+  `tag-key` - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value.
+  `usage-price` - The usage price of the Reserved Instance, per hour (for example, 0.84).
Type: Array of [Filter](API_Filter.md) objects
Required: No

 **OfferingClass**
Describes whether the Reserved Instance is Standard or Convertible.
Type: String
Valid Values: `standard | convertible`
Required: No

 **OfferingType**
The Reserved Instance offering type. If you are using tools that predate the 2011-11-01 API version, you only have access to the `Medium Utilization` Reserved Instance offering type.
Type: String
Valid Values: `Heavy Utilization | Medium Utilization | Light Utilization | No Upfront | Partial Upfront | All Upfront`
Required: No

 **ReservedInstancesId.N**
One or more Reserved Instance IDs.
Default: Describes all your Reserved Instances, or only those otherwise specified.
Type: Array of strings
Required: No

## Response Elements
<a name="API_DescribeReservedInstances_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **reservedInstancesSet**
A list of Reserved Instances.
Type: Array of [ReservedInstances](API_ReservedInstances.md) objects

## Errors
<a name="API_DescribeReservedInstances_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DescribeReservedInstances_Examples"></a>

### Example
<a name="API_DescribeReservedInstances_Example_1"></a>

This example describes Reserved Instances owned by your account.

#### Sample Request
<a name="API_DescribeReservedInstances_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=DescribeReservedInstances
&AUTHPARAMS
```

#### Sample Response
<a name="API_DescribeReservedInstances_Example_1_Response"></a>

```
<DescribeReservedInstancesResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
   <requestId>59dbff89-35bd-4eac-99ed-be587EXAMPLE</requestId>
   <reservedInstancesSet>
   ...
      <item>
         <reservedInstancesId>e5a2ff3b-7d14-494f-90af-0b5d0EXAMPLE</reservedInstancesId>
         <instanceType>m1.xlarge</instanceType>
         <availabilityZone>us-east-1b</availabilityZone>
         <start>2015-07-14T11:00:00:00.000Z</start>
         <end>2016-07-13T1212:00:00:000Z</end>
         <duration>31536000</duration>
         <fixedPrice>0.0</fixedPrice>
         <usagePrice>0.034</usagePrice>
         <instanceCount>2</instanceCount>
         <productDescription>Linux/UNIX (Amazon VPC)</productDescription>
         <state>active</state>
         <instanceTenancy>default</instanceTenancy>
         <currencyCode>USD</currencyCode>
         <offeringType>Partial Upfront</offeringType>
         <recurringCharges>
                  <item>
                        <frequency>Hourly</frequency>
                        <amount>0.05</amount>
                  </item>
         </recurringCharges>
         <offeringClass>standard</offeringClass>
         <scope>AvailabilityZone</scope>
      </item>
      ...
   </reservedInstancesSet>
</DescribeReservedInstancesResponse>
```

### Example
<a name="API_DescribeReservedInstances_Example_2"></a>

This example filters the response to include only one-year, `m1.small` Linux/UNIX Reserved Instances. If you want Linux/UNIX Reserved Instances specifically for use with a VPC, set the product description to `Linux/UNIX (Amazon VPC)`.

#### Sample Request
<a name="API_DescribeReservedInstances_Example_2_Request"></a>

```
https://ec2.amazonaws.com/?Action=DescribeReservedInstances
&Filter.1.Name=duration
&Filter.1.Value.1=31536000
&Filter.2.Name=instance-type
&Filter.2.Value.1=m1.small
&Filter.3.Name=product-description
&Filter.3.Value.1=Linux%2FUNIX
&AUTHPARAMS
```

## See Also
<a name="API_DescribeReservedInstances_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DescribeReservedInstances)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DescribeReservedInstances)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DescribeReservedInstances)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DescribeReservedInstances)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DescribeReservedInstances)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DescribeReservedInstances)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DescribeReservedInstances)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DescribeReservedInstances)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DescribeReservedInstances)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DescribeReservedInstances)
