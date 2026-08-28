---
source_url: https://docs.aws.amazon.com/mgn/latest/APIReference/API_TerminateTargetInstances.html
---

# TerminateTargetInstances
<a name="API_TerminateTargetInstances"></a>

Starts a job that terminates specific launched EC2 Test and Cutover instances. This command will not work for any Source Server with a lifecycle.state of TESTING, CUTTING\_OVER, or CUTOVER.

## Request Syntax
<a name="API_TerminateTargetInstances_RequestSyntax"></a>

```
POST /TerminateTargetInstances HTTP/1.1
Content-type: application/json

{
   "accountID": "{{string}}",
   "sourceServerIDs": [ "{{string}}" ],
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_TerminateTargetInstances_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_TerminateTargetInstances_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [accountID](#API_TerminateTargetInstances_RequestSyntax) **   <a name="mgn-TerminateTargetInstances-request-accountID"></a>
Terminate Target instance by Account ID
Type: String
Length Constraints: Fixed length of 12.
Pattern: `.*[0-9]{12,}.*`
Required: No

 ** [sourceServerIDs](#API_TerminateTargetInstances_RequestSyntax) **   <a name="mgn-TerminateTargetInstances-request-sourceServerIDs"></a>
Terminate Target instance by Source Server IDs.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 200 items.
Length Constraints: Fixed length of 19.
Pattern: `s-[0-9a-zA-Z]{17}`
Required: Yes

 ** [tags](#API_TerminateTargetInstances_RequestSyntax) **   <a name="mgn-TerminateTargetInstances-request-tags"></a>
Terminate Target instance by Tags.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 0. Maximum length of 256.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_TerminateTargetInstances_ResponseSyntax"></a>

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
      "participatingServers": [
         {
            "launchedEc2InstanceID": "string",
            "launchStatus": "string",
            "postLaunchActionsStatus": {
               "postLaunchActionsLaunchStatusList": [
                  {
                     "executionID": "string",
                     "executionStatus": "string",
                     "failureReason": "string",
                     "ssmDocument": {
                        "actionName": "string",
                        "externalParameters": {
                           "string" : { ... }
                        },
                        "mustSucceedForCutover": boolean,
                        "parameters": {
                           "string" : [
                              {
                                 "parameterName": "string",
                                 "parameterType": "string"
                              }
                           ]
                        },
                        "ssmDocumentName": "string",
                        "timeoutSeconds": number
                     },
                     "ssmDocumentType": "string"
                  }
               ],
               "ssmAgentDiscoveryDatetime": "string"
            },
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
<a name="API_TerminateTargetInstances_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [job](#API_TerminateTargetInstances_ResponseSyntax) **   <a name="mgn-TerminateTargetInstances-response-job"></a>
Terminate Target instance Job response.
Type: [Job](API_Job.md) object

## Errors
<a name="API_TerminateTargetInstances_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
The request could not be completed due to a conflict with the current state of the target resource.
 ** errors **
Conflict Exception specific errors.
 ** resourceId **
A conflict occurred when prompting for the Resource ID.
 ** resourceType **
A conflict occurred when prompting for resource type.
HTTP Status Code: 409

 ** UninitializedAccountException **
Uninitialized account exception.
HTTP Status Code: 400

 ** ValidationException **
Validate exception.
 ** fieldList **
Validate exception field list.
 ** reason **
Validate exception reason.
HTTP Status Code: 400

## See Also
<a name="API_TerminateTargetInstances_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mgn-2020-02-26/TerminateTargetInstances)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mgn-2020-02-26/TerminateTargetInstances)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mgn-2020-02-26/TerminateTargetInstances)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mgn-2020-02-26/TerminateTargetInstances)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mgn-2020-02-26/TerminateTargetInstances)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mgn-2020-02-26/TerminateTargetInstances)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mgn-2020-02-26/TerminateTargetInstances)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mgn-2020-02-26/TerminateTargetInstances)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mgn-2020-02-26/TerminateTargetInstances)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mgn-2020-02-26/TerminateTargetInstances)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for ApplicationMigrationService. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mgn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
