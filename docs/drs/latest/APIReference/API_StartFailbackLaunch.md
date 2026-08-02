---
source_url: https://docs.aws.amazon.com/drs/latest/APIReference/API_StartFailbackLaunch.html
---

# StartFailbackLaunch
<a name="API_StartFailbackLaunch"></a>

Initiates a Job for launching the machine that is being failed back to from the specified Recovery Instance. This will run conversion on the failback client and will reboot your machine, thus completing the failback process.

## Request Syntax
<a name="API_StartFailbackLaunch_RequestSyntax"></a>

```
POST /StartFailbackLaunch HTTP/1.1
Content-type: application/json

{
   "recoveryInstanceIDs": [ "{{string}}" ],
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_StartFailbackLaunch_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_StartFailbackLaunch_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [recoveryInstanceIDs](#API_StartFailbackLaunch_RequestSyntax) **   <a name="drs-StartFailbackLaunch-request-recoveryInstanceIDs"></a>
The IDs of the Recovery Instance whose failback launch we want to request.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 200 items.
Length Constraints: Minimum length of 10. Maximum length of 19.
Pattern: `i-[0-9a-fA-F]{8,}`
Required: Yes

 ** [tags](#API_StartFailbackLaunch_RequestSyntax) **   <a name="drs-StartFailbackLaunch-request-tags"></a>
The tags to be associated with the failback launch Job.
Type: String to string map
Key Length Constraints: Minimum length of 0. Maximum length of 256.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_StartFailbackLaunch_ResponseSyntax"></a>

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
<a name="API_StartFailbackLaunch_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [job](#API_StartFailbackLaunch_ResponseSyntax) **   <a name="drs-StartFailbackLaunch-response-job"></a>
The failback launch Job.
Type: [Job](API_Job.md) object

## Errors
<a name="API_StartFailbackLaunch_Errors"></a>

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

 ** ValidationException **
The input fails to satisfy the constraints specified by the AWS service.
 ** fieldList **
A list of fields that failed validation.
 ** reason **
Validation exception reason.
HTTP Status Code: 400

## See Also
<a name="API_StartFailbackLaunch_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/drs-2020-02-26/StartFailbackLaunch)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/drs-2020-02-26/StartFailbackLaunch)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/drs-2020-02-26/StartFailbackLaunch)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/drs-2020-02-26/StartFailbackLaunch)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/drs-2020-02-26/StartFailbackLaunch)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/drs-2020-02-26/StartFailbackLaunch)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/drs-2020-02-26/StartFailbackLaunch)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/drs-2020-02-26/StartFailbackLaunch)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/drs-2020-02-26/StartFailbackLaunch)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/drs-2020-02-26/StartFailbackLaunch)
