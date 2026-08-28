---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_billing_ListBillingViews.html
---

# ListBillingViews
<a name="API_billing_ListBillingViews"></a>

Lists the billing views available for a given time period.

Every AWS account has a unique `PRIMARY` billing view that represents the billing data available by default. Accounts that use AWS Billing Conductor also have `BILLING_GROUP` billing views representing pro forma costs associated with each created billing group.

## Request Syntax
<a name="API_billing_ListBillingViews_RequestSyntax"></a>

```
{
   "activeTimeRange": {
      "activeAfterInclusive": {{number}},
      "activeBeforeInclusive": {{number}}
   },
   "arns": [ "{{string}}" ],
   "billingViewTypes": [ "{{string}}" ],
   "maxResults": {{number}},
   "names": [
      {
         "searchOption": "{{string}}",
         "searchValue": "{{string}}"
      }
   ],
   "nextToken": "{{string}}",
   "ownerAccountId": "{{string}}",
   "sourceAccountId": "{{string}}"
}
```

## Request Parameters
<a name="API_billing_ListBillingViews_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [activeTimeRange](#API_billing_ListBillingViews_RequestSyntax) **   <a name="awscostmanagement-billing_ListBillingViews-request-activeTimeRange"></a>
 The time range for the billing views listed. `PRIMARY` billing view is always listed. `BILLING_GROUP` billing views are listed for time ranges when the associated billing group resource in AWS Billing Conductor is active. The time range must be within one calendar month.
Type: [ActiveTimeRange](API_billing_ActiveTimeRange.md) object
Required: No

 ** [arns](#API_billing_ListBillingViews_RequestSyntax) **   <a name="awscostmanagement-billing_ListBillingViews-request-arns"></a>
The Amazon Resource Name (ARN) that can be used to uniquely identify the billing view.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Pattern: `arn:aws[a-z-]*:(billing)::[0-9]{12}:billingview/[a-zA-Z0-9/:_\+=\.\-@]{0,75}[a-zA-Z0-9]`
Required: No

 ** [billingViewTypes](#API_billing_ListBillingViews_RequestSyntax) **   <a name="awscostmanagement-billing_ListBillingViews-request-billingViewTypes"></a>
The type of billing view.
Type: Array of strings
Valid Values: `PRIMARY | BILLING_GROUP | CUSTOM | BILLING_TRANSFER | BILLING_TRANSFER_SHOWBACK`
Required: No

 ** [maxResults](#API_billing_ListBillingViews_RequestSyntax) **   <a name="awscostmanagement-billing_ListBillingViews-request-maxResults"></a>
The maximum number of billing views to retrieve. Default is 100.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [names](#API_billing_ListBillingViews_RequestSyntax) **   <a name="awscostmanagement-billing_ListBillingViews-request-names"></a>
 Filters the list of billing views by name. You can specify search criteria to match billing view names based on the search option provided.
Type: Array of [StringSearch](API_billing_StringSearch.md) objects
Array Members: Fixed number of 1 item.
Required: No

 ** [nextToken](#API_billing_ListBillingViews_RequestSyntax) **   <a name="awscostmanagement-billing_ListBillingViews-request-nextToken"></a>
The pagination token that is used on subsequent calls to list billing views.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4095.
Pattern: `[-a-zA-Z0-9+=/_]+`
Required: No

 ** [ownerAccountId](#API_billing_ListBillingViews_RequestSyntax) **   <a name="awscostmanagement-billing_ListBillingViews-request-ownerAccountId"></a>
 The list of owners of the billing view.
Type: String
Pattern: `[0-9]{12}`
Required: No

 ** [sourceAccountId](#API_billing_ListBillingViews_RequestSyntax) **   <a name="awscostmanagement-billing_ListBillingViews-request-sourceAccountId"></a>
 Filters the results to include only billing views that use the specified account as a source.
Type: String
Pattern: `[0-9]{12}`
Required: No

## Response Syntax
<a name="API_billing_ListBillingViews_ResponseSyntax"></a>

```
{
   "billingViews": [
      {
         "arn": "string",
         "billingViewType": "string",
         "description": "string",
         "healthStatus": {
            "statusCode": "string",
            "statusReasons": [ "string" ]
         },
         "name": "string",
         "ownerAccountId": "string",
         "sourceAccountId": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_billing_ListBillingViews_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [billingViews](#API_billing_ListBillingViews_ResponseSyntax) **   <a name="awscostmanagement-billing_ListBillingViews-response-billingViews"></a>
A list of `BillingViewListElement` retrieved.
Type: Array of [BillingViewListElement](API_billing_BillingViewListElement.md) objects

 ** [nextToken](#API_billing_ListBillingViews_ResponseSyntax) **   <a name="awscostmanagement-billing_ListBillingViews-response-nextToken"></a>
The pagination token to use on subsequent calls to list billing views.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4095.
Pattern: `[-a-zA-Z0-9+=/_]+`

## Errors
<a name="API_billing_ListBillingViews_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient access to perform this action.
HTTP Status Code: 400

 ** InternalServerException **
The request processing failed because of an unknown error, exception, or failure.
HTTP Status Code: 500

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
<a name="API_billing_ListBillingViews_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/billing-2023-09-07/ListBillingViews)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/billing-2023-09-07/ListBillingViews)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/billing-2023-09-07/ListBillingViews)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/billing-2023-09-07/ListBillingViews)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/billing-2023-09-07/ListBillingViews)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/billing-2023-09-07/ListBillingViews)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/billing-2023-09-07/ListBillingViews)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/billing-2023-09-07/ListBillingViews)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/billing-2023-09-07/ListBillingViews)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/billing-2023-09-07/ListBillingViews)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
