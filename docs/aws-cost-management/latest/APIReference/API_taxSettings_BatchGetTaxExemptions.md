---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_taxSettings_BatchGetTaxExemptions.html
---

# BatchGetTaxExemptions
<a name="API_taxSettings_BatchGetTaxExemptions"></a>

Get the active tax exemptions for a given list of accounts. The IAM action is `tax:GetExemptions`.

## Request Syntax
<a name="API_taxSettings_BatchGetTaxExemptions_RequestSyntax"></a>

```
POST /BatchGetTaxExemptions HTTP/1.1
Content-type: application/json

{
   "accountIds": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_taxSettings_BatchGetTaxExemptions_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_taxSettings_BatchGetTaxExemptions_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [accountIds](#API_taxSettings_BatchGetTaxExemptions_RequestSyntax) **   <a name="awscostmanagement-taxSettings_BatchGetTaxExemptions-request-accountIds"></a>
 List of unique account identifiers.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Length Constraints: Fixed length of 12.
Pattern: `\d+`
Required: Yes

## Response Syntax
<a name="API_taxSettings_BatchGetTaxExemptions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "failedAccounts": [ "string" ],
   "taxExemptionDetailsMap": {
      "string" : {
         "heritageObtainedDetails": boolean,
         "heritageObtainedParentEntity": "string",
         "heritageObtainedReason": "string",
         "taxExemptions": [
            {
               "authority": {
                  "country": "string",
                  "state": "string"
               },
               "effectiveDate": number,
               "expirationDate": number,
               "status": "string",
               "systemEffectiveDate": number,
               "taxExemptionType": {
                  "applicableJurisdictions": [
                     {
                        "country": "string",
                        "state": "string"
                     }
                  ],
                  "description": "string",
                  "displayName": "string"
               }
            }
         ]
      }
   }
}
```

## Response Elements
<a name="API_taxSettings_BatchGetTaxExemptions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [failedAccounts](#API_taxSettings_BatchGetTaxExemptions_ResponseSyntax) **   <a name="awscostmanagement-taxSettings_BatchGetTaxExemptions-response-failedAccounts"></a>
The list of accounts that failed to get tax exemptions.
Type: Array of strings
Length Constraints: Fixed length of 12.
Pattern: `\d+`

 ** [taxExemptionDetailsMap](#API_taxSettings_BatchGetTaxExemptions_ResponseSyntax) **   <a name="awscostmanagement-taxSettings_BatchGetTaxExemptions-response-taxExemptionDetailsMap"></a>
The tax exemption details map of accountId and tax exemption details.
Type: String to [TaxExemptionDetails](API_taxSettings_TaxExemptionDetails.md) object map
Key Length Constraints: Fixed length of 12.
Key Pattern: `\d+`

## Errors
<a name="API_taxSettings_BatchGetTaxExemptions_Errors"></a>

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
<a name="API_taxSettings_BatchGetTaxExemptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/taxsettings-2018-05-10/BatchGetTaxExemptions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/taxsettings-2018-05-10/BatchGetTaxExemptions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/taxsettings-2018-05-10/BatchGetTaxExemptions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/taxsettings-2018-05-10/BatchGetTaxExemptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/taxsettings-2018-05-10/BatchGetTaxExemptions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/taxsettings-2018-05-10/BatchGetTaxExemptions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/taxsettings-2018-05-10/BatchGetTaxExemptions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/taxsettings-2018-05-10/BatchGetTaxExemptions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/taxsettings-2018-05-10/BatchGetTaxExemptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/taxsettings-2018-05-10/BatchGetTaxExemptions)
