---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_billing_ListSourceViewsForBillingView.html
---

# ListSourceViewsForBillingView
<a name="API_billing_ListSourceViewsForBillingView"></a>

Lists the source views (managed AWS billing views) associated with the billing view.

## Request Syntax
<a name="API_billing_ListSourceViewsForBillingView_RequestSyntax"></a>

```
{
   "arn": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_billing_ListSourceViewsForBillingView_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [arn](#API_billing_ListSourceViewsForBillingView_RequestSyntax) **   <a name="awscostmanagement-billing_ListSourceViewsForBillingView-request-arn"></a>
 The Amazon Resource Name (ARN) that can be used to uniquely identify the billing view.
Type: String
Pattern: `arn:aws[a-z-]*:(billing)::[0-9]{12}:billingview/[a-zA-Z0-9/:_\+=\.\-@]{0,75}[a-zA-Z0-9]`
Required: Yes

 ** [maxResults](#API_billing_ListSourceViewsForBillingView_RequestSyntax) **   <a name="awscostmanagement-billing_ListSourceViewsForBillingView-request-maxResults"></a>
 The number of entries a paginated response contains.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_billing_ListSourceViewsForBillingView_RequestSyntax) **   <a name="awscostmanagement-billing_ListSourceViewsForBillingView-request-nextToken"></a>
 The pagination token that is used on subsequent calls to list billing views.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4095.
Pattern: `[-a-zA-Z0-9+=/_]+`
Required: No

## Response Syntax
<a name="API_billing_ListSourceViewsForBillingView_ResponseSyntax"></a>

```
{
   "nextToken": "string",
   "sourceViews": [ "string" ]
}
```

## Response Elements
<a name="API_billing_ListSourceViewsForBillingView_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_billing_ListSourceViewsForBillingView_ResponseSyntax) **   <a name="awscostmanagement-billing_ListSourceViewsForBillingView-response-nextToken"></a>
 The pagination token that is used on subsequent calls to list billing views.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4095.
Pattern: `[-a-zA-Z0-9+=/_]+`

 ** [sourceViews](#API_billing_ListSourceViewsForBillingView_ResponseSyntax) **   <a name="awscostmanagement-billing_ListSourceViewsForBillingView-response-sourceViews"></a>
A list of billing views used as the data source for the custom billing view.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Pattern: `arn:aws[a-z-]*:(billing)::[0-9]{12}:billingview/[a-zA-Z0-9/:_\+=\.\-@]{0,75}[a-zA-Z0-9]`

## Errors
<a name="API_billing_ListSourceViewsForBillingView_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient access to perform this action.
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
<a name="API_billing_ListSourceViewsForBillingView_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/billing-2023-09-07/ListSourceViewsForBillingView)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/billing-2023-09-07/ListSourceViewsForBillingView)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/billing-2023-09-07/ListSourceViewsForBillingView)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/billing-2023-09-07/ListSourceViewsForBillingView)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/billing-2023-09-07/ListSourceViewsForBillingView)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/billing-2023-09-07/ListSourceViewsForBillingView)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/billing-2023-09-07/ListSourceViewsForBillingView)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/billing-2023-09-07/ListSourceViewsForBillingView)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/billing-2023-09-07/ListSourceViewsForBillingView)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/billing-2023-09-07/ListSourceViewsForBillingView)
