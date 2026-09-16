---
source_url: https://docs.aws.amazon.com/pricingplanmanager/latest/APIReference/API_CreateSubscription.html
---

# CreateSubscription
<a name="API_CreateSubscription"></a>

Creates a flat-rate pricing subscription for the specified resources.

**Note**
When `approvalMode` is set to `MANUAL`, paid-tier subscriptions are created in `PENDING_APPROVAL` status and require a separate `ApprovePaidSubscription` call before billing starts. Free-tier subscriptions are always activated immediately regardless of approval mode.
When `approvalMode` is set to `IMMEDIATE` or is not specified, the subscription is activated immediately.

## Request Syntax
<a name="API_CreateSubscription_RequestSyntax"></a>

```
POST /v1/CreateSubscription HTTP/1.1
Content-type: application/json

{
   "approvalMode": "{{string}}",
   "clientToken": "{{string}}",
   "planFamily": "{{string}}",
   "planTier": "{{string}}",
   "resourceArns": [ "{{string}}" ],
   "usageLevel": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateSubscription_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateSubscription_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [planFamily](#API_CreateSubscription_RequestSyntax) **   <a name="pricingplanmanager-CreateSubscription-request-planFamily"></a>
The pricing plan family to subscribe to, such as `CloudFront`.
Type: String
Required: Yes

 ** [planTier](#API_CreateSubscription_RequestSyntax) **   <a name="pricingplanmanager-CreateSubscription-request-planTier"></a>
The tier level for the subscription, such as `FREE`, `PRO`, `BUSINESS`, or `PREMIUM`.
Type: String
Required: Yes

 ** [resourceArns](#API_CreateSubscription_RequestSyntax) **   <a name="pricingplanmanager-CreateSubscription-request-resourceArns"></a>
The ARNs of the AWS resources to include in the subscription. Specify one or more supported resources.
For subscriptions in the CloudFront plan family, the resources must include exactly one Amazon CloudFront distribution and exactly one AWS WAF web ACL. You can also include other supported resources, such as Amazon Route 53 hosted zones and CloudFront KeyValueStores.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: Yes

 ** [approvalMode](#API_CreateSubscription_RequestSyntax) **   <a name="pricingplanmanager-CreateSubscription-request-approvalMode"></a>
Determines whether the subscription requires explicit approval before billing starts. Set to `MANUAL` to require a separate `ApprovePaidSubscription` call, or `IMMEDIATE` to activate the subscription right away. For paid tier plans, this defaults to `MANUAL` if not specified. For the `FREE` plan tier, only `IMMEDIATE` is supported, and it is the default.
Type: String
Valid Values: `MANUAL | IMMEDIATE`
Required: No

 ** [clientToken](#API_CreateSubscription_RequestSyntax) **   <a name="pricingplanmanager-CreateSubscription-request-clientToken"></a>
A unique, case-sensitive identifier that you provide to ensure that the request is handled only once. If you send the same request with the same client token, the API returns the original response without creating a duplicate subscription.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** [usageLevel](#API_CreateSubscription_RequestSyntax) **   <a name="pricingplanmanager-CreateSubscription-request-usageLevel"></a>
The usage level within the plan tier. Specify `DEFAULT` for the base configuration, or a higher level if your plan tier supports it.
Type: String
Required: No

## Response Syntax
<a name="API_CreateSubscription_ResponseSyntax"></a>

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
<a name="API_CreateSubscription_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The response returns the following HTTP headers.

 ** [eTag](#API_CreateSubscription_ResponseSyntax) **   <a name="pricingplanmanager-CreateSubscription-response-eTag"></a>
The entity tag for concurrency control. Use this value in the `If-Match` header for subsequent operations on this subscription.

The following data is returned in JSON format by the service.

 ** [arn](#API_CreateSubscription_ResponseSyntax) **   <a name="pricingplanmanager-CreateSubscription-response-arn"></a>
The Amazon Resource Name (ARN) that uniquely identifies this subscription.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [createdAt](#API_CreateSubscription_ResponseSyntax) **   <a name="pricingplanmanager-CreateSubscription-response-createdAt"></a>
The date and time when the subscription was created, in ISO 8601 format.
Type: Timestamp

 ** [planFamily](#API_CreateSubscription_ResponseSyntax) **   <a name="pricingplanmanager-CreateSubscription-response-planFamily"></a>
The pricing plan family for the subscription, such as `CloudFront`.
Type: String

 ** [planTier](#API_CreateSubscription_ResponseSyntax) **   <a name="pricingplanmanager-CreateSubscription-response-planTier"></a>
The current tier level of the pricing plan, such as `FREE`, `PRO`, `BUSINESS`, or `PREMIUM`.
Type: String

 ** [resourceArns](#API_CreateSubscription_ResponseSyntax) **   <a name="pricingplanmanager-CreateSubscription-response-resourceArns"></a>
The ARNs of the AWS resources covered by this subscription.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.

 ** [status](#API_CreateSubscription_ResponseSyntax) **   <a name="pricingplanmanager-CreateSubscription-response-status"></a>
The current status of the subscription. For the list of possible values, see the `Status` type.
Type: String
Valid Values: `PENDING_APPROVAL | ACTIVE | SYNC_IN_PROGRESS | FAILED`

 ** [updatedAt](#API_CreateSubscription_ResponseSyntax) **   <a name="pricingplanmanager-CreateSubscription-response-updatedAt"></a>
The date and time when the subscription was last modified, in ISO 8601 format.
Type: Timestamp

 ** [scheduledChange](#API_CreateSubscription_ResponseSyntax) **   <a name="pricingplanmanager-CreateSubscription-response-scheduledChange"></a>
A pending change that will take effect at the end of the current billing period. This field is present only when a downgrade or cancellation is scheduled.
Type: [ScheduledChange](API_ScheduledChange.md) object

 ** [statusReason](#API_CreateSubscription_ResponseSyntax) **   <a name="pricingplanmanager-CreateSubscription-response-statusReason"></a>
A human-readable explanation of the current status, present when additional context is available.
Type: String

 ** [usageLevel](#API_CreateSubscription_ResponseSyntax) **   <a name="pricingplanmanager-CreateSubscription-response-usageLevel"></a>
The usage level within the plan tier. When present, indicates a specific capacity configuration beyond the base tier.
Type: String

## Errors
<a name="API_CreateSubscription_Errors"></a>

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

 ** ServiceQuotaExceededException **
The request would exceed a service limit. You have reached the maximum number of subscriptions allowed for your account.
HTTP Status Code: 402

 ** ThrottlingException **
The request rate exceeds the allowed limit. Wait briefly and retry the request.
HTTP Status Code: 429

 ** ValidationException **
The request failed a business rule validation. For example, the specified resource might already be associated with another subscription, or the subscription might not be in the required state for this operation.
 ** resourceId **
The identifier of the resource that failed validation.
HTTP Status Code: 400

## See Also
<a name="API_CreateSubscription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pricing-plan-manager-2025-08-05/CreateSubscription)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pricing-plan-manager-2025-08-05/CreateSubscription)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pricing-plan-manager-2025-08-05/CreateSubscription)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pricing-plan-manager-2025-08-05/CreateSubscription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pricing-plan-manager-2025-08-05/CreateSubscription)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pricing-plan-manager-2025-08-05/CreateSubscription)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pricing-plan-manager-2025-08-05/CreateSubscription)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pricing-plan-manager-2025-08-05/CreateSubscription)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/pricing-plan-manager-2025-08-05/CreateSubscription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pricing-plan-manager-2025-08-05/CreateSubscription)
