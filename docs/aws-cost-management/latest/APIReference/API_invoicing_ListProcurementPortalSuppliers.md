---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_invoicing_ListProcurementPortalSuppliers.html
---

# ListProcurementPortalSuppliers
<a name="API_invoicing_ListProcurementPortalSuppliers"></a>

Returns the suppliers configured for a specified procurement portal, including supplier identifiers and associated metadata. For faster, more reliable responses, use pagination.

## Request Syntax
<a name="API_invoicing_ListProcurementPortalSuppliers_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "PortalIdentifier": "{{string}}"
}
```

## Request Parameters
<a name="API_invoicing_ListProcurementPortalSuppliers_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_invoicing_ListProcurementPortalSuppliers_RequestSyntax) **   <a name="awscostmanagement-invoicing_ListProcurementPortalSuppliers-request-MaxResults"></a>
The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned NextToken value. Default is 100.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_invoicing_ListProcurementPortalSuppliers_RequestSyntax) **   <a name="awscostmanagement-invoicing_ListProcurementPortalSuppliers-request-NextToken"></a>
The token for the next set of results. You received this token from a previous call.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `\S+`
Required: No

 ** [PortalIdentifier](#API_invoicing_ListProcurementPortalSuppliers_RequestSyntax) **   <a name="awscostmanagement-invoicing_ListProcurementPortalSuppliers-request-PortalIdentifier"></a>
The unique identifier of the procurement portal for which to list suppliers. Use the `PortalIdentifier` value returned by `ListProcurementPortals`.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

## Response Syntax
<a name="API_invoicing_ListProcurementPortalSuppliers_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "ProcurementPortalSuppliers": [
      {
         "CountryCode": "string",
         "Environment": "string",
         "SellerOfRecord": "string",
         "SupplierIdentifier": "string"
      }
   ]
}
```

## Response Elements
<a name="API_invoicing_ListProcurementPortalSuppliers_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_invoicing_ListProcurementPortalSuppliers_ResponseSyntax) **   <a name="awscostmanagement-invoicing_ListProcurementPortalSuppliers-response-NextToken"></a>
The token to use to retrieve the next set of results, or null if there are no more results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `\S+`

 ** [ProcurementPortalSuppliers](#API_invoicing_ListProcurementPortalSuppliers_ResponseSyntax) **   <a name="awscostmanagement-invoicing_ListProcurementPortalSuppliers-response-ProcurementPortalSuppliers"></a>
The list of suppliers configured for the specified procurement portal.
Type: Array of [ProcurementPortalSupplier](API_invoicing_ProcurementPortalSupplier.md) objects

## Errors
<a name="API_invoicing_ListProcurementPortalSuppliers_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient access to perform this action.
 ** resourceName **
You don't have sufficient access to perform this action.
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
<a name="API_invoicing_ListProcurementPortalSuppliers_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/invoicing-2024-12-01/ListProcurementPortalSuppliers)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/invoicing-2024-12-01/ListProcurementPortalSuppliers)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/invoicing-2024-12-01/ListProcurementPortalSuppliers)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/invoicing-2024-12-01/ListProcurementPortalSuppliers)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/invoicing-2024-12-01/ListProcurementPortalSuppliers)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/invoicing-2024-12-01/ListProcurementPortalSuppliers)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/invoicing-2024-12-01/ListProcurementPortalSuppliers)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/invoicing-2024-12-01/ListProcurementPortalSuppliers)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/invoicing-2024-12-01/ListProcurementPortalSuppliers)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/invoicing-2024-12-01/ListProcurementPortalSuppliers)
