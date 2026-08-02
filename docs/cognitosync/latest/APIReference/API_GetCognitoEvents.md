---
source_url: https://docs.aws.amazon.com/cognitosync/latest/APIReference/API_GetCognitoEvents.html
---

# GetCognitoEvents
<a name="API_GetCognitoEvents"></a>

**Note**
Amazon Cognito Sync is no longer open to new customers. For alternatives to Cognito Sync, please explore [AWS AppSync](https://aws.amazon.com/appsync/) and [Amazon DynamoDB](https://aws.amazon.com/dynamodb/). [Learn more](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-sync-availability-change.html).

Gets the events and the corresponding Lambda functions associated with an identity pool.

This API can only be called with developer credentials. You cannot call this API with the temporary user credentials provided by Cognito Identity.

## Request Syntax
<a name="API_GetCognitoEvents_RequestSyntax"></a>

```
GET /identitypools/{{IdentityPoolId}}/events HTTP/1.1
```

## URI Request Parameters
<a name="API_GetCognitoEvents_RequestParameters"></a>

The request uses the following URI parameters.

 ** [IdentityPoolId](#API_GetCognitoEvents_RequestSyntax) **   <a name="Cognito-GetCognitoEvents-request-uri-IdentityPoolId"></a>
The Cognito Identity Pool ID for the request
Length Constraints: Minimum length of 1. Maximum length of 55.
Pattern: `[\w-]+:[0-9a-f-]+`
Required: Yes

## Request Body
<a name="API_GetCognitoEvents_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetCognitoEvents_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Events": {
      "string" : "string"
   }
}
```

## Response Elements
<a name="API_GetCognitoEvents_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Events](#API_GetCognitoEvents_ResponseSyntax) **   <a name="Cognito-GetCognitoEvents-response-Events"></a>
The Cognito Events returned from the GetCognitoEvents request
Type: String to string map
Map Entries: Maximum number of 1 item.

## Errors
<a name="API_GetCognitoEvents_Errors"></a>

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

## See Also
<a name="API_GetCognitoEvents_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cognito-sync-2014-06-30/GetCognitoEvents)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cognito-sync-2014-06-30/GetCognitoEvents)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-sync-2014-06-30/GetCognitoEvents)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cognito-sync-2014-06-30/GetCognitoEvents)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-sync-2014-06-30/GetCognitoEvents)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cognito-sync-2014-06-30/GetCognitoEvents)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cognito-sync-2014-06-30/GetCognitoEvents)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cognito-sync-2014-06-30/GetCognitoEvents)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cognito-sync-2014-06-30/GetCognitoEvents)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-sync-2014-06-30/GetCognitoEvents)
