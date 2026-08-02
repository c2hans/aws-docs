---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_ListWirelessDeviceImportTasks.html
---

# ListWirelessDeviceImportTasks
<a name="API_ListWirelessDeviceImportTasks"></a>

List of import tasks and summary information of onboarding status of devices in each import task.

## Request Syntax
<a name="API_ListWirelessDeviceImportTasks_RequestSyntax"></a>

```
GET /wireless_device_import_tasks?maxResults={{MaxResults}}&nextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListWirelessDeviceImportTasks_RequestParameters"></a>

The request uses the following URI parameters.

 ** [MaxResults](#API_ListWirelessDeviceImportTasks_RequestSyntax) **   <a name="iotwireless-ListWirelessDeviceImportTasks-request-uri-MaxResults"></a>
The maximum number of results to return in this operation.
Valid Range: Minimum value of 0. Maximum value of 250.

 ** [NextToken](#API_ListWirelessDeviceImportTasks_RequestSyntax) **   <a name="iotwireless-ListWirelessDeviceImportTasks-request-uri-NextToken"></a>
To retrieve the next set of results, the `nextToken` value from a previous response; otherwise `null` to receive the first set of results.
Length Constraints: Maximum length of 4096.

## Request Body
<a name="API_ListWirelessDeviceImportTasks_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListWirelessDeviceImportTasks_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "WirelessDeviceImportTaskList": [
      {
         "Arn": "string",
         "CreationTime": "string",
         "DestinationName": "string",
         "FailedImportedDeviceCount": number,
         "Id": "string",
         "InitializedImportedDeviceCount": number,
         "OnboardedImportedDeviceCount": number,
         "PendingImportedDeviceCount": number,
         "Positioning": "string",
         "Sidewalk": {
            "DeviceCreationFileList": [ "string" ],
            "Positioning": {
               "DestinationName": "string"
            },
            "Role": "string"
         },
         "Status": "string",
         "StatusReason": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListWirelessDeviceImportTasks_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListWirelessDeviceImportTasks_ResponseSyntax) **   <a name="iotwireless-ListWirelessDeviceImportTasks-response-NextToken"></a>
The token to use to get the next set of results, or `null` if there are no additional results.
Type: String
Length Constraints: Maximum length of 4096.

 ** [WirelessDeviceImportTaskList](#API_ListWirelessDeviceImportTasks_ResponseSyntax) **   <a name="iotwireless-ListWirelessDeviceImportTasks-response-WirelessDeviceImportTaskList"></a>
List of import tasks and summary information of onboarding status of devices in each import task.
Type: Array of [WirelessDeviceImportTask](API_WirelessDeviceImportTask.md) objects

## Errors
<a name="API_ListWirelessDeviceImportTasks_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User does not have permission to perform this action.
HTTP Status Code: 403

 ** ConflictException **
Adding, updating, or deleting the resource can cause an inconsistent state.
 ** ResourceId **
Id of the resource in the conflicting operation.
 ** ResourceType **
Type of the resource in the conflicting operation.
HTTP Status Code: 409

 ** InternalServerException **
An unexpected error occurred while processing a request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
Resource does not exist.
 ** ResourceId **
Id of the not found resource.
 ** ResourceType **
Type of the font found resource.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied because it exceeded the allowed API request rate.
HTTP Status Code: 429

 ** ValidationException **
The input did not meet the specified constraints.
HTTP Status Code: 400

## See Also
<a name="API_ListWirelessDeviceImportTasks_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotwireless-2025-11-06/ListWirelessDeviceImportTasks)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotwireless-2025-11-06/ListWirelessDeviceImportTasks)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotwireless-2025-11-06/ListWirelessDeviceImportTasks)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotwireless-2025-11-06/ListWirelessDeviceImportTasks)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotwireless-2025-11-06/ListWirelessDeviceImportTasks)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotwireless-2025-11-06/ListWirelessDeviceImportTasks)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotwireless-2025-11-06/ListWirelessDeviceImportTasks)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotwireless-2025-11-06/ListWirelessDeviceImportTasks)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iotwireless-2025-11-06/ListWirelessDeviceImportTasks)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotwireless-2025-11-06/ListWirelessDeviceImportTasks)
