---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_invoicing_ListProcurementPortals.html
---

# ListProcurementPortals
<a name="API_invoicing_ListProcurementPortals"></a>

Returns the AWS-supported procurement portals for e-invoice delivery and purchase order retrieval. Each entry includes the portal identifier, name, and default feature configurations, which define the supported document and attachment types. For faster, more reliable responses, use pagination.

## Request Syntax
<a name="API_invoicing_ListProcurementPortals_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_invoicing_ListProcurementPortals_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_invoicing_ListProcurementPortals_RequestSyntax) **   <a name="awscostmanagement-invoicing_ListProcurementPortals-request-MaxResults"></a>
The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned NextToken value. Default is 100.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_invoicing_ListProcurementPortals_RequestSyntax) **   <a name="awscostmanagement-invoicing_ListProcurementPortals-request-NextToken"></a>
The token for the next set of results. You received this token from a previous call.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `\S+`
Required: No

## Response Syntax
<a name="API_invoicing_ListProcurementPortals_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "ProcurementPortals": [
      {
         "DefaultFeatureConfigurations": {
            "InvoiceConfiguration": {
               "AttachmentTypes": [ "string" ],
               "DocumentTypes": [ "string" ]
            }
         },
         "PortalDisplayName": "string",
         "PortalIdentifier": "string",
         "PortalName": "string"
      }
   ]
}
```

## Response Elements
<a name="API_invoicing_ListProcurementPortals_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_invoicing_ListProcurementPortals_ResponseSyntax) **   <a name="awscostmanagement-invoicing_ListProcurementPortals-response-NextToken"></a>
The token to use to retrieve the next set of results, or null if there are no more results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `\S+`

 ** [ProcurementPortals](#API_invoicing_ListProcurementPortals_ResponseSyntax) **   <a name="awscostmanagement-invoicing_ListProcurementPortals-response-ProcurementPortals"></a>
The list of procurement portals available for configuration.
Type: Array of [ProcurementPortal](API_invoicing_ProcurementPortal.md) objects

## Errors
<a name="API_invoicing_ListProcurementPortals_Errors"></a>

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
<a name="API_invoicing_ListProcurementPortals_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/invoicing-2024-12-01/ListProcurementPortals)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/invoicing-2024-12-01/ListProcurementPortals)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/invoicing-2024-12-01/ListProcurementPortals)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/invoicing-2024-12-01/ListProcurementPortals)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/invoicing-2024-12-01/ListProcurementPortals)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/invoicing-2024-12-01/ListProcurementPortals)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/invoicing-2024-12-01/ListProcurementPortals)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/invoicing-2024-12-01/ListProcurementPortals)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/invoicing-2024-12-01/ListProcurementPortals)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/invoicing-2024-12-01/ListProcurementPortals)
