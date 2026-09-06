---
source_url: https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_DescribePullThroughCacheRules.html
---

# DescribePullThroughCacheRules
<a name="API_DescribePullThroughCacheRules"></a>

Returns the pull through cache rules for a registry.

## Request Syntax
<a name="API_DescribePullThroughCacheRules_RequestSyntax"></a>

```
{
   "ecrRepositoryPrefixes": [ "{{string}}" ],
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "registryId": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribePullThroughCacheRules_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ecrRepositoryPrefixes](#API_DescribePullThroughCacheRules_RequestSyntax) **   <a name="ECR-DescribePullThroughCacheRules-request-ecrRepositoryPrefixes"></a>
The Amazon ECR repository prefixes associated with the pull through cache rules to return. If no repository prefix value is specified, all pull through cache rules are returned.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Length Constraints: Minimum length of 2. Maximum length of 30.
Pattern: `^([a-z0-9]+((\.|_|__|-+)[a-z0-9]+)*(\/[a-z0-9]+((\.|_|__|-+)[a-z0-9]+)*)*\/?|ROOT)$`
Required: No

 ** [maxResults](#API_DescribePullThroughCacheRules_RequestSyntax) **   <a name="ECR-DescribePullThroughCacheRules-request-maxResults"></a>
The maximum number of pull through cache rules returned by `DescribePullThroughCacheRulesRequest` in paginated output. When this parameter is used, `DescribePullThroughCacheRulesRequest` only returns `maxResults` results in a single page along with a `nextToken` response element. The remaining results of the initial request can be seen by sending another `DescribePullThroughCacheRulesRequest` request with the returned `nextToken` value. This value can be between 1 and 1000. If this parameter is not used, then `DescribePullThroughCacheRulesRequest` returns up to 100 results and a `nextToken` value, if applicable.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [nextToken](#API_DescribePullThroughCacheRules_RequestSyntax) **   <a name="ECR-DescribePullThroughCacheRules-request-nextToken"></a>
The `nextToken` value returned from a previous paginated `DescribePullThroughCacheRulesRequest` request where `maxResults` was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the `nextToken` value. This value is null when there are no more results to return.
Type: String
Required: No

 ** [registryId](#API_DescribePullThroughCacheRules_RequestSyntax) **   <a name="ECR-DescribePullThroughCacheRules-request-registryId"></a>
The AWS account ID associated with the registry to return the pull through cache rules for. If you do not specify a registry, the default registry is assumed.
Type: String
Pattern: `[0-9]{12}`
Required: No

## Response Syntax
<a name="API_DescribePullThroughCacheRules_ResponseSyntax"></a>

```
{
   "nextToken": "string",
   "pullThroughCacheRules": [
      {
         "createdAt": number,
         "credentialArn": "string",
         "customRoleArn": "string",
         "ecrRepositoryPrefix": "string",
         "registryId": "string",
         "updatedAt": number,
         "upstreamRegistry": "string",
         "upstreamRegistryUrl": "string",
         "upstreamRepositoryPrefix": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribePullThroughCacheRules_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_DescribePullThroughCacheRules_ResponseSyntax) **   <a name="ECR-DescribePullThroughCacheRules-response-nextToken"></a>
The `nextToken` value to include in a future `DescribePullThroughCacheRulesRequest` request. When the results of a `DescribePullThroughCacheRulesRequest` request exceed `maxResults`, this value can be used to retrieve the next page of results. This value is null when there are no more results to return.
Type: String

 ** [pullThroughCacheRules](#API_DescribePullThroughCacheRules_ResponseSyntax) **   <a name="ECR-DescribePullThroughCacheRules-response-pullThroughCacheRules"></a>
The details of the pull through cache rules.
Type: Array of [PullThroughCacheRule](API_PullThroughCacheRule.md) objects

## Errors
<a name="API_DescribePullThroughCacheRules_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterException **
The specified parameter is invalid. Review the available parameters for the API request.
 ** message **
The error message associated with the exception.
HTTP Status Code: 400

 ** PullThroughCacheRuleNotFoundException **
The pull through cache rule was not found. Specify a valid pull through cache rule and try again.
HTTP Status Code: 400

 ** ServerException **
These errors are usually caused by a server-side issue.
 ** message **
The error message associated with the exception.
HTTP Status Code: 500

 ** ValidationException **
There was an exception validating this request.
HTTP Status Code: 400

## See Also
<a name="API_DescribePullThroughCacheRules_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ecr-2015-09-21/DescribePullThroughCacheRules)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ecr-2015-09-21/DescribePullThroughCacheRules)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecr-2015-09-21/DescribePullThroughCacheRules)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ecr-2015-09-21/DescribePullThroughCacheRules)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-2015-09-21/DescribePullThroughCacheRules)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ecr-2015-09-21/DescribePullThroughCacheRules)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ecr-2015-09-21/DescribePullThroughCacheRules)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ecr-2015-09-21/DescribePullThroughCacheRules)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ecr-2015-09-21/DescribePullThroughCacheRules)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecr-2015-09-21/DescribePullThroughCacheRules)
