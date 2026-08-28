---
source_url: https://docs.aws.amazon.com/cognitosync/latest/APIReference/API_ListRecords.html
---

# ListRecords
<a name="API_ListRecords"></a>

**Note**
Amazon Cognito Sync is no longer open to new customers. For alternatives to Cognito Sync, please explore [AWS AppSync](https://aws.amazon.com/appsync/) and [Amazon DynamoDB](https://aws.amazon.com/dynamodb/). [Learn more](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-sync-availability-change.html).

Gets paginated records, optionally changed after a particular sync count for a dataset and identity. With Amazon Cognito Sync, each identity has access only to its own data. Thus, the credentials used to make this API call need to have access to the identity data.

ListRecords can be called with temporary user credentials provided by Cognito Identity or with developer credentials. You should use Cognito Identity credentials to make this API call.

## Request Syntax
<a name="API_ListRecords_RequestSyntax"></a>

```
GET /identitypools/{{IdentityPoolId}}/identities/{{IdentityId}}/datasets/{{DatasetName}}/records?lastSyncCount={{LastSyncCount}}&maxResults={{MaxResults}}&nextToken={{NextToken}}&syncSessionToken={{SyncSessionToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListRecords_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DatasetName](#API_ListRecords_RequestSyntax) **   <a name="Cognito-ListRecords-request-uri-DatasetName"></a>
A string of up to 128 characters. Allowed characters are a-z, A-Z, 0-9, '\_' (underscore), '-' (dash), and '.' (dot).
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_.:-]+`
Required: Yes

 ** [IdentityId](#API_ListRecords_RequestSyntax) **   <a name="Cognito-ListRecords-request-uri-IdentityId"></a>
A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
Length Constraints: Minimum length of 1. Maximum length of 55.
Pattern: `[\w-]+:[0-9a-f-]+`
Required: Yes

 ** [IdentityPoolId](#API_ListRecords_RequestSyntax) **   <a name="Cognito-ListRecords-request-uri-IdentityPoolId"></a>
A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
Length Constraints: Minimum length of 1. Maximum length of 55.
Pattern: `[\w-]+:[0-9a-f-]+`
Required: Yes

 ** [LastSyncCount](#API_ListRecords_RequestSyntax) **   <a name="Cognito-ListRecords-request-uri-LastSyncCount"></a>
The last server sync count for this record.

 ** [MaxResults](#API_ListRecords_RequestSyntax) **   <a name="Cognito-ListRecords-request-uri-MaxResults"></a>
The maximum number of results to be returned.

 ** [NextToken](#API_ListRecords_RequestSyntax) **   <a name="Cognito-ListRecords-request-uri-NextToken"></a>
A pagination token for obtaining the next page of results.

 ** [SyncSessionToken](#API_ListRecords_RequestSyntax) **   <a name="Cognito-ListRecords-request-uri-SyncSessionToken"></a>
A token containing a session ID, identity ID, and expiration.

## Request Body
<a name="API_ListRecords_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListRecords_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Count": number,
   "DatasetDeletedAfterRequestedSyncCount": boolean,
   "DatasetExists": boolean,
   "DatasetSyncCount": number,
   "LastModifiedBy": "string",
   "MergedDatasetNames": [ "string" ],
   "NextToken": "string",
   "Records": [
      {
         "DeviceLastModifiedDate": number,
         "Key": "string",
         "LastModifiedBy": "string",
         "LastModifiedDate": number,
         "SyncCount": number,
         "Value": "string"
      }
   ],
   "SyncSessionToken": "string"
}
```

## Response Elements
<a name="API_ListRecords_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Count](#API_ListRecords_ResponseSyntax) **   <a name="Cognito-ListRecords-response-Count"></a>
Total number of records.
Type: Integer

 ** [DatasetDeletedAfterRequestedSyncCount](#API_ListRecords_ResponseSyntax) **   <a name="Cognito-ListRecords-response-DatasetDeletedAfterRequestedSyncCount"></a>
A boolean value specifying whether to delete the dataset locally.
Type: Boolean

 ** [DatasetExists](#API_ListRecords_ResponseSyntax) **   <a name="Cognito-ListRecords-response-DatasetExists"></a>
Indicates whether the dataset exists.
Type: Boolean

 ** [DatasetSyncCount](#API_ListRecords_ResponseSyntax) **   <a name="Cognito-ListRecords-response-DatasetSyncCount"></a>
Server sync count for this dataset.
Type: Long

 ** [LastModifiedBy](#API_ListRecords_ResponseSyntax) **   <a name="Cognito-ListRecords-response-LastModifiedBy"></a>
The user/device that made the last change to this record.
Type: String

 ** [MergedDatasetNames](#API_ListRecords_ResponseSyntax) **   <a name="Cognito-ListRecords-response-MergedDatasetNames"></a>
Names of merged datasets.
Type: Array of strings

 ** [NextToken](#API_ListRecords_ResponseSyntax) **   <a name="Cognito-ListRecords-response-NextToken"></a>
A pagination token for obtaining the next page of results.
Type: String

 ** [Records](#API_ListRecords_ResponseSyntax) **   <a name="Cognito-ListRecords-response-Records"></a>
A list of all records.
Type: Array of [Record](API_Record.md) objects

 ** [SyncSessionToken](#API_ListRecords_ResponseSyntax) **   <a name="Cognito-ListRecords-response-SyncSessionToken"></a>
A token containing a session ID, identity ID, and expiration.
Type: String

## Errors
<a name="API_ListRecords_Errors"></a>

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
<a name="API_ListRecords_Examples"></a>

### ListRecords
<a name="API_ListRecords_Example_1"></a>

The following examples have been edited for readability.

#### Sample Request
<a name="API_ListRecords_Example_1_Request"></a>

```
POST / HTTP/1.1
CONTENT-TYPE: application/json
X-AMZN-REQUESTID: b3d2e31e-d6b7-4612-8e84-c9ba288dab5d
X-AMZ-TARGET: com.amazonaws.cognito.sync.model.AWSCognitoSyncService.ListRecords
HOST: cognito-sync.us-east-1.amazonaws.com:443
X-AMZ-DATE: 20141111T183230Z
AUTHORIZATION: AWS4-HMAC-SHA256 Credential=<credential>, SignedHeaders=content-type;host;x-amz-date;x-amz-target;x-amzn-requestid, Signature=<signature>

{
    "IdentityPoolId": "IDENTITY_POOL_ID",
    "IdentityId": "IDENTITY_ID",
    "DatasetName": "newDataSet"
}
```

#### Sample Response
<a name="API_ListRecords_Example_1_Response"></a>

```
1.1 200 OK
x-amzn-requestid: b3d2e31e-d6b7-4612-8e84-c9ba288dab5d
content-type: application/json
content-length: 623
date: Tue, 11 Nov 2014 18:32:30 GMT

{
    "Count": 0,
    "DatasetDeletedAfterRequestedSyncCount": false,
    "DatasetExists": false,
    "DatasetSyncCount": 0,
    "LastModifiedBy": null,
    "MergedDatasetNames": null,
    "NextToken": null,
    "Records": [],
    "SyncSessionToken": "SYNC_SESSION_TOKEN"
}
```

## See Also
<a name="API_ListRecords_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cognito-sync-2014-06-30/ListRecords)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cognito-sync-2014-06-30/ListRecords)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-sync-2014-06-30/ListRecords)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cognito-sync-2014-06-30/ListRecords)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-sync-2014-06-30/ListRecords)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cognito-sync-2014-06-30/ListRecords)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cognito-sync-2014-06-30/ListRecords)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cognito-sync-2014-06-30/ListRecords)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cognito-sync-2014-06-30/ListRecords)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-sync-2014-06-30/ListRecords)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Cognito Sync. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cognitosync` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
