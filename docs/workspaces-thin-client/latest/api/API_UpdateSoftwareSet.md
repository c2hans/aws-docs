---
source_url: https://docs.aws.amazon.com/workspaces-thin-client/latest/api/API_UpdateSoftwareSet.html
---

# UpdateSoftwareSet
<a name="API_UpdateSoftwareSet"></a>

**Important**
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkSpaces Thin Client. After March 31, 2027, you will no longer be able to access the WorkSpaces Thin Client console or WorkSpaces Thin Client resources. For more information, see [Amazon WorkSpaces Thin Client end of support](https://docs.aws.amazon.com/workspaces-thin-client/latest/ug/workspacesthinclient-end-of-support.html).

Updates a software set.

## Request Syntax
<a name="API_UpdateSoftwareSet_RequestSyntax"></a>

```
PATCH /softwaresets/{{id}} HTTP/1.1
Content-type: application/json

{
   "validationStatus": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateSoftwareSet_RequestParameters"></a>

The request uses the following URI parameters.

 ** [id](#API_UpdateSoftwareSet_RequestSyntax) **   <a name="workspacesthinclient-UpdateSoftwareSet-request-uri-id"></a>
The ID of the software set to update.
Pattern: `[0-9]{1,9}`
Required: Yes

## Request Body
<a name="API_UpdateSoftwareSet_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [validationStatus](#API_UpdateSoftwareSet_RequestSyntax) **   <a name="workspacesthinclient-UpdateSoftwareSet-request-validationStatus"></a>
An option to define if the software set has been validated.
Type: String
Valid Values: `VALIDATED | NOT_VALIDATED`
Required: Yes

## Response Syntax
<a name="API_UpdateSoftwareSet_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_UpdateSoftwareSet_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_UpdateSoftwareSet_Errors"></a>

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
<a name="API_UpdateSoftwareSet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workspaces-thin-client-2023-08-22/UpdateSoftwareSet)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workspaces-thin-client-2023-08-22/UpdateSoftwareSet)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-thin-client-2023-08-22/UpdateSoftwareSet)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workspaces-thin-client-2023-08-22/UpdateSoftwareSet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-thin-client-2023-08-22/UpdateSoftwareSet)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workspaces-thin-client-2023-08-22/UpdateSoftwareSet)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workspaces-thin-client-2023-08-22/UpdateSoftwareSet)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workspaces-thin-client-2023-08-22/UpdateSoftwareSet)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/workspaces-thin-client-2023-08-22/UpdateSoftwareSet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-thin-client-2023-08-22/UpdateSoftwareSet)
