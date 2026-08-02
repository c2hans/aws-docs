---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_invoicing_ListProcurementPortalPreferences.html
---

# ListProcurementPortalPreferences
<a name="API_invoicing_ListProcurementPortalPreferences"></a>

 * **This feature API is subject to changing at any time. For more information, see the [AWS Service Terms](https://aws.amazon.com/service-terms/) (Betas and Previews).** *

Retrieves a list of procurement portal preferences associated with the AWS account.

## Request Syntax
<a name="API_invoicing_ListProcurementPortalPreferences_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_invoicing_ListProcurementPortalPreferences_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_invoicing_ListProcurementPortalPreferences_RequestSyntax) **   <a name="awscostmanagement-invoicing_ListProcurementPortalPreferences-request-MaxResults"></a>
The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned NextToken value.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_invoicing_ListProcurementPortalPreferences_RequestSyntax) **   <a name="awscostmanagement-invoicing_ListProcurementPortalPreferences-request-NextToken"></a>
The token for the next set of results. (You received this token from a previous call.)
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `\S+`
Required: No

## Response Syntax
<a name="API_invoicing_ListProcurementPortalPreferences_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "ProcurementPortalPreferences": [
      {
         "AwsAccountId": "string",
         "BuyerDomain": "string",
         "BuyerIdentifier": "string",
         "CreateDate": number,
         "EinvoiceDeliveryEnabled": boolean,
         "EinvoiceDeliveryPreferenceStatus": "string",
         "EinvoiceDeliveryPreferenceStatusReason": "string",
         "LastUpdateDate": number,
         "ProcurementPortalName": "string",
         "ProcurementPortalPreferenceArn": "string",
         "PurchaseOrderRetrievalEnabled": boolean,
         "PurchaseOrderRetrievalPreferenceStatus": "string",
         "PurchaseOrderRetrievalPreferenceStatusReason": "string",
         "Selector": {
            "InvoiceUnitArns": [ "string" ],
            "SellerOfRecords": [ "string" ]
         },
         "SupplierDomain": "string",
         "SupplierIdentifier": "string",
         "Version": number
      }
   ]
}
```

## Response Elements
<a name="API_invoicing_ListProcurementPortalPreferences_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_invoicing_ListProcurementPortalPreferences_ResponseSyntax) **   <a name="awscostmanagement-invoicing_ListProcurementPortalPreferences-response-NextToken"></a>
The token to use to retrieve the next set of results, or null if there are no more results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `\S+`

 ** [ProcurementPortalPreferences](#API_invoicing_ListProcurementPortalPreferences_ResponseSyntax) **   <a name="awscostmanagement-invoicing_ListProcurementPortalPreferences-response-ProcurementPortalPreferences"></a>
The list of procurement portal preferences associated with the AWS account.
Type: Array of [ProcurementPortalPreferenceSummary](API_invoicing_ProcurementPortalPreferenceSummary.md) objects

## Errors
<a name="API_invoicing_ListProcurementPortalPreferences_Errors"></a>

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
<a name="API_invoicing_ListProcurementPortalPreferences_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/invoicing-2024-12-01/ListProcurementPortalPreferences)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/invoicing-2024-12-01/ListProcurementPortalPreferences)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/invoicing-2024-12-01/ListProcurementPortalPreferences)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/invoicing-2024-12-01/ListProcurementPortalPreferences)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/invoicing-2024-12-01/ListProcurementPortalPreferences)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/invoicing-2024-12-01/ListProcurementPortalPreferences)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/invoicing-2024-12-01/ListProcurementPortalPreferences)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/invoicing-2024-12-01/ListProcurementPortalPreferences)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/invoicing-2024-12-01/ListProcurementPortalPreferences)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/invoicing-2024-12-01/ListProcurementPortalPreferences)
