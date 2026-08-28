---
source_url: https://docs.aws.amazon.com/cognitosync/latest/APIReference/API_ListIdentityPoolUsage.html
---

# ListIdentityPoolUsage
<a name="API_ListIdentityPoolUsage"></a>

**Note**
Amazon Cognito Sync is no longer open to new customers. For alternatives to Cognito Sync, please explore [AWS AppSync](https://aws.amazon.com/appsync/) and [Amazon DynamoDB](https://aws.amazon.com/dynamodb/). [Learn more](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-sync-availability-change.html).

Gets a list of identity pools registered with Cognito.

ListIdentityPoolUsage can only be called with developer credentials. You cannot make this API call with the temporary user credentials provided by Cognito Identity.

## Request Syntax
<a name="API_ListIdentityPoolUsage_RequestSyntax"></a>

```
GET /identitypools?maxResults={{MaxResults}}&nextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListIdentityPoolUsage_RequestParameters"></a>

The request uses the following URI parameters.

 ** [MaxResults](#API_ListIdentityPoolUsage_RequestSyntax) **   <a name="Cognito-ListIdentityPoolUsage-request-uri-MaxResults"></a>
The maximum number of results to be returned.

 ** [NextToken](#API_ListIdentityPoolUsage_RequestSyntax) **   <a name="Cognito-ListIdentityPoolUsage-request-uri-NextToken"></a>
A pagination token for obtaining the next page of results.

## Request Body
<a name="API_ListIdentityPoolUsage_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListIdentityPoolUsage_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Count": number,
   "IdentityPoolUsages": [
      {
         "DataStorage": number,
         "IdentityPoolId": "string",
         "LastModifiedDate": number,
         "SyncSessionsCount": number
      }
   ],
   "MaxResults": number,
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListIdentityPoolUsage_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Count](#API_ListIdentityPoolUsage_ResponseSyntax) **   <a name="Cognito-ListIdentityPoolUsage-response-Count"></a>
Total number of identities for the identity pool.
Type: Integer

 ** [IdentityPoolUsages](#API_ListIdentityPoolUsage_ResponseSyntax) **   <a name="Cognito-ListIdentityPoolUsage-response-IdentityPoolUsages"></a>
Usage information for the identity pools.
Type: Array of [IdentityPoolUsage](API_IdentityPoolUsage.md) objects

 ** [MaxResults](#API_ListIdentityPoolUsage_ResponseSyntax) **   <a name="Cognito-ListIdentityPoolUsage-response-MaxResults"></a>
The maximum number of results to be returned.
Type: Integer

 ** [NextToken](#API_ListIdentityPoolUsage_ResponseSyntax) **   <a name="Cognito-ListIdentityPoolUsage-response-NextToken"></a>
A pagination token for obtaining the next page of results.
Type: String

## Errors
<a name="API_ListIdentityPoolUsage_Errors"></a>

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

 ** TooManyRequestsException **
Thrown if the request is throttled.
 ** message **
Message returned by a TooManyRequestsException.
HTTP Status Code: 429

## Examples
<a name="API_ListIdentityPoolUsage_Examples"></a>

### ListIdentityPoolUsage
<a name="API_ListIdentityPoolUsage_Example_1"></a>

The following examples have been edited for readability.

#### Sample Request
<a name="API_ListIdentityPoolUsage_Example_1_Request"></a>

```
POST / HTTP/1.1
CONTENT-TYPE: application/json
X-AMZN-REQUESTID: 9be7c425-ef05-48c0-aef3-9f0ff2fe17d3
X-AMZ-TARGET: com.amazonaws.cognito.sync.model.AWSCognitoSyncService.ListIdentityPoolUsage
HOST: cognito-sync.us-east-1.amazonaws.com:443
X-AMZ-DATE: 20141111T211414Z
AUTHORIZATION: AWS4-HMAC-SHA256 Credential=<credential>, SignedHeaders=content-type;host;x-amz-date;x-amz-target;x-amzn-requestid, Signature=<signature>

{
    "MaxResults": "2"
}
```

#### Sample Response
<a name="API_ListIdentityPoolUsage_Example_1_Response"></a>

```
1.1 200 OK
x-amzn-requestid: 9be7c425-ef05-48c0-aef3-9f0ff2fe17d3
content-type: application/json
content-length: 519
date: Tue, 11 Nov 2014 21:14:14 GMT

{
    "Count": 2,
    "IdentityPoolUsages": [
    {
        "DataStorage": 0,
        "IdentityPoolId": "IDENTITY_POOL_ID",
        "LastModifiedDate": 1.413836234607E9,
        "SyncSessionsCount": null
    },
    {
        "DataStorage": 0,
        "IdentityPoolId": "IDENTITY_POOL_ID",
        "LastModifiedDate": 1.410892165601E9,
        "SyncSessionsCount": null
    }],
    "MaxResults": 2,
    "NextToken": "dXMtZWFzdC0xOjBjMWJhMDUyLWUwOTgtNDFmYS1hNzZlLWVhYTJjMTI1Zjg2MQ=="
}
```

## See Also
<a name="API_ListIdentityPoolUsage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cognito-sync-2014-06-30/ListIdentityPoolUsage)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cognito-sync-2014-06-30/ListIdentityPoolUsage)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-sync-2014-06-30/ListIdentityPoolUsage)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cognito-sync-2014-06-30/ListIdentityPoolUsage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-sync-2014-06-30/ListIdentityPoolUsage)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cognito-sync-2014-06-30/ListIdentityPoolUsage)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cognito-sync-2014-06-30/ListIdentityPoolUsage)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cognito-sync-2014-06-30/ListIdentityPoolUsage)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cognito-sync-2014-06-30/ListIdentityPoolUsage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-sync-2014-06-30/ListIdentityPoolUsage)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Cognito Sync. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cognitosync` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
