---
source_url: https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_CreateCustomLineItem.html
---

# CreateCustomLineItem
<a name="API_CreateCustomLineItem"></a>

Creates a custom line item that can be used to create a one-time fixed charge that can be applied to a single billing group for the current or previous billing period. The one-time fixed charge is either a fee or discount.

## Request Syntax
<a name="API_CreateCustomLineItem_RequestSyntax"></a>

```
POST /create-custom-line-item HTTP/1.1
X-Amzn-Client-Token: {{ClientToken}}
Content-type: application/json

{
   "AccountId": "{{string}}",
   "BillingGroupArn": "{{string}}",
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
         "AssociatedValues": [ "{{string}}" ],
         "PercentageValue": {{number}}
      },
      "Type": "{{string}}"
   },
   "ComputationRule": "{{string}}",
   "Description": "{{string}}",
   "Name": "{{string}}",
   "PresentationDetails": {
      "Service": "{{string}}"
   },
   "Tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateCustomLineItem_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ClientToken](#API_CreateCustomLineItem_RequestSyntax) **   <a name="billingconductor-CreateCustomLineItem-request-ClientToken"></a>
A unique, case-sensitive identifier that you specify to ensure idempotency of the request. Idempotency ensures that an API request completes no more than one time. With an idempotent request, if the original request completes successfully, any subsequent retries complete successfully without performing any further actions.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9-]+`

## Request Body
<a name="API_CreateCustomLineItem_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AccountId](#API_CreateCustomLineItem_RequestSyntax) **   <a name="billingconductor-CreateCustomLineItem-request-AccountId"></a>
The AWS account in which this custom line item will be applied to.
Type: String
Pattern: `[0-9]{12}`
Required: No

 ** [BillingGroupArn](#API_CreateCustomLineItem_RequestSyntax) **   <a name="billingconductor-CreateCustomLineItem-request-BillingGroupArn"></a>
 The Amazon Resource Name (ARN) that references the billing group where the custom line item applies to.
Type: String
Pattern: `(arn:aws(-cn)?:billingconductor::[0-9]{12}:billinggroup/)?[a-zA-Z0-9]{10,12}`
Required: Yes

 ** [BillingPeriodRange](#API_CreateCustomLineItem_RequestSyntax) **   <a name="billingconductor-CreateCustomLineItem-request-BillingPeriodRange"></a>
 A time range for which the custom line item is effective.
Type: [CustomLineItemBillingPeriodRange](API_CustomLineItemBillingPeriodRange.md) object
Required: No

 ** [ChargeDetails](#API_CreateCustomLineItem_RequestSyntax) **   <a name="billingconductor-CreateCustomLineItem-request-ChargeDetails"></a>
 A `CustomLineItemChargeDetails` that describes the charge details for a custom line item.
Type: [CustomLineItemChargeDetails](API_CustomLineItemChargeDetails.md) object
Required: Yes

 ** [ComputationRule](#API_CreateCustomLineItem_RequestSyntax) **   <a name="billingconductor-CreateCustomLineItem-request-ComputationRule"></a>
 Specifies how the custom line item charges are computed.
Type: String
Valid Values: `ITEMIZED | CONSOLIDATED`
Required: No

 ** [Description](#API_CreateCustomLineItem_RequestSyntax) **   <a name="billingconductor-CreateCustomLineItem-request-Description"></a>
 The description of the custom line item. This is shown on the Bills page in association with the charge value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** [Name](#API_CreateCustomLineItem_RequestSyntax) **   <a name="billingconductor-CreateCustomLineItem-request-Name"></a>
 The name of the custom line item.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_\+=\.\-@]+`
Required: Yes

 ** [PresentationDetails](#API_CreateCustomLineItem_RequestSyntax) **   <a name="billingconductor-CreateCustomLineItem-request-PresentationDetails"></a>
 Details controlling how the custom line item charges are presented in the bill. Contains specifications for which service the charges will be shown under.
Type: [PresentationObject](API_PresentationObject.md) object
Required: No

 ** [Tags](#API_CreateCustomLineItem_RequestSyntax) **   <a name="billingconductor-CreateCustomLineItem-request-Tags"></a>
 A map that contains tag keys and tag values that are attached to a custom line item.
Type: String to string map
Map Entries: Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateCustomLineItem_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Arn": "string"
}
```

## Response Elements
<a name="API_CreateCustomLineItem_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_CreateCustomLineItem_ResponseSyntax) **   <a name="billingconductor-CreateCustomLineItem-response-Arn"></a>
 The Amazon Resource Name (ARN) of the created custom line item.
Type: String
Pattern: `(arn:aws(-cn)?:billingconductor::[0-9]{12}:customlineitem/)?[a-zA-Z0-9]{10}`

## Errors
<a name="API_CreateCustomLineItem_Errors"></a>

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

 ** ServiceLimitExceededException **
The request would cause a service limit to exceed.
 ** LimitCode **
The unique code identifier of the service limit that is being exceeded.
 ** ResourceId **
Identifier of the resource affected.
 ** ResourceType **
Type of the resource affected.
 ** ServiceCode **
The unique code for the service of the limit that is being exceeded.
HTTP Status Code: 402

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

## Examples
<a name="API_CreateCustomLineItem_Examples"></a>

### The following example applies a custom line item to another linked account (555555555555) in the billing group.
<a name="API_CreateCustomLineItem_Example_1"></a>

This example illustrates one usage of CreateCustomLineItem.

#### Sample Request
<a name="API_CreateCustomLineItem_Example_1_Request"></a>

```
POST /create-custom-line-item HTTP/1.1
X-Amzn-Client-Token: ClientToken
Content-type: application/json
{
   "BillingGroupArn": "arn:aws:billingconductor::123456789012:billinggroup/111122223333",
   "ChargeDetails": {
      "Flat": {
         "ChargeValue":10
      },
      "Type": "FEE"
   },
   "Description": "My custom line item",
   "Name": "MyCustomLineItem",
   "AccountId": "555555555555"

}
```

#### Sample Response
<a name="API_CreateCustomLineItem_Example_1_Response"></a>

```
HTTP/1.1 200
Content-type: application/json
{
   "Arn": "arn:aws:billingconductor::123456789012:customlineitem/555555555555"
}
```

## See Also
<a name="API_CreateCustomLineItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/billingconductor-2021-07-30/CreateCustomLineItem)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/billingconductor-2021-07-30/CreateCustomLineItem)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/billingconductor-2021-07-30/CreateCustomLineItem)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/billingconductor-2021-07-30/CreateCustomLineItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/billingconductor-2021-07-30/CreateCustomLineItem)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/billingconductor-2021-07-30/CreateCustomLineItem)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/billingconductor-2021-07-30/CreateCustomLineItem)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/billingconductor-2021-07-30/CreateCustomLineItem)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/billingconductor-2021-07-30/CreateCustomLineItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/billingconductor-2021-07-30/CreateCustomLineItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Billing Conductor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query billingconductor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
