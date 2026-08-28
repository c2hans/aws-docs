---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_PurchaseHostReservation.html
---

# PurchaseHostReservation
<a name="API_PurchaseHostReservation"></a>

Purchase a reservation with configurations that match those of your Dedicated Host. You must have active Dedicated Hosts in your account before you purchase a reservation. This action results in the specified reservation being purchased and charged to your account.

## Request Parameters
<a name="API_PurchaseHostReservation_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **ClientToken**
Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see [Ensuring Idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html).
Type: String
Required: No

 **CurrencyCode**
The currency in which the `totalUpfrontPrice`, `LimitPrice`, and `totalHourlyPrice` amounts are specified. At this time, the only supported currency is `USD`.
Type: String
Valid Values: `USD`
Required: No

 **HostIdSet.N**
The IDs of the Dedicated Hosts with which the reservation will be associated.
Type: Array of strings
Required: Yes

 **LimitPrice**
The specified limit is checked against the total upfront cost of the reservation (calculated as the offering's upfront cost multiplied by the host count). If the total upfront cost is greater than the specified price limit, the request fails. This is used to ensure that the purchase does not exceed the expected upfront cost of the purchase. At this time, the only supported currency is `USD`. For example, to indicate a limit price of USD 100, specify 100.00.
Type: String
Required: No

 **OfferingId**
The ID of the offering.
Type: String
Required: Yes

 **TagSpecification.N**
The tags to apply to the Dedicated Host Reservation during purchase.
Type: Array of [TagSpecification](API_TagSpecification.md) objects
Required: No

## Response Elements
<a name="API_PurchaseHostReservation_ResponseElements"></a>

The following elements are returned by the service.

 **clientToken**
Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see [Ensuring Idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html).
Type: String

 **currencyCode**
The currency in which the `totalUpfrontPrice` and `totalHourlyPrice` amounts are specified. At this time, the only supported currency is `USD`.
Type: String
Valid Values: `USD`

 **purchase**
Describes the details of the purchase.
Type: Array of [Purchase](API_Purchase.md) objects

 **requestId**
The ID of the request.
Type: String

 **totalHourlyPrice**
The total hourly price of the reservation calculated per hour.
Type: String

 **totalUpfrontPrice**
The total amount charged to your account when you purchase the reservation.
Type: String

## Errors
<a name="API_PurchaseHostReservation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_PurchaseHostReservation_Examples"></a>

### Example
<a name="API_PurchaseHostReservation_Example_1"></a>

This example uses the same configuration information from [GetHostReservationPurchasePreview](API_GetHostReservationPurchasePreview.md) to make the purchase and associate the offering with the specified Dedicated Host.

#### Sample Request
<a name="API_PurchaseHostReservation_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=PurchaseHostReservation
&OfferingId=hro-0eb3541dght849c2d
&HostIdSet=h-0fgr9ddb0ecd0a1cd
&AUTHPARAMS
```

#### Sample Response
<a name="API_PurchaseHostReservation_Example_1_Response"></a>

```
<PurchaseHostReservationResult xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>d4904fd9-84c3-b40d-gtyk-a9983EXAMPLE</requestId>
        <purchase>
            <item>
                <duration>31536000</duration>
                <upfrontPrice>7453.000</upfrontPrice>
                <paymentOption>PartialUpfront</paymentOption>
                <instanceFamily>m4</instanceFamily>
                <hourlyPrice>0.850</hourlyPrice>
                <hostIdSet>
                    <item>h-0fgr9ddb0ecd0a1cd</item>
                </hostIdSet>
            </item>
       </purchase>
       <totalHourlyPrice>0.850<totalHourlyPrice>
       <totalUpfrontPrice>7453.000<totalUpfrontPrice>
</PurchaseHostReservationResult>
```

## See Also
<a name="API_PurchaseHostReservation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/PurchaseHostReservation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/PurchaseHostReservation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/PurchaseHostReservation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/PurchaseHostReservation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/PurchaseHostReservation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/PurchaseHostReservation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/PurchaseHostReservation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/PurchaseHostReservation)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/PurchaseHostReservation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/PurchaseHostReservation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
