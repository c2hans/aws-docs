---
source_url: https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_UpdateCustomLineItem.html
---

# UpdateCustomLineItem
<a name="API_UpdateCustomLineItem"></a>

 Update an existing custom line item in the current or previous billing period.

## Request Syntax
<a name="API_UpdateCustomLineItem_RequestSyntax"></a>

```
POST /update-custom-line-item HTTP/1.1
Content-type: application/json

{
   "Arn": "{{string}}",
   "BillingPeriodRange": {
      "ExclusiveEndBillingPeriod": "{{string}}",
      "InclusiveStartBillingPeriod": "{{string}}"
   },
   "ChargeDetails": {
      "Flat": {
         "ChargeValue": {{number}}
      },
      "LineItemFilters": [
         {
            "Attribute": "{{string}}",
            "AttributeValues": [ "{{string}}" ],
            "MatchOption": "{{string}}",
            "Values": [ "{{string}}" ]
         }
      ],
      "Percentage": {
         "PercentageValue": {{number}}
      }
   },
   "Description": "{{string}}",
   "Name": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateCustomLineItem_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdateCustomLineItem_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Arn](#API_UpdateCustomLineItem_RequestSyntax) **   <a name="billingconductor-UpdateCustomLineItem-request-Arn"></a>
 The ARN of the custom line item to be updated.
Type: String
Pattern: `(arn:aws(-cn)?:billingconductor::[0-9]{12}:customlineitem/)?[a-zA-Z0-9]{10}`
Required: Yes

 ** [BillingPeriodRange](#API_UpdateCustomLineItem_RequestSyntax) **   <a name="billingconductor-UpdateCustomLineItem-request-BillingPeriodRange"></a>
The billing period range in which the custom line item request will be applied.
Type: [CustomLineItemBillingPeriodRange](API_CustomLineItemBillingPeriodRange.md) object
Required: No

 ** [ChargeDetails](#API_UpdateCustomLineItem_RequestSyntax) **   <a name="billingconductor-UpdateCustomLineItem-request-ChargeDetails"></a>
 A `ListCustomLineItemChargeDetails` containing the new charge details for the custom line item.
Type: [UpdateCustomLineItemChargeDetails](API_UpdateCustomLineItemChargeDetails.md) object
Required: No

 ** [Description](#API_UpdateCustomLineItem_RequestSyntax) **   <a name="billingconductor-UpdateCustomLineItem-request-Description"></a>
 The new line item description of the custom line item.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** [Name](#API_UpdateCustomLineItem_RequestSyntax) **   <a name="billingconductor-UpdateCustomLineItem-request-Name"></a>
 The new name for the custom line item.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_\+=\.\-@]+`
Required: No

## Response Syntax
<a name="API_UpdateCustomLineItem_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Arn": "string",
   "AssociationSize": number,
   "BillingGroupArn": "string",
   "ChargeDetails": {
      "Flat": {
         "ChargeValue": number
      },
      "LineItemFilters": [
         {
            "Attribute": "string",
            "AttributeValues": [ "string" ],
            "MatchOption": "string",
            "Values": [ "string" ]
         }
      ],
      "Percentage": {
         "PercentageValue": number
      },
      "Type": "string"
   },
   "Description": "string",
   "LastModifiedTime": number,
   "Name": "string"
}
```

## Response Elements
<a name="API_UpdateCustomLineItem_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_UpdateCustomLineItem_ResponseSyntax) **   <a name="billingconductor-UpdateCustomLineItem-response-Arn"></a>
 The ARN of the successfully updated custom line item.
Type: String
Pattern: `(arn:aws(-cn)?:billingconductor::[0-9]{12}:customlineitem/)?[a-zA-Z0-9]{10}`

 ** [AssociationSize](#API_UpdateCustomLineItem_ResponseSyntax) **   <a name="billingconductor-UpdateCustomLineItem-response-AssociationSize"></a>
 The number of resources that are associated to the custom line item.
Type: Long
Valid Range: Minimum value of 0.

 ** [BillingGroupArn](#API_UpdateCustomLineItem_ResponseSyntax) **   <a name="billingconductor-UpdateCustomLineItem-response-BillingGroupArn"></a>
 The ARN of the billing group that the custom line item is applied to.
Type: String
Pattern: `arn:aws(-cn)?:billingconductor::[0-9]{12}:billinggroup/[a-zA-Z0-9]{10,12}`

 ** [ChargeDetails](#API_UpdateCustomLineItem_ResponseSyntax) **   <a name="billingconductor-UpdateCustomLineItem-response-ChargeDetails"></a>
 A `ListCustomLineItemChargeDetails` containing the charge details of the successfully updated custom line item.
Type: [ListCustomLineItemChargeDetails](API_ListCustomLineItemChargeDetails.md) object

 ** [Description](#API_UpdateCustomLineItem_ResponseSyntax) **   <a name="billingconductor-UpdateCustomLineItem-response-Description"></a>
 The description of the successfully updated custom line item.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.

 ** [LastModifiedTime](#API_UpdateCustomLineItem_ResponseSyntax) **   <a name="billingconductor-UpdateCustomLineItem-response-LastModifiedTime"></a>
 The most recent time when the custom line item was modified.
Type: Long

 ** [Name](#API_UpdateCustomLineItem_ResponseSyntax) **   <a name="billingconductor-UpdateCustomLineItem-response-Name"></a>
 The name of the successfully updated custom line item.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_\+=\.\-@]+`

## Errors
<a name="API_UpdateCustomLineItem_Errors"></a>

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
<a name="API_UpdateCustomLineItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/billingconductor-2021-07-30/UpdateCustomLineItem)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/billingconductor-2021-07-30/UpdateCustomLineItem)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/billingconductor-2021-07-30/UpdateCustomLineItem)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/billingconductor-2021-07-30/UpdateCustomLineItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/billingconductor-2021-07-30/UpdateCustomLineItem)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/billingconductor-2021-07-30/UpdateCustomLineItem)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/billingconductor-2021-07-30/UpdateCustomLineItem)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/billingconductor-2021-07-30/UpdateCustomLineItem)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/billingconductor-2021-07-30/UpdateCustomLineItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/billingconductor-2021-07-30/UpdateCustomLineItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Billing Conductor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query billingconductor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
