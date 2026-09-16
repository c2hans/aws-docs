---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_invoicing_UpdateProcurementPortalPreferenceStatus.html
---

# UpdateProcurementPortalPreferenceStatus
<a name="API_invoicing_UpdateProcurementPortalPreferenceStatus"></a>

 * **This feature API is subject to changing at any time. For more information, see the [AWS Service Terms](https://aws.amazon.com/service-terms/) (Betas and Previews).** *

Updates the status of a procurement portal preference, including the activation state of e-invoice delivery and purchase order retrieval features.

## Request Syntax
<a name="API_invoicing_UpdateProcurementPortalPreferenceStatus_RequestSyntax"></a>

```
{
   "ClientToken": "{{string}}",
   "EinvoiceDeliveryPreferenceStatus": "{{string}}",
   "EinvoiceDeliveryPreferenceStatusReason": "{{string}}",
   "ProcurementPortalPreferenceArn": "{{string}}",
   "PurchaseOrderRetrievalPreferenceStatus": "{{string}}",
   "PurchaseOrderRetrievalPreferenceStatusReason": "{{string}}"
}
```

## Request Parameters
<a name="API_invoicing_UpdateProcurementPortalPreferenceStatus_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClientToken](#API_invoicing_UpdateProcurementPortalPreferenceStatus_RequestSyntax) **   <a name="awscostmanagement-invoicing_UpdateProcurementPortalPreferenceStatus-request-ClientToken"></a>
A unique, case-sensitive identifier that you provide to ensure idempotency of the request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `\S+`
Required: No

 ** [EinvoiceDeliveryPreferenceStatus](#API_invoicing_UpdateProcurementPortalPreferenceStatus_RequestSyntax) **   <a name="awscostmanagement-invoicing_UpdateProcurementPortalPreferenceStatus-request-EinvoiceDeliveryPreferenceStatus"></a>
The updated status of the e-invoice delivery preference.
Type: String
Valid Values: `PENDING_VERIFICATION | VALIDATED | TEST_INITIALIZED | TEST_INITIALIZATION_FAILED | TEST_FAILED | ACTIVE | SUSPENDED`
Required: No

 ** [EinvoiceDeliveryPreferenceStatusReason](#API_invoicing_UpdateProcurementPortalPreferenceStatus_RequestSyntax) **   <a name="awscostmanagement-invoicing_UpdateProcurementPortalPreferenceStatus-request-EinvoiceDeliveryPreferenceStatusReason"></a>
The reason for the e-invoice delivery preference status update, providing context for the change.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\s\S]*`
Required: No

 ** [ProcurementPortalPreferenceArn](#API_invoicing_UpdateProcurementPortalPreferenceStatus_RequestSyntax) **   <a name="awscostmanagement-invoicing_UpdateProcurementPortalPreferenceStatus-request-ProcurementPortalPreferenceArn"></a>
The Amazon Resource Name (ARN) of the procurement portal preference to update.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `arn:aws:invoicing::[0-9]{12}:procurement-portal-preference/[-a-zA-Z0-9]+`
Required: Yes

 ** [PurchaseOrderRetrievalPreferenceStatus](#API_invoicing_UpdateProcurementPortalPreferenceStatus_RequestSyntax) **   <a name="awscostmanagement-invoicing_UpdateProcurementPortalPreferenceStatus-request-PurchaseOrderRetrievalPreferenceStatus"></a>
The updated status of the purchase order retrieval preference.
Type: String
Valid Values: `PENDING_VERIFICATION | VALIDATED | TEST_INITIALIZED | TEST_INITIALIZATION_FAILED | TEST_FAILED | ACTIVE | SUSPENDED`
Required: No

 ** [PurchaseOrderRetrievalPreferenceStatusReason](#API_invoicing_UpdateProcurementPortalPreferenceStatus_RequestSyntax) **   <a name="awscostmanagement-invoicing_UpdateProcurementPortalPreferenceStatus-request-PurchaseOrderRetrievalPreferenceStatusReason"></a>
The reason for the purchase order retrieval preference status update, providing context for the change.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\s\S]*`
Required: No

## Response Syntax
<a name="API_invoicing_UpdateProcurementPortalPreferenceStatus_ResponseSyntax"></a>

```
{
   "ProcurementPortalPreferenceArn": "string"
}
```

## Response Elements
<a name="API_invoicing_UpdateProcurementPortalPreferenceStatus_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ProcurementPortalPreferenceArn](#API_invoicing_UpdateProcurementPortalPreferenceStatus_ResponseSyntax) **   <a name="awscostmanagement-invoicing_UpdateProcurementPortalPreferenceStatus-response-ProcurementPortalPreferenceArn"></a>
The Amazon Resource Name (ARN) of the procurement portal preference with updated status.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `arn:aws:invoicing::[0-9]{12}:procurement-portal-preference/[-a-zA-Z0-9]+`

## Errors
<a name="API_invoicing_UpdateProcurementPortalPreferenceStatus_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient access to perform this action.
 ** resourceName **
You don't have sufficient access to perform this action.
HTTP Status Code: 400

 ** ConflictException **
The request could not be completed due to a conflict with the current state of the resource. This exception occurs when a concurrent modification is detected during an update operation, or when attempting to create a resource that already exists.
 ** resourceId **
The identifier of the resource that caused the conflict.
 ** resourceType **
The type of resource that caused the conflict.
HTTP Status Code: 400

 ** InternalServerException **
The processing request failed because of an unknown error, exception, or failure.
 ** retryAfterSeconds **
The processing request failed because of an unknown error, exception, or failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The resource could not be found.
 ** resourceName **
The resource could not be found.
HTTP Status Code: 400

 ** ServiceQuotaExceededException **
The request was rejected because it attempted to create resources beyond the current AWS account limits. The error message describes the limit exceeded.
HTTP Status Code: 400

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 400

 ** ValidationException **
 The input fails to satisfy the constraints specified by an AWS service.
 ** fieldList **
 The input fails to satisfy the constraints specified by an AWS service.
 ** reason **
You don't have sufficient access to perform this action.
 ** resourceName **
You don't have sufficient access to perform this action.
HTTP Status Code: 400

## See Also
<a name="API_invoicing_UpdateProcurementPortalPreferenceStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/invoicing-2024-12-01/UpdateProcurementPortalPreferenceStatus)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/invoicing-2024-12-01/UpdateProcurementPortalPreferenceStatus)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/invoicing-2024-12-01/UpdateProcurementPortalPreferenceStatus)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/invoicing-2024-12-01/UpdateProcurementPortalPreferenceStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/invoicing-2024-12-01/UpdateProcurementPortalPreferenceStatus)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/invoicing-2024-12-01/UpdateProcurementPortalPreferenceStatus)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/invoicing-2024-12-01/UpdateProcurementPortalPreferenceStatus)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/invoicing-2024-12-01/UpdateProcurementPortalPreferenceStatus)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/invoicing-2024-12-01/UpdateProcurementPortalPreferenceStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/invoicing-2024-12-01/UpdateProcurementPortalPreferenceStatus)
