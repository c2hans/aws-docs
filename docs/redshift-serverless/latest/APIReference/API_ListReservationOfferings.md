---
source_url: https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_ListReservationOfferings.html
---

# ListReservationOfferings
<a name="API_ListReservationOfferings"></a>

Returns the current reservation offerings in your account.

## Request Syntax
<a name="API_ListReservationOfferings_RequestSyntax"></a>

```
{
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListReservationOfferings_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [maxResults](#API_ListReservationOfferings_RequestSyntax) **   <a name="redshiftserverless-ListReservationOfferings-request-maxResults"></a>
The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_ListReservationOfferings_RequestSyntax) **   <a name="redshiftserverless-ListReservationOfferings-request-nextToken"></a>
The token for the next set of items to return. (You received this token from a previous call.)
Type: String
Length Constraints: Minimum length of 8. Maximum length of 1024.
Required: No

## Response Syntax
<a name="API_ListReservationOfferings_ResponseSyntax"></a>

```
{
   "nextToken": "string",
   "reservationOfferingsList": [
      {
         "currencyCode": "string",
         "duration": number,
         "hourlyCharge": number,
         "offeringId": "string",
         "offeringType": "string",
         "upfrontCharge": number
      }
   ]
}
```

## Response Elements
<a name="API_ListReservationOfferings_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListReservationOfferings_ResponseSyntax) **   <a name="redshiftserverless-ListReservationOfferings-response-nextToken"></a>
The token to use when requesting the next set of items.
Type: String
Length Constraints: Minimum length of 8. Maximum length of 1024.

 ** [reservationOfferingsList](#API_ListReservationOfferings_ResponseSyntax) **   <a name="redshiftserverless-ListReservationOfferings-response-reservationOfferingsList"></a>
The returned list of reservation offerings.
Type: Array of [ReservationOffering](API_ReservationOffering.md) objects

## Errors
<a name="API_ListReservationOfferings_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 400

 ** ValidationException **
The input failed to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_ListReservationOfferings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-serverless-2021-04-21/ListReservationOfferings)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-serverless-2021-04-21/ListReservationOfferings)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-serverless-2021-04-21/ListReservationOfferings)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-serverless-2021-04-21/ListReservationOfferings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-serverless-2021-04-21/ListReservationOfferings)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-serverless-2021-04-21/ListReservationOfferings)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-serverless-2021-04-21/ListReservationOfferings)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-serverless-2021-04-21/ListReservationOfferings)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-serverless-2021-04-21/ListReservationOfferings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-serverless-2021-04-21/ListReservationOfferings)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift Serverless. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift-serverless` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
