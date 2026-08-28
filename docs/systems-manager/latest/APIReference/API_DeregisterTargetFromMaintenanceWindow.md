---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DeregisterTargetFromMaintenanceWindow.html
---

# DeregisterTargetFromMaintenanceWindow
<a name="API_DeregisterTargetFromMaintenanceWindow"></a>

Removes a target from a maintenance window.

## Request Syntax
<a name="API_DeregisterTargetFromMaintenanceWindow_RequestSyntax"></a>

```
{
   "Safe": {{boolean}},
   "WindowId": "{{string}}",
   "WindowTargetId": "{{string}}"
}
```

## Request Parameters
<a name="API_DeregisterTargetFromMaintenanceWindow_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Safe](#API_DeregisterTargetFromMaintenanceWindow_RequestSyntax) **   <a name="systemsmanager-DeregisterTargetFromMaintenanceWindow-request-Safe"></a>
The system checks if the target is being referenced by a task. If the target is being referenced, the system returns an error and doesn't deregister the target from the maintenance window.
Type: Boolean
Required: No

 ** [WindowId](#API_DeregisterTargetFromMaintenanceWindow_RequestSyntax) **   <a name="systemsmanager-DeregisterTargetFromMaintenanceWindow-request-WindowId"></a>
The ID of the maintenance window the target should be removed from.
Type: String
Length Constraints: Fixed length of 20.
Pattern: `^mw-[0-9a-f]{17}$`
Required: Yes

 ** [WindowTargetId](#API_DeregisterTargetFromMaintenanceWindow_RequestSyntax) **   <a name="systemsmanager-DeregisterTargetFromMaintenanceWindow-request-WindowTargetId"></a>
The ID of the target definition to remove.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[0-9a-fA-F]{8}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{12}$`
Required: Yes

## Response Syntax
<a name="API_DeregisterTargetFromMaintenanceWindow_ResponseSyntax"></a>

```
{
   "WindowId": "string",
   "WindowTargetId": "string"
}
```

## Response Elements
<a name="API_DeregisterTargetFromMaintenanceWindow_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [WindowId](#API_DeregisterTargetFromMaintenanceWindow_ResponseSyntax) **   <a name="systemsmanager-DeregisterTargetFromMaintenanceWindow-response-WindowId"></a>
The ID of the maintenance window the target was removed from.
Type: String
Length Constraints: Fixed length of 20.
Pattern: `^mw-[0-9a-f]{17}$`

 ** [WindowTargetId](#API_DeregisterTargetFromMaintenanceWindow_ResponseSyntax) **   <a name="systemsmanager-DeregisterTargetFromMaintenanceWindow-response-WindowTargetId"></a>
The ID of the removed target definition.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[0-9a-fA-F]{8}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{12}$`

## Errors
<a name="API_DeregisterTargetFromMaintenanceWindow_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DoesNotExistException **
Error returned when the ID specified for a resource, such as a maintenance window or patch baseline, doesn't exist.
For information about resource quotas in AWS Systems Manager, see [Systems Manager service quotas](https://docs.aws.amazon.com/general/latest/gr/ssm.html#limits_ssm) in the *Amazon Web Services General Reference*.
HTTP Status Code: 400

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

 ** TargetInUseException **
You specified the `Safe` option for the DeregisterTargetFromMaintenanceWindow operation, but the target is still referenced in a task.
HTTP Status Code: 400

## Examples
<a name="API_DeregisterTargetFromMaintenanceWindow_Examples"></a>

### Example
<a name="API_DeregisterTargetFromMaintenanceWindow_Example_1"></a>

This example illustrates one usage of DeregisterTargetFromMaintenanceWindow.

#### Sample Request
<a name="API_DeregisterTargetFromMaintenanceWindow_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-east-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: AmazonSSM.DeregisterTargetFromMaintenanceWindow
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/2.0.0 Python/3.7.5 Windows/10 botocore/2.0.0dev4
X-Amz-Date: 20240225T182719Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240225/us-east-2/ssm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 94

{
    "WindowId": "mw-0c50858d01EXAMPLE",
    "WindowTargetId": "23639a0b-ddbc-4bca-9e72-78d96EXAMPLE"
}
```

#### Sample Response
<a name="API_DeregisterTargetFromMaintenanceWindow_Example_1_Response"></a>

```
{
    "WindowId": "mw-0c50858d01EXAMPLE",
    "WindowTargetId": "23639a0b-ddbc-4bca-9e72-78d96EXAMPLE"
}
```

## See Also
<a name="API_DeregisterTargetFromMaintenanceWindow_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/DeregisterTargetFromMaintenanceWindow)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/DeregisterTargetFromMaintenanceWindow)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/DeregisterTargetFromMaintenanceWindow)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/DeregisterTargetFromMaintenanceWindow)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/DeregisterTargetFromMaintenanceWindow)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/DeregisterTargetFromMaintenanceWindow)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/DeregisterTargetFromMaintenanceWindow)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/DeregisterTargetFromMaintenanceWindow)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/DeregisterTargetFromMaintenanceWindow)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/DeregisterTargetFromMaintenanceWindow)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
