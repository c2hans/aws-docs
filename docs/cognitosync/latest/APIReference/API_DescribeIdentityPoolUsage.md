---
source_url: https://docs.aws.amazon.com/cognitosync/latest/APIReference/API_DescribeIdentityPoolUsage.html
---

# DescribeIdentityPoolUsage
<a name="API_DescribeIdentityPoolUsage"></a>

**Note**
Amazon Cognito Sync is no longer open to new customers. For alternatives to Cognito Sync, please explore [AWS AppSync](https://aws.amazon.com/appsync/) and [Amazon DynamoDB](https://aws.amazon.com/dynamodb/). [Learn more](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-sync-availability-change.html).

Gets usage details (for example, data storage) about a particular identity pool.

This API can only be called with developer credentials. You cannot call this API with the temporary user credentials provided by Cognito Identity.

## Request Syntax
<a name="API_DescribeIdentityPoolUsage_RequestSyntax"></a>

```
GET /identitypools/{{IdentityPoolId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeIdentityPoolUsage_RequestParameters"></a>

The request uses the following URI parameters.

 ** [IdentityPoolId](#API_DescribeIdentityPoolUsage_RequestSyntax) **   <a name="Cognito-DescribeIdentityPoolUsage-request-uri-IdentityPoolId"></a>
A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
Length Constraints: Minimum length of 1. Maximum length of 55.
Pattern: `[\w-]+:[0-9a-f-]+`
Required: Yes

## Request Body
<a name="API_DescribeIdentityPoolUsage_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeIdentityPoolUsage_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "IdentityPoolUsage": {
      "DataStorage": number,
      "IdentityPoolId": "string",
      "LastModifiedDate": number,
      "SyncSessionsCount": number
   }
}
```

## Response Elements
<a name="API_DescribeIdentityPoolUsage_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [IdentityPoolUsage](#API_DescribeIdentityPoolUsage_ResponseSyntax) **   <a name="Cognito-DescribeIdentityPoolUsage-response-IdentityPoolUsage"></a>
Information about the usage of the identity pool.
Type: [IdentityPoolUsage](API_IdentityPoolUsage.md) object

## Errors
<a name="API_DescribeIdentityPoolUsage_Errors"></a>

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
<a name="API_DescribeIdentityPoolUsage_Examples"></a>

### DescribeIdentityPoolUsage
<a name="API_DescribeIdentityPoolUsage_Example_1"></a>

The following examples have been edited for readability.

#### Sample Request
<a name="API_DescribeIdentityPoolUsage_Example_1_Request"></a>

```
POST / HTTP/1.1
CONTENT-TYPE: application/json
X-AMZN-REQUESTID: 8dc0e749-c8cd-48bd-8520-da6be00d528b
X-AMZ-TARGET: com.amazonaws.cognito.sync.model.AWSCognitoSyncService.DescribeIdentityPoolUsage
HOST: cognito-sync.us-east-1.amazonaws.com:443
X-AMZ-DATE: 20141111T205737Z
AUTHORIZATION: AWS4-HMAC-SHA256 Credential=<credential>, SignedHeaders=content-type;host;x-amz-date;x-amz-target;x-amzn-requestid, Signature=<signature>

{
    "IdentityPoolId": "IDENTITY_POOL_ID"
}
```

#### Sample Response
<a name="API_DescribeIdentityPoolUsage_Example_1_Response"></a>

```
1.1 200 OK
x-amzn-requestid: 8dc0e749-c8cd-48bd-8520-da6be00d528b
content-type: application/json
content-length: 271
date: Tue, 11 Nov 2014 20:57:37 GMT

{
    "IdentityPoolUsage":
    {
        "DataStorage": 0,
        "IdentityPoolId": "IDENTITY_POOL_ID",
        "LastModifiedDate": 1.413231134115E9,
        "SyncSessionsCount": null
    }
}
```

## See Also
<a name="API_DescribeIdentityPoolUsage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cognito-sync-2014-06-30/DescribeIdentityPoolUsage)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cognito-sync-2014-06-30/DescribeIdentityPoolUsage)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-sync-2014-06-30/DescribeIdentityPoolUsage)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cognito-sync-2014-06-30/DescribeIdentityPoolUsage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-sync-2014-06-30/DescribeIdentityPoolUsage)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cognito-sync-2014-06-30/DescribeIdentityPoolUsage)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cognito-sync-2014-06-30/DescribeIdentityPoolUsage)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cognito-sync-2014-06-30/DescribeIdentityPoolUsage)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cognito-sync-2014-06-30/DescribeIdentityPoolUsage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-sync-2014-06-30/DescribeIdentityPoolUsage)
