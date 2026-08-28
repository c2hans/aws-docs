---
source_url: https://docs.aws.amazon.com/workspaces-thin-client/latest/api/API_UpdateEnvironment.html
---

# UpdateEnvironment
<a name="API_UpdateEnvironment"></a>

**Important**
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkSpaces Thin Client. After March 31, 2027, you will no longer be able to access the WorkSpaces Thin Client console or WorkSpaces Thin Client resources. For more information, see [Amazon WorkSpaces Thin Client end of support](https://docs.aws.amazon.com/workspaces-thin-client/latest/ug/workspacesthinclient-end-of-support.html).

Updates an environment.

## Request Syntax
<a name="API_UpdateEnvironment_RequestSyntax"></a>

```
PATCH /environments/{{id}} HTTP/1.1
Content-type: application/json

{
   "desiredSoftwareSetId": "{{string}}",
   "desktopArn": "{{string}}",
   "desktopEndpoint": "{{string}}",
   "deviceCreationTags": {
      "{{string}}" : "{{string}}"
   },
   "maintenanceWindow": {
      "applyTimeOf": "{{string}}",
      "daysOfTheWeek": [ "{{string}}" ],
      "endTimeHour": {{number}},
      "endTimeMinute": {{number}},
      "startTimeHour": {{number}},
      "startTimeMinute": {{number}},
      "type": "{{string}}"
   },
   "name": "{{string}}",
   "softwareSetUpdateMode": "{{string}}",
   "softwareSetUpdateSchedule": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateEnvironment_RequestParameters"></a>

The request uses the following URI parameters.

 ** [id](#API_UpdateEnvironment_RequestSyntax) **   <a name="workspacesthinclient-UpdateEnvironment-request-uri-id"></a>
The ID of the environment to update.
Pattern: `[a-z0-9]{9}`
Required: Yes

## Request Body
<a name="API_UpdateEnvironment_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [desiredSoftwareSetId](#API_UpdateEnvironment_RequestSyntax) **   <a name="workspacesthinclient-UpdateEnvironment-request-desiredSoftwareSetId"></a>
The ID of the software set to apply.
Type: String
Pattern: `[0-9]{0,9}`
Required: No

 ** [desktopArn](#API_UpdateEnvironment_RequestSyntax) **   <a name="workspacesthinclient-UpdateEnvironment-request-desktopArn"></a>
The Amazon Resource Name (ARN) of the desktop to stream from Amazon WorkSpaces, WorkSpaces Secure Browser, or WorkSpaces Applications.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[\w+=\/,.@-]+:[a-zA-Z0-9\-]+:[a-zA-Z0-9\-]*:[0-9]{0,12}:[a-zA-Z0-9\-\/\._]+`
Required: No

 ** [desktopEndpoint](#API_UpdateEnvironment_RequestSyntax) **   <a name="workspacesthinclient-UpdateEnvironment-request-desktopEndpoint"></a>
The URL for the identity provider login (only for environments that use WorkSpaces Applications).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `(https:\/\/)[a-z0-9]+([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,32}(:[0-9]{1,5})?(\/.*)?`
Required: No

 ** [deviceCreationTags](#API_UpdateEnvironment_RequestSyntax) **   <a name="workspacesthinclient-UpdateEnvironment-request-deviceCreationTags"></a>
A map of the key-value pairs of the tag or tags to assign to the newly created devices for this environment.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `(?!aws:)[A-Za-z0-9 _=@:.+-/]+`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `[A-Za-z0-9 _=@:.+-/]+`
Required: No

 ** [maintenanceWindow](#API_UpdateEnvironment_RequestSyntax) **   <a name="workspacesthinclient-UpdateEnvironment-request-maintenanceWindow"></a>
A specification for a time window to apply software updates.
Type: [MaintenanceWindow](API_MaintenanceWindow.md) object
Required: No

 ** [name](#API_UpdateEnvironment_RequestSyntax) **   <a name="workspacesthinclient-UpdateEnvironment-request-name"></a>
The name of the environment to update.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Pattern: `$|^[0-9\p{IsAlphabetic}+:,.@'" -][0-9\p{IsAlphabetic}+=:,.@'" -]*`
Required: No

 ** [softwareSetUpdateMode](#API_UpdateEnvironment_RequestSyntax) **   <a name="workspacesthinclient-UpdateEnvironment-request-softwareSetUpdateMode"></a>
An option to define which software updates to apply.
Type: String
Valid Values: `USE_LATEST | USE_DESIRED`
Required: No

 ** [softwareSetUpdateSchedule](#API_UpdateEnvironment_RequestSyntax) **   <a name="workspacesthinclient-UpdateEnvironment-request-softwareSetUpdateSchedule"></a>
An option to define if software updates should be applied within a maintenance window.
Type: String
Valid Values: `USE_MAINTENANCE_WINDOW | APPLY_IMMEDIATELY`
Required: No

## Response Syntax
<a name="API_UpdateEnvironment_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "environment": {
      "activationCode": "string",
      "arn": "string",
      "createdAt": number,
      "desiredSoftwareSetId": "string",
      "desktopArn": "string",
      "desktopEndpoint": "string",
      "desktopType": "string",
      "id": "string",
      "maintenanceWindow": {
         "applyTimeOf": "string",
         "daysOfTheWeek": [ "string" ],
         "endTimeHour": number,
         "endTimeMinute": number,
         "startTimeHour": number,
         "startTimeMinute": number,
         "type": "string"
      },
      "name": "string",
      "pendingSoftwareSetId": "string",
      "softwareSetUpdateMode": "string",
      "softwareSetUpdateSchedule": "string",
      "updatedAt": number
   }
}
```

## Response Elements
<a name="API_UpdateEnvironment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [environment](#API_UpdateEnvironment_ResponseSyntax) **   <a name="workspacesthinclient-UpdateEnvironment-response-environment"></a>
Describes an environment.
Type: [EnvironmentSummary](API_EnvironmentSummary.md) object

## Errors
<a name="API_UpdateEnvironment_Errors"></a>

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
<a name="API_UpdateEnvironment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workspaces-thin-client-2023-08-22/UpdateEnvironment)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workspaces-thin-client-2023-08-22/UpdateEnvironment)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-thin-client-2023-08-22/UpdateEnvironment)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workspaces-thin-client-2023-08-22/UpdateEnvironment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-thin-client-2023-08-22/UpdateEnvironment)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workspaces-thin-client-2023-08-22/UpdateEnvironment)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workspaces-thin-client-2023-08-22/UpdateEnvironment)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workspaces-thin-client-2023-08-22/UpdateEnvironment)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/workspaces-thin-client-2023-08-22/UpdateEnvironment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-thin-client-2023-08-22/UpdateEnvironment)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Thin Client. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces-thin-client` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
