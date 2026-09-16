---
source_url: https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_ListIngestConfigurations.html
---

# ListIngestConfigurations
<a name="API_ListIngestConfigurations"></a>

Lists all IngestConfigurations in your account, in the AWS region where the API request is processed.

## Request Syntax
<a name="API_ListIngestConfigurations_RequestSyntax"></a>

```
POST /ListIngestConfigurations HTTP/1.1
Content-type: application/json

{
   "filterByStageArn": "{{string}}",
   "filterByState": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListIngestConfigurations_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListIngestConfigurations_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [filterByStageArn](#API_ListIngestConfigurations_RequestSyntax) **   <a name="ivsrealtimeeapireference-ListIngestConfigurations-request-filterByStageArn"></a>
Filters the response list to match the specified stage ARN. Only one filter (by stage ARN or by state) can be used at a time.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:aws:ivs:[a-z0-9-]+:[0-9]+:stage/[a-zA-Z0-9-]+`
Required: No

 ** [filterByState](#API_ListIngestConfigurations_RequestSyntax) **   <a name="ivsrealtimeeapireference-ListIngestConfigurations-request-filterByState"></a>
Filters the response list to match the specified state. Only one filter (by stage ARN or by state) can be used at a time.
Type: String
Valid Values: `ACTIVE | INACTIVE`
Required: No

 ** [maxResults](#API_ListIngestConfigurations_RequestSyntax) **   <a name="ivsrealtimeeapireference-ListIngestConfigurations-request-maxResults"></a>
Maximum number of results to return. Default: 50.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_ListIngestConfigurations_RequestSyntax) **   <a name="ivsrealtimeeapireference-ListIngestConfigurations-request-nextToken"></a>
The first IngestConfiguration to retrieve. This is used for pagination; see the `nextToken` response field.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[a-zA-Z0-9+/=_-]*`
Required: No

## Response Syntax
<a name="API_ListIngestConfigurations_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ingestConfigurations": [
      {
         "arn": "string",
         "ingestProtocol": "string",
         "name": "string",
         "participantId": "string",
         "redundantIngest": boolean,
         "stageArn": "string",
         "state": "string",
         "userId": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListIngestConfigurations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ingestConfigurations](#API_ListIngestConfigurations_ResponseSyntax) **   <a name="ivsrealtimeeapireference-ListIngestConfigurations-response-ingestConfigurations"></a>
List of the matching ingest configurations (summary information only).
Type: Array of [IngestConfigurationSummary](API_IngestConfigurationSummary.md) objects

 ** [nextToken](#API_ListIngestConfigurations_ResponseSyntax) **   <a name="ivsrealtimeeapireference-ListIngestConfigurations-response-nextToken"></a>
If there are more IngestConfigurations than `maxResults`, use `nextToken` in the request to get the next set.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[a-zA-Z0-9+/=_-]*`

## Errors
<a name="API_ListIngestConfigurations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **

 ** exceptionMessage **
User does not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ValidationException **

 ** exceptionMessage **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_ListIngestConfigurations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ivs-realtime-2020-07-14/ListIngestConfigurations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ivs-realtime-2020-07-14/ListIngestConfigurations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ivs-realtime-2020-07-14/ListIngestConfigurations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ivs-realtime-2020-07-14/ListIngestConfigurations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ivs-realtime-2020-07-14/ListIngestConfigurations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ivs-realtime-2020-07-14/ListIngestConfigurations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ivs-realtime-2020-07-14/ListIngestConfigurations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ivs-realtime-2020-07-14/ListIngestConfigurations)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ivs-realtime-2020-07-14/ListIngestConfigurations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ivs-realtime-2020-07-14/ListIngestConfigurations)
