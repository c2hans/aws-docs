---
source_url: https://docs.aws.amazon.com/panorama/latest/api/API_ListApplicationInstanceDependencies.html
---

# ListApplicationInstanceDependencies
<a name="API_ListApplicationInstanceDependencies"></a>

**Important**
End of support notice: On May 31, 2026, AWS will end support for AWS Panorama. After May 31, 2026, you will no longer be able to access the AWS Panorama console or AWS Panorama resources. For more information, see [AWS Panorama end of support](https://docs.aws.amazon.com/panorama/latest/dev/panorama-end-of-support.html).

Returns a list of application instance dependencies.

## Request Syntax
<a name="API_ListApplicationInstanceDependencies_RequestSyntax"></a>

```
GET /application-instances/{{ApplicationInstanceId}}/package-dependencies?maxResults={{MaxResults}}&nextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListApplicationInstanceDependencies_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ApplicationInstanceId](#API_ListApplicationInstanceDependencies_RequestSyntax) **   <a name="panorama-ListApplicationInstanceDependencies-request-uri-ApplicationInstanceId"></a>
The application instance's ID.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9\-\_]+`
Required: Yes

 ** [MaxResults](#API_ListApplicationInstanceDependencies_RequestSyntax) **   <a name="panorama-ListApplicationInstanceDependencies-request-uri-MaxResults"></a>
The maximum number of application instance dependencies to return in one page of results.
Valid Range: Minimum value of 0. Maximum value of 25.

 ** [NextToken](#API_ListApplicationInstanceDependencies_RequestSyntax) **   <a name="panorama-ListApplicationInstanceDependencies-request-uri-NextToken"></a>
Specify the pagination token from a previous request to retrieve the next page of results.
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `.+`

## Request Body
<a name="API_ListApplicationInstanceDependencies_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListApplicationInstanceDependencies_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "PackageObjects": [
      {
         "Name": "string",
         "PackageVersion": "string",
         "PatchVersion": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListApplicationInstanceDependencies_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListApplicationInstanceDependencies_ResponseSyntax) **   <a name="panorama-ListApplicationInstanceDependencies-response-NextToken"></a>
A pagination token that's included if more results are available.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `.+`

 ** [PackageObjects](#API_ListApplicationInstanceDependencies_ResponseSyntax) **   <a name="panorama-ListApplicationInstanceDependencies-response-PackageObjects"></a>
A list of package objects.
Type: Array of [PackageObject](API_PackageObject.md) objects

## Errors
<a name="API_ListApplicationInstanceDependencies_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The requestor does not have permission to access the target action or resource.
HTTP Status Code: 403

 ** InternalServerException **
An internal error occurred.
 ** RetryAfterSeconds **
The number of seconds a client should wait before retrying the call.
HTTP Status Code: 500

## See Also
<a name="API_ListApplicationInstanceDependencies_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/panorama-2019-07-24/ListApplicationInstanceDependencies)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/panorama-2019-07-24/ListApplicationInstanceDependencies)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/panorama-2019-07-24/ListApplicationInstanceDependencies)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/panorama-2019-07-24/ListApplicationInstanceDependencies)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/panorama-2019-07-24/ListApplicationInstanceDependencies)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/panorama-2019-07-24/ListApplicationInstanceDependencies)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/panorama-2019-07-24/ListApplicationInstanceDependencies)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/panorama-2019-07-24/ListApplicationInstanceDependencies)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/panorama-2019-07-24/ListApplicationInstanceDependencies)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/panorama-2019-07-24/ListApplicationInstanceDependencies)
