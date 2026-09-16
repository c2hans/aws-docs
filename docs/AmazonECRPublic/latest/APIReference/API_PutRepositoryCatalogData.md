---
source_url: https://docs.aws.amazon.com/AmazonECRPublic/latest/APIReference/API_PutRepositoryCatalogData.html
---

# PutRepositoryCatalogData
<a name="API_PutRepositoryCatalogData"></a>

Creates or updates the catalog data for a repository in a public registry.

## Request Syntax
<a name="API_PutRepositoryCatalogData_RequestSyntax"></a>

```
{
   "catalogData": {
      "aboutText": "{{string}}",
      "architectures": [ "{{string}}" ],
      "description": "{{string}}",
      "logoImageBlob": {{blob}},
      "operatingSystems": [ "{{string}}" ],
      "usageText": "{{string}}"
   },
   "registryId": "{{string}}",
   "repositoryName": "{{string}}"
}
```

## Request Parameters
<a name="API_PutRepositoryCatalogData_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [catalogData](#API_PutRepositoryCatalogData_RequestSyntax) **   <a name="ecrpublic-PutRepositoryCatalogData-request-catalogData"></a>
An object containing the catalog data for a repository. This data is publicly visible in the Amazon ECR Public Gallery.
Type: [RepositoryCatalogDataInput](API_RepositoryCatalogDataInput.md) object
Required: Yes

 ** [registryId](#API_PutRepositoryCatalogData_RequestSyntax) **   <a name="ecrpublic-PutRepositoryCatalogData-request-registryId"></a>
The AWS account ID that's associated with the public registry the repository is in. If you do not specify a registry, the default public registry is assumed.
Type: String
Pattern: `[0-9]{12}`
Required: No

 ** [repositoryName](#API_PutRepositoryCatalogData_RequestSyntax) **   <a name="ecrpublic-PutRepositoryCatalogData-request-repositoryName"></a>
The name of the repository to create or update the catalog data for.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 205.
Pattern: `(?:[a-z0-9]+(?:[._-][a-z0-9]+)*/)*[a-z0-9]+(?:[._-][a-z0-9]+)*`
Required: Yes

## Response Syntax
<a name="API_PutRepositoryCatalogData_ResponseSyntax"></a>

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
<a name="API_PutRepositoryCatalogData_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [catalogData](#API_PutRepositoryCatalogData_ResponseSyntax) **   <a name="ecrpublic-PutRepositoryCatalogData-response-catalogData"></a>
The catalog data for the repository.
Type: [RepositoryCatalogData](API_RepositoryCatalogData.md) object

## Errors
<a name="API_PutRepositoryCatalogData_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterException **
The specified parameter is invalid. Review the available parameters for the API request.
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
<a name="API_PutRepositoryCatalogData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ecr-public-2020-10-30/PutRepositoryCatalogData)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ecr-public-2020-10-30/PutRepositoryCatalogData)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecr-public-2020-10-30/PutRepositoryCatalogData)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ecr-public-2020-10-30/PutRepositoryCatalogData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-public-2020-10-30/PutRepositoryCatalogData)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ecr-public-2020-10-30/PutRepositoryCatalogData)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ecr-public-2020-10-30/PutRepositoryCatalogData)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ecr-public-2020-10-30/PutRepositoryCatalogData)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ecr-public-2020-10-30/PutRepositoryCatalogData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecr-public-2020-10-30/PutRepositoryCatalogData)
