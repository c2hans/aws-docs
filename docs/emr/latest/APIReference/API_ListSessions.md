---
source_url: https://docs.aws.amazon.com/emr/latest/APIReference/API_ListSessions.html
---

# ListSessions
<a name="API_ListSessions"></a>

Lists the sessions on a cluster. You can filter the results by session state. Newer sessions are returned first.

## Request Syntax
<a name="API_ListSessions_RequestSyntax"></a>

```
{
   "ClusterId": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "SessionStates": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_ListSessions_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClusterId](#API_ListSessions_RequestSyntax) **   <a name="EMR-ListSessions-request-ClusterId"></a>
The ID of the cluster to list sessions for.
Type: String
Length Constraints: Maximum length of 256.
Required: Yes

 ** [MaxResults](#API_ListSessions_RequestSyntax) **   <a name="EMR-ListSessions-request-MaxResults"></a>
The maximum number of sessions to return in each page of results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListSessions_RequestSyntax) **   <a name="EMR-ListSessions-request-NextToken"></a>
The pagination token returned by a previous `ListSessions` call. Use it to retrieve the next page of results.
Type: String
Required: No

 ** [SessionStates](#API_ListSessions_RequestSyntax) **   <a name="EMR-ListSessions-request-SessionStates"></a>
An optional filter that limits the results to sessions in the specified states.
Type: Array of strings
Valid Values: `SUBMITTED | STARTING | STARTED | IDLE | BUSY | TERMINATING | TERMINATED | FAILED`
Required: No

## Response Syntax
<a name="API_ListSessions_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "Sessions": [
      {
         "AccountId": "string",
         "Arn": "string",
         "ClusterId": "string",
         "CreatedAt": number,
         "EndedAt": number,
         "EngineConfigurations": [
            {
               "Classification": "string",
               "Configurations": [
                  "Configuration"
               ],
               "Properties": {
                  "string" : "string"
               }
            }
         ],
         "ExecutionRoleArn": "string",
         "Id": "string",
         "IdleSince": number,
         "MonitoringConfiguration": {
            "CloudWatchLoggingConfiguration": {
               "Enabled": boolean,
               "EncryptionKeyArn": "string",
               "LogGroup": "string",
               "LogStreamNamePrefix": "string",
               "LogTypes": {
                  "string" : [ "string" ]
               }
            },
            "ManagedLoggingConfiguration": {
               "Enabled": boolean,
               "EncryptionKeyArn": "string"
            },
            "S3LoggingConfiguration": {
               "Enabled": boolean,
               "EncryptionKeyArn": "string",
               "LogTypes": {
                  "string" : [ "string" ]
               },
               "LogUri": "string"
            }
         },
         "Name": "string",
         "ReleaseLabel": "string",
         "ServerUrl": "string",
         "SessionIdleTimeoutInMinutes": number,
         "StartedAt": number,
         "State": "string",
         "StateChangeReason": "string",
         "Tags": [
            {
               "Key": "string",
               "Value": "string"
            }
         ],
         "UpdatedAt": number
      }
   ]
}
```

## Response Elements
<a name="API_ListSessions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListSessions_ResponseSyntax) **   <a name="EMR-ListSessions-response-NextToken"></a>
The pagination token to use in a subsequent `ListSessions` call to retrieve the next page of results. This field is absent when there are no more results.
Type: String

 ** [Sessions](#API_ListSessions_ResponseSyntax) **   <a name="EMR-ListSessions-response-Sessions"></a>
The sessions that match the request.
Type: Array of [Session](API_Session.md) objects

## Errors
<a name="API_ListSessions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
This exception occurs when there is an internal failure in the Amazon EMR service.
 ** Message **
The message associated with the exception.
HTTP Status Code: 500

 ** InvalidRequestException **
This exception occurs when there is something wrong with user input.
 ** ErrorCode **
The error code associated with the exception.
 ** Message **
The message associated with the exception.
HTTP Status Code: 400

## See Also
<a name="API_ListSessions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticmapreduce-2009-03-31/ListSessions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticmapreduce-2009-03-31/ListSessions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/ListSessions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticmapreduce-2009-03-31/ListSessions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/ListSessions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticmapreduce-2009-03-31/ListSessions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticmapreduce-2009-03-31/ListSessions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticmapreduce-2009-03-31/ListSessions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticmapreduce-2009-03-31/ListSessions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/ListSessions)
