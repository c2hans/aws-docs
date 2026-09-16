---
source_url: https://docs.aws.amazon.com/cognitosync/latest/APIReference/API_UnsubscribeFromDataset.html
---

# UnsubscribeFromDataset
<a name="API_UnsubscribeFromDataset"></a>

**Note**
Amazon Cognito Sync is no longer open to new customers. For alternatives to Cognito Sync, please explore [AWS AppSync](https://aws.amazon.com/appsync/) and [Amazon DynamoDB](https://aws.amazon.com/dynamodb/). [Learn more](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-sync-availability-change.html).

Unsubscribes from receiving notifications when a dataset is modified by another device.

This API can only be called with temporary credentials provided by Cognito Identity. You cannot call this API with developer credentials.

## Request Syntax
<a name="API_UnsubscribeFromDataset_RequestSyntax"></a>

```
DELETE /identitypools/{{IdentityPoolId}}/identities/{{IdentityId}}/datasets/{{DatasetName}}/subscriptions/{{DeviceId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_UnsubscribeFromDataset_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DatasetName](#API_UnsubscribeFromDataset_RequestSyntax) **   <a name="Cognito-UnsubscribeFromDataset-request-uri-DatasetName"></a>
The name of the dataset from which to unsubcribe.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_.:-]+`
Required: Yes

 ** [DeviceId](#API_UnsubscribeFromDataset_RequestSyntax) **   <a name="Cognito-UnsubscribeFromDataset-request-uri-DeviceId"></a>
The unique ID generated for this device by Cognito.
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** [IdentityId](#API_UnsubscribeFromDataset_RequestSyntax) **   <a name="Cognito-UnsubscribeFromDataset-request-uri-IdentityId"></a>
Unique ID for this identity.
Length Constraints: Minimum length of 1. Maximum length of 55.
Pattern: `[\w-]+:[0-9a-f-]+`
Required: Yes

 ** [IdentityPoolId](#API_UnsubscribeFromDataset_RequestSyntax) **   <a name="Cognito-UnsubscribeFromDataset-request-uri-IdentityPoolId"></a>
A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. The ID of the pool to which this identity belongs.
Length Constraints: Minimum length of 1. Maximum length of 55.
Pattern: `[\w-]+:[0-9a-f-]+`
Required: Yes

## Request Body
<a name="API_UnsubscribeFromDataset_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_UnsubscribeFromDataset_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UnsubscribeFromDataset_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UnsubscribeFromDataset_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalErrorException **
Indicates an internal service error.
 ** message **
Message returned by InternalErrorException.
HTTP Status Code: 500

 ** InvalidConfigurationException **
This exception is thrown when Amazon Cognito detects an invalid configuration.
 ** message **
Message returned by InvalidConfigurationException.
HTTP Status Code: 400

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
<a name="API_UnsubscribeFromDataset_Examples"></a>

### UnsubscribeFromDataset
<a name="API_UnsubscribeFromDataset_Example_1"></a>

The following examples have been edited for readability.

#### Sample Request
<a name="API_UnsubscribeFromDataset_Example_1_Request"></a>

```
POST / HTTP/1.1
CONTENT-TYPE: application/json
X-AMZ-REQUESTSUPERTRACE: true
X-AMZN-REQUESTID: 676896d6-14ca-45b1-8029-6d36b10a077e
X-AMZ-TARGET: com.amazonaws.cognito.sync.model.AWSCognitoSyncService.UnsubscribeFromDataset
HOST: cognito-sync.us-east-1.amazonaws.com
X-AMZ-DATE: 20141004T195446Z
X-AMZ-SECURITY-TOKEN: <securitytoken>
AUTHORIZATION: AWS4-HMAC-SHA256 Credential=<credential>, SignedHeaders=content-type;content-length;host;x-amz-date;x-amz-target, Signature=<signature>

{
    "IdentityPoolId": "ID_POOL_ID",
    "IdentityId": "IDENTITY_ID",
    "DatasetName": "Rufus",
    "DeviceId": "5cd28fbe-dd83-47ab-9f83-19093a5fb014"
}
```

#### Sample Response
<a name="API_UnsubscribeFromDataset_Example_1_Response"></a>

```
1.1 200 OK
x-amzn-requestid: 676896d6-14ca-45b1-8029-6d36b10a077e
date: Sat, 04 Oct 2014 19:54:46 GMT
content-type: application/json
content-length: 103

{
}
```

## See Also
<a name="API_UnsubscribeFromDataset_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cognito-sync-2014-06-30/UnsubscribeFromDataset)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cognito-sync-2014-06-30/UnsubscribeFromDataset)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-sync-2014-06-30/UnsubscribeFromDataset)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cognito-sync-2014-06-30/UnsubscribeFromDataset)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-sync-2014-06-30/UnsubscribeFromDataset)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cognito-sync-2014-06-30/UnsubscribeFromDataset)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cognito-sync-2014-06-30/UnsubscribeFromDataset)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cognito-sync-2014-06-30/UnsubscribeFromDataset)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/cognito-sync-2014-06-30/UnsubscribeFromDataset)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-sync-2014-06-30/UnsubscribeFromDataset)
