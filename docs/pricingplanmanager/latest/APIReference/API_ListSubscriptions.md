---
source_url: https://docs.aws.amazon.com/pricingplanmanager/latest/APIReference/API_ListSubscriptions.html
---

# ListSubscriptions
<a name="API_ListSubscriptions"></a>

Returns a summary of all flat-rate pricing subscriptions in the calling account.

## Request Syntax
<a name="API_ListSubscriptions_RequestSyntax"></a>

```
POST /v1/ListSubscriptions HTTP/1.1
Content-type: application/json

{
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListSubscriptions_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListSubscriptions_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [nextToken](#API_ListSubscriptions_RequestSyntax) **   <a name="pricingplanmanager-ListSubscriptions-request-nextToken"></a>
A token from a previous `ListSubscriptions` response. If the response included a `nextToken`, there are more results available. Pass this value to retrieve the next page of results.
Type: String
Required: No

## Response Syntax
<a name="API_ListSubscriptions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "subscriptionSummaries": [
      {
         "arn": "string",
         "createdAt": "string",
         "eTag": "string",
         "planFamily": "string",
         "planTier": "string",
         "resourceArns": [ "string" ],
         "scheduledChange": {
            "changeType": "string",
            "effectiveDate": "string",
            "planTier": "string",
            "usageLevel": "string"
         },
         "status": "string",
         "statusReason": "string",
         "updatedAt": "string",
         "usageLevel": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListSubscriptions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [subscriptionSummaries](#API_ListSubscriptions_ResponseSyntax) **   <a name="pricingplanmanager-ListSubscriptions-response-subscriptionSummaries"></a>
The list of subscription summaries for the calling account.
Type: Array of [SubscriptionSummary](API_SubscriptionSummary.md) objects

 ** [nextToken](#API_ListSubscriptions_ResponseSyntax) **   <a name="pricingplanmanager-ListSubscriptions-response-nextToken"></a>
A token that indicates there are more results available. Pass this value in a subsequent `ListSubscriptions` request to retrieve the next page of results.
Type: String

## Errors
<a name="API_ListSubscriptions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have the required permissions to perform this operation. Verify that your IAM policy grants access to this action.
HTTP Status Code: 403

 ** InternalServerException **
An unexpected error occurred on the server. Retry the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified subscription was not found. Verify that the ARN is correct and that the subscription belongs to your account.
 ** resourceId **
The identifier of the resource that was not found.
HTTP Status Code: 404

 ** ThrottlingException **
The request rate exceeds the allowed limit. Wait briefly and retry the request.
HTTP Status Code: 429

 ** ValidationException **
The request failed a business rule validation. For example, the specified resource might already be associated with another subscription, or the subscription might not be in the required state for this operation.
 ** resourceId **
The identifier of the resource that failed validation.
HTTP Status Code: 400

## See Also
<a name="API_ListSubscriptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pricing-plan-manager-2025-08-05/ListSubscriptions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pricing-plan-manager-2025-08-05/ListSubscriptions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pricing-plan-manager-2025-08-05/ListSubscriptions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pricing-plan-manager-2025-08-05/ListSubscriptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pricing-plan-manager-2025-08-05/ListSubscriptions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pricing-plan-manager-2025-08-05/ListSubscriptions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pricing-plan-manager-2025-08-05/ListSubscriptions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pricing-plan-manager-2025-08-05/ListSubscriptions)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/pricing-plan-manager-2025-08-05/ListSubscriptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pricing-plan-manager-2025-08-05/ListSubscriptions)
