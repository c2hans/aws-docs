---
source_url: https://docs.aws.amazon.com/cognitosync/latest/APIReference/API_GetIdentityPoolConfiguration.html
---

# GetIdentityPoolConfiguration
<a name="API_GetIdentityPoolConfiguration"></a>

**Note**
Amazon Cognito Sync is no longer open to new customers. For alternatives to Cognito Sync, please explore [AWS AppSync](https://aws.amazon.com/appsync/) and [Amazon DynamoDB](https://aws.amazon.com/dynamodb/). [Learn more](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-sync-availability-change.html).

Gets the configuration settings of an identity pool.

This API can only be called with developer credentials. You cannot call this API with the temporary user credentials provided by Cognito Identity.

## Request Syntax
<a name="API_GetIdentityPoolConfiguration_RequestSyntax"></a>

```
GET /identitypools/{{IdentityPoolId}}/configuration HTTP/1.1
```

## URI Request Parameters
<a name="API_GetIdentityPoolConfiguration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [IdentityPoolId](#API_GetIdentityPoolConfiguration_RequestSyntax) **   <a name="Cognito-GetIdentityPoolConfiguration-request-uri-IdentityPoolId"></a>
A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. This is the ID of the pool for which to return a configuration.
Length Constraints: Minimum length of 1. Maximum length of 55.
Pattern: `[\w-]+:[0-9a-f-]+`
Required: Yes

## Request Body
<a name="API_GetIdentityPoolConfiguration_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetIdentityPoolConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "CognitoStreams": {
      "DisabledReason": "string",
      "RoleArn": "string",
      "StreamingStatus": "string",
      "StreamName": "string"
   },
   "IdentityPoolId": "string",
   "PushSync": {
      "ApplicationArns": [ "string" ],
      "RoleArn": "string"
   }
}
```

## Response Elements
<a name="API_GetIdentityPoolConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CognitoStreams](#API_GetIdentityPoolConfiguration_ResponseSyntax) **   <a name="Cognito-GetIdentityPoolConfiguration-response-CognitoStreams"></a>
Options to apply to this identity pool for Amazon Cognito streams.
Type: [CognitoStreams](API_CognitoStreams.md) object

 ** [IdentityPoolId](#API_GetIdentityPoolConfiguration_ResponseSyntax) **   <a name="Cognito-GetIdentityPoolConfiguration-response-IdentityPoolId"></a>
A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 55.
Pattern: `[\w-]+:[0-9a-f-]+`

 ** [PushSync](#API_GetIdentityPoolConfiguration_ResponseSyntax) **   <a name="Cognito-GetIdentityPoolConfiguration-response-PushSync"></a>
Options to apply to this identity pool for push synchronization.
Type: [PushSync](API_PushSync.md) object

## Errors
<a name="API_GetIdentityPoolConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalErrorException **
Indicates an internal service error.
 ** message **
Message returned by InternalErrorException.
HTTP Status Code: 500

 ** InvalidParameterException **
Thrown when a request parameter does not comply with the associated constraints.
 ** message **
Message returned by InvalidParameterException.
HTTP Status Code: 400

 ** NotAuthorizedException **
Thrown when a user is not authorized to access the requested resource.
 ** message **
The message returned by a NotAuthorizedException.
HTTP Status Code: 403

 ** ResourceNotFoundException **
Thrown if the resource doesn't exist.
 ** message **
Message returned by a ResourceNotFoundException.
HTTP Status Code: 404

 ** TooManyRequestsException **
Thrown if the request is throttled.
 ** message **
Message returned by a TooManyRequestsException.
HTTP Status Code: 429

## Examples
<a name="API_GetIdentityPoolConfiguration_Examples"></a>

### GetIdentityPoolConfiguration
<a name="API_GetIdentityPoolConfiguration_Example_1"></a>

The following examples have been edited for readability.

#### Sample Request
<a name="API_GetIdentityPoolConfiguration_Example_1_Request"></a>

```
POST / HTTP/1.1
CONTENT-TYPE: application/json
X-AMZN-REQUESTID: b1cfdd4b-f620-4fe4-be0f-02024a1d33da
X-AMZ-TARGET: com.amazonaws.cognito.sync.model.AWSCognitoSyncService.GetIdentityPoolConfiguration
HOST: cognito-sync.us-east-1.amazonaws.com
X-AMZ-DATE: 20141004T195722Z
AUTHORIZATION: AWS4-HMAC-SHA256 Credential=<credential>, SignedHeaders=content-type;content-length;host;x-amz-date;x-amz-target, Signature=<signature>

{
    "IdentityPoolId": "ID_POOL_ID"
}
```

#### Sample Response
<a name="API_GetIdentityPoolConfiguration_Example_1_Response"></a>

```
1.1 200 OK
x-amzn-requestid: b1cfdd4b-f620-4fe4-be0f-02024a1d33da
date: Sat, 04 Oct 2014 19:57:22 GMT
content-type: application/json
content-length: 332

{
    "IdentityPoolId": "ID_POOL_ID",
    "PushSync":
    {
        "ApplicationArns": ["PLATFORMARN1", "PLATFORMARN2"],
        "RoleArn": "ROLEARN"
    }
}
```

## See Also
<a name="API_GetIdentityPoolConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cognito-sync-2014-06-30/GetIdentityPoolConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cognito-sync-2014-06-30/GetIdentityPoolConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-sync-2014-06-30/GetIdentityPoolConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cognito-sync-2014-06-30/GetIdentityPoolConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-sync-2014-06-30/GetIdentityPoolConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cognito-sync-2014-06-30/GetIdentityPoolConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cognito-sync-2014-06-30/GetIdentityPoolConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cognito-sync-2014-06-30/GetIdentityPoolConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cognito-sync-2014-06-30/GetIdentityPoolConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-sync-2014-06-30/GetIdentityPoolConfiguration)
