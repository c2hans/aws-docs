---
source_url: https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_ListCustomLineItemVersions.html
---

# ListCustomLineItemVersions
<a name="API_ListCustomLineItemVersions"></a>

A paginated call to get a list of all custom line item versions.

## Request Syntax
<a name="API_ListCustomLineItemVersions_RequestSyntax"></a>

```
POST /list-custom-line-item-versions HTTP/1.1
Content-type: application/json

{
   "Arn": "{{string}}",
   "Filters": {
      "BillingPeriodRange": {
         "EndBillingPeriod": "{{string}}",
         "StartBillingPeriod": "{{string}}"
      }
   },
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListCustomLineItemVersions_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListCustomLineItemVersions_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Arn](#API_ListCustomLineItemVersions_RequestSyntax) **   <a name="billingconductor-ListCustomLineItemVersions-request-Arn"></a>
The Amazon Resource Name (ARN) for the custom line item.
Type: String
Pattern: `(arn:aws(-cn)?:billingconductor::[0-9]{12}:customlineitem/)?[a-zA-Z0-9]{10}`
Required: Yes

 ** [Filters](#API_ListCustomLineItemVersions_RequestSyntax) **   <a name="billingconductor-ListCustomLineItemVersions-request-Filters"></a>
A `ListCustomLineItemVersionsFilter` that specifies the billing period range in which the custom line item versions are applied.
Type: [ListCustomLineItemVersionsFilter](API_ListCustomLineItemVersionsFilter.md) object
Required: No

 ** [MaxResults](#API_ListCustomLineItemVersions_RequestSyntax) **   <a name="billingconductor-ListCustomLineItemVersions-request-MaxResults"></a>
The maximum number of custom line item versions to retrieve.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListCustomLineItemVersions_RequestSyntax) **   <a name="billingconductor-ListCustomLineItemVersions-request-NextToken"></a>
The pagination token that's used on subsequent calls to retrieve custom line item versions.
Type: String
Required: No

## Response Syntax
<a name="API_ListCustomLineItemVersions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "CustomLineItemVersions": [
      {
         "AccountId": "string",
         "Arn": "string",
         "AssociationSize": number,
         "BillingGroupArn": "string",
         "ChargeDetails": {
            "Flat": {
               "ChargeValue": number
            },
            "LineItemFilters": [
               {
                  "Attribute": "string",
                  "AttributeValues": [ "string" ],
                  "MatchOption": "string",
                  "Values": [ "string" ]
               }
            ],
            "Percentage": {
               "PercentageValue": number
            },
            "Type": "string"
         },
         "ComputationRule": "string",
         "CreationTime": number,
         "CurrencyCode": "string",
         "Description": "string",
         "EndBillingPeriod": "string",
         "LastModifiedTime": number,
         "Name": "string",
         "PresentationDetails": {
            "Service": "string"
         },
         "ProductCode": "string",
         "StartBillingPeriod": "string",
         "StartTime": number
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListCustomLineItemVersions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CustomLineItemVersions](#API_ListCustomLineItemVersions_ResponseSyntax) **   <a name="billingconductor-ListCustomLineItemVersions-response-CustomLineItemVersions"></a>
A list of `CustomLineItemVersionListElements` that are received.
Type: Array of [CustomLineItemVersionListElement](API_CustomLineItemVersionListElement.md) objects

 ** [NextToken](#API_ListCustomLineItemVersions_ResponseSyntax) **   <a name="billingconductor-ListCustomLineItemVersions-response-NextToken"></a>
The pagination token that's used on subsequent calls to retrieve custom line item versions.
Type: String

## Errors
<a name="API_ListCustomLineItemVersions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
An unexpected error occurred while processing a request.
 ** RetryAfterSeconds **
Number of seconds you can retry after the call.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
 ** RetryAfterSeconds **
Number of seconds you can safely retry after the call.
HTTP Status Code: 429

 ** ValidationException **
The input doesn't match with the constraints specified by AWS services.
 ** Fields **
The fields that caused the error, if applicable.
 ** Reason **
The reason the request's validation failed.
HTTP Status Code: 400

## See Also
<a name="API_ListCustomLineItemVersions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/billingconductor-2021-07-30/ListCustomLineItemVersions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/billingconductor-2021-07-30/ListCustomLineItemVersions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/billingconductor-2021-07-30/ListCustomLineItemVersions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/billingconductor-2021-07-30/ListCustomLineItemVersions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/billingconductor-2021-07-30/ListCustomLineItemVersions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/billingconductor-2021-07-30/ListCustomLineItemVersions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/billingconductor-2021-07-30/ListCustomLineItemVersions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/billingconductor-2021-07-30/ListCustomLineItemVersions)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/billingconductor-2021-07-30/ListCustomLineItemVersions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/billingconductor-2021-07-30/ListCustomLineItemVersions)
