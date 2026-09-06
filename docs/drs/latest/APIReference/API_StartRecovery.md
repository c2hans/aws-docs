---
source_url: https://docs.aws.amazon.com/drs/latest/APIReference/API_StartRecovery.html
---

# StartRecovery
<a name="API_StartRecovery"></a>

Launches Recovery Instances for the specified Source Servers. For each Source Server you may choose a point in time snapshot to launch from, or use an on demand snapshot.

## Request Syntax
<a name="API_StartRecovery_RequestSyntax"></a>

```
POST /StartRecovery HTTP/1.1
Content-type: application/json

{
   "isDrill": {{boolean}},
   "sourceServers": [
      {
         "recoverySnapshotID": "{{string}}",
         "sourceServerID": "{{string}}"
      }
   ],
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_StartRecovery_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_StartRecovery_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [isDrill](#API_StartRecovery_RequestSyntax) **   <a name="drs-StartRecovery-request-isDrill"></a>
Whether this Source Server Recovery operation is a drill or not.
Type: Boolean
Required: No

 ** [sourceServers](#API_StartRecovery_RequestSyntax) **   <a name="drs-StartRecovery-request-sourceServers"></a>
The Source Servers that we want to start a Recovery Job for.
Type: Array of [StartRecoveryRequestSourceServer](API_StartRecoveryRequestSourceServer.md) objects
Array Members: Minimum number of 1 item. Maximum number of 200 items.
Required: Yes

 ** [tags](#API_StartRecovery_RequestSyntax) **   <a name="drs-StartRecovery-request-tags"></a>
The tags to be associated with the Recovery Job.
Type: String to string map
Key Length Constraints: Minimum length of 0. Maximum length of 256.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_StartRecovery_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "job": {
      "arn": "string",
      "creationDateTime": "string",
      "endDateTime": "string",
      "initiatedBy": "string",
      "jobID": "string",
      "participatingResources": [
         {
            "launchStatus": "string",
            "participatingResourceID": { ... }
         }
      ],
      "participatingServers": [
         {
            "launchActionsStatus": {
               "runs": [
                  {
                     "action": {
                        "actionCode": "string",
                        "actionId": "string",
                        "actionVersion": "string",
                        "active": boolean,
                        "category": "string",
                        "description": "string",
                        "name": "string",
                        "optional": boolean,
                        "order": number,
                        "parameters": {
                           "string" : {
                              "type": "string",
                              "value": "string"
                           }
                        },
                        "type": "string"
                     },
                     "failureReason": "string",
                     "runId": "string",
                     "status": "string"
                  }
               ],
               "ssmAgentDiscoveryDatetime": "string"
            },
            "launchStatus": "string",
            "recoveryInstanceID": "string",
            "sourceServerID": "string"
         }
      ],
      "status": "string",
      "tags": {
         "string" : "string"
      },
      "type": "string"
   }
}
```

## Response Elements
<a name="API_StartRecovery_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [job](#API_StartRecovery_ResponseSyntax) **   <a name="drs-StartRecovery-response-job"></a>
The Recovery Job.
Type: [Job](API_Job.md) object

## Errors
<a name="API_StartRecovery_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
The request could not be completed due to a conflict with the current state of the target resource.
 ** resourceId **
The ID of the resource.
 ** resourceType **
The type of the resource.
HTTP Status Code: 409

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure.
 ** retryAfterSeconds **
The number of seconds after which the request should be safe to retry.
HTTP Status Code: 500

 ** ServiceQuotaExceededException **
The request could not be completed because its exceeded the service quota.
 ** quotaCode **
Quota code.
 ** resourceId **
The ID of the resource.
 ** resourceType **
The type of the resource.
 ** serviceCode **
Service code.
HTTP Status Code: 402

 ** ThrottlingException **
The request was denied due to request throttling.
 ** quotaCode **
Quota code.
 ** retryAfterSeconds **
The number of seconds after which the request should be safe to retry.
 ** serviceCode **
Service code.
HTTP Status Code: 429

 ** UninitializedAccountException **
The account performing the request has not been initialized.
HTTP Status Code: 400

## See Also
<a name="API_StartRecovery_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/drs-2020-02-26/StartRecovery)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/drs-2020-02-26/StartRecovery)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/drs-2020-02-26/StartRecovery)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/drs-2020-02-26/StartRecovery)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/drs-2020-02-26/StartRecovery)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/drs-2020-02-26/StartRecovery)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/drs-2020-02-26/StartRecovery)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/drs-2020-02-26/StartRecovery)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/drs-2020-02-26/StartRecovery)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/drs-2020-02-26/StartRecovery)
