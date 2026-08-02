---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DeregisterTaskFromMaintenanceWindow.html
---

# DeregisterTaskFromMaintenanceWindow
<a name="API_DeregisterTaskFromMaintenanceWindow"></a>

Removes a task from a maintenance window.

## Request Syntax
<a name="API_DeregisterTaskFromMaintenanceWindow_RequestSyntax"></a>

```
{
   "WindowId": "{{string}}",
   "WindowTaskId": "{{string}}"
}
```

## Request Parameters
<a name="API_DeregisterTaskFromMaintenanceWindow_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [WindowId](#API_DeregisterTaskFromMaintenanceWindow_RequestSyntax) **   <a name="systemsmanager-DeregisterTaskFromMaintenanceWindow-request-WindowId"></a>
The ID of the maintenance window the task should be removed from.
Type: String
Length Constraints: Fixed length of 20.
Pattern: `^mw-[0-9a-f]{17}$`
Required: Yes

 ** [WindowTaskId](#API_DeregisterTaskFromMaintenanceWindow_RequestSyntax) **   <a name="systemsmanager-DeregisterTaskFromMaintenanceWindow-request-WindowTaskId"></a>
The ID of the task to remove from the maintenance window.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[0-9a-fA-F]{8}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{12}$`
Required: Yes

## Response Syntax
<a name="API_DeregisterTaskFromMaintenanceWindow_ResponseSyntax"></a>

```
{
   "WindowId": "string",
   "WindowTaskId": "string"
}
```

## Response Elements
<a name="API_DeregisterTaskFromMaintenanceWindow_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [WindowId](#API_DeregisterTaskFromMaintenanceWindow_ResponseSyntax) **   <a name="systemsmanager-DeregisterTaskFromMaintenanceWindow-response-WindowId"></a>
The ID of the maintenance window the task was removed from.
Type: String
Length Constraints: Fixed length of 20.
Pattern: `^mw-[0-9a-f]{17}$`

 ** [WindowTaskId](#API_DeregisterTaskFromMaintenanceWindow_ResponseSyntax) **   <a name="systemsmanager-DeregisterTaskFromMaintenanceWindow-response-WindowTaskId"></a>
The ID of the task removed from the maintenance window.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[0-9a-fA-F]{8}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{12}$`

## Errors
<a name="API_DeregisterTaskFromMaintenanceWindow_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DoesNotExistException **
Error returned when the ID specified for a resource, such as a maintenance window or patch baseline, doesn't exist.
For information about resource quotas in AWS Systems Manager, see [Systems Manager service quotas](https://docs.aws.amazon.com/general/latest/gr/ssm.html#limits_ssm) in the *Amazon Web Services General Reference*.
HTTP Status Code: 400

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

## Examples
<a name="API_DeregisterTaskFromMaintenanceWindow_Examples"></a>

### Example
<a name="API_DeregisterTaskFromMaintenanceWindow_Example_1"></a>

This example illustrates one usage of DeregisterTaskFromMaintenanceWindow.

#### Sample Request
<a name="API_DeregisterTaskFromMaintenanceWindow_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-east-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: AmazonSSM.DeregisterTaskFromMaintenanceWindow
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/2.0.0 Python/3.7.5 Windows/10 botocore/2.0.0dev4
X-Amz-Date: 20240225T180133Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240225/us-east-2/ssm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 92

{
    "WindowId": "mw-0c50858d01EXAMPLE",
    "WindowTaskId": "50772993-c6b5-4a2a-8d04-7bfd7EXAMPLE"
}
```

#### Sample Response
<a name="API_DeregisterTaskFromMaintenanceWindow_Example_1_Response"></a>

```
{
    "WindowId": "mw-0c50858d01EXAMPLE",
    "WindowTaskId": "50772993-c6b5-4a2a-8d04-7bfd7EXAMPLE"
}
```

## See Also
<a name="API_DeregisterTaskFromMaintenanceWindow_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/DeregisterTaskFromMaintenanceWindow)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/DeregisterTaskFromMaintenanceWindow)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/DeregisterTaskFromMaintenanceWindow)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/DeregisterTaskFromMaintenanceWindow)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/DeregisterTaskFromMaintenanceWindow)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/DeregisterTaskFromMaintenanceWindow)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/DeregisterTaskFromMaintenanceWindow)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/DeregisterTaskFromMaintenanceWindow)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/DeregisterTaskFromMaintenanceWindow)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/DeregisterTaskFromMaintenanceWindow)
