---
source_url: https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_CreateReservation.html
---

# CreateReservation
<a name="API_CreateReservation"></a>

Creates an Amazon Redshift Serverless reservation, which gives you the option to commit to a specified number of Redshift Processing Units (RPUs) for a year at a discount from Serverless on-demand (OD) rates.

## Request Syntax
<a name="API_CreateReservation_RequestSyntax"></a>

```
{
   "capacity": {{number}},
   "clientToken": "{{string}}",
   "offeringId": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateReservation_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [capacity](#API_CreateReservation_RequestSyntax) **   <a name="redshiftserverless-CreateReservation-request-capacity"></a>
The number of Redshift Processing Units (RPUs) to reserve.
Type: Integer
Required: Yes

 ** [clientToken](#API_CreateReservation_RequestSyntax) **   <a name="redshiftserverless-CreateReservation-request-clientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. This token must be a valid UUIDv4 value. For more information about idempotency, see [ Making retries safe with idempotent APIs ](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/).
Type: String
Required: No

 ** [offeringId](#API_CreateReservation_RequestSyntax) **   <a name="redshiftserverless-CreateReservation-request-offeringId"></a>
The ID of the offering associated with the reservation. The offering determines the payment schedule for the reservation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

## Response Syntax
<a name="API_CreateReservation_ResponseSyntax"></a>

```
{
   "reservation": {
      "capacity": number,
      "endDate": "string",
      "offering": {
         "currencyCode": "string",
         "duration": number,
         "hourlyCharge": number,
         "offeringId": "string",
         "offeringType": "string",
         "upfrontCharge": number
      },
      "reservationArn": "string",
      "reservationId": "string",
      "startDate": "string",
      "status": "string"
   }
}
```

## Response Elements
<a name="API_CreateReservation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [reservation](#API_CreateReservation_ResponseSyntax) **   <a name="redshiftserverless-CreateReservation-response-reservation"></a>
The reservation object that the `CreateReservation` action created.
Type: [Reservation](API_Reservation.md) object

## Errors
<a name="API_CreateReservation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
The submitted action has conflicts.
HTTP Status Code: 400

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The resource could not be found.
 ** resourceName **
The name of the resource that could not be found.
HTTP Status Code: 400

 ** ServiceQuotaExceededException **
The service limit was exceeded.
HTTP Status Code: 400

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 400

 ** TooManyTagsException **
The request exceeded the number of tags allowed for a resource.
 ** resourceName **
The name of the resource that exceeded the number of tags allowed for a resource.
HTTP Status Code: 400

 ** ValidationException **
The input failed to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_CreateReservation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-serverless-2021-04-21/CreateReservation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-serverless-2021-04-21/CreateReservation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-serverless-2021-04-21/CreateReservation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-serverless-2021-04-21/CreateReservation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-serverless-2021-04-21/CreateReservation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-serverless-2021-04-21/CreateReservation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-serverless-2021-04-21/CreateReservation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-serverless-2021-04-21/CreateReservation)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-serverless-2021-04-21/CreateReservation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-serverless-2021-04-21/CreateReservation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift Serverless. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift-serverless` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
