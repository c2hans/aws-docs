---
source_url: https://docs.aws.amazon.com/AmazonECRPublic/latest/APIReference/API_GetRepositoryCatalogData.html
---

# GetRepositoryCatalogData
<a name="API_GetRepositoryCatalogData"></a>

Retrieve catalog metadata for a repository in a public registry. This metadata is displayed publicly in the Amazon ECR Public Gallery.

## Request Syntax
<a name="API_GetRepositoryCatalogData_RequestSyntax"></a>

```
{
   "registryId": "{{string}}",
   "repositoryName": "{{string}}"
}
```

## Request Parameters
<a name="API_GetRepositoryCatalogData_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [registryId](#API_GetRepositoryCatalogData_RequestSyntax) **   <a name="ecrpublic-GetRepositoryCatalogData-request-registryId"></a>
The AWS account ID that's associated with the registry that contains the repositories to be described. If you do not specify a registry, the default public registry is assumed.
Type: String
Pattern: `[0-9]{12}`
Required: No

 ** [repositoryName](#API_GetRepositoryCatalogData_RequestSyntax) **   <a name="ecrpublic-GetRepositoryCatalogData-request-repositoryName"></a>
The name of the repository to retrieve the catalog metadata for.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 205.
Pattern: `(?:[a-z0-9]+(?:[._-][a-z0-9]+)*/)*[a-z0-9]+(?:[._-][a-z0-9]+)*`
Required: Yes

## Response Syntax
<a name="API_GetRepositoryCatalogData_ResponseSyntax"></a>

```
{
   "catalogData": {
      "aboutText": "string",
      "architectures": [ "string" ],
      "description": "string",
      "logoUrl": "string",
      "marketplaceCertified": boolean,
      "operatingSystems": [ "string" ],
      "usageText": "string"
   }
}
```

## Response Elements
<a name="API_GetRepositoryCatalogData_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [catalogData](#API_GetRepositoryCatalogData_ResponseSyntax) **   <a name="ecrpublic-GetRepositoryCatalogData-response-catalogData"></a>
The catalog metadata for the repository.
Type: [RepositoryCatalogData](API_RepositoryCatalogData.md) object

## Errors
<a name="API_GetRepositoryCatalogData_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterException **
The specified parameter is invalid. Review the available parameters for the API request.
HTTP Status Code: 400

 ** RepositoryCatalogDataNotFoundException **
The repository catalog data doesn't exist.
HTTP Status Code: 400

 ** RepositoryNotFoundException **
The specified repository can't be found. Check the spelling of the specified repository and ensure that you're performing operations on the correct registry.
HTTP Status Code: 400

 ** ServerException **
These errors are usually caused by a server-side issue.
HTTP Status Code: 500

 ** UnsupportedCommandException **
The action isn't supported in this Region.
HTTP Status Code: 400

## See Also
<a name="API_GetRepositoryCatalogData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ecr-public-2020-10-30/GetRepositoryCatalogData)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ecr-public-2020-10-30/GetRepositoryCatalogData)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecr-public-2020-10-30/GetRepositoryCatalogData)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ecr-public-2020-10-30/GetRepositoryCatalogData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-public-2020-10-30/GetRepositoryCatalogData)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ecr-public-2020-10-30/GetRepositoryCatalogData)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ecr-public-2020-10-30/GetRepositoryCatalogData)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ecr-public-2020-10-30/GetRepositoryCatalogData)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ecr-public-2020-10-30/GetRepositoryCatalogData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecr-public-2020-10-30/GetRepositoryCatalogData)
