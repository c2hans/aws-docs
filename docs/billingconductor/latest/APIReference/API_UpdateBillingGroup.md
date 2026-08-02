---
source_url: https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_UpdateBillingGroup.html
---

# UpdateBillingGroup
<a name="API_UpdateBillingGroup"></a>

This updates an existing billing group.

## Request Syntax
<a name="API_UpdateBillingGroup_RequestSyntax"></a>

```
POST /update-billing-group HTTP/1.1
Content-type: application/json

{
   "AccountGrouping": {
      "AutoAssociate": {{boolean}},
      "ResponsibilityTransferArn": "{{string}}"
   },
   "Arn": "{{string}}",
   "ComputationPreference": {
      "PricingPlanArn": "{{string}}"
   },
   "Description": "{{string}}",
   "Name": "{{string}}",
   "Status": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateBillingGroup_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdateBillingGroup_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AccountGrouping](#API_UpdateBillingGroup_RequestSyntax) **   <a name="billingconductor-UpdateBillingGroup-request-AccountGrouping"></a>
Specifies if the billing group has automatic account association (`AutoAssociate`) enabled.
Type: [UpdateBillingGroupAccountGrouping](API_UpdateBillingGroupAccountGrouping.md) object
Required: No

 ** [Arn](#API_UpdateBillingGroup_RequestSyntax) **   <a name="billingconductor-UpdateBillingGroup-request-Arn"></a>
The Amazon Resource Name (ARN) of the billing group being updated.
Type: String
Pattern: `(arn:aws(-cn)?:billingconductor::[0-9]{12}:billinggroup/)?[a-zA-Z0-9]{10,12}`
Required: Yes

 ** [ComputationPreference](#API_UpdateBillingGroup_RequestSyntax) **   <a name="billingconductor-UpdateBillingGroup-request-ComputationPreference"></a>
 The preferences and settings that will be used to compute the AWS charges for a billing group.
Type: [ComputationPreference](API_ComputationPreference.md) object
Required: No

 ** [Description](#API_UpdateBillingGroup_RequestSyntax) **   <a name="billingconductor-UpdateBillingGroup-request-Description"></a>
A description of the billing group.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** [Name](#API_UpdateBillingGroup_RequestSyntax) **   <a name="billingconductor-UpdateBillingGroup-request-Name"></a>
The name of the billing group. The names must be unique to each billing group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_\+=\.\-@]+`
Required: No

 ** [Status](#API_UpdateBillingGroup_RequestSyntax) **   <a name="billingconductor-UpdateBillingGroup-request-Status"></a>
The status of the billing group. Only one of the valid values can be used.
Type: String
Valid Values: `ACTIVE | PRIMARY_ACCOUNT_MISSING | PENDING`
Required: No

## Response Syntax
<a name="API_UpdateBillingGroup_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "AccountGrouping": {
      "AutoAssociate": boolean,
      "ResponsibilityTransferArn": "string"
   },
   "Arn": "string",
   "Description": "string",
   "LastModifiedTime": number,
   "Name": "string",
   "PricingPlanArn": "string",
   "PrimaryAccountId": "string",
   "Size": number,
   "Status": "string",
   "StatusReason": "string"
}
```

## Response Elements
<a name="API_UpdateBillingGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AccountGrouping](#API_UpdateBillingGroup_ResponseSyntax) **   <a name="billingconductor-UpdateBillingGroup-response-AccountGrouping"></a>
Specifies if the billing group has automatic account association (`AutoAssociate`) enabled.
Type: [UpdateBillingGroupAccountGrouping](API_UpdateBillingGroupAccountGrouping.md) object

 ** [Arn](#API_UpdateBillingGroup_ResponseSyntax) **   <a name="billingconductor-UpdateBillingGroup-response-Arn"></a>
The Amazon Resource Name (ARN) of the billing group that was updated.
Type: String
Pattern: `(arn:aws(-cn)?:billingconductor::[0-9]{12}:billinggroup/)?[a-zA-Z0-9]{10,12}`

 ** [Description](#API_UpdateBillingGroup_ResponseSyntax) **   <a name="billingconductor-UpdateBillingGroup-response-Description"></a>
 A description of the billing group.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.

 ** [LastModifiedTime](#API_UpdateBillingGroup_ResponseSyntax) **   <a name="billingconductor-UpdateBillingGroup-response-LastModifiedTime"></a>
 The most recent time when the billing group was modified.
Type: Long

 ** [Name](#API_UpdateBillingGroup_ResponseSyntax) **   <a name="billingconductor-UpdateBillingGroup-response-Name"></a>
 The name of the billing group. The names must be unique to each billing group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_\+=\.\-@]+`

 ** [PricingPlanArn](#API_UpdateBillingGroup_ResponseSyntax) **   <a name="billingconductor-UpdateBillingGroup-response-PricingPlanArn"></a>
 The Amazon Resource Name (ARN) of the pricing plan to compute AWS charges for the billing group.
Type: String
Pattern: `(arn:aws(-cn)?:billingconductor::(aws|[0-9]{12}):pricingplan/)?(BasicPricingPlan|Passthrough|[a-zA-Z0-9]{10})`

 ** [PrimaryAccountId](#API_UpdateBillingGroup_ResponseSyntax) **   <a name="billingconductor-UpdateBillingGroup-response-PrimaryAccountId"></a>
 The account ID that serves as the main account in a billing group.
Type: String
Pattern: `[0-9]{12}`

 ** [Size](#API_UpdateBillingGroup_ResponseSyntax) **   <a name="billingconductor-UpdateBillingGroup-response-Size"></a>
 The number of accounts in the particular billing group.
Type: Long
Valid Range: Minimum value of 0.

 ** [Status](#API_UpdateBillingGroup_ResponseSyntax) **   <a name="billingconductor-UpdateBillingGroup-response-Status"></a>
 The status of the billing group. Only one of the valid values can be used.
Type: String
Valid Values: `ACTIVE | PRIMARY_ACCOUNT_MISSING | PENDING`

 ** [StatusReason](#API_UpdateBillingGroup_ResponseSyntax) **   <a name="billingconductor-UpdateBillingGroup-response-StatusReason"></a>
 The reason why the billing group is in its current status.
Type: String

## Errors
<a name="API_UpdateBillingGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
You can cause an inconsistent state by updating or deleting a resource.
 ** Reason **
Reason for the inconsistent state.
 ** ResourceId **
Identifier of the resource in use.
 ** ResourceType **
Type of the resource in use.
HTTP Status Code: 409

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
<a name="API_UpdateBillingGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/billingconductor-2021-07-30/UpdateBillingGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/billingconductor-2021-07-30/UpdateBillingGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/billingconductor-2021-07-30/UpdateBillingGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/billingconductor-2021-07-30/UpdateBillingGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/billingconductor-2021-07-30/UpdateBillingGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/billingconductor-2021-07-30/UpdateBillingGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/billingconductor-2021-07-30/UpdateBillingGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/billingconductor-2021-07-30/UpdateBillingGroup)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/billingconductor-2021-07-30/UpdateBillingGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/billingconductor-2021-07-30/UpdateBillingGroup)
