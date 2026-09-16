---
source_url: https://docs.aws.amazon.com/mgn/latest/APIReference/API_StartCutover.html
---

# StartCutover
<a name="API_StartCutover"></a>

Launches a Cutover Instance for specific Source Servers. This command starts a LAUNCH job whose initiatedBy property is StartCutover and changes the SourceServer.lifeCycle.state property to CUTTING\_OVER.

## Request Syntax
<a name="API_StartCutover_RequestSyntax"></a>

```
POST /StartCutover HTTP/1.1
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
<a name="API_StartCutover_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_StartCutover_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [accountID](#API_StartCutover_RequestSyntax) **   <a name="mgn-StartCutover-request-accountID"></a>
Start Cutover by Account IDs
Type: String
Length Constraints: Fixed length of 12.
Pattern: `.*[0-9]{12,}.*`
Required: No

 ** [sourceServerIDs](#API_StartCutover_RequestSyntax) **   <a name="mgn-StartCutover-request-sourceServerIDs"></a>
Start Cutover by Source Server IDs.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 200 items.
Length Constraints: Fixed length of 19.
Pattern: `s-[0-9a-zA-Z]{17}`
Required: Yes

 ** [tags](#API_StartCutover_RequestSyntax) **   <a name="mgn-StartCutover-request-tags"></a>
Start Cutover by Tags.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 0. Maximum length of 256.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_StartCutover_ResponseSyntax"></a>

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
<a name="API_StartCutover_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [job](#API_StartCutover_ResponseSyntax) **   <a name="mgn-StartCutover-response-job"></a>
Start Cutover Job response.
Type: [Job](API_Job.md) object

## Errors
<a name="API_StartCutover_Errors"></a>

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
<a name="API_StartCutover_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mgn-2020-02-26/StartCutover)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mgn-2020-02-26/StartCutover)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mgn-2020-02-26/StartCutover)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mgn-2020-02-26/StartCutover)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mgn-2020-02-26/StartCutover)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mgn-2020-02-26/StartCutover)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mgn-2020-02-26/StartCutover)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mgn-2020-02-26/StartCutover)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/mgn-2020-02-26/StartCutover)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mgn-2020-02-26/StartCutover)
