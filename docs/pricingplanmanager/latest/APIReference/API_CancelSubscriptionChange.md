---
source_url: https://docs.aws.amazon.com/pricingplanmanager/latest/APIReference/API_CancelSubscriptionChange.html
---

# CancelSubscriptionChange
<a name="API_CancelSubscriptionChange"></a>

Cancels a pending scheduled change on a subscription, such as a pending downgrade or cancellation. The subscription returns to its state before the change was scheduled.

**Note**
You cannot cancel a scheduled change close to its effective date. If the change is within the processing window, this operation returns an error.

## Request Syntax
<a name="API_CancelSubscriptionChange_RequestSyntax"></a>

```
POST /v1/CancelSubscriptionChange HTTP/1.1
If-Match: {{ifMatch}}
Content-type: application/json

{
   "arn": "{{string}}",
   "clientToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CancelSubscriptionChange_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ifMatch](#API_CancelSubscriptionChange_RequestSyntax) **   <a name="pricingplanmanager-CancelSubscriptionChange-request-ifMatch"></a>
The `ETag` value from a previous `GetSubscription` or `ListSubscriptions` response.
Required: Yes

## Request Body
<a name="API_CancelSubscriptionChange_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [arn](#API_CancelSubscriptionChange_RequestSyntax) **   <a name="pricingplanmanager-CancelSubscriptionChange-request-arn"></a>
The ARN of the subscription whose pending change you want to cancel.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

 ** [clientToken](#API_CancelSubscriptionChange_RequestSyntax) **   <a name="pricingplanmanager-CancelSubscriptionChange-request-clientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the request is handled only once.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

## Response Syntax
<a name="API_CancelSubscriptionChange_ResponseSyntax"></a>

```
HTTP/1.1 200
ETag: {{eTag}}
Content-type: application/json

{
   "arn": "string",
   "createdAt": "string",
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
```

## Response Elements
<a name="API_CancelSubscriptionChange_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The response returns the following HTTP headers.

 ** [eTag](#API_CancelSubscriptionChange_ResponseSyntax) **   <a name="pricingplanmanager-CancelSubscriptionChange-response-eTag"></a>
The updated entity tag for concurrency control.

The following data is returned in JSON format by the service.

 ** [arn](#API_CancelSubscriptionChange_ResponseSyntax) **   <a name="pricingplanmanager-CancelSubscriptionChange-response-arn"></a>
The Amazon Resource Name (ARN) that uniquely identifies this subscription.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [createdAt](#API_CancelSubscriptionChange_ResponseSyntax) **   <a name="pricingplanmanager-CancelSubscriptionChange-response-createdAt"></a>
The date and time when the subscription was created, in ISO 8601 format.
Type: Timestamp

 ** [planFamily](#API_CancelSubscriptionChange_ResponseSyntax) **   <a name="pricingplanmanager-CancelSubscriptionChange-response-planFamily"></a>
The pricing plan family for the subscription, such as `CloudFront`.
Type: String

 ** [planTier](#API_CancelSubscriptionChange_ResponseSyntax) **   <a name="pricingplanmanager-CancelSubscriptionChange-response-planTier"></a>
The current tier level of the pricing plan, such as `FREE`, `PRO`, `BUSINESS`, or `PREMIUM`.
Type: String

 ** [resourceArns](#API_CancelSubscriptionChange_ResponseSyntax) **   <a name="pricingplanmanager-CancelSubscriptionChange-response-resourceArns"></a>
The ARNs of the AWS resources covered by this subscription.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.

 ** [status](#API_CancelSubscriptionChange_ResponseSyntax) **   <a name="pricingplanmanager-CancelSubscriptionChange-response-status"></a>
The current status of the subscription. For the list of possible values, see the `Status` type.
Type: String
Valid Values: `PENDING_APPROVAL | ACTIVE | SYNC_IN_PROGRESS | FAILED`

 ** [updatedAt](#API_CancelSubscriptionChange_ResponseSyntax) **   <a name="pricingplanmanager-CancelSubscriptionChange-response-updatedAt"></a>
The date and time when the subscription was last modified, in ISO 8601 format.
Type: Timestamp

 ** [scheduledChange](#API_CancelSubscriptionChange_ResponseSyntax) **   <a name="pricingplanmanager-CancelSubscriptionChange-response-scheduledChange"></a>
A pending change that will take effect at the end of the current billing period. This field is present only when a downgrade or cancellation is scheduled.
Type: [ScheduledChange](API_ScheduledChange.md) object

 ** [statusReason](#API_CancelSubscriptionChange_ResponseSyntax) **   <a name="pricingplanmanager-CancelSubscriptionChange-response-statusReason"></a>
A human-readable explanation of the current status, present when additional context is available.
Type: String

 ** [usageLevel](#API_CancelSubscriptionChange_ResponseSyntax) **   <a name="pricingplanmanager-CancelSubscriptionChange-response-usageLevel"></a>
The usage level within the plan tier. When present, indicates a specific capacity configuration beyond the base tier.
Type: String

## Errors
<a name="API_CancelSubscriptionChange_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have the required permissions to perform this operation. Verify that your IAM policy grants access to this action.
HTTP Status Code: 403

 ** ConflictException **
The request conflicts with the current state of the resource. This typically occurs when the `ETag` value in the `If-Match` header does not match the current version of the subscription. Retrieve the latest version and retry.
 ** resourceId **
The identifier of the resource that has a conflicting state.
HTTP Status Code: 409

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
<a name="API_CancelSubscriptionChange_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pricing-plan-manager-2025-08-05/CancelSubscriptionChange)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pricing-plan-manager-2025-08-05/CancelSubscriptionChange)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pricing-plan-manager-2025-08-05/CancelSubscriptionChange)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pricing-plan-manager-2025-08-05/CancelSubscriptionChange)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pricing-plan-manager-2025-08-05/CancelSubscriptionChange)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pricing-plan-manager-2025-08-05/CancelSubscriptionChange)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pricing-plan-manager-2025-08-05/CancelSubscriptionChange)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pricing-plan-manager-2025-08-05/CancelSubscriptionChange)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/pricing-plan-manager-2025-08-05/CancelSubscriptionChange)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pricing-plan-manager-2025-08-05/CancelSubscriptionChange)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Pricing Plan Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pricingplanmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
