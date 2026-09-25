---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_billing_ListBillingViewSegments.html
---

# ListBillingViewSegments
<a name="API_billing_ListBillingViewSegments"></a>

Lists the segments of a billing view over a given time period. Each segment identifies the billing domain (`PRO_FORMA` or `BILLABLE`) and the account relationships that apply during its time range.

If you don't provide an `arn`, the response includes segments for the caller's `PRIMARY` billing view.

If a mid-period change occurs, the response includes multiple segments, each with its own time range. The response omits hidden segments, so the segments it returns might not cover the entire requested time period.

## Request Syntax
<a name="API_billing_ListBillingViewSegments_RequestSyntax"></a>

```
{
   "arn": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "timeRange": {
      "beginDateInclusive": {{number}},
      "endDateExclusive": {{number}}
   }
}
```

## Request Parameters
<a name="API_billing_ListBillingViewSegments_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [arn](#API_billing_ListBillingViewSegments_RequestSyntax) **   <a name="awscostmanagement-billing_ListBillingViewSegments-request-arn"></a>
 The Amazon Resource Name (ARN) that uniquely identifies the billing view to query. If you don't provide an ARN, the caller's `PRIMARY` billing view is used. The ARN must reference a primary billing view. Custom billing views aren't supported.
Type: String
Pattern: `arn:aws[a-z-]*:(billing)::[0-9]{12}:billingview/[a-zA-Z0-9/:_\+=\.\-@]{0,75}[a-zA-Z0-9]`
Required: No

 ** [maxResults](#API_billing_ListBillingViewSegments_RequestSyntax) **   <a name="awscostmanagement-billing_ListBillingViewSegments-request-maxResults"></a>
 The number of entries a paginated response contains. Valid values range from 1 to 100. The default is 100.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_billing_ListBillingViewSegments_RequestSyntax) **   <a name="awscostmanagement-billing_ListBillingViewSegments-request-nextToken"></a>
 The pagination token that is used on subsequent calls to list billing view segments.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4095.
Pattern: `[-a-zA-Z0-9+=/_]+`
Required: No

 ** [timeRange](#API_billing_ListBillingViewSegments_RequestSyntax) **   <a name="awscostmanagement-billing_ListBillingViewSegments-request-timeRange"></a>
 The billing period to query. If you don't provide a time range, the current billing period, which is the calendar month in UTC, is used.
Type: [BillingViewSegmentTimeRange](API_billing_BillingViewSegmentTimeRange.md) object
Required: No

## Response Syntax
<a name="API_billing_ListBillingViewSegments_ResponseSyntax"></a>

```
{
   "items": [
      {
         "billingGroupPrimaryAccountId": "string",
         "billingTransferAccountId": "string",
         "domain": "string",
         "managementAccountId": "string",
         "timeRange": {
            "beginDateInclusive": number,
            "endDateExclusive": number
         }
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_billing_ListBillingViewSegments_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [items](#API_billing_ListBillingViewSegments_ResponseSyntax) **   <a name="awscostmanagement-billing_ListBillingViewSegments-response-items"></a>
 A list of billing view segments. Each segment covers a portion of the requested time period. The response omits hidden segments, so the segments it returns might not cover the entire requested time period.
Type: Array of [BillingViewSegmentsListElement](API_billing_BillingViewSegmentsListElement.md) objects

 ** [nextToken](#API_billing_ListBillingViewSegments_ResponseSyntax) **   <a name="awscostmanagement-billing_ListBillingViewSegments-response-nextToken"></a>
 The pagination token that is used on subsequent calls to list billing view segments.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4095.
Pattern: `[-a-zA-Z0-9+=/_]+`

## Errors
<a name="API_billing_ListBillingViewSegments_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient access to perform this action.
HTTP Status Code: 400

 ** BillingViewHealthStatusException **
 Exception thrown when a billing view's health status prevents an operation from being performed. This may occur if the billing view is in a state other than `HEALTHY`.
HTTP Status Code: 400

 ** InternalServerException **
The request processing failed because of an unknown error, exception, or failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
 The specified ARN in the request doesn't exist.
 ** resourceId **
 Value is a list of resource IDs that were not found.
 ** resourceType **
 Value is the type of resource that was not found.
HTTP Status Code: 400

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 400

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
 ** fieldList **
The input fails to satisfy the constraints specified by an AWS service.
 ** reason **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_billing_ListBillingViewSegments_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/billing-2023-09-07/ListBillingViewSegments)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/billing-2023-09-07/ListBillingViewSegments)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/billing-2023-09-07/ListBillingViewSegments)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/billing-2023-09-07/ListBillingViewSegments)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/billing-2023-09-07/ListBillingViewSegments)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/billing-2023-09-07/ListBillingViewSegments)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/billing-2023-09-07/ListBillingViewSegments)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/billing-2023-09-07/ListBillingViewSegments)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/billing-2023-09-07/ListBillingViewSegments)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/billing-2023-09-07/ListBillingViewSegments)
