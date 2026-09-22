---
source_url: https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_GetBillingTransferPreference.html
---

# GetBillingTransferPreference
<a name="API_GetBillingTransferPreference"></a>

Retrieves the auto billing group creation preference for a billing transfer.

## Request Syntax
<a name="API_GetBillingTransferPreference_RequestSyntax"></a>

```
POST /get-billing-transfer-preference HTTP/1.1
Content-type: application/json

{
   "ResponsibilityTransferArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_GetBillingTransferPreference_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetBillingTransferPreference_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ResponsibilityTransferArn](#API_GetBillingTransferPreference_RequestSyntax) **   <a name="billingconductor-GetBillingTransferPreference-request-ResponsibilityTransferArn"></a>
The Amazon Resource Name (ARN) of the billing transfer whose preference you want to retrieve.
Type: String
Pattern: `arn:[a-z0-9][a-z0-9-.]{0,62}:organizations::\d{12}:transfer/o-[a-z0-9]{10,32}/(billing)/(inbound|outbound)/rt-[0-9a-z]{8,32}`
Required: Yes

## Response Syntax
<a name="API_GetBillingTransferPreference_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "AutoBillingTransferBillingGroupCreation": {
      "Enabled": boolean,
      "PricingPlanArn": "string"
   },
   "LastModifiedTime": number,
   "ResponsibilityTransferArn": "string"
}
```

## Response Elements
<a name="API_GetBillingTransferPreference_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AutoBillingTransferBillingGroupCreation](#API_GetBillingTransferPreference_ResponseSyntax) **   <a name="billingconductor-GetBillingTransferPreference-response-AutoBillingTransferBillingGroupCreation"></a>
The auto billing group creation preference for the billing transfer.
Type: [AutoTransferBillingGroupCreationPreference](API_AutoTransferBillingGroupCreationPreference.md) object

 ** [LastModifiedTime](#API_GetBillingTransferPreference_ResponseSyntax) **   <a name="billingconductor-GetBillingTransferPreference-response-LastModifiedTime"></a>
The most recent time when the preference was modified. This value is empty if the preference has never been set for the billing transfer.
Type: Long

 ** [ResponsibilityTransferArn](#API_GetBillingTransferPreference_ResponseSyntax) **   <a name="billingconductor-GetBillingTransferPreference-response-ResponsibilityTransferArn"></a>
The Amazon Resource Name (ARN) of the billing transfer that the preference applies to.
Type: String
Pattern: `arn:[a-z0-9][a-z0-9-.]{0,62}:organizations::\d{12}:transfer/o-[a-z0-9]{10,32}/(billing)/(inbound|outbound)/rt-[0-9a-z]{8,32}`

## Errors
<a name="API_GetBillingTransferPreference_Errors"></a>

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
<a name="API_GetBillingTransferPreference_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/billingconductor-2021-07-30/GetBillingTransferPreference)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/billingconductor-2021-07-30/GetBillingTransferPreference)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/billingconductor-2021-07-30/GetBillingTransferPreference)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/billingconductor-2021-07-30/GetBillingTransferPreference)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/billingconductor-2021-07-30/GetBillingTransferPreference)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/billingconductor-2021-07-30/GetBillingTransferPreference)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/billingconductor-2021-07-30/GetBillingTransferPreference)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/billingconductor-2021-07-30/GetBillingTransferPreference)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/billingconductor-2021-07-30/GetBillingTransferPreference)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/billingconductor-2021-07-30/GetBillingTransferPreference)
