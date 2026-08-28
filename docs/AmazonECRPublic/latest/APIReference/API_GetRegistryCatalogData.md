---
source_url: https://docs.aws.amazon.com/AmazonECRPublic/latest/APIReference/API_GetRegistryCatalogData.html
---

# GetRegistryCatalogData
<a name="API_GetRegistryCatalogData"></a>

Retrieves catalog metadata for a public registry.

## Response Syntax
<a name="API_GetRegistryCatalogData_ResponseSyntax"></a>

```
{
   "registryCatalogData": {
      "displayName": "string"
   }
}
```

## Response Elements
<a name="API_GetRegistryCatalogData_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [registryCatalogData](#API_GetRegistryCatalogData_ResponseSyntax) **   <a name="ecrpublic-GetRegistryCatalogData-response-registryCatalogData"></a>
The catalog metadata for the public registry.
Type: [RegistryCatalogData](API_RegistryCatalogData.md) object

## Errors
<a name="API_GetRegistryCatalogData_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ServerException **
These errors are usually caused by a server-side issue.
HTTP Status Code: 500

 ** UnsupportedCommandException **
The action isn't supported in this Region.
HTTP Status Code: 400

## See Also
<a name="API_GetRegistryCatalogData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ecr-public-2020-10-30/GetRegistryCatalogData)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ecr-public-2020-10-30/GetRegistryCatalogData)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecr-public-2020-10-30/GetRegistryCatalogData)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ecr-public-2020-10-30/GetRegistryCatalogData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-public-2020-10-30/GetRegistryCatalogData)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ecr-public-2020-10-30/GetRegistryCatalogData)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ecr-public-2020-10-30/GetRegistryCatalogData)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ecr-public-2020-10-30/GetRegistryCatalogData)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ecr-public-2020-10-30/GetRegistryCatalogData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecr-public-2020-10-30/GetRegistryCatalogData)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ECR. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECRPublic` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
