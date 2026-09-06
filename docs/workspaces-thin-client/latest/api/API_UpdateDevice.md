---
source_url: https://docs.aws.amazon.com/workspaces-thin-client/latest/api/API_UpdateDevice.html
---

# UpdateDevice
<a name="API_UpdateDevice"></a>

**Important**
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkSpaces Thin Client. After March 31, 2027, you will no longer be able to access the WorkSpaces Thin Client console or WorkSpaces Thin Client resources. For more information, see [Amazon WorkSpaces Thin Client end of support](https://docs.aws.amazon.com/workspaces-thin-client/latest/ug/workspacesthinclient-end-of-support.html).

Updates a thin client device.

## Request Syntax
<a name="API_UpdateDevice_RequestSyntax"></a>

```
PATCH /devices/{{id}} HTTP/1.1
Content-type: application/json

{
   "desiredSoftwareSetId": "{{string}}",
   "name": "{{string}}",
   "softwareSetUpdateSchedule": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateDevice_RequestParameters"></a>

The request uses the following URI parameters.

 ** [id](#API_UpdateDevice_RequestSyntax) **   <a name="workspacesthinclient-UpdateDevice-request-uri-id"></a>
The ID of the device to update.
Pattern: `[a-zA-Z0-9]{24}`
Required: Yes

## Request Body
<a name="API_UpdateDevice_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [desiredSoftwareSetId](#API_UpdateDevice_RequestSyntax) **   <a name="workspacesthinclient-UpdateDevice-request-desiredSoftwareSetId"></a>
The ID of the software set to apply.
Type: String
Pattern: `[0-9]{1,9}`
Required: No

 ** [name](#API_UpdateDevice_RequestSyntax) **   <a name="workspacesthinclient-UpdateDevice-request-name"></a>
The name of the device to update.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Pattern: `$|^[0-9\p{IsAlphabetic}+:,.@'" -]*`
Required: No

 ** [softwareSetUpdateSchedule](#API_UpdateDevice_RequestSyntax) **   <a name="workspacesthinclient-UpdateDevice-request-softwareSetUpdateSchedule"></a>
An option to define if software updates should be applied within a maintenance window.
Type: String
Valid Values: `USE_MAINTENANCE_WINDOW | APPLY_IMMEDIATELY`
Required: No

## Response Syntax
<a name="API_UpdateDevice_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "device": {
      "arn": "string",
      "createdAt": number,
      "currentSoftwareSetId": "string",
      "desiredSoftwareSetId": "string",
      "environmentId": "string",
      "id": "string",
      "lastConnectedAt": number,
      "lastPostureAt": number,
      "model": "string",
      "name": "string",
      "pendingSoftwareSetId": "string",
      "serialNumber": "string",
      "softwareSetUpdateSchedule": "string",
      "status": "string",
      "updatedAt": number
   }
}
```

## Response Elements
<a name="API_UpdateDevice_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [device](#API_UpdateDevice_ResponseSyntax) **   <a name="workspacesthinclient-UpdateDevice-response-device"></a>
Describes a device.
Type: [DeviceSummary](API_DeviceSummary.md) object

## Errors
<a name="API_UpdateDevice_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkSpaces Thin Client. After March 31, 2027, you will no longer be able to access the WorkSpaces Thin Client console or WorkSpaces Thin Client resources. For more information, see [Amazon WorkSpaces Thin Client end of support](https://docs.aws.amazon.com/workspaces-thin-client/latest/ug/workspacesthinclient-end-of-support.html).
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkSpaces Thin Client. After March 31, 2027, you will no longer be able to access the WorkSpaces Thin Client console or WorkSpaces Thin Client resources. For more information, see [Amazon WorkSpaces Thin Client end of support](https://docs.aws.amazon.com/workspaces-thin-client/latest/ug/workspacesthinclient-end-of-support.html).
The server encountered an internal error and is unable to complete the request.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the next request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkSpaces Thin Client. After March 31, 2027, you will no longer be able to access the WorkSpaces Thin Client console or WorkSpaces Thin Client resources. For more information, see [Amazon WorkSpaces Thin Client end of support](https://docs.aws.amazon.com/workspaces-thin-client/latest/ug/workspacesthinclient-end-of-support.html).
The resource specified in the request was not found.
 ** resourceId **
The ID of the resource associated with the request.
 ** resourceType **
The type of the resource associated with the request.
HTTP Status Code: 404

 ** ThrottlingException **
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkSpaces Thin Client. After March 31, 2027, you will no longer be able to access the WorkSpaces Thin Client console or WorkSpaces Thin Client resources. For more information, see [Amazon WorkSpaces Thin Client end of support](https://docs.aws.amazon.com/workspaces-thin-client/latest/ug/workspacesthinclient-end-of-support.html).
The request was denied due to request throttling.
 ** quotaCode **
The code for the quota in [Service Quotas](https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html).
 ** retryAfterSeconds **
The number of seconds to wait before retrying the next request.
 ** serviceCode **
The code for the service in [Service Quotas](https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html).
HTTP Status Code: 429

 ** ValidationException **
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkSpaces Thin Client. After March 31, 2027, you will no longer be able to access the WorkSpaces Thin Client console or WorkSpaces Thin Client resources. For more information, see [Amazon WorkSpaces Thin Client end of support](https://docs.aws.amazon.com/workspaces-thin-client/latest/ug/workspacesthinclient-end-of-support.html).
The input fails to satisfy the specified constraints.
 ** fieldList **
A list of fields that didn't validate.
 ** reason **
The reason for the exception.
HTTP Status Code: 400

## See Also
<a name="API_UpdateDevice_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workspaces-thin-client-2023-08-22/UpdateDevice)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workspaces-thin-client-2023-08-22/UpdateDevice)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-thin-client-2023-08-22/UpdateDevice)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workspaces-thin-client-2023-08-22/UpdateDevice)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-thin-client-2023-08-22/UpdateDevice)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workspaces-thin-client-2023-08-22/UpdateDevice)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workspaces-thin-client-2023-08-22/UpdateDevice)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workspaces-thin-client-2023-08-22/UpdateDevice)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/workspaces-thin-client-2023-08-22/UpdateDevice)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-thin-client-2023-08-22/UpdateDevice)
