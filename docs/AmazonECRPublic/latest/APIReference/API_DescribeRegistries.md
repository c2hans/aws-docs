---
source_url: https://docs.aws.amazon.com/AmazonECRPublic/latest/APIReference/API_DescribeRegistries.html
---

# DescribeRegistries
<a name="API_DescribeRegistries"></a>

Returns details for a public registry.

## Request Syntax
<a name="API_DescribeRegistries_RequestSyntax"></a>

```
{
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeRegistries_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [maxResults](#API_DescribeRegistries_RequestSyntax) **   <a name="ecrpublic-DescribeRegistries-request-maxResults"></a>
The maximum number of repository results that's returned by `DescribeRegistries` in paginated output. When this parameter is used, `DescribeRegistries` only returns `maxResults` results in a single page along with a `nextToken` response element. The remaining results of the initial request can be seen by sending another `DescribeRegistries` request with the returned `nextToken` value. This value can be between 1 and 1000. If this parameter isn't used, then `DescribeRegistries` returns up to 100 results and a `nextToken` value, if applicable.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [nextToken](#API_DescribeRegistries_RequestSyntax) **   <a name="ecrpublic-DescribeRegistries-request-nextToken"></a>
The `nextToken` value that's returned from a previous paginated `DescribeRegistries` request where `maxResults` was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the `nextToken` value. If there are no more results to return, this value is `null`.
This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.
Type: String
Required: No

## Response Syntax
<a name="API_DescribeRegistries_ResponseSyntax"></a>

```
{
   "nextToken": "string",
   "registries": [
      {
         "aliases": [
            {
               "defaultRegistryAlias": boolean,
               "name": "string",
               "primaryRegistryAlias": boolean,
               "status": "string"
            }
         ],
         "registryArn": "string",
         "registryId": "string",
         "registryUri": "string",
         "verified": boolean
      }
   ]
}
```

## Response Elements
<a name="API_DescribeRegistries_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_DescribeRegistries_ResponseSyntax) **   <a name="ecrpublic-DescribeRegistries-response-nextToken"></a>
The `nextToken` value to include in a future `DescribeRepositories` request. If the results of a `DescribeRepositories` request exceed `maxResults`, you can use this value to retrieve the next page of results. If there are no more results, this value is `null`.
Type: String

 ** [registries](#API_DescribeRegistries_ResponseSyntax) **   <a name="ecrpublic-DescribeRegistries-response-registries"></a>
An object that contains the details for a public registry.
Type: Array of [Registry](API_Registry.md) objects

## Errors
<a name="API_DescribeRegistries_Errors"></a>

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
<a name="API_DescribeRegistries_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ecr-public-2020-10-30/DescribeRegistries)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ecr-public-2020-10-30/DescribeRegistries)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecr-public-2020-10-30/DescribeRegistries)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ecr-public-2020-10-30/DescribeRegistries)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-public-2020-10-30/DescribeRegistries)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ecr-public-2020-10-30/DescribeRegistries)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ecr-public-2020-10-30/DescribeRegistries)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ecr-public-2020-10-30/DescribeRegistries)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ecr-public-2020-10-30/DescribeRegistries)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecr-public-2020-10-30/DescribeRegistries)
