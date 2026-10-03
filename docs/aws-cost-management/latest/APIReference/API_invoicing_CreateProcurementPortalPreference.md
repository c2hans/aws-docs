---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_invoicing_CreateProcurementPortalPreference.html
---

# CreateProcurementPortalPreference
<a name="API_invoicing_CreateProcurementPortalPreference"></a>

 * **This feature API is subject to changing at any time. For more information, see the [AWS Service Terms](https://aws.amazon.com/service-terms/) (Betas and Previews).** *

Creates a procurement portal preference configuration for e-invoice delivery and purchase order retrieval. This preference defines how invoices are delivered to a procurement portal and how purchase orders are retrieved.

## Request Syntax
<a name="API_invoicing_CreateProcurementPortalPreference_RequestSyntax"></a>

```
{
   "BuyerDomain": "{{string}}",
   "BuyerIdentifier": "{{string}}",
   "ClientToken": "{{string}}",
   "Contacts": [
      {
         "Email": "{{string}}",
         "Name": "{{string}}"
      }
   ],
   "EinvoiceDeliveryEnabled": {{boolean}},
   "EinvoiceDeliveryPreference": {
      "ConnectionTestingMethod": "{{string}}",
      "EinvoiceDeliveryActivationDate": {{number}},
      "EinvoiceDeliveryAttachmentTypes": [ "{{string}}" ],
      "EinvoiceDeliveryDocumentTypes": [ "{{string}}" ],
      "Protocol": "{{string}}",
      "PurchaseOrderDataSources": [
         {
            "EinvoiceDeliveryDocumentType": "{{string}}",
            "PurchaseOrderDataSourceType": "{{string}}"
         }
      ]
   },
   "MarketplacePunchOutEnabled": {{boolean}},
   "MarketplacePunchOutPreference": {
      "ApprovalRequestRedirectUrl": "{{string}}"
   },
   "ProcurementPortalInstanceEndpoint": "{{string}}",
   "ProcurementPortalName": "{{string}}",
   "ProcurementPortalSharedSecret": "{{string}}",
   "PurchaseOrderRetrievalEnabled": {{boolean}},
   "ResourceTags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "Selector": {
      "InvoiceUnitArns": [ "{{string}}" ],
      "SellerOfRecords": [ "{{string}}" ]
   },
   "SupplierDomain": "{{string}}",
   "SupplierIdentifier": "{{string}}",
   "TestEnvPreference": {
      "BuyerDomain": "{{string}}",
      "BuyerIdentifier": "{{string}}",
      "ProcurementPortalInstanceEndpoint": "{{string}}",
      "ProcurementPortalSharedSecret": "{{string}}",
      "SupplierDomain": "{{string}}",
      "SupplierIdentifier": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_invoicing_CreateProcurementPortalPreference_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [BuyerDomain](#API_invoicing_CreateProcurementPortalPreference_RequestSyntax) **   <a name="awscostmanagement-invoicing_CreateProcurementPortalPreference-request-BuyerDomain"></a>
The domain identifier for the buyer in the procurement portal.
Type: String
Valid Values: `NetworkID`
Required: Yes

 ** [BuyerIdentifier](#API_invoicing_CreateProcurementPortalPreference_RequestSyntax) **   <a name="awscostmanagement-invoicing_CreateProcurementPortalPreference-request-BuyerIdentifier"></a>
The unique identifier for the buyer in the procurement portal.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `\S+`
Required: Yes

 ** [ClientToken](#API_invoicing_CreateProcurementPortalPreference_RequestSyntax) **   <a name="awscostmanagement-invoicing_CreateProcurementPortalPreference-request-ClientToken"></a>
A unique, case-sensitive identifier that you provide to ensure idempotency of the request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `\S+`
Required: No

 ** [Contacts](#API_invoicing_CreateProcurementPortalPreference_RequestSyntax) **   <a name="awscostmanagement-invoicing_CreateProcurementPortalPreference-request-Contacts"></a>
List of contact information for portal administrators and technical contacts responsible for the e-invoice integration.
Type: Array of [Contact](API_invoicing_Contact.md) objects
Array Members: Fixed number of 1 item.
Required: Yes

 ** [EinvoiceDeliveryEnabled](#API_invoicing_CreateProcurementPortalPreference_RequestSyntax) **   <a name="awscostmanagement-invoicing_CreateProcurementPortalPreference-request-EinvoiceDeliveryEnabled"></a>
Indicates whether e-invoice delivery is enabled for this procurement portal preference. Set to true to enable e-invoice delivery, false to disable.
Type: Boolean
Required: Yes

 ** [EinvoiceDeliveryPreference](#API_invoicing_CreateProcurementPortalPreference_RequestSyntax) **   <a name="awscostmanagement-invoicing_CreateProcurementPortalPreference-request-EinvoiceDeliveryPreference"></a>
Specifies the e-invoice delivery configuration including document types, attachment types, and customization settings for the portal.
Type: [EinvoiceDeliveryPreference](API_invoicing_EinvoiceDeliveryPreference.md) object
Required: No

 ** [MarketplacePunchOutEnabled](#API_invoicing_CreateProcurementPortalPreference_RequestSyntax) **   <a name="awscostmanagement-invoicing_CreateProcurementPortalPreference-request-MarketplacePunchOutEnabled"></a>
Specifies whether Marketplace PunchOut is enabled for this procurement portal connection. The default value is false.
Type: Boolean
Required: No

 ** [MarketplacePunchOutPreference](#API_invoicing_CreateProcurementPortalPreference_RequestSyntax) **   <a name="awscostmanagement-invoicing_CreateProcurementPortalPreference-request-MarketplacePunchOutPreference"></a>
The configuration for Marketplace PunchOut. This member is required for Coupa when `MarketplacePunchOutEnabled` is `true`.
Type: [MarketplacePunchOutPreference](API_invoicing_MarketplacePunchOutPreference.md) object
Required: No

 ** [ProcurementPortalInstanceEndpoint](#API_invoicing_CreateProcurementPortalPreference_RequestSyntax) **   <a name="awscostmanagement-invoicing_CreateProcurementPortalPreference-request-ProcurementPortalInstanceEndpoint"></a>
The endpoint URL where e-invoices will be delivered to the procurement portal. Must be a valid HTTPS URL.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `\S+`
Required: No

 ** [ProcurementPortalName](#API_invoicing_CreateProcurementPortalPreference_RequestSyntax) **   <a name="awscostmanagement-invoicing_CreateProcurementPortalPreference-request-ProcurementPortalName"></a>
The name of the procurement portal.
Type: String
Valid Values: `SAP_BUSINESS_NETWORK | COUPA`
Required: Yes

 ** [ProcurementPortalSharedSecret](#API_invoicing_CreateProcurementPortalPreference_RequestSyntax) **   <a name="awscostmanagement-invoicing_CreateProcurementPortalPreference-request-ProcurementPortalSharedSecret"></a>
The shared secret or authentication credential used to establish secure communication with the procurement portal. This value must be encrypted at rest.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `\S+`
Required: No

 ** [PurchaseOrderRetrievalEnabled](#API_invoicing_CreateProcurementPortalPreference_RequestSyntax) **   <a name="awscostmanagement-invoicing_CreateProcurementPortalPreference-request-PurchaseOrderRetrievalEnabled"></a>
Indicates whether purchase order retrieval is enabled for this procurement portal preference. Set to true to enable PO retrieval, false to disable.
Type: Boolean
Required: Yes

 ** [ResourceTags](#API_invoicing_CreateProcurementPortalPreference_RequestSyntax) **   <a name="awscostmanagement-invoicing_CreateProcurementPortalPreference-request-ResourceTags"></a>
The tags to apply to this procurement portal preference resource. Each tag consists of a key and an optional value.
Type: Array of [ResourceTag](API_invoicing_ResourceTag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

 ** [Selector](#API_invoicing_CreateProcurementPortalPreference_RequestSyntax) **   <a name="awscostmanagement-invoicing_CreateProcurementPortalPreference-request-Selector"></a>
Specifies criteria for selecting which invoices should be processed using a particular procurement portal preference.
Type: [ProcurementPortalPreferenceSelector](API_invoicing_ProcurementPortalPreferenceSelector.md) object
Required: No

 ** [SupplierDomain](#API_invoicing_CreateProcurementPortalPreference_RequestSyntax) **   <a name="awscostmanagement-invoicing_CreateProcurementPortalPreference-request-SupplierDomain"></a>
The domain identifier for the supplier in the procurement portal.
Type: String
Valid Values: `NetworkID`
Required: Yes

 ** [SupplierIdentifier](#API_invoicing_CreateProcurementPortalPreference_RequestSyntax) **   <a name="awscostmanagement-invoicing_CreateProcurementPortalPreference-request-SupplierIdentifier"></a>
The unique identifier for the supplier in the procurement portal.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `\S+`
Required: Yes

 ** [TestEnvPreference](#API_invoicing_CreateProcurementPortalPreference_RequestSyntax) **   <a name="awscostmanagement-invoicing_CreateProcurementPortalPreference-request-TestEnvPreference"></a>
Configuration settings for the test environment of the procurement portal. Includes test credentials and endpoints that are used for validation before production deployment.
Type: [TestEnvPreferenceInput](API_invoicing_TestEnvPreferenceInput.md) object
Required: No

## Response Syntax
<a name="API_invoicing_CreateProcurementPortalPreference_ResponseSyntax"></a>

```
{
   "ProcurementPortalPreferenceArn": "string"
}
```

## Response Elements
<a name="API_invoicing_CreateProcurementPortalPreference_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ProcurementPortalPreferenceArn](#API_invoicing_CreateProcurementPortalPreference_ResponseSyntax) **   <a name="awscostmanagement-invoicing_CreateProcurementPortalPreference-response-ProcurementPortalPreferenceArn"></a>
The Amazon Resource Name (ARN) of the created procurement portal preference.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `arn:aws:invoicing::[0-9]{12}:procurement-portal-preference/[-a-zA-Z0-9]+`

## Errors
<a name="API_invoicing_CreateProcurementPortalPreference_Errors"></a>

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
<a name="API_invoicing_CreateProcurementPortalPreference_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/invoicing-2024-12-01/CreateProcurementPortalPreference)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/invoicing-2024-12-01/CreateProcurementPortalPreference)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/invoicing-2024-12-01/CreateProcurementPortalPreference)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/invoicing-2024-12-01/CreateProcurementPortalPreference)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/invoicing-2024-12-01/CreateProcurementPortalPreference)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/invoicing-2024-12-01/CreateProcurementPortalPreference)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/invoicing-2024-12-01/CreateProcurementPortalPreference)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/invoicing-2024-12-01/CreateProcurementPortalPreference)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/invoicing-2024-12-01/CreateProcurementPortalPreference)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/invoicing-2024-12-01/CreateProcurementPortalPreference)
