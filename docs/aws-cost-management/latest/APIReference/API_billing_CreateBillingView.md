---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_billing_CreateBillingView.html
---

# CreateBillingView
<a name="API_billing_CreateBillingView"></a>

 Creates a billing view with the specified billing view attributes.

## Request Syntax
<a name="API_billing_CreateBillingView_RequestSyntax"></a>

```
{
   "clientToken": "{{string}}",
   "dataFilterExpression": {
      "costCategories": {
         "key": "{{string}}",
         "values": [ "{{string}}" ]
      },
      "dimensions": {
         "key": "{{string}}",
         "values": [ "{{string}}" ]
      },
      "tags": {
         "key": "{{string}}",
         "values": [ "{{string}}" ]
      },
      "timeRange": {
         "beginDateInclusive": {{number}},
         "endDateInclusive": {{number}}
      }
   },
   "description": "{{string}}",
   "name": "{{string}}",
   "resourceTags": [
      {
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ],
   "sourceViews": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_billing_CreateBillingView_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [clientToken](#API_billing_CreateBillingView_RequestSyntax) **   <a name="awscostmanagement-billing_CreateBillingView-request-clientToken"></a>
A unique, case-sensitive identifier you specify to ensure idempotency of the request. Idempotency ensures that an API request completes no more than one time. If the original request completes successfully, any subsequent retries complete successfully without performing any further actions with an idempotent request.
Type: String
Pattern: `[a-zA-Z0-9-]+`
Required: No

 ** [dataFilterExpression](#API_billing_CreateBillingView_RequestSyntax) **   <a name="awscostmanagement-billing_CreateBillingView-request-dataFilterExpression"></a>
 See [Expression](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_billing_Expression.html). Billing view only supports `LINKED_ACCOUNT`, `Tags`, and `CostCategories`.
Type: [Expression](API_billing_Expression.md) object
Required: No

 ** [description](#API_billing_CreateBillingView_RequestSyntax) **   <a name="awscostmanagement-billing_CreateBillingView-request-description"></a>
 The description of the billing view.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `([ a-zA-Z0-9_\+=\.\-@]+)?`
Required: No

 ** [name](#API_billing_CreateBillingView_RequestSyntax) **   <a name="awscostmanagement-billing_CreateBillingView-request-name"></a>
 The name of the billing view.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[ a-zA-Z0-9_\+=\.\-@]+`
Required: Yes

 ** [resourceTags](#API_billing_CreateBillingView_RequestSyntax) **   <a name="awscostmanagement-billing_CreateBillingView-request-resourceTags"></a>
A list of key value map specifying tags associated to the billing view being created.
Type: Array of [ResourceTag](API_billing_ResourceTag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

 ** [sourceViews](#API_billing_CreateBillingView_RequestSyntax) **   <a name="awscostmanagement-billing_CreateBillingView-request-sourceViews"></a>
A list of billing views used as the data source for the custom billing view.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Pattern: `arn:aws[a-z-]*:(billing)::[0-9]{12}:billingview/[a-zA-Z0-9/:_\+=\.\-@]{0,75}[a-zA-Z0-9]`
Required: Yes

## Response Syntax
<a name="API_billing_CreateBillingView_ResponseSyntax"></a>

```
{
   "arn": "string",
   "createdAt": number
}
```

## Response Elements
<a name="API_billing_CreateBillingView_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_billing_CreateBillingView_ResponseSyntax) **   <a name="awscostmanagement-billing_CreateBillingView-response-arn"></a>
 The Amazon Resource Name (ARN) that can be used to uniquely identify the billing view.
Type: String
Pattern: `arn:aws[a-z-]*:(billing)::[0-9]{12}:billingview/[a-zA-Z0-9/:_\+=\.\-@]{0,75}[a-zA-Z0-9]`

 ** [createdAt](#API_billing_CreateBillingView_ResponseSyntax) **   <a name="awscostmanagement-billing_CreateBillingView-response-createdAt"></a>
 The time when the billing view was created.
Type: Timestamp

## Errors
<a name="API_billing_CreateBillingView_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient access to perform this action.
HTTP Status Code: 400

 ** BillingViewHealthStatusException **
 Exception thrown when a billing view's health status prevents an operation from being performed. This may occur if the billing view is in a state other than `HEALTHY`.
HTTP Status Code: 400

 ** ConflictException **
 The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request.
 ** resourceId **
 The identifier for the service resource associated with the request.
 ** resourceType **
 The type of resource associated with the request.
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

 ** ServiceQuotaExceededException **
 You've reached the limit of resources you can create, or exceeded the size of an individual resource.
 ** quotaCode **
 The container for the `quotaCode`.
 ** resourceId **
 The ID of the resource.
 ** resourceType **
 The type of AWS resource.
 ** serviceCode **
 The container for the `serviceCode`.
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
<a name="API_billing_CreateBillingView_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/billing-2023-09-07/CreateBillingView)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/billing-2023-09-07/CreateBillingView)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/billing-2023-09-07/CreateBillingView)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/billing-2023-09-07/CreateBillingView)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/billing-2023-09-07/CreateBillingView)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/billing-2023-09-07/CreateBillingView)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/billing-2023-09-07/CreateBillingView)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/billing-2023-09-07/CreateBillingView)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/billing-2023-09-07/CreateBillingView)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/billing-2023-09-07/CreateBillingView)
