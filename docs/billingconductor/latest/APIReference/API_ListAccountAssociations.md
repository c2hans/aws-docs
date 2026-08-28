---
source_url: https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_ListAccountAssociations.html
---

# ListAccountAssociations
<a name="API_ListAccountAssociations"></a>

 This is a paginated call to list linked accounts that are linked to the payer account for the specified time period. If no information is provided, the current billing period is used. The response will optionally include the billing group that's associated with the linked account.

## Request Syntax
<a name="API_ListAccountAssociations_RequestSyntax"></a>

```
POST /list-account-associations HTTP/1.1
Content-type: application/json

{
   "BillingPeriod": "{{string}}",
   "Filters": {
      "AccountId": "{{string}}",
      "AccountIds": [ "{{string}}" ],
      "Association": "{{string}}"
   },
   "NextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListAccountAssociations_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListAccountAssociations_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [BillingPeriod](#API_ListAccountAssociations_RequestSyntax) **   <a name="billingconductor-ListAccountAssociations-request-BillingPeriod"></a>
 The preferred billing period to get account associations.
Type: String
Pattern: `\d{4}-(0?[1-9]|1[012])`
Required: No

 ** [Filters](#API_ListAccountAssociations_RequestSyntax) **   <a name="billingconductor-ListAccountAssociations-request-Filters"></a>
The filter on the account ID of the linked account, or any of the following:
 `MONITORED`: linked accounts that are associated to billing groups.
 `UNMONITORED`: linked accounts that aren't associated to billing groups.
 `Billing Group Arn`: linked accounts that are associated to the provided billing group Arn.
Type: [ListAccountAssociationsFilter](API_ListAccountAssociationsFilter.md) object
Required: No

 ** [NextToken](#API_ListAccountAssociations_RequestSyntax) **   <a name="billingconductor-ListAccountAssociations-request-NextToken"></a>
 The pagination token that's used on subsequent calls to retrieve accounts.
Type: String
Required: No

## Response Syntax
<a name="API_ListAccountAssociations_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "LinkedAccounts": [
      {
         "AccountEmail": "string",
         "AccountId": "string",
         "AccountName": "string",
         "BillingGroupArn": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListAccountAssociations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [LinkedAccounts](#API_ListAccountAssociations_ResponseSyntax) **   <a name="billingconductor-ListAccountAssociations-response-LinkedAccounts"></a>
 The list of linked accounts in the payer account.
Type: Array of [AccountAssociationsListElement](API_AccountAssociationsListElement.md) objects

 ** [NextToken](#API_ListAccountAssociations_ResponseSyntax) **   <a name="billingconductor-ListAccountAssociations-response-NextToken"></a>
 The pagination token that's used on subsequent calls to get accounts.
Type: String

## Errors
<a name="API_ListAccountAssociations_Errors"></a>

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
<a name="API_ListAccountAssociations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/billingconductor-2021-07-30/ListAccountAssociations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/billingconductor-2021-07-30/ListAccountAssociations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/billingconductor-2021-07-30/ListAccountAssociations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/billingconductor-2021-07-30/ListAccountAssociations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/billingconductor-2021-07-30/ListAccountAssociations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/billingconductor-2021-07-30/ListAccountAssociations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/billingconductor-2021-07-30/ListAccountAssociations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/billingconductor-2021-07-30/ListAccountAssociations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/billingconductor-2021-07-30/ListAccountAssociations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/billingconductor-2021-07-30/ListAccountAssociations)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Billing Conductor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query billingconductor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
