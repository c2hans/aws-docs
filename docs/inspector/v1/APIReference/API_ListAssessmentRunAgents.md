---
source_url: https://docs.aws.amazon.com/inspector/v1/APIReference/API_ListAssessmentRunAgents.html
---

# ListAssessmentRunAgents
<a name="API_ListAssessmentRunAgents"></a>

**Important**
End of support notice: On May 20, 2026, AWS will end support for (Amazon Inspector Classic). After May 20, 2026, you will no longer be able to access the Amazon Inspector Classic console or Amazon Inspector Classic resources. For more information, see [Amazon Inspector Classic end of support](https://docs.aws.amazon.com/inspector/v1/userguide/inspector-migration.html).

Lists the agents of the assessment runs that are specified by the ARNs of the assessment runs.

## Request Syntax
<a name="API_ListAssessmentRunAgents_RequestSyntax"></a>

```
{
   "assessmentRunArn": "{{string}}",
   "filter": {
      "agentHealthCodes": [ "{{string}}" ],
      "agentHealths": [ "{{string}}" ]
   },
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListAssessmentRunAgents_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [assessmentRunArn](#API_ListAssessmentRunAgents_RequestSyntax) **   <a name="Inspector-ListAssessmentRunAgents-request-assessmentRunArn"></a>
The ARN that specifies the assessment run whose agents you want to list.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: Yes

 ** [filter](#API_ListAssessmentRunAgents_RequestSyntax) **   <a name="Inspector-ListAssessmentRunAgents-request-filter"></a>
You can use this parameter to specify a subset of data to be included in the action's response.
For a record to match a filter, all specified filter attributes must match. When multiple values are specified for a filter attribute, any of the values can match.
Type: [AgentFilter](API_AgentFilter.md) object
Required: No

 ** [maxResults](#API_ListAssessmentRunAgents_RequestSyntax) **   <a name="Inspector-ListAssessmentRunAgents-request-maxResults"></a>
You can use this parameter to indicate the maximum number of items that you want in the response. The default value is 10. The maximum value is 500.
Type: Integer
Required: No

 ** [nextToken](#API_ListAssessmentRunAgents_RequestSyntax) **   <a name="Inspector-ListAssessmentRunAgents-request-nextToken"></a>
You can use this parameter when paginating results. Set the value of this parameter to null on your first call to the **ListAssessmentRunAgents** action. Subsequent calls to the action fill **nextToken** in the request with the value of **NextToken** from the previous response to continue listing data.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: No

## Response Syntax
<a name="API_ListAssessmentRunAgents_ResponseSyntax"></a>

```
{
   "assessmentRunAgents": [
      {
         "agentHealth": "string",
         "agentHealthCode": "string",
         "agentHealthDetails": "string",
         "agentId": "string",
         "assessmentRunArn": "string",
         "autoScalingGroup": "string",
         "telemetryMetadata": [
            {
               "count": number,
               "dataSize": number,
               "messageType": "string"
            }
         ]
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListAssessmentRunAgents_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [assessmentRunAgents](#API_ListAssessmentRunAgents_ResponseSyntax) **   <a name="Inspector-ListAssessmentRunAgents-response-assessmentRunAgents"></a>
A list of ARNs that specifies the agents returned by the action.
Type: Array of [AssessmentRunAgent](API_AssessmentRunAgent.md) objects
Array Members: Minimum number of 0 items. Maximum number of 500 items.

 ** [nextToken](#API_ListAssessmentRunAgents_ResponseSyntax) **   <a name="Inspector-ListAssessmentRunAgents-response-nextToken"></a>
 When a response is generated, if there is more data to be listed, this parameter is present in the response and contains the value to use for the **nextToken** parameter in a subsequent pagination request. If there is no more data to be listed, this parameter is set to null.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.

## Errors
<a name="API_ListAssessmentRunAgents_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalException **
Internal server error.
 ** canRetry **
You can immediately retry your request.
 ** message **
Details of the exception error.
HTTP Status Code: 500

 ** InvalidInputException **
The request was rejected because an invalid or out-of-range value was supplied for an input parameter.
 ** canRetry **
You can immediately retry your request.
 ** errorCode **
Code that indicates the type of error that is generated.
 ** message **
Details of the exception error.
HTTP Status Code: 400

 ** NoSuchEntityException **
The request was rejected because it referenced an entity that does not exist. The error code describes the entity.
 ** canRetry **
You can immediately retry your request.
 ** errorCode **
Code that indicates the type of error that is generated.
 ** message **
Details of the exception error.
HTTP Status Code: 400

## Examples
<a name="API_ListAssessmentRunAgents_Examples"></a>

### Example
<a name="API_ListAssessmentRunAgents_Example_1"></a>

This example illustrates one usage of ListAssessmentRunAgents.

#### Sample Request
<a name="API_ListAssessmentRunAgents_Example_1_Request"></a>

```

               POST / HTTP/1.1
               Host: inspector.us-west-2.amazonaws.com
               Accept-Encoding: identity
               Content-Length: 117
               X-Amz-Target: InspectorService.ListAssessmentRunAgents
               X-Amz-Date: 20160323T212138Z
               User-Agent: aws-cli/1.10.12 Python/2.7.9 Windows/7 botocore/1.4.3
               Content-Type: application/x-amz-json-1.1
               Authorization: AUTHPARAMS
               {
                 "assessmentRunArn": "arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq/template/0-4r1V2mAw/run/0-MKkpXXPE"
               }
```

#### Sample Response
<a name="API_ListAssessmentRunAgents_Example_1_Response"></a>

```

               HTTP/1.1 200 OK
               x-amzn-RequestId: 3b752481-f13d-11e5-9f2a-87dc3189b81c
               Content-Type: application/x-amz-json-1.1
               Content-Length: 2206
               Date: Wed, 23 Mar 2016 21:21:39 GMT
               {
                 "assessmentRunAgents": [
                   {
                     "agentHealth": "HEALTHY",
                     "agentHealthCode": "HEALTHY",
                     "agentId": "i-49113b93",
                     "assessmentRunArn": "arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq/template/0-4r1V2mAw/run/0-MKkpXXPE",
                     "telemetryMetadata": [
                       {
                         "count": 2,
                         "dataSize": 345,
                         "messageType": "InspectorDuplicateProcess"
                       },
                       {
                         "count": 3,
                         "dataSize": 255,
                         "messageType": "InspectorTimeEventMsg"
                       },
                       {
                         "count": 4,
                         "dataSize": 1082,
                         "messageType": "InspectorNetworkInterface"
                       },
                       {
                         "count": 2,
                         "dataSize": 349,
                         "messageType": "InspectorDnsEntry"
                       },
                       {
                         "count": 11,
                         "dataSize": 2514,
                         "messageType": "InspectorDirectoryInfoMsg"
                       },
                       {
                         "count": 1,
                         "dataSize": 179,
                         "messageType": "InspectorTcpV6ListeningPort"
                       },
                       {
                         "count": 101,
                         "dataSize": 10949,
                         "messageType": "InspectorTerminal"
                       },
                       {
                         "count": 26,
                         "dataSize": 5916,
                         "messageType": "InspectorUser"
                       },
                       {
                         "count": 282,
                         "dataSize": 32148,
                         "messageType": "InspectorDynamicallyLoadedCodeModule"
                       },
                       {
                         "count": 18,
                         "dataSize": 10172,
                         "messageType": "InspectorCreateProcess"
                       },
                       {
                         "count": 3,
                         "dataSize": 8001,
                         "messageType": "InspectorProcessPerformance"
                       },
                       {
                         "count": 1,
                         "dataSize": 360,
                         "messageType": "InspectorOperatingSystem"
                       },
                       {
                         "count": 6,
                         "dataSize": 546,
                         "messageType": "InspectorStopProcess"
                       },
                       {
                         "count": 1,
                         "dataSize": 1553,
                         "messageType": "InspectorInstanceMetaData"
                       },
                       {
                         "count": 2,
                         "dataSize": 434,
                         "messageType": "InspectorTcpV4Connection"
                       },
                       {
                         "count": 474,
                         "dataSize": 2960322,
                         "messageType": "InspectorPackageInfo"
                       },
                       {
                         "count": 3,
                         "dataSize": 2235,
                         "messageType": "InspectorSystemPerformance"
                       },
                       {
                         "count": 105,
                         "dataSize": 46048,
                         "messageType": "InspectorCodeModule"
                       },
                       {
                         "count": 1,
                         "dataSize": 182,
                         "messageType": "InspectorUdpV6ListeningPort"
                       },
                       {
                         "count": 2,
                         "dataSize": 371,
                         "messageType": "InspectorUdpV4ListeningPort"
                       },
                       {
                         "count": 18,
                         "dataSize": 8362,
                         "messageType": "InspectorKernelModule"
                       },
                       {
                         "count": 29,
                         "dataSize": 48788,
                         "messageType": "InspectorConfigurationInfo"
                       },
                       {
                         "count": 1,
                         "dataSize": 79,
                         "messageType": "InspectorMonitoringStart"
                       },
                       {
                         "count": 5,
                         "dataSize": 0,
                         "messageType": "InspectorSplitMsgBegin"
                       },
                       {
                         "count": 51,
                         "dataSize": 4593,
                         "messageType": "InspectorGroup"
                       },
                       {
                         "count": 1,
                         "dataSize": 184,
                         "messageType": "InspectorTcpV4ListeningPort"
                       },
                       {
                         "count": 1159,
                         "dataSize": 3146579,
                         "messageType": "Total"
                       },
                       {
                         "count": 5,
                         "dataSize": 0,
                         "messageType": "InspectorSplitMsgEnd"
                       },
                       {
                         "count": 1,
                         "dataSize": 612,
                         "messageType": "InspectorLoadImageInProcess"
                       }
                     ]
                   }
                 ]
               }
```

## See Also
<a name="API_ListAssessmentRunAgents_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/inspector-2016-02-16/ListAssessmentRunAgents)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/inspector-2016-02-16/ListAssessmentRunAgents)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector-2016-02-16/ListAssessmentRunAgents)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/inspector-2016-02-16/ListAssessmentRunAgents)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector-2016-02-16/ListAssessmentRunAgents)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/inspector-2016-02-16/ListAssessmentRunAgents)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/inspector-2016-02-16/ListAssessmentRunAgents)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/inspector-2016-02-16/ListAssessmentRunAgents)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/inspector-2016-02-16/ListAssessmentRunAgents)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector-2016-02-16/ListAssessmentRunAgents)
