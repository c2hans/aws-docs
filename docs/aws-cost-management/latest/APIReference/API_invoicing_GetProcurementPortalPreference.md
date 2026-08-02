---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_invoicing_GetProcurementPortalPreference.html
---

# GetProcurementPortalPreference
<a name="API_invoicing_GetProcurementPortalPreference"></a>

 * **This feature API is subject to changing at any time. For more information, see the [AWS Service Terms](https://aws.amazon.com/service-terms/) (Betas and Previews).** *

Retrieves the details of a specific procurement portal preference configuration.

## Request Syntax
<a name="API_invoicing_GetProcurementPortalPreference_RequestSyntax"></a>

```
{
   "ProcurementPortalPreferenceArn": "{{string}}"
}
```

## Request Parameters
<a name="API_invoicing_GetProcurementPortalPreference_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ProcurementPortalPreferenceArn](#API_invoicing_GetProcurementPortalPreference_RequestSyntax) **   <a name="awscostmanagement-invoicing_GetProcurementPortalPreference-request-ProcurementPortalPreferenceArn"></a>
The Amazon Resource Name (ARN) of the procurement portal preference to retrieve.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `arn:aws:invoicing::[0-9]{12}:procurement-portal-preference/[-a-zA-Z0-9]+`
Required: Yes

## Response Syntax
<a name="API_invoicing_GetProcurementPortalPreference_ResponseSyntax"></a>

```
{
   "ProcurementPortalPreference": {
      "AwsAccountId": "string",
      "BuyerDomain": "string",
      "BuyerIdentifier": "string",
      "Contacts": [
         {
            "Email": "string",
            "Name": "string"
         }
      ],
      "CreateDate": number,
      "EinvoiceDeliveryEnabled": boolean,
      "EinvoiceDeliveryPreference": {
         "ConnectionTestingMethod": "string",
         "EinvoiceDeliveryActivationDate": number,
         "EinvoiceDeliveryAttachmentTypes": [ "string" ],
         "EinvoiceDeliveryDocumentTypes": [ "string" ],
         "Protocol": "string",
         "PurchaseOrderDataSources": [
            {
               "EinvoiceDeliveryDocumentType": "string",
               "PurchaseOrderDataSourceType": "string"
            }
         ]
      },
      "EinvoiceDeliveryPreferenceStatus": "string",
      "EinvoiceDeliveryPreferenceStatusReason": "string",
      "LastUpdateDate": number,
      "ProcurementPortalInstanceEndpoint": "string",
      "ProcurementPortalName": "string",
      "ProcurementPortalPreferenceArn": "string",
      "ProcurementPortalSharedSecret": "string",
      "PurchaseOrderRetrievalEnabled": boolean,
      "PurchaseOrderRetrievalEndpoint": "string",
      "PurchaseOrderRetrievalPreferenceStatus": "string",
      "PurchaseOrderRetrievalPreferenceStatusReason": "string",
      "Selector": {
         "InvoiceUnitArns": [ "string" ],
         "SellerOfRecords": [ "string" ]
      },
      "SupplierDomain": "string",
      "SupplierIdentifier": "string",
      "TestEnvPreference": {
         "BuyerDomain": "string",
         "BuyerIdentifier": "string",
         "ProcurementPortalInstanceEndpoint": "string",
         "ProcurementPortalSharedSecret": "string",
         "PurchaseOrderRetrievalEndpoint": "string",
         "SupplierDomain": "string",
         "SupplierIdentifier": "string"
      },
      "Version": number
   }
}
```

## Response Elements
<a name="API_invoicing_GetProcurementPortalPreference_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ProcurementPortalPreference](#API_invoicing_GetProcurementPortalPreference_ResponseSyntax) **   <a name="awscostmanagement-invoicing_GetProcurementPortalPreference-response-ProcurementPortalPreference"></a>
The detailed configuration of the requested procurement portal preference.
Type: [ProcurementPortalPreference](API_invoicing_ProcurementPortalPreference.md) object

## Errors
<a name="API_invoicing_GetProcurementPortalPreference_Errors"></a>

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
<a name="API_invoicing_GetProcurementPortalPreference_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/invoicing-2024-12-01/GetProcurementPortalPreference)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/invoicing-2024-12-01/GetProcurementPortalPreference)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/invoicing-2024-12-01/GetProcurementPortalPreference)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/invoicing-2024-12-01/GetProcurementPortalPreference)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/invoicing-2024-12-01/GetProcurementPortalPreference)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/invoicing-2024-12-01/GetProcurementPortalPreference)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/invoicing-2024-12-01/GetProcurementPortalPreference)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/invoicing-2024-12-01/GetProcurementPortalPreference)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/invoicing-2024-12-01/GetProcurementPortalPreference)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/invoicing-2024-12-01/GetProcurementPortalPreference)
