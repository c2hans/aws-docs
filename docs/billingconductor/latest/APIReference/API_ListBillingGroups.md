---
source_url: https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_ListBillingGroups.html
---

# ListBillingGroups
<a name="API_ListBillingGroups"></a>

A paginated call to retrieve a list of billing groups for the given billing period. If you don't provide a billing group, the current billing period is used.

## Request Syntax
<a name="API_ListBillingGroups_RequestSyntax"></a>

```
POST /list-billing-groups HTTP/1.1
Content-type: application/json

{
   "BillingPeriod": "{{string}}",
   "Filters": {
      "Arns": [ "{{string}}" ],
      "AutoAssociate": {{boolean}},
      "BillingGroupTypes": [ "{{string}}" ],
      "Names": [
         {
            "SearchOption": "{{string}}",
            "SearchValue": "{{string}}"
         }
      ],
      "PricingPlan": "{{string}}",
      "PrimaryAccountIds": [ "{{string}}" ],
      "ResponsibilityTransferArns": [ "{{string}}" ],
      "Statuses": [ "{{string}}" ]
   },
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListBillingGroups_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListBillingGroups_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [BillingPeriod](#API_ListBillingGroups_RequestSyntax) **   <a name="billingconductor-ListBillingGroups-request-BillingPeriod"></a>
The preferred billing period to get billing groups.
Type: String
Pattern: `\d{4}-(0?[1-9]|1[012])`
Required: No

 ** [Filters](#API_ListBillingGroups_RequestSyntax) **   <a name="billingconductor-ListBillingGroups-request-Filters"></a>
A `ListBillingGroupsFilter` that specifies the billing group and pricing plan to retrieve billing group information.
Type: [ListBillingGroupsFilter](API_ListBillingGroupsFilter.md) object
Required: No

 ** [MaxResults](#API_ListBillingGroups_RequestSyntax) **   <a name="billingconductor-ListBillingGroups-request-MaxResults"></a>
The maximum number of billing groups to retrieve.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListBillingGroups_RequestSyntax) **   <a name="billingconductor-ListBillingGroups-request-NextToken"></a>
The pagination token that's used on subsequent calls to get billing groups.
Type: String
Required: No

## Response Syntax
<a name="API_ListBillingGroups_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "BillingGroups": [
      {
         "AccountGrouping": {
            "AutoAssociate": boolean,
            "ResponsibilityTransferArn": "string"
         },
         "Arn": "string",
         "BillingGroupType": "string",
         "ComputationPreference": {
            "PricingPlanArn": "string"
         },
         "CreationTime": number,
         "Description": "string",
         "LastModifiedTime": number,
         "Name": "string",
         "PrimaryAccountId": "string",
         "Size": number,
         "Status": "string",
         "StatusReason": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListBillingGroups_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [BillingGroups](#API_ListBillingGroups_ResponseSyntax) **   <a name="billingconductor-ListBillingGroups-response-BillingGroups"></a>
A list of `BillingGroupListElement` retrieved.
Type: Array of [BillingGroupListElement](API_BillingGroupListElement.md) objects

 ** [NextToken](#API_ListBillingGroups_ResponseSyntax) **   <a name="billingconductor-ListBillingGroups-response-NextToken"></a>
The pagination token that's used on subsequent calls to get billing groups.
Type: String

## Errors
<a name="API_ListBillingGroups_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
An unexpected error occurred while processing a request.
 ** RetryAfterSeconds **
Number of seconds you can retry after the call.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The request references a resource that doesn't exist.
 ** ResourceId **
Resource identifier that was not found.
 ** ResourceType **
Resource type that was not found.
HTTP Status Code: 404

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
<a name="API_ListBillingGroups_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/billingconductor-2021-07-30/ListBillingGroups)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/billingconductor-2021-07-30/ListBillingGroups)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/billingconductor-2021-07-30/ListBillingGroups)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/billingconductor-2021-07-30/ListBillingGroups)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/billingconductor-2021-07-30/ListBillingGroups)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/billingconductor-2021-07-30/ListBillingGroups)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/billingconductor-2021-07-30/ListBillingGroups)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/billingconductor-2021-07-30/ListBillingGroups)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/billingconductor-2021-07-30/ListBillingGroups)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/billingconductor-2021-07-30/ListBillingGroups)
