---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_taxSettings_PutTaxInheritance.html
---

# PutTaxInheritance
<a name="API_taxSettings_PutTaxInheritance"></a>

The updated tax inheritance status.

## Request Syntax
<a name="API_taxSettings_PutTaxInheritance_RequestSyntax"></a>

```
POST /PutTaxInheritance HTTP/1.1
Content-type: application/json

{
   "heritageStatus": "{{string}}"
}
```

## URI Request Parameters
<a name="API_taxSettings_PutTaxInheritance_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_taxSettings_PutTaxInheritance_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [heritageStatus](#API_taxSettings_PutTaxInheritance_RequestSyntax) **   <a name="awscostmanagement-taxSettings_PutTaxInheritance-request-heritageStatus"></a>
The tax inheritance status.
Type: String
Valid Values: `OptIn | OptOut`
Required: No

## Response Syntax
<a name="API_taxSettings_PutTaxInheritance_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_taxSettings_PutTaxInheritance_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_taxSettings_PutTaxInheritance_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
The exception when the input is creating conflict with the given state.
 ** errorCode **
409
HTTP Status Code: 409

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
<a name="API_taxSettings_PutTaxInheritance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/taxsettings-2018-05-10/PutTaxInheritance)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/taxsettings-2018-05-10/PutTaxInheritance)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/taxsettings-2018-05-10/PutTaxInheritance)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/taxsettings-2018-05-10/PutTaxInheritance)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/taxsettings-2018-05-10/PutTaxInheritance)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/taxsettings-2018-05-10/PutTaxInheritance)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/taxsettings-2018-05-10/PutTaxInheritance)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/taxsettings-2018-05-10/PutTaxInheritance)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/taxsettings-2018-05-10/PutTaxInheritance)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/taxsettings-2018-05-10/PutTaxInheritance)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
