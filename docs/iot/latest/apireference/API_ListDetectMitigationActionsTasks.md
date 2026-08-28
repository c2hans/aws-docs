---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_ListDetectMitigationActionsTasks.html
---

# ListDetectMitigationActionsTasks
<a name="API_ListDetectMitigationActionsTasks"></a>

**Note**
The AWS IoT Device Defender detect feature will no longer be available to new customers starting August 31, 2026. If you would like to use the detect feature, sign up prior to August 31, 2026. To learn about alternatives to AWS IoT Device Defender detect, see [AWS IoT Device Defender detect feature availability change](https://docs.aws.amazon.com/iot-device-defender/latest/devguide/dd-detect-availability-change.html). There is no change to AWS IoT Device Defender audit availability.

 List of Device Defender ML Detect mitigation actions tasks.

Requires permission to access the [ListDetectMitigationActionsTasks](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_ListDetectMitigationActionsTasks_RequestSyntax"></a>

```
GET /detect/mitigationactions/tasks?endTime={{endTime}}&maxResults={{maxResults}}&nextToken={{nextToken}}&startTime={{startTime}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListDetectMitigationActionsTasks_RequestParameters"></a>

The request uses the following URI parameters.

 ** [endTime](#API_ListDetectMitigationActionsTasks_RequestSyntax) **   <a name="iot-ListDetectMitigationActionsTasks-request-uri-endTime"></a>
 The end of the time period for which ML Detect mitigation actions tasks are returned.
Required: Yes

 ** [maxResults](#API_ListDetectMitigationActionsTasks_RequestSyntax) **   <a name="iot-ListDetectMitigationActionsTasks-request-uri-maxResults"></a>
The maximum number of results to return at one time. The default is 25.
Valid Range: Minimum value of 1. Maximum value of 250.

 ** [nextToken](#API_ListDetectMitigationActionsTasks_RequestSyntax) **   <a name="iot-ListDetectMitigationActionsTasks-request-uri-nextToken"></a>
 The token for the next set of results.

 ** [startTime](#API_ListDetectMitigationActionsTasks_RequestSyntax) **   <a name="iot-ListDetectMitigationActionsTasks-request-uri-startTime"></a>
 A filter to limit results to those found after the specified time. You must specify either the startTime and endTime or the taskId, but not both.
Required: Yes

## Request Body
<a name="API_ListDetectMitigationActionsTasks_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListDetectMitigationActionsTasks_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "tasks": [
      {
         "actionsDefinition": [
            {
               "actionParams": {
                  "addThingsToThingGroupParams": {
                     "overrideDynamicGroups": boolean,
                     "thingGroupNames": [ "string" ]
                  },
                  "enableIoTLoggingParams": {
                     "logLevel": "string",
                     "roleArnForLogging": "string"
                  },
                  "publishFindingToSnsParams": {
                     "topicArn": "string"
                  },
                  "replaceDefaultPolicyVersionParams": {
                     "templateName": "string"
                  },
                  "updateCACertificateParams": {
                     "action": "string"
                  },
                  "updateDeviceCertificateParams": {
                     "action": "string"
                  }
               },
               "id": "string",
               "name": "string",
               "roleArn": "string"
            }
         ],
         "onlyActiveViolationsIncluded": boolean,
         "suppressedAlertsIncluded": boolean,
         "target": {
            "behaviorName": "string",
            "securityProfileName": "string",
            "violationIds": [ "string" ]
         },
         "taskEndTime": number,
         "taskId": "string",
         "taskStartTime": number,
         "taskStatistics": {
            "actionsExecuted": number,
            "actionsFailed": number,
            "actionsSkipped": number
         },
         "taskStatus": "string",
         "violationEventOccurrenceRange": {
            "endTime": number,
            "startTime": number
         }
      }
   ]
}
```

## Response Elements
<a name="API_ListDetectMitigationActionsTasks_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListDetectMitigationActionsTasks_ResponseSyntax) **   <a name="iot-ListDetectMitigationActionsTasks-response-nextToken"></a>
 A token that can be used to retrieve the next set of results, or `null` if there are no additional results.
Type: String

 ** [tasks](#API_ListDetectMitigationActionsTasks_ResponseSyntax) **   <a name="iot-ListDetectMitigationActionsTasks-response-tasks"></a>
 The collection of ML Detect mitigation tasks that matched the filter criteria.
Type: Array of [DetectMitigationActionsTaskSummary](API_DetectMitigationActionsTaskSummary.md) objects

## Errors
<a name="API_ListDetectMitigationActionsTasks_Errors"></a>

 ** InternalFailureException **
An unexpected error has occurred.
 ** message **
The message for the exception.
HTTP Status Code: 500

 ** InvalidRequestException **
The request is not valid.
 ** message **
The message for the exception.
HTTP Status Code: 400

 ** ThrottlingException **
The rate exceeds the limit.
 ** message **
The message for the exception.
HTTP Status Code: 400

## See Also
<a name="API_ListDetectMitigationActionsTasks_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/ListDetectMitigationActionsTasks)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/ListDetectMitigationActionsTasks)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/ListDetectMitigationActionsTasks)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/ListDetectMitigationActionsTasks)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/ListDetectMitigationActionsTasks)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/ListDetectMitigationActionsTasks)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/ListDetectMitigationActionsTasks)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/ListDetectMitigationActionsTasks)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/ListDetectMitigationActionsTasks)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/ListDetectMitigationActionsTasks)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
