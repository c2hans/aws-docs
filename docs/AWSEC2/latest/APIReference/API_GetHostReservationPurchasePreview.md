---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetHostReservationPurchasePreview.html
---

# GetHostReservationPurchasePreview
<a name="API_GetHostReservationPurchasePreview"></a>

Preview a reservation purchase with configurations that match those of your Dedicated Host. You must have active Dedicated Hosts in your account before you purchase a reservation.

This is a preview of the [PurchaseHostReservation](API_PurchaseHostReservation.md) action and does not result in the offering being purchased.

## Request Parameters
<a name="API_GetHostReservationPurchasePreview_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **HostIdSet.N**
The IDs of the Dedicated Hosts with which the reservation is associated.
Type: Array of strings
Required: Yes

 **OfferingId**
The offering ID of the reservation.
Type: String
Required: Yes

## Response Elements
<a name="API_GetHostReservationPurchasePreview_ResponseElements"></a>

The following elements are returned by the service.

 **currencyCode**
The currency in which the `totalUpfrontPrice` and `totalHourlyPrice` amounts are specified. At this time, the only supported currency is `USD`.
Type: String
Valid Values: `USD`

 **purchase**
The purchase information of the Dedicated Host reservation and the Dedicated Hosts associated with it.
Type: Array of [Purchase](API_Purchase.md) objects

 **requestId**
The ID of the request.
Type: String

 **totalHourlyPrice**
The potential total hourly price of the reservation per hour.
Type: String

 **totalUpfrontPrice**
The potential total upfront price. This is billed immediately.
Type: String

## Errors
<a name="API_GetHostReservationPurchasePreview_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_GetHostReservationPurchasePreview_Examples"></a>

### Example
<a name="API_GetHostReservationPurchasePreview_Example_1"></a>

This example is a preview of the reservation to be purchased.

#### Sample Request
<a name="API_GetHostReservationPurchasePreview_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=GetHostReservationPurchasePreview
&OfferingId=hro-0eb3541dght849c2d
&HostIdSet=h-0fgr9ddb0ecd0a1cd
&AUTHPARAMS
```

#### Sample Response
<a name="API_GetHostReservationPurchasePreview_Example_1_Response"></a>

```
<GetHostReservationPurchasePreviewResult xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>d4904fd9-84c3-4967-gtyk-a9983EXAMPLE</requestId>
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
</GetHostReservationPurchasePreviewResult>
```

## See Also
<a name="API_GetHostReservationPurchasePreview_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/GetHostReservationPurchasePreview)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/GetHostReservationPurchasePreview)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/GetHostReservationPurchasePreview)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/GetHostReservationPurchasePreview)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/GetHostReservationPurchasePreview)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/GetHostReservationPurchasePreview)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/GetHostReservationPurchasePreview)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/GetHostReservationPurchasePreview)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/GetHostReservationPurchasePreview)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/GetHostReservationPurchasePreview)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
