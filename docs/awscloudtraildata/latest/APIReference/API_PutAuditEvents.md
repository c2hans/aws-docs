---
source_url: https://docs.aws.amazon.com/awscloudtraildata/latest/APIReference/API_PutAuditEvents.html
---

# PutAuditEvents
<a name="API_PutAuditEvents"></a>

Ingests your application events into CloudTrail Lake. A required parameter, `auditEvents`, accepts the JSON records (also called *payload*) of events that you want CloudTrail to ingest. You can add up to 100 of these events (or up to 1 MB) per `PutAuditEvents` request.

## Request Syntax
<a name="API_PutAuditEvents_RequestSyntax"></a>

```
POST /PutAuditEvents?channelArn={{channelArn}}&externalId={{externalId}} HTTP/1.1
Content-type: application/json

{
   "auditEvents": [
      {
         "eventData": "{{string}}",
         "eventDataChecksum": "{{string}}",
         "id": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_PutAuditEvents_RequestParameters"></a>

The request uses the following URI parameters.

 ** [channelArn](#API_PutAuditEvents_RequestSyntax) **   <a name="awscloudtraildata-PutAuditEvents-request-uri-channelArn"></a>
The ARN or ID (the ARN suffix) of a channel.
Pattern: `arn:.*`
Required: Yes

 ** [externalId](#API_PutAuditEvents_RequestSyntax) **   <a name="awscloudtraildata-PutAuditEvents-request-uri-externalId"></a>
A unique identifier that is conditionally required when the channel's resource policy includes an external ID. This value can be any string, such as a passphrase or account number.
Length Constraints: Minimum length of 2. Maximum length of 1224.
Pattern: `[\w+=,.@:\/-]*`

## Request Body
<a name="API_PutAuditEvents_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [auditEvents](#API_PutAuditEvents_RequestSyntax) **   <a name="awscloudtraildata-PutAuditEvents-request-auditEvents"></a>
The JSON payload of events that you want to ingest. You can also point to the JSON event payload in a file.
Type: Array of [AuditEvent](API_AuditEvent.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: Yes

## Response Syntax
<a name="API_PutAuditEvents_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "failed": [
      {
         "errorCode": "string",
         "errorMessage": "string",
         "id": "string"
      }
   ],
   "successful": [
      {
         "eventID": "string",
         "id": "string"
      }
   ]
}
```

## Response Elements
<a name="API_PutAuditEvents_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [failed](#API_PutAuditEvents_ResponseSyntax) **   <a name="awscloudtraildata-PutAuditEvents-response-failed"></a>
Lists events in the provided event payload that could not be ingested into CloudTrail, and includes the error code and error message returned for events that could not be ingested.
Type: Array of [ResultErrorEntry](API_ResultErrorEntry.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.

 ** [successful](#API_PutAuditEvents_ResponseSyntax) **   <a name="awscloudtraildata-PutAuditEvents-response-successful"></a>
Lists events in the provided event payload that were successfully ingested into CloudTrail.
Type: Array of [AuditEventResultEntry](API_AuditEventResultEntry.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.

## Errors
<a name="API_PutAuditEvents_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ChannelInsufficientPermission **
The caller's account ID must be the same as the channel owner's account ID.
HTTP Status Code: 400

 ** ChannelNotFound **
The channel could not be found.
HTTP Status Code: 400

 ** ChannelUnsupportedSchema **
The schema type of the event is not supported.
HTTP Status Code: 400

 ** DuplicatedAuditEventId **
Two or more entries in the request have the same event ID.
HTTP Status Code: 400

 ** InvalidChannelARN **
The specified channel ARN is not a valid channel ARN.
HTTP Status Code: 400

 ** UnsupportedOperationException **
The operation requested is not supported in this region or account.
HTTP Status Code: 400

## See Also
<a name="API_PutAuditEvents_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudtrail-data-2021-08-11/PutAuditEvents)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudtrail-data-2021-08-11/PutAuditEvents)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-data-2021-08-11/PutAuditEvents)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudtrail-data-2021-08-11/PutAuditEvents)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-data-2021-08-11/PutAuditEvents)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudtrail-data-2021-08-11/PutAuditEvents)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudtrail-data-2021-08-11/PutAuditEvents)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudtrail-data-2021-08-11/PutAuditEvents)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudtrail-data-2021-08-11/PutAuditEvents)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-data-2021-08-11/PutAuditEvents)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudTrail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query awscloudtraildata` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
