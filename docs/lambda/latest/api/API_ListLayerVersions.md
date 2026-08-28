---
source_url: https://docs.aws.amazon.com/lambda/latest/api/API_ListLayerVersions.html
---

# ListLayerVersions
<a name="API_ListLayerVersions"></a>

Lists the versions of an [AWS Lambda layer](https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html). Versions that have been deleted aren't listed. Specify a [runtime identifier](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html) to list only versions that indicate that they're compatible with that runtime. Specify a compatible architecture to include only layer versions that are compatible with that architecture.

## Request Syntax
<a name="API_ListLayerVersions_RequestSyntax"></a>

```
GET /2018-10-31/layers/{{LayerName}}/versions?CompatibleArchitecture={{CompatibleArchitecture}}&CompatibleRuntime={{CompatibleRuntime}}&Marker={{Marker}}&MaxItems={{MaxItems}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListLayerVersions_RequestParameters"></a>

The request uses the following URI parameters.

 ** [CompatibleArchitecture](#API_ListLayerVersions_RequestSyntax) **   <a name="lambda-ListLayerVersions-request-uri-CompatibleArchitecture"></a>
The compatible [instruction set architecture](https://docs.aws.amazon.com/lambda/latest/dg/foundation-arch.html).
Valid Values: `x86_64 | arm64`

 ** [CompatibleRuntime](#API_ListLayerVersions_RequestSyntax) **   <a name="lambda-ListLayerVersions-request-uri-CompatibleRuntime"></a>
A runtime identifier.
The following list includes deprecated runtimes. For more information, see [Runtime use after deprecation](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html#runtime-deprecation-levels).
For a list of all currently supported runtimes, see [Supported runtimes](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html#runtimes-supported).
Valid Values: `nodejs | nodejs4.3 | nodejs6.10 | nodejs8.10 | nodejs10.x | nodejs12.x | nodejs14.x | nodejs16.x | java8 | java8.al2 | java11 | python2.7 | python3.6 | python3.7 | python3.8 | python3.9 | dotnetcore1.0 | dotnetcore2.0 | dotnetcore2.1 | dotnetcore3.1 | dotnet6 | dotnet8 | nodejs4.3-edge | go1.x | ruby2.5 | ruby2.7 | provided | provided.al2 | nodejs18.x | python3.10 | java17 | ruby3.2 | ruby3.3 | ruby3.4 | python3.11 | nodejs20.x | provided.al2023 | python3.12 | java21 | python3.13 | nodejs22.x | nodejs24.x | python3.14 | java25 | dotnet10 | ruby4.0`

 ** [LayerName](#API_ListLayerVersions_RequestSyntax) **   <a name="lambda-ListLayerVersions-request-uri-LayerName"></a>
The name or Amazon Resource Name (ARN) of the layer.
Length Constraints: Minimum length of 1. Maximum length of 140.
Pattern: `(arn:[a-zA-Z0-9-]+:lambda:[a-zA-Z0-9-]+:\d{12}:layer:[a-zA-Z0-9-_]+)|[a-zA-Z0-9-_]+`
Required: Yes

 ** [Marker](#API_ListLayerVersions_RequestSyntax) **   <a name="lambda-ListLayerVersions-request-uri-Marker"></a>
A pagination token returned by a previous call.

 ** [MaxItems](#API_ListLayerVersions_RequestSyntax) **   <a name="lambda-ListLayerVersions-request-uri-MaxItems"></a>
The maximum number of versions to return.
Valid Range: Minimum value of 1. Maximum value of 50.

## Request Body
<a name="API_ListLayerVersions_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListLayerVersions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "LayerVersions": [
      {
         "CompatibleArchitectures": [ "string" ],
         "CompatibleRuntimes": [ "string" ],
         "CreatedDate": "string",
         "Description": "string",
         "LayerVersionArn": "string",
         "LicenseInfo": "string",
         "Version": number
      }
   ],
   "NextMarker": "string"
}
```

## Response Elements
<a name="API_ListLayerVersions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [LayerVersions](#API_ListLayerVersions_ResponseSyntax) **   <a name="lambda-ListLayerVersions-response-LayerVersions"></a>
A list of versions.
Type: Array of [LayerVersionsListItem](API_LayerVersionsListItem.md) objects

 ** [NextMarker](#API_ListLayerVersions_ResponseSyntax) **   <a name="lambda-ListLayerVersions-response-NextMarker"></a>
A pagination token returned when the response doesn't contain all versions.
Type: String

## Errors
<a name="API_ListLayerVersions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterValueException **
One of the parameters in the request is not valid.
 ** message **
The exception message.
 ** Type **
The exception type.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The resource specified in the request does not exist.
HTTP Status Code: 404

 ** ServiceException **
The AWS Lambda service encountered an internal error.
HTTP Status Code: 500

 ** TooManyRequestsException **
The request throughput limit was exceeded. For more information, see [Lambda quotas](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests).
 ** retryAfterSeconds **
The number of seconds the caller should wait before retrying.
HTTP Status Code: 429

## See Also
<a name="API_ListLayerVersions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lambda-2015-03-31/ListLayerVersions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lambda-2015-03-31/ListLayerVersions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-2015-03-31/ListLayerVersions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lambda-2015-03-31/ListLayerVersions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-2015-03-31/ListLayerVersions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lambda-2015-03-31/ListLayerVersions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lambda-2015-03-31/ListLayerVersions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lambda-2015-03-31/ListLayerVersions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lambda-2015-03-31/ListLayerVersions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-2015-03-31/ListLayerVersions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Lambda. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lambda` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
