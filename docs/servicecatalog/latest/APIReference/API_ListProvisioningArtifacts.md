---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_ListProvisioningArtifacts.html
---

# ListProvisioningArtifacts
<a name="API_ListProvisioningArtifacts"></a>

Lists all provisioning artifacts (also known as versions) for the specified product.

## Request Syntax
<a name="API_ListProvisioningArtifacts_RequestSyntax"></a>

```
{
   "AcceptLanguage": "{{string}}",
   "ProductId": "{{string}}"
}
```

## Request Parameters
<a name="API_ListProvisioningArtifacts_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [AcceptLanguage](#API_ListProvisioningArtifacts_RequestSyntax) **   <a name="servicecatalog-ListProvisioningArtifacts-request-AcceptLanguage"></a>
The language code.
+  `jp` - Japanese
+  `zh` - Chinese
Type: String
Length Constraints: Maximum length of 100.
Required: No

 ** [ProductId](#API_ListProvisioningArtifacts_RequestSyntax) **   <a name="servicecatalog-ListProvisioningArtifacts-request-ProductId"></a>
The product identifier.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[a-zA-Z0-9_\-]*`
Required: Yes

## Response Syntax
<a name="API_ListProvisioningArtifacts_ResponseSyntax"></a>

```
{
   "NextPageToken": "string",
   "ProvisioningArtifactDetails": [
      {
         "Active": boolean,
         "CreatedTime": number,
         "Description": "string",
         "Guidance": "string",
         "Id": "string",
         "Name": "string",
         "SourceRevision": "string",
         "Type": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListProvisioningArtifacts_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextPageToken](#API_ListProvisioningArtifacts_ResponseSyntax) **   <a name="servicecatalog-ListProvisioningArtifacts-response-NextPageToken"></a>
The page token to use to retrieve the next set of results. If there are no additional results, this value is null.
Type: String
Length Constraints: Maximum length of 2024.
Pattern: `[\u0009\u000a\u000d\u0020-\uD7FF\uE000-\uFFFD]*`

 ** [ProvisioningArtifactDetails](#API_ListProvisioningArtifacts_ResponseSyntax) **   <a name="servicecatalog-ListProvisioningArtifacts-response-ProvisioningArtifactDetails"></a>
Information about the provisioning artifacts.
Type: Array of [ProvisioningArtifactDetail](API_ProvisioningArtifactDetail.md) objects

## Errors
<a name="API_ListProvisioningArtifacts_Errors"></a>

 ** InvalidParametersException **
One or more parameters provided to the operation are not valid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
HTTP Status Code: 400

## See Also
<a name="API_ListProvisioningArtifacts_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/servicecatalog-2015-12-10/ListProvisioningArtifacts)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/servicecatalog-2015-12-10/ListProvisioningArtifacts)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicecatalog-2015-12-10/ListProvisioningArtifacts)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/servicecatalog-2015-12-10/ListProvisioningArtifacts)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicecatalog-2015-12-10/ListProvisioningArtifacts)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/ListProvisioningArtifacts)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/servicecatalog-2015-12-10/ListProvisioningArtifacts)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/servicecatalog-2015-12-10/ListProvisioningArtifacts)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/servicecatalog-2015-12-10/ListProvisioningArtifacts)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicecatalog-2015-12-10/ListProvisioningArtifacts)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Service Catalog. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query servicecatalog` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
