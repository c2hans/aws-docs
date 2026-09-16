---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_UpdateMaintenanceWindowTarget.html
---

# UpdateMaintenanceWindowTarget
<a name="API_UpdateMaintenanceWindowTarget"></a>

Modifies the target of an existing maintenance window. You can change the following:
+ Name
+ Description
+ Owner
+ IDs for an ID target
+ Tags for a Tag target
+ From any supported tag type to another. The three supported tag types are ID target, Tag target, and resource group. For more information, see [Target](API_Target.md).

**Note**
If a parameter is null, then the corresponding field isn't modified.

## Request Syntax
<a name="API_UpdateMaintenanceWindowTarget_RequestSyntax"></a>

```
{
   "Description": "{{string}}",
   "Name": "{{string}}",
   "OwnerInformation": "{{string}}",
   "Replace": {{boolean}},
   "Targets": [
      {
         "Key": "{{string}}",
         "Values": [ "{{string}}" ]
      }
   ],
   "WindowId": "{{string}}",
   "WindowTargetId": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateMaintenanceWindowTarget_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Description](#API_UpdateMaintenanceWindowTarget_RequestSyntax) **   <a name="systemsmanager-UpdateMaintenanceWindowTarget-request-Description"></a>
An optional description for the update.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** [Name](#API_UpdateMaintenanceWindowTarget_RequestSyntax) **   <a name="systemsmanager-UpdateMaintenanceWindowTarget-request-Name"></a>
A name for the update.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 128.
Pattern: `^[a-zA-Z0-9_\-.]{3,128}$`
Required: No

 ** [OwnerInformation](#API_UpdateMaintenanceWindowTarget_RequestSyntax) **   <a name="systemsmanager-UpdateMaintenanceWindowTarget-request-OwnerInformation"></a>
User-provided value that will be included in any Amazon CloudWatch Events events raised while running tasks for these targets in this maintenance window.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** [Replace](#API_UpdateMaintenanceWindowTarget_RequestSyntax) **   <a name="systemsmanager-UpdateMaintenanceWindowTarget-request-Replace"></a>
If `True`, then all fields that are required by the [RegisterTargetWithMaintenanceWindow](API_RegisterTargetWithMaintenanceWindow.md) operation are also required for this API request. Optional fields that aren't specified are set to null.
Type: Boolean
Required: No

 ** [Targets](#API_UpdateMaintenanceWindowTarget_RequestSyntax) **   <a name="systemsmanager-UpdateMaintenanceWindowTarget-request-Targets"></a>
The targets to add or replace.
Type: Array of [Target](API_Target.md) objects
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Required: No

 ** [WindowId](#API_UpdateMaintenanceWindowTarget_RequestSyntax) **   <a name="systemsmanager-UpdateMaintenanceWindowTarget-request-WindowId"></a>
The maintenance window ID with which to modify the target.
Type: String
Length Constraints: Fixed length of 20.
Pattern: `^mw-[0-9a-f]{17}$`
Required: Yes

 ** [WindowTargetId](#API_UpdateMaintenanceWindowTarget_RequestSyntax) **   <a name="systemsmanager-UpdateMaintenanceWindowTarget-request-WindowTargetId"></a>
The target ID to modify.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[0-9a-fA-F]{8}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{12}$`
Required: Yes

## Response Syntax
<a name="API_UpdateMaintenanceWindowTarget_ResponseSyntax"></a>

```
{
   "Description": "string",
   "Name": "string",
   "OwnerInformation": "string",
   "Targets": [
      {
         "Key": "string",
         "Values": [ "string" ]
      }
   ],
   "WindowId": "string",
   "WindowTargetId": "string"
}
```

## Response Elements
<a name="API_UpdateMaintenanceWindowTarget_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Description](#API_UpdateMaintenanceWindowTarget_ResponseSyntax) **   <a name="systemsmanager-UpdateMaintenanceWindowTarget-response-Description"></a>
The updated description.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.

 ** [Name](#API_UpdateMaintenanceWindowTarget_ResponseSyntax) **   <a name="systemsmanager-UpdateMaintenanceWindowTarget-response-Name"></a>
The updated name.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 128.
Pattern: `^[a-zA-Z0-9_\-.]{3,128}$`

 ** [OwnerInformation](#API_UpdateMaintenanceWindowTarget_ResponseSyntax) **   <a name="systemsmanager-UpdateMaintenanceWindowTarget-response-OwnerInformation"></a>
The updated owner.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.

 ** [Targets](#API_UpdateMaintenanceWindowTarget_ResponseSyntax) **   <a name="systemsmanager-UpdateMaintenanceWindowTarget-response-Targets"></a>
The updated targets.
Type: Array of [Target](API_Target.md) objects
Array Members: Minimum number of 0 items. Maximum number of 5 items.

 ** [WindowId](#API_UpdateMaintenanceWindowTarget_ResponseSyntax) **   <a name="systemsmanager-UpdateMaintenanceWindowTarget-response-WindowId"></a>
The maintenance window ID specified in the update request.
Type: String
Length Constraints: Fixed length of 20.
Pattern: `^mw-[0-9a-f]{17}$`

 ** [WindowTargetId](#API_UpdateMaintenanceWindowTarget_ResponseSyntax) **   <a name="systemsmanager-UpdateMaintenanceWindowTarget-response-WindowTargetId"></a>
The target ID specified in the update request.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[0-9a-fA-F]{8}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{12}$`

## Errors
<a name="API_UpdateMaintenanceWindowTarget_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DoesNotExistException **
Error returned when the ID specified for a resource, such as a maintenance window or patch baseline, doesn't exist.
For information about resource quotas in AWS Systems Manager, see [Systems Manager service quotas](https://docs.aws.amazon.com/general/latest/gr/ssm.html#limits_ssm) in the *Amazon Web Services General Reference*.
HTTP Status Code: 400

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

## Examples
<a name="API_UpdateMaintenanceWindowTarget_Examples"></a>

### Example
<a name="API_UpdateMaintenanceWindowTarget_Example_1"></a>

This example illustrates one usage of UpdateMaintenanceWindowTarget.

#### Sample Request
<a name="API_UpdateMaintenanceWindowTarget_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-east-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: AmazonSSM.UpdateMaintenanceWindowTarget
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/2.0.0 Python/3.7.5 Windows/10 botocore/2.0.0dev4
X-Amz-Date: 20240225T005329Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240225/us-east-2/ssm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 233

{
    "WindowId": "mw-0c50858d01EXAMPLE",
    "WindowTargetId": "23639a0b-ddbc-4bca-9e72-78d96EXAMPLE",
    "Targets": [
        {
            "Key": "InstanceIds",
            "Values": [
                "i-07782c72faEXAMPLE"
            ]
        }
    ],
    "Name": "MyNewTaskName",
    "Description": "My new task description"
}
```

#### Sample Response
<a name="API_UpdateMaintenanceWindowTarget_Example_1_Response"></a>

```
{
    "Description": "My new task description",
    "Name": "MyNewTaskName",
    "Targets": [
        {
            "Key": "InstanceIds",
            "Values": [
                "i-07782c72faEXAMPLE"
            ]
        }
    ],
    "WindowId": "mw-0c50858d01EXAMPLE",
    "WindowTargetId": "23639a0b-ddbc-4bca-9e72-78d96EXAMPLE"
}
```

## See Also
<a name="API_UpdateMaintenanceWindowTarget_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/UpdateMaintenanceWindowTarget)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/UpdateMaintenanceWindowTarget)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/UpdateMaintenanceWindowTarget)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/UpdateMaintenanceWindowTarget)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/UpdateMaintenanceWindowTarget)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/UpdateMaintenanceWindowTarget)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/UpdateMaintenanceWindowTarget)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/UpdateMaintenanceWindowTarget)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/UpdateMaintenanceWindowTarget)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/UpdateMaintenanceWindowTarget)
