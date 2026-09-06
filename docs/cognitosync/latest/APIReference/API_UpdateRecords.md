---
source_url: https://docs.aws.amazon.com/cognitosync/latest/APIReference/API_UpdateRecords.html
---

# UpdateRecords
<a name="API_UpdateRecords"></a>

**Note**
Amazon Cognito Sync is no longer open to new customers. For alternatives to Cognito Sync, please explore [AWS AppSync](https://aws.amazon.com/appsync/) and [Amazon DynamoDB](https://aws.amazon.com/dynamodb/). [Learn more](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-sync-availability-change.html).

Posts updates to records and adds and deletes records for a dataset and user.

The sync count in the record patch is your last known sync count for that record. The server will reject an UpdateRecords request with a ResourceConflictException if you try to patch a record with a new value but a stale sync count.

For example, if the sync count on the server is 5 for a key called highScore and you try and submit a new highScore with sync count of 4, the request will be rejected. To obtain the current sync count for a record, call ListRecords. On a successful update of the record, the response returns the new sync count for that record. You should present that sync count the next time you try to update that same record. When the record does not exist, specify the sync count as 0.

This API can be called with temporary user credentials provided by Cognito Identity or with developer credentials.

## Request Syntax
<a name="API_UpdateRecords_RequestSyntax"></a>

```
POST /identitypools/{{IdentityPoolId}}/identities/{{IdentityId}}/datasets/{{DatasetName}} HTTP/1.1
x-amz-Client-Context: {{ClientContext}}
Content-type: application/json

{
   "DeviceId": "{{string}}",
   "RecordPatches": [
      {
         "DeviceLastModifiedDate": {{number}},
         "Key": "{{string}}",
         "Op": "{{string}}",
         "SyncCount": {{number}},
         "Value": "{{string}}"
      }
   ],
   "SyncSessionToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateRecords_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ClientContext](#API_UpdateRecords_RequestSyntax) **   <a name="Cognito-UpdateRecords-request-ClientContext"></a>
Intended to supply a device ID that will populate the lastModifiedBy field referenced in other methods. The ClientContext field is not yet implemented.

 ** [DatasetName](#API_UpdateRecords_RequestSyntax) **   <a name="Cognito-UpdateRecords-request-uri-DatasetName"></a>
A string of up to 128 characters. Allowed characters are a-z, A-Z, 0-9, '\_' (underscore), '-' (dash), and '.' (dot).
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_.:-]+`
Required: Yes

 ** [IdentityId](#API_UpdateRecords_RequestSyntax) **   <a name="Cognito-UpdateRecords-request-uri-IdentityId"></a>
A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
Length Constraints: Minimum length of 1. Maximum length of 55.
Pattern: `[\w-]+:[0-9a-f-]+`
Required: Yes

 ** [IdentityPoolId](#API_UpdateRecords_RequestSyntax) **   <a name="Cognito-UpdateRecords-request-uri-IdentityPoolId"></a>
A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
Length Constraints: Minimum length of 1. Maximum length of 55.
Pattern: `[\w-]+:[0-9a-f-]+`
Required: Yes

## Request Body
<a name="API_UpdateRecords_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [DeviceId](#API_UpdateRecords_RequestSyntax) **   <a name="Cognito-UpdateRecords-request-DeviceId"></a>
The unique ID generated for this device by Cognito.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** [RecordPatches](#API_UpdateRecords_RequestSyntax) **   <a name="Cognito-UpdateRecords-request-RecordPatches"></a>
A list of patch operations.
Type: Array of [RecordPatch](API_RecordPatch.md) objects
Required: No

 ** [SyncSessionToken](#API_UpdateRecords_RequestSyntax) **   <a name="Cognito-UpdateRecords-request-SyncSessionToken"></a>
The SyncSessionToken returned by a previous call to ListRecords for this dataset and identity.
Type: String
Required: Yes

## Response Syntax
<a name="API_UpdateRecords_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Records": [
      {
         "DeviceLastModifiedDate": number,
         "Key": "string",
         "LastModifiedBy": "string",
         "LastModifiedDate": number,
         "SyncCount": number,
         "Value": "string"
      }
   ]
}
```

## Response Elements
<a name="API_UpdateRecords_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Records](#API_UpdateRecords_ResponseSyntax) **   <a name="Cognito-UpdateRecords-response-Records"></a>
A list of records that have been updated.
Type: Array of [Record](API_Record.md) objects

## Errors
<a name="API_UpdateRecords_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalErrorException **
Indicates an internal service error.
 ** message **
Message returned by InternalErrorException.
HTTP Status Code: 500

 ** InvalidLambdaFunctionOutputException **
The AWS Lambda function returned invalid output or an exception.
 ** message **
A message returned when an InvalidLambdaFunctionOutputException occurs
HTTP Status Code: 400

 ** InvalidParameterException **
Thrown when a request parameter does not comply with the associated constraints.
 ** message **
Message returned by InvalidParameterException.
HTTP Status Code: 400

 ** LambdaSocketTimeoutException **
This exception is thrown when your Lambda function fails to respond within 5 seconds. For more information, see [Amazon Cognito Events](http://docs.aws.amazon.com/cognito/latest/developerguide/cognito-events.html).
HTTP Status Code: 400

 ** LambdaThrottledException **
AWS Lambda throttled your account, please contact AWS Support
 ** message **
A message returned when an LambdaThrottledException is thrown
HTTP Status Code: 429

 ** LimitExceededException **
Thrown when the limit on the number of objects or operations has been exceeded.
 ** message **
Message returned by LimitExceededException.
HTTP Status Code: 400

 ** NotAuthorizedException **
Thrown when a user is not authorized to access the requested resource.
 ** message **
The message returned by a NotAuthorizedException.
HTTP Status Code: 403

 ** ResourceConflictException **
Thrown if an update can't be applied because the resource was changed by another call and this would result in a conflict.
 ** message **
The message returned by a ResourceConflictException.
HTTP Status Code: 409

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
<a name="API_UpdateRecords_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cognito-sync-2014-06-30/UpdateRecords)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cognito-sync-2014-06-30/UpdateRecords)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-sync-2014-06-30/UpdateRecords)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cognito-sync-2014-06-30/UpdateRecords)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-sync-2014-06-30/UpdateRecords)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cognito-sync-2014-06-30/UpdateRecords)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cognito-sync-2014-06-30/UpdateRecords)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cognito-sync-2014-06-30/UpdateRecords)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cognito-sync-2014-06-30/UpdateRecords)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-sync-2014-06-30/UpdateRecords)
