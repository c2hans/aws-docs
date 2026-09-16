---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeHostReservationOfferings.html
---

# DescribeHostReservationOfferings
<a name="API_DescribeHostReservationOfferings"></a>

Describes the Dedicated Host reservations that are available to purchase.

The results describe all of the Dedicated Host reservation offerings, including offerings that might not match the instance family and Region of your Dedicated Hosts. When purchasing an offering, ensure that the instance family and Region of the offering matches that of the Dedicated Hosts with which it is to be associated. For more information about supported instance types, see [Dedicated Hosts](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/dedicated-hosts-overview.html) in the *Amazon EC2 User Guide*.

## Request Parameters
<a name="API_DescribeHostReservationOfferings_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **Filter.N**
The filters.
+  `instance-family` - The instance family of the offering (for example, `m4`).
+  `payment-option` - The payment option (`NoUpfront` \| `PartialUpfront` \| `AllUpfront`).
Type: Array of [Filter](API_Filter.md) objects
Required: No

 **MaxDuration**
This is the maximum duration of the reservation to purchase, specified in seconds. Reservations are available in one-year and three-year terms. The number of seconds specified must be the number of seconds in a year (365x24x60x60) times one of the supported durations (1 or 3). For example, specify 94608000 for three years.
Type: Integer
Required: No

 **MaxResults**
The maximum number of results to return for the request in a single page. The remaining results can be seen by sending another request with the returned `nextToken` value. This value can be between 5 and 500. If `maxResults` is given a larger value than 500, you receive an error.
Type: Integer
Valid Range: Minimum value of 5. Maximum value of 500.
Required: No

 **MinDuration**
This is the minimum duration of the reservation you'd like to purchase, specified in seconds. Reservations are available in one-year and three-year terms. The number of seconds specified must be the number of seconds in a year (365x24x60x60) times one of the supported durations (1 or 3). For example, specify 31536000 for one year.
Type: Integer
Required: No

 **NextToken**
The token to use to retrieve the next page of results.
Type: String
Required: No

 **OfferingId**
The ID of the reservation offering.
Type: String
Required: No

## Response Elements
<a name="API_DescribeHostReservationOfferings_ResponseElements"></a>

The following elements are returned by the service.

 **nextToken**
The token to use to retrieve the next page of results. This value is `null` when there are no more results to return.
Type: String

 **offeringSet**
Information about the offerings.
Type: Array of [HostOffering](API_HostOffering.md) objects

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_DescribeHostReservationOfferings_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DescribeHostReservationOfferings_Examples"></a>

### Example 1
<a name="API_DescribeHostReservationOfferings_Example_1"></a>

This example describes all of the Dedicated Host Reservation offerings.

#### Sample Request
<a name="API_DescribeHostReservationOfferings_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=DescribeHostReservationOfferings
&AUTHPARAMS
```

#### Sample Response
<a name="API_DescribeHostReservationOfferings_Example_1_Response"></a>

```
<DescribeHostReservationOfferingsResult xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
<requestId>d4904fd9-84c3-4ea5-gtyk-a9cc3EXAMPLE</requestId>
<offeringSet>
    <item>
        <duration>94608000</duration>
        <upfrontPrice>28396.000</upfrontPrice>
        <paymentOption>AllUpfront</paymentOption>
        <instanceFamily>m4</instanceFamily>
        <offeringId>hro-0875903788203856fg</offeringId>
        <hourlyPrice>0.000</hourlyPrice>
    </item>
    <item>
        <duration>31536000</duration>
        <upfrontPrice>13603.000</upfrontPrice>
        <paymentOption>AllUpfront</paymentOption>
        <instanceFamily>r3</instanceFamily>
        <offeringId>hro-08ddfitlb8990hhkmp</offeringId>
        <hourlyPrice>0.000</hourlyPrice>
    </item>
    <item>
        <duration>94608000</duration>
        <upfrontPrice>57382.000</upfrontPrice>
        <paymentOption>PartialUpfront</paymentOption>
        <instanceFamily>x1</instanceFamily>
        <offeringId>hro-0875903788207657fg</offeringId>
        <hourlyPrice>2.183</hourlyPrice>
    </item>
</offeringSet>
</DescribeHostReservationOfferingsResult>
```

### Example 2
<a name="API_DescribeHostReservationOfferings_Example_2"></a>

This example describes all of the Dedicated Host reservation offerings, with a maximum duration of three years, that are available to purchase.

#### Sample Request
<a name="API_DescribeHostReservationOfferings_Example_2_Request"></a>

```
https://ec2.amazonaws.com/?Action=DescribeHostReservationOfferings
&MaxDuration=94608000
&AUTHPARAMS
```

#### Sample Response
<a name="API_DescribeHostReservationOfferings_Example_2_Response"></a>

```
<DescribeHostReservationOfferingsResult xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
<requestId>d4905678-84c3-4ea5-gtyk-a9cc3EXAMPLE</requestId>
<offeringSet>
    <item>
        <duration>31536000</duration>
        <upfrontPrice>4879.000</upfrontPrice>
        <paymentOption>PartialUpfront</paymentOption>
        <instanceFamily>c3</instanceFamily>
        <offeringId>hro-7890903788203856fg</offeringId>
        <hourlyPrice>0.557</hourlyPrice>
    </item>
    <item>
        <duration>94608000</duration>
        <upfrontPrice>18892.000</upfrontPrice>
        <paymentOption>AllUpfront</paymentOption>
        <instanceFamily>c4</instanceFamily>
        <offeringId>hro-1092903788203856fg</offeringId>
        <hourlyPrice>0.000</hourlyPrice>
    </item>
</offeringSet>
</DescribeHostReservationOfferingsResult>
```

## See Also
<a name="API_DescribeHostReservationOfferings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DescribeHostReservationOfferings)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DescribeHostReservationOfferings)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DescribeHostReservationOfferings)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DescribeHostReservationOfferings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DescribeHostReservationOfferings)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DescribeHostReservationOfferings)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DescribeHostReservationOfferings)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DescribeHostReservationOfferings)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DescribeHostReservationOfferings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DescribeHostReservationOfferings)
