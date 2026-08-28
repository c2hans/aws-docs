---
source_url: https://docs.aws.amazon.com/cognitosync/latest/APIReference/API_DescribeIdentityUsage.html
---

# DescribeIdentityUsage
<a name="API_DescribeIdentityUsage"></a>

**Note**
Amazon Cognito Sync is no longer open to new customers. For alternatives to Cognito Sync, please explore [AWS AppSync](https://aws.amazon.com/appsync/) and [Amazon DynamoDB](https://aws.amazon.com/dynamodb/). [Learn more](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-sync-availability-change.html).

Gets usage information for an identity, including number of datasets and data usage.

This API can be called with temporary user credentials provided by Cognito Identity or with developer credentials.

## Request Syntax
<a name="API_DescribeIdentityUsage_RequestSyntax"></a>

```
GET /identitypools/{{IdentityPoolId}}/identities/{{IdentityId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeIdentityUsage_RequestParameters"></a>

The request uses the following URI parameters.

 ** [IdentityId](#API_DescribeIdentityUsage_RequestSyntax) **   <a name="Cognito-DescribeIdentityUsage-request-uri-IdentityId"></a>
A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
Length Constraints: Minimum length of 1. Maximum length of 55.
Pattern: `[\w-]+:[0-9a-f-]+`
Required: Yes

 ** [IdentityPoolId](#API_DescribeIdentityUsage_RequestSyntax) **   <a name="Cognito-DescribeIdentityUsage-request-uri-IdentityPoolId"></a>
A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
Length Constraints: Minimum length of 1. Maximum length of 55.
Pattern: `[\w-]+:[0-9a-f-]+`
Required: Yes

## Request Body
<a name="API_DescribeIdentityUsage_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeIdentityUsage_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "IdentityUsage": {
      "DatasetCount": number,
      "DataStorage": number,
      "IdentityId": "string",
      "IdentityPoolId": "string",
      "LastModifiedDate": number
   }
}
```

## Response Elements
<a name="API_DescribeIdentityUsage_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [IdentityUsage](#API_DescribeIdentityUsage_ResponseSyntax) **   <a name="Cognito-DescribeIdentityUsage-response-IdentityUsage"></a>
Usage information for the identity.
Type: [IdentityUsage](API_IdentityUsage.md) object

## Errors
<a name="API_DescribeIdentityUsage_Errors"></a>

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
<a name="API_DescribeIdentityUsage_Examples"></a>

### DescribeIdentityUsage
<a name="API_DescribeIdentityUsage_Example_1"></a>

The following examples have been edited for readability.

#### Sample Request
<a name="API_DescribeIdentityUsage_Example_1_Request"></a>

```
POST / HTTP/1.1
CONTENT-TYPE: application/json
X-AMZN-REQUESTID: 33f9b4e4-a177-4aad-a3bb-6edb7980b283
X-AMZ-TARGET: com.amazonaws.cognito.sync.model.AWSCognitoSyncService.DescribeIdentityUsage
HOST: cognito-sync.us-east-1.amazonaws.com:443
X-AMZ-DATE: 20141111T215129Z
AUTHORIZATION: AWS4-HMAC-SHA256 Credential=<credential>, SignedHeaders=content-type;host;x-amz-date;x-amz-target;x-amzn-requestid, Signature=<signature>

{
    "IdentityPoolId": "IDENTITY_POOL_ID",
    "IdentityId": "IDENTITY_ID"
}
```

#### Sample Response
<a name="API_DescribeIdentityUsage_Example_1_Response"></a>

```
               1.1 200 OK
x-amzn-requestid: 33f9b4e4-a177-4aad-a3bb-6edb7980b283
content-type: application/json
content-length: 318
date: Tue, 11 Nov 2014 21:51:29 GMT

{
    "IdentityUsage":
    {
        "DataStorage": 16,
        "DatasetCount": 1,
        "IdentityId": "IDENTITY_ID",
        "IdentityPoolId": "IDENTITY_POOL_ID",
        "LastModifiedDate": 1.412974081336E9
    }
}
```

## See Also
<a name="API_DescribeIdentityUsage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cognito-sync-2014-06-30/DescribeIdentityUsage)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cognito-sync-2014-06-30/DescribeIdentityUsage)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-sync-2014-06-30/DescribeIdentityUsage)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cognito-sync-2014-06-30/DescribeIdentityUsage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-sync-2014-06-30/DescribeIdentityUsage)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cognito-sync-2014-06-30/DescribeIdentityUsage)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cognito-sync-2014-06-30/DescribeIdentityUsage)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cognito-sync-2014-06-30/DescribeIdentityUsage)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cognito-sync-2014-06-30/DescribeIdentityUsage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-sync-2014-06-30/DescribeIdentityUsage)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Cognito Sync. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cognitosync` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
