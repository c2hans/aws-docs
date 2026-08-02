---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_iotdeviceadvisor_ListSuiteDefinitions.html
---

# ListSuiteDefinitions
<a name="API_iotdeviceadvisor_ListSuiteDefinitions"></a>

Lists the Device Advisor test suites you have created.

Requires permission to access the [ListSuiteDefinitions](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_iotdeviceadvisor_ListSuiteDefinitions_RequestSyntax"></a>

```
GET /suiteDefinitions?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_iotdeviceadvisor_ListSuiteDefinitions_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_iotdeviceadvisor_ListSuiteDefinitions_RequestSyntax) **   <a name="iot-iotdeviceadvisor_ListSuiteDefinitions-request-uri-maxResults"></a>
The maximum number of results to return at once.
Valid Range: Minimum value of 1. Maximum value of 50.

 ** [nextToken](#API_iotdeviceadvisor_ListSuiteDefinitions_RequestSyntax) **   <a name="iot-iotdeviceadvisor_ListSuiteDefinitions-request-uri-nextToken"></a>
A token used to get the next set of results.
Length Constraints: Maximum length of 2000.

## Request Body
<a name="API_iotdeviceadvisor_ListSuiteDefinitions_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_iotdeviceadvisor_ListSuiteDefinitions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "suiteDefinitionInformationList": [
      {
         "createdAt": number,
         "defaultDevices": [
            {
               "certificateArn": "string",
               "deviceRoleArn": "string",
               "thingArn": "string"
            }
         ],
         "intendedForQualification": boolean,
         "isLongDurationTest": boolean,
         "protocol": "string",
         "suiteDefinitionId": "string",
         "suiteDefinitionName": "string"
      }
   ]
}
```

## Response Elements
<a name="API_iotdeviceadvisor_ListSuiteDefinitions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_iotdeviceadvisor_ListSuiteDefinitions_ResponseSyntax) **   <a name="iot-iotdeviceadvisor_ListSuiteDefinitions-response-nextToken"></a>
A token used to get the next set of results.
Type: String
Length Constraints: Maximum length of 2000.

 ** [suiteDefinitionInformationList](#API_iotdeviceadvisor_ListSuiteDefinitions_ResponseSyntax) **   <a name="iot-iotdeviceadvisor_ListSuiteDefinitions-response-suiteDefinitionInformationList"></a>
An array of objects that provide summaries of information about the suite definitions in the list.
Type: Array of [SuiteDefinitionInformation](API_iotdeviceadvisor_SuiteDefinitionInformation.md) objects

## Errors
<a name="API_iotdeviceadvisor_ListSuiteDefinitions_Errors"></a>

 ** InternalServerException **
Sends an Internal Failure exception.
 ** message **
Sends an Internal Failure Exception message.
HTTP Status Code: 500

 ** ValidationException **
Sends a validation exception.
 ** message **
Sends a Validation Exception message.
HTTP Status Code: 400

## See Also
<a name="API_iotdeviceadvisor_ListSuiteDefinitions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotdeviceadvisor-2020-09-18/ListSuiteDefinitions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotdeviceadvisor-2020-09-18/ListSuiteDefinitions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotdeviceadvisor-2020-09-18/ListSuiteDefinitions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotdeviceadvisor-2020-09-18/ListSuiteDefinitions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotdeviceadvisor-2020-09-18/ListSuiteDefinitions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotdeviceadvisor-2020-09-18/ListSuiteDefinitions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotdeviceadvisor-2020-09-18/ListSuiteDefinitions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotdeviceadvisor-2020-09-18/ListSuiteDefinitions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iotdeviceadvisor-2020-09-18/ListSuiteDefinitions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotdeviceadvisor-2020-09-18/ListSuiteDefinitions)
