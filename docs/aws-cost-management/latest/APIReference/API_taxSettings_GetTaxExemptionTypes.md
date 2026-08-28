---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_taxSettings_GetTaxExemptionTypes.html
---

# GetTaxExemptionTypes
<a name="API_taxSettings_GetTaxExemptionTypes"></a>

Get supported tax exemption types. The IAM action is `tax:GetExemptions`.

## Request Syntax
<a name="API_taxSettings_GetTaxExemptionTypes_RequestSyntax"></a>

```
POST /GetTaxExemptionTypes HTTP/1.1
```

## URI Request Parameters
<a name="API_taxSettings_GetTaxExemptionTypes_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_taxSettings_GetTaxExemptionTypes_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_taxSettings_GetTaxExemptionTypes_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "taxExemptionTypes": [
      {
         "applicableJurisdictions": [
            {
               "country": "string",
               "state": "string"
            }
         ],
         "description": "string",
         "displayName": "string"
      }
   ]
}
```

## Response Elements
<a name="API_taxSettings_GetTaxExemptionTypes_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [taxExemptionTypes](#API_taxSettings_GetTaxExemptionTypes_ResponseSyntax) **   <a name="awscostmanagement-taxSettings_GetTaxExemptionTypes-response-taxExemptionTypes"></a>
The supported types of tax exemptions.
Type: Array of [TaxExemptionType](API_taxSettings_TaxExemptionType.md) objects

## Errors
<a name="API_taxSettings_GetTaxExemptionTypes_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
The exception thrown when an unexpected error occurs when processing a request.
 ** errorCode **
500
HTTP Status Code: 500

 ** ResourceNotFoundException **
The exception thrown when the input doesn't have a resource associated to it.
 ** errorCode **
404
HTTP Status Code: 404

 ** ValidationException **
The exception when the input doesn't pass validation for at least one of the input parameters.
 ** errorCode **
400
 ** fieldList **
400
HTTP Status Code: 400

## See Also
<a name="API_taxSettings_GetTaxExemptionTypes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/taxsettings-2018-05-10/GetTaxExemptionTypes)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/taxsettings-2018-05-10/GetTaxExemptionTypes)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/taxsettings-2018-05-10/GetTaxExemptionTypes)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/taxsettings-2018-05-10/GetTaxExemptionTypes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/taxsettings-2018-05-10/GetTaxExemptionTypes)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/taxsettings-2018-05-10/GetTaxExemptionTypes)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/taxsettings-2018-05-10/GetTaxExemptionTypes)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/taxsettings-2018-05-10/GetTaxExemptionTypes)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/taxsettings-2018-05-10/GetTaxExemptionTypes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/taxsettings-2018-05-10/GetTaxExemptionTypes)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
