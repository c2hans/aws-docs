---
source_url: https://docs.aws.amazon.com/proton/latest/APIReference/API_ListRepositories.html
---

AWS has decided to discontinue AWS Proton, with support ending on October 7, 2026. New customers will not be able to sign up after October 7, 2025, but existing customers can continue to use the service until October 7, 2026.For more information, see [AWS Proton Service Deprecation and Migration Guide](https://docs.aws.amazon.com/proton/latest/userguide/proton-end-of-support.html).

# ListRepositories
<a name="API_ListRepositories"></a>

List linked repositories with detail data.

## Request Syntax
<a name="API_ListRepositories_RequestSyntax"></a>

```
{
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListRepositories_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [maxResults](#API_ListRepositories_RequestSyntax) **   <a name="proton-ListRepositories-request-maxResults"></a>
The maximum number of repositories to list.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_ListRepositories_RequestSyntax) **   <a name="proton-ListRepositories-request-nextToken"></a>
A token that indicates the location of the next repository in the array of repositories, after the list of repositories previously requested.
Type: String
Pattern: `[A-Za-z0-9+=/]+`
Required: No

## Response Syntax
<a name="API_ListRepositories_ResponseSyntax"></a>

```
{
   "nextToken": "string",
   "repositories": [
      {
         "arn": "string",
         "connectionArn": "string",
         "name": "string",
         "provider": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListRepositories_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListRepositories_ResponseSyntax) **   <a name="proton-ListRepositories-response-nextToken"></a>
A token that indicates the location of the next repository in the array of repositories, after the current requested list of repositories.
Type: String
Pattern: `[A-Za-z0-9+=/]+`

 ** [repositories](#API_ListRepositories_ResponseSyntax) **   <a name="proton-ListRepositories-response-repositories"></a>
An array of repository links.
Type: Array of [RepositorySummary](API_RepositorySummary.md) objects

## Errors
<a name="API_ListRepositories_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
There *isn't* sufficient access for performing this action.
HTTP Status Code: 400

 ** InternalServerException **
The request failed to register with the service.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The requested resource *wasn't* found.
HTTP Status Code: 400

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 400

 ** ValidationException **
The input is invalid or an out-of-range value was supplied for the input parameter.
HTTP Status Code: 400

## See Also
<a name="API_ListRepositories_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/proton-2020-07-20/ListRepositories)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/proton-2020-07-20/ListRepositories)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/proton-2020-07-20/ListRepositories)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/proton-2020-07-20/ListRepositories)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/proton-2020-07-20/ListRepositories)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/proton-2020-07-20/ListRepositories)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/proton-2020-07-20/ListRepositories)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/proton-2020-07-20/ListRepositories)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/proton-2020-07-20/ListRepositories)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/proton-2020-07-20/ListRepositories)
