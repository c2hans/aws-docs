---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_iotdeviceadvisor_ListSuiteRuns.html
---

# ListSuiteRuns
<a name="API_iotdeviceadvisor_ListSuiteRuns"></a>

Lists runs of the specified Device Advisor test suite. You can list all runs of the test suite, or the runs of a specific version of the test suite.

Requires permission to access the [ListSuiteRuns](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_iotdeviceadvisor_ListSuiteRuns_RequestSyntax"></a>

```
GET /suiteRuns?maxResults={{maxResults}}&nextToken={{nextToken}}&suiteDefinitionId={{suiteDefinitionId}}&suiteDefinitionVersion={{suiteDefinitionVersion}} HTTP/1.1
```

## URI Request Parameters
<a name="API_iotdeviceadvisor_ListSuiteRuns_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_iotdeviceadvisor_ListSuiteRuns_RequestSyntax) **   <a name="iot-iotdeviceadvisor_ListSuiteRuns-request-uri-maxResults"></a>
The maximum number of results to return at once.
Valid Range: Minimum value of 1. Maximum value of 50.

 ** [nextToken](#API_iotdeviceadvisor_ListSuiteRuns_RequestSyntax) **   <a name="iot-iotdeviceadvisor_ListSuiteRuns-request-uri-nextToken"></a>
A token to retrieve the next set of results.
Length Constraints: Maximum length of 2000.

 ** [suiteDefinitionId](#API_iotdeviceadvisor_ListSuiteRuns_RequestSyntax) **   <a name="iot-iotdeviceadvisor_ListSuiteRuns-request-uri-suiteDefinitionId"></a>
Lists the test suite runs of the specified test suite based on suite definition ID.
Length Constraints: Minimum length of 12. Maximum length of 36.

 ** [suiteDefinitionVersion](#API_iotdeviceadvisor_ListSuiteRuns_RequestSyntax) **   <a name="iot-iotdeviceadvisor_ListSuiteRuns-request-uri-suiteDefinitionVersion"></a>
Must be passed along with `suiteDefinitionId`. Lists the test suite runs of the specified test suite based on suite definition version.
Length Constraints: Minimum length of 2. Maximum length of 255.

## Request Body
<a name="API_iotdeviceadvisor_ListSuiteRuns_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_iotdeviceadvisor_ListSuiteRuns_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "suiteRunsList": [
      {
         "createdAt": number,
         "endAt": number,
         "failed": number,
         "passed": number,
         "startedAt": number,
         "status": "string",
         "suiteDefinitionId": "string",
         "suiteDefinitionName": "string",
         "suiteDefinitionVersion": "string",
         "suiteRunId": "string"
      }
   ]
}
```

## Response Elements
<a name="API_iotdeviceadvisor_ListSuiteRuns_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_iotdeviceadvisor_ListSuiteRuns_ResponseSyntax) **   <a name="iot-iotdeviceadvisor_ListSuiteRuns-response-nextToken"></a>
A token to retrieve the next set of results.
Type: String
Length Constraints: Maximum length of 2000.

 ** [suiteRunsList](#API_iotdeviceadvisor_ListSuiteRuns_ResponseSyntax) **   <a name="iot-iotdeviceadvisor_ListSuiteRuns-response-suiteRunsList"></a>
An array of objects that provide summaries of information about the suite runs in the list.
Type: Array of [SuiteRunInformation](API_iotdeviceadvisor_SuiteRunInformation.md) objects

## Errors
<a name="API_iotdeviceadvisor_ListSuiteRuns_Errors"></a>

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
<a name="API_iotdeviceadvisor_ListSuiteRuns_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotdeviceadvisor-2020-09-18/ListSuiteRuns)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotdeviceadvisor-2020-09-18/ListSuiteRuns)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotdeviceadvisor-2020-09-18/ListSuiteRuns)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotdeviceadvisor-2020-09-18/ListSuiteRuns)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotdeviceadvisor-2020-09-18/ListSuiteRuns)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotdeviceadvisor-2020-09-18/ListSuiteRuns)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotdeviceadvisor-2020-09-18/ListSuiteRuns)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotdeviceadvisor-2020-09-18/ListSuiteRuns)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iotdeviceadvisor-2020-09-18/ListSuiteRuns)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotdeviceadvisor-2020-09-18/ListSuiteRuns)
