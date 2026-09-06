---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeHostReservations.html
---

# DescribeHostReservations
<a name="API_DescribeHostReservations"></a>

Describes reservations that are associated with Dedicated Hosts in your account.

## Request Parameters
<a name="API_DescribeHostReservations_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **Filter.N**
The filters.
+  `instance-family` - The instance family (for example, `m4`).
+  `payment-option` - The payment option (`NoUpfront` \| `PartialUpfront` \| `AllUpfront`).
+  `state` - The state of the reservation (`payment-pending` \| `payment-failed` \| `active` \| `retired`).
+  `tag:<key>` - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key `Owner` and the value `TeamA`, specify `tag:Owner` for the filter name and `TeamA` for the filter value.
+  `tag-key` - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value.
Type: Array of [Filter](API_Filter.md) objects
Required: No

 **HostReservationIdSet.N**
The host reservation IDs.
Type: Array of strings
Required: No

 **MaxResults**
The maximum number of results to return for the request in a single page. The remaining results can be seen by sending another request with the returned `nextToken` value. This value can be between 5 and 500. If `maxResults` is given a larger value than 500, you receive an error.
Type: Integer
Required: No

 **NextToken**
The token to use to retrieve the next page of results.
Type: String
Required: No

## Response Elements
<a name="API_DescribeHostReservations_ResponseElements"></a>

The following elements are returned by the service.

 **hostReservationSet**
Details about the reservation's configuration.
Type: Array of [HostReservation](API_HostReservation.md) objects

 **nextToken**
The token to use to retrieve the next page of results. This value is `null` when there are no more results to return.
Type: String

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_DescribeHostReservations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DescribeHostReservations_Examples"></a>

### Example
<a name="API_DescribeHostReservations_Example_1"></a>

This example describes all of the Dedicated Host reservations in your account.

#### Sample Request
<a name="API_DescribeHostReservations_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=DescribeHostReservations
&AUTHPARAMS
```

#### Sample Response
<a name="API_DescribeHostReservations_Example_1_Response"></a>

```
<DescribeHostReservationsResult xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
<requestId>d4904fd9-84c3-4ea5-gtyk-a9983EXAMPLE</requestId>
<hostReservationSet>
    <item>
        <upfrontPrice>0.000</upfrontPrice>
        <count>2</count>
        <start>2016-08-01T15:43:15Z</start>
        <instanceFamily>m4</instanceFamily>
        <offeringId>hro-0875903778903856fg</offeringId>
        <duration>31536000</duration>
        <paymentOption>NoUpfront</paymentOption>
        <end>2017-08-01T15:43:15Z</end>
        <hostReservationId>hr-0875903778903856fg</hostReservationId>
        <state>active</state>
        <hourlyPrice>1.990</hourlyPrice>
        <hostIdSet>
            <item>h-0897086hfkttn</item>
            <item>h-0891346hytrtn</item>
        </hostIdSet>
    </item>
</hostReservationSet>
</DescribeHostReservationsResult>
```

## See Also
<a name="API_DescribeHostReservations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DescribeHostReservations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DescribeHostReservations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DescribeHostReservations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DescribeHostReservations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DescribeHostReservations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DescribeHostReservations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DescribeHostReservations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DescribeHostReservations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DescribeHostReservations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DescribeHostReservations)
