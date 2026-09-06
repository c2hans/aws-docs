---
source_url: https://docs.aws.amazon.com/drs/latest/APIReference/API_TerminateRecoveryInstances.html
---

# TerminateRecoveryInstances
<a name="API_TerminateRecoveryInstances"></a>

Initiates a Job for terminating the EC2 resources associated with the specified Recovery Instances, and then will delete the Recovery Instances from the Elastic Disaster Recovery service.

## Request Syntax
<a name="API_TerminateRecoveryInstances_RequestSyntax"></a>

```
POST /TerminateRecoveryInstances HTTP/1.1
Content-type: application/json

{
   "recoveryInstanceIDs": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_TerminateRecoveryInstances_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_TerminateRecoveryInstances_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [recoveryInstanceIDs](#API_TerminateRecoveryInstances_RequestSyntax) **   <a name="drs-TerminateRecoveryInstances-request-recoveryInstanceIDs"></a>
The IDs of the Recovery Instances that should be terminated.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 200 items.
Length Constraints: Minimum length of 10. Maximum length of 19.
Pattern: `i-[0-9a-fA-F]{8,}`
Required: Yes

## Response Syntax
<a name="API_TerminateRecoveryInstances_ResponseSyntax"></a>

```
HTTP/1.1 200
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
<a name="API_TerminateRecoveryInstances_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [job](#API_TerminateRecoveryInstances_ResponseSyntax) **   <a name="drs-TerminateRecoveryInstances-response-job"></a>
The Job for terminating the Recovery Instances.
Type: [Job](API_Job.md) object

## Errors
<a name="API_TerminateRecoveryInstances_Errors"></a>

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
<a name="API_TerminateRecoveryInstances_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/drs-2020-02-26/TerminateRecoveryInstances)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/drs-2020-02-26/TerminateRecoveryInstances)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/drs-2020-02-26/TerminateRecoveryInstances)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/drs-2020-02-26/TerminateRecoveryInstances)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/drs-2020-02-26/TerminateRecoveryInstances)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/drs-2020-02-26/TerminateRecoveryInstances)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/drs-2020-02-26/TerminateRecoveryInstances)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/drs-2020-02-26/TerminateRecoveryInstances)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/drs-2020-02-26/TerminateRecoveryInstances)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/drs-2020-02-26/TerminateRecoveryInstances)
