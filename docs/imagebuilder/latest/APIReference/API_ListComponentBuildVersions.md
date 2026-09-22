---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_ListComponentBuildVersions.html
---

# ListComponentBuildVersions
<a name="API_ListComponentBuildVersions"></a>

Returns a list of component build versions for the specified component version ARN. You can only list build versions for components that your account owns. Deprecated build versions aren't included in the results.

## Request Syntax
<a name="API_ListComponentBuildVersions_RequestSyntax"></a>

```
POST /ListComponentBuildVersions HTTP/1.1
Content-type: application/json

{
   "componentVersionArn": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListComponentBuildVersions_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListComponentBuildVersions_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [componentVersionArn](#API_ListComponentBuildVersions_RequestSyntax) **   <a name="imagebuilder-ListComponentBuildVersions-request-componentVersionArn"></a>
The component version ARN whose build versions you want to list. The ARN must specify an exact version, without a build number suffix. If you don't specify an ARN, Image Builder returns build versions for the components that your account owns.
Type: String
Pattern: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws(?:-[a-z-]+)?|third-party):component/[a-z0-9-_]+/[0-9]+\.[0-9]+\.[0-9]+$`
Required: No

 ** [maxResults](#API_ListComponentBuildVersions_RequestSyntax) **   <a name="imagebuilder-ListComponentBuildVersions-request-maxResults"></a>
The maximum number of items to return in a single request.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 25.
Required: No

 ** [nextToken](#API_ListComponentBuildVersions_RequestSyntax) **   <a name="imagebuilder-ListComponentBuildVersions-request-nextToken"></a>
A token to specify where to start paginating. Use the `nextToken` value from a previously truncated response.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 65535.
Required: No

## Response Syntax
<a name="API_ListComponentBuildVersions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "componentSummaryList": [
      {
         "arn": "string",
         "changeDescription": "string",
         "dateCreated": "string",
         "description": "string",
         "name": "string",
         "obfuscate": boolean,
         "owner": "string",
         "platform": "string",
         "publisher": "string",
         "state": {
            "reason": "string",
            "status": "string"
         },
         "supportedOsVersions": [ "string" ],
         "tags": {
            "string" : "string"
         },
         "type": "string",
         "version": "string"
      }
   ],
   "nextToken": "string",
   "requestId": "string"
}
```

## Response Elements
<a name="API_ListComponentBuildVersions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [componentSummaryList](#API_ListComponentBuildVersions_ResponseSyntax) **   <a name="imagebuilder-ListComponentBuildVersions-response-componentSummaryList"></a>
The list of component summaries. Each summary represents one build version of the specified component version, or of the components that your account owns if you didn't specify an ARN. Deprecated build versions aren't included.
Type: Array of [ComponentSummary](API_ComponentSummary.md) objects

 ** [nextToken](#API_ListComponentBuildVersions_ResponseSyntax) **   <a name="imagebuilder-ListComponentBuildVersions-response-nextToken"></a>
The next token used for paginated responses. When this field isn't empty, there are additional elements that the service hasn't included in this request. Use this token with the next request to retrieve additional objects.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 65535.

 ** [requestId](#API_ListComponentBuildVersions_ResponseSyntax) **   <a name="imagebuilder-ListComponentBuildVersions-response-requestId"></a>
The request ID that uniquely identifies this request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

## Errors
<a name="API_ListComponentBuildVersions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** CallRateLimitExceededException **
You have exceeded the permitted request rate for the Amazon EC2 APIs that Image Builder calls on your behalf. Retry with an increasing or variable delay between requests.
HTTP Status Code: 429

 ** ClientException **
A generic client error. This error usually indicates that the request failed a validation check, such as when a downstream service rejects a configured value.
HTTP Status Code: 400

 ** ForbiddenException **
You are not authorized to perform the requested operation.
HTTP Status Code: 403

 ** InvalidPaginationTokenException **
You have provided an invalid pagination token in your request.
HTTP Status Code: 400

 ** InvalidRequestException **
The request is malformed or otherwise invalid. Verify the request and try again.
HTTP Status Code: 400

 ** ServiceException **
An internal server error occurred while Image Builder processed the request. Retrying the request may succeed.
HTTP Status Code: 500

 ** ServiceUnavailableException **
The service is unable to process your request at this time.
HTTP Status Code: 503

## Examples
<a name="API_ListComponentBuildVersions_Examples"></a>

### List the build versions of a component
<a name="API_ListComponentBuildVersions_Example_1"></a>

The following example lists the build versions that exist for version 1.0.0 of the specified component. The list returns the most recent build version first.

#### Sample Request
<a name="API_ListComponentBuildVersions_Example_1_Request"></a>

```
POST /ListComponentBuildVersions HTTP/1.1
Content-type: application/json

{
    "componentVersionArn": "arn:aws:imagebuilder:us-west-2:111122223333:component/my-example-component/1.0.0"
}
```

#### Sample Response
<a name="API_ListComponentBuildVersions_Example_1_Response"></a>

```
HTTP/1.1 200
Content-type: application/json

{
    "componentSummaryList": [
        {
            "arn": "arn:aws:imagebuilder:us-west-2:111122223333:component/my-example-component/1.0.0/2",
            "name": "my-example-component",
            "version": "1.0.0",
            "platform": "Linux",
            "supportedOsVersions": [
                "Amazon Linux 2023"
            ],
            "state": {
                "status": "ACTIVE"
            },
            "type": "BUILD",
            "owner": "111122223333",
            "description": "Installs the latest version of my application",
            "changeDescription": "Updated the install command to use dnf",
            "dateCreated": "2026-09-09T18:35:23.098Z",
            "tags": {
                "Environment": "Production"
            }
        },
        {
            "arn": "arn:aws:imagebuilder:us-west-2:111122223333:component/my-example-component/1.0.0/1",
            "name": "my-example-component",
            "version": "1.0.0",
            "platform": "Linux",
            "supportedOsVersions": [
                "Amazon Linux 2023"
            ],
            "state": {
                "status": "ACTIVE"
            },
            "type": "BUILD",
            "owner": "111122223333",
            "description": "Installs the latest version of my application",
            "changeDescription": "Initial version",
            "dateCreated": "2026-09-09T18:35:20.731Z",
            "tags": {
                "Environment": "Production"
            }
        }
    ],
    "requestId": "1d8693f0-26e1-42d7-ba35-d95ace1ce7e0"
}
```

## See Also
<a name="API_ListComponentBuildVersions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/imagebuilder-2019-12-02/ListComponentBuildVersions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/imagebuilder-2019-12-02/ListComponentBuildVersions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/ListComponentBuildVersions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/imagebuilder-2019-12-02/ListComponentBuildVersions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/ListComponentBuildVersions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/imagebuilder-2019-12-02/ListComponentBuildVersions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/imagebuilder-2019-12-02/ListComponentBuildVersions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/imagebuilder-2019-12-02/ListComponentBuildVersions)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/imagebuilder-2019-12-02/ListComponentBuildVersions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/ListComponentBuildVersions)
