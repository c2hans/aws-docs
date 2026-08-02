---
source_url: https://docs.aws.amazon.com/AmazonECRPublic/latest/APIReference/API_DescribeRepositories.html
---

# DescribeRepositories
<a name="API_DescribeRepositories"></a>

Describes repositories that are in a public registry.

## Request Syntax
<a name="API_DescribeRepositories_RequestSyntax"></a>

```
{
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "registryId": "{{string}}",
   "repositoryNames": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_DescribeRepositories_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [maxResults](#API_DescribeRepositories_RequestSyntax) **   <a name="ecrpublic-DescribeRepositories-request-maxResults"></a>
The maximum number of repository results that's returned by `DescribeRepositories` in paginated output. When this parameter is used, `DescribeRepositories` only returns `maxResults` results in a single page along with a `nextToken` response element. You can see the remaining results of the initial request by sending another `DescribeRepositories` request with the returned `nextToken` value. This value can be between 1 and 1000. If this parameter isn't used, then `DescribeRepositories` returns up to 100 results and a `nextToken` value, if applicable. If you specify repositories with `repositoryNames`, you can't use this option.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [nextToken](#API_DescribeRepositories_RequestSyntax) **   <a name="ecrpublic-DescribeRepositories-request-nextToken"></a>
The `nextToken` value that's returned from a previous paginated `DescribeRepositories` request where `maxResults` was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the `nextToken` value. If there are no more results to return, this value is `null`. If you specify repositories with `repositoryNames`, you can't use this option.
This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.
Type: String
Required: No

 ** [registryId](#API_DescribeRepositories_RequestSyntax) **   <a name="ecrpublic-DescribeRepositories-request-registryId"></a>
The AWS account ID that's associated with the registry that contains the repositories to be described. If you do not specify a registry, the default public registry is assumed.
Type: String
Pattern: `[0-9]{12}`
Required: No

 ** [repositoryNames](#API_DescribeRepositories_RequestSyntax) **   <a name="ecrpublic-DescribeRepositories-request-repositoryNames"></a>
A list of repositories to describe. If this parameter is omitted, then all repositories in a registry are described.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Length Constraints: Minimum length of 2. Maximum length of 205.
Pattern: `(?:[a-z0-9]+(?:[._-][a-z0-9]+)*/)*[a-z0-9]+(?:[._-][a-z0-9]+)*`
Required: No

## Response Syntax
<a name="API_DescribeRepositories_ResponseSyntax"></a>

```
{
   "nextToken": "string",
   "repositories": [
      {
         "createdAt": number,
         "registryId": "string",
         "repositoryArn": "string",
         "repositoryName": "string",
         "repositoryUri": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeRepositories_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_DescribeRepositories_ResponseSyntax) **   <a name="ecrpublic-DescribeRepositories-response-nextToken"></a>
The `nextToken` value to include in a future `DescribeRepositories` request. When the results of a `DescribeRepositories` request exceed `maxResults`, this value can be used to retrieve the next page of results. If there are no more results to return, this value is `null`.
Type: String

 ** [repositories](#API_DescribeRepositories_ResponseSyntax) **   <a name="ecrpublic-DescribeRepositories-response-repositories"></a>
A list of repository objects corresponding to valid repositories.
Type: Array of [Repository](API_Repository.md) objects

## Errors
<a name="API_DescribeRepositories_Errors"></a>

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
<a name="API_DescribeRepositories_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ecr-public-2020-10-30/DescribeRepositories)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ecr-public-2020-10-30/DescribeRepositories)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecr-public-2020-10-30/DescribeRepositories)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ecr-public-2020-10-30/DescribeRepositories)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-public-2020-10-30/DescribeRepositories)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ecr-public-2020-10-30/DescribeRepositories)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ecr-public-2020-10-30/DescribeRepositories)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ecr-public-2020-10-30/DescribeRepositories)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ecr-public-2020-10-30/DescribeRepositories)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecr-public-2020-10-30/DescribeRepositories)
