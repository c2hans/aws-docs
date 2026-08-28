---
source_url: https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_GetReservationOffering.html
---

# GetReservationOffering
<a name="API_GetReservationOffering"></a>

Returns the reservation offering. The offering determines the payment schedule for the reservation.

## Request Syntax
<a name="API_GetReservationOffering_RequestSyntax"></a>

```
{
   "offeringId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetReservationOffering_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [offeringId](#API_GetReservationOffering_RequestSyntax) **   <a name="redshiftserverless-GetReservationOffering-request-offeringId"></a>
The identifier for the offering..
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

## Response Syntax
<a name="API_GetReservationOffering_ResponseSyntax"></a>

```
{
   "reservationOffering": {
      "currencyCode": "string",
      "duration": number,
      "hourlyCharge": number,
      "offeringId": "string",
      "offeringType": "string",
      "upfrontCharge": number
   }
}
```

## Response Elements
<a name="API_GetReservationOffering_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [reservationOffering](#API_GetReservationOffering_ResponseSyntax) **   <a name="redshiftserverless-GetReservationOffering-response-reservationOffering"></a>
The returned reservation offering. The offering determines the payment schedule for the reservation.
Type: [ReservationOffering](API_ReservationOffering.md) object

## Errors
<a name="API_GetReservationOffering_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The resource could not be found.
 ** resourceName **
The name of the resource that could not be found.
HTTP Status Code: 400

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 400

 ** ValidationException **
The input failed to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_GetReservationOffering_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-serverless-2021-04-21/GetReservationOffering)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-serverless-2021-04-21/GetReservationOffering)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-serverless-2021-04-21/GetReservationOffering)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-serverless-2021-04-21/GetReservationOffering)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-serverless-2021-04-21/GetReservationOffering)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-serverless-2021-04-21/GetReservationOffering)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-serverless-2021-04-21/GetReservationOffering)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-serverless-2021-04-21/GetReservationOffering)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-serverless-2021-04-21/GetReservationOffering)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-serverless-2021-04-21/GetReservationOffering)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift Serverless. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift-serverless` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
