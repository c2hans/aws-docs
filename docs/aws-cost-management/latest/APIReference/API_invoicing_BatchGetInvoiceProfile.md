---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_invoicing_BatchGetInvoiceProfile.html
---

# BatchGetInvoiceProfile
<a name="API_invoicing_BatchGetInvoiceProfile"></a>

This gets the invoice profile associated with a set of accounts. The accounts must be linked accounts under the requester management account organization.

## Request Syntax
<a name="API_invoicing_BatchGetInvoiceProfile_RequestSyntax"></a>

```
{
   "AccountIds": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_invoicing_BatchGetInvoiceProfile_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AccountIds](#API_invoicing_BatchGetInvoiceProfile_RequestSyntax) **   <a name="awscostmanagement-invoicing_BatchGetInvoiceProfile-request-AccountIds"></a>
Retrieves the corresponding invoice profile data for these account IDs.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 1000 items.
Pattern: `\d{12}`
Required: Yes

## Response Syntax
<a name="API_invoicing_BatchGetInvoiceProfile_ResponseSyntax"></a>

```
{
   "Profiles": [
      {
         "AccountId": "string",
         "Issuer": "string",
         "ReceiverAddress": {
            "AddressLine1": "string",
            "AddressLine2": "string",
            "AddressLine3": "string",
            "City": "string",
            "CompanyName": "string",
            "CountryCode": "string",
            "DistrictOrCounty": "string",
            "PostalCode": "string",
            "StateOrRegion": "string"
         },
         "ReceiverEmail": "string",
         "ReceiverName": "string",
         "TaxRegistrationNumber": "string"
      }
   ]
}
```

## Response Elements
<a name="API_invoicing_BatchGetInvoiceProfile_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Profiles](#API_invoicing_BatchGetInvoiceProfile_ResponseSyntax) **   <a name="awscostmanagement-invoicing_BatchGetInvoiceProfile-response-Profiles"></a>
 A list of invoice profiles corresponding to the requested accounts.
Type: Array of [InvoiceProfile](API_invoicing_InvoiceProfile.md) objects

## Errors
<a name="API_invoicing_BatchGetInvoiceProfile_Errors"></a>

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
<a name="API_invoicing_BatchGetInvoiceProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/invoicing-2024-12-01/BatchGetInvoiceProfile)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/invoicing-2024-12-01/BatchGetInvoiceProfile)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/invoicing-2024-12-01/BatchGetInvoiceProfile)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/invoicing-2024-12-01/BatchGetInvoiceProfile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/invoicing-2024-12-01/BatchGetInvoiceProfile)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/invoicing-2024-12-01/BatchGetInvoiceProfile)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/invoicing-2024-12-01/BatchGetInvoiceProfile)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/invoicing-2024-12-01/BatchGetInvoiceProfile)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/invoicing-2024-12-01/BatchGetInvoiceProfile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/invoicing-2024-12-01/BatchGetInvoiceProfile)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
