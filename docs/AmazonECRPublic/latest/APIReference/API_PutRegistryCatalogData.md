---
source_url: https://docs.aws.amazon.com/AmazonECRPublic/latest/APIReference/API_PutRegistryCatalogData.html
---

# PutRegistryCatalogData
<a name="API_PutRegistryCatalogData"></a>

Create or update the catalog data for a public registry.

## Request Syntax
<a name="API_PutRegistryCatalogData_RequestSyntax"></a>

```
{
   "displayName": "{{string}}"
}
```

## Request Parameters
<a name="API_PutRegistryCatalogData_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [displayName](#API_PutRegistryCatalogData_RequestSyntax) **   <a name="ecrpublic-PutRegistryCatalogData-request-displayName"></a>
The display name for a public registry. The display name is shown as the repository author in the Amazon ECR Public Gallery.
The registry display name is only publicly visible in the Amazon ECR Public Gallery for verified accounts.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100.
Required: No

## Response Syntax
<a name="API_PutRegistryCatalogData_ResponseSyntax"></a>

```
{
   "registryCatalogData": {
      "displayName": "string"
   }
}
```

## Response Elements
<a name="API_PutRegistryCatalogData_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [registryCatalogData](#API_PutRegistryCatalogData_ResponseSyntax) **   <a name="ecrpublic-PutRegistryCatalogData-response-registryCatalogData"></a>
The catalog data for the public registry.
Type: [RegistryCatalogData](API_RegistryCatalogData.md) object

## Errors
<a name="API_PutRegistryCatalogData_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterException **
The specified parameter is invalid. Review the available parameters for the API request.
HTTP Status Code: 400

 ** ServerException **
These errors are usually caused by a server-side issue.
HTTP Status Code: 500

 ** UnsupportedCommandException **
The action isn't supported in this Region.
HTTP Status Code: 400

## See Also
<a name="API_PutRegistryCatalogData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ecr-public-2020-10-30/PutRegistryCatalogData)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ecr-public-2020-10-30/PutRegistryCatalogData)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecr-public-2020-10-30/PutRegistryCatalogData)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ecr-public-2020-10-30/PutRegistryCatalogData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-public-2020-10-30/PutRegistryCatalogData)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ecr-public-2020-10-30/PutRegistryCatalogData)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ecr-public-2020-10-30/PutRegistryCatalogData)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ecr-public-2020-10-30/PutRegistryCatalogData)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ecr-public-2020-10-30/PutRegistryCatalogData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecr-public-2020-10-30/PutRegistryCatalogData)
