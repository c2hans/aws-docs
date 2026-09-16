---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_RegisterTargetWithMaintenanceWindow.html
---

# RegisterTargetWithMaintenanceWindow
<a name="API_RegisterTargetWithMaintenanceWindow"></a>

Registers a target with a maintenance window.

## Request Syntax
<a name="API_RegisterTargetWithMaintenanceWindow_RequestSyntax"></a>

```
{
   "ClientToken": "{{string}}",
   "Description": "{{string}}",
   "Name": "{{string}}",
   "OwnerInformation": "{{string}}",
   "ResourceType": "{{string}}",
   "Targets": [
      {
         "Key": "{{string}}",
         "Values": [ "{{string}}" ]
      }
   ],
   "WindowId": "{{string}}"
}
```

## Request Parameters
<a name="API_RegisterTargetWithMaintenanceWindow_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClientToken](#API_RegisterTargetWithMaintenanceWindow_RequestSyntax) **   <a name="systemsmanager-RegisterTargetWithMaintenanceWindow-request-ClientToken"></a>
User-provided idempotency token.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** [Description](#API_RegisterTargetWithMaintenanceWindow_RequestSyntax) **   <a name="systemsmanager-RegisterTargetWithMaintenanceWindow-request-Description"></a>
An optional description for the target.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** [Name](#API_RegisterTargetWithMaintenanceWindow_RequestSyntax) **   <a name="systemsmanager-RegisterTargetWithMaintenanceWindow-request-Name"></a>
An optional name for the target.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 128.
Pattern: `^[a-zA-Z0-9_\-.]{3,128}$`
Required: No

 ** [OwnerInformation](#API_RegisterTargetWithMaintenanceWindow_RequestSyntax) **   <a name="systemsmanager-RegisterTargetWithMaintenanceWindow-request-OwnerInformation"></a>
User-provided value that will be included in any Amazon CloudWatch Events events raised while running tasks for these targets in this maintenance window.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** [ResourceType](#API_RegisterTargetWithMaintenanceWindow_RequestSyntax) **   <a name="systemsmanager-RegisterTargetWithMaintenanceWindow-request-ResourceType"></a>
The type of target being registered with the maintenance window.
Type: String
Valid Values: `INSTANCE | RESOURCE_GROUP`
Required: Yes

 ** [Targets](#API_RegisterTargetWithMaintenanceWindow_RequestSyntax) **   <a name="systemsmanager-RegisterTargetWithMaintenanceWindow-request-Targets"></a>
The targets to register with the maintenance window. In other words, the managed nodes to run commands on when the maintenance window runs.
If a single maintenance window task is registered with multiple targets, its task invocations occur sequentially and not in parallel. If your task must run on multiple targets at the same time, register a task for each target individually and assign each task the same priority level.
You can specify targets using managed node IDs, resource group names, or tags that have been applied to managed nodes.
 **Example 1**: Specify managed node IDs
 `Key=InstanceIds,Values=<instance-id-1>,<instance-id-2>,<instance-id-3>`
 **Example 2**: Use tag key-pairs applied to managed nodes
 `Key=tag:<my-tag-key>,Values=<my-tag-value-1>,<my-tag-value-2>`
 **Example 3**: Use tag-keys applied to managed nodes
 `Key=tag-key,Values=<my-tag-key-1>,<my-tag-key-2>`
 **Example 4**: Use resource group names
 `Key=resource-groups:Name,Values=<resource-group-name>`
 **Example 5**: Use filters for resource group types
 `Key=resource-groups:ResourceTypeFilters,Values=<resource-type-1>,<resource-type-2>`
For `Key=resource-groups:ResourceTypeFilters`, specify resource types in the following format
 `Key=resource-groups:ResourceTypeFilters,Values=AWS::EC2::INSTANCE,AWS::EC2::VPC`
For more information about these examples formats, including the best use case for each one, see [Examples: Register targets with a maintenance window](https://docs.aws.amazon.com/systems-manager/latest/userguide/mw-cli-tutorial-targets-examples.html) in the * AWS Systems Manager User Guide*.
Type: Array of [Target](API_Target.md) objects
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Required: Yes

 ** [WindowId](#API_RegisterTargetWithMaintenanceWindow_RequestSyntax) **   <a name="systemsmanager-RegisterTargetWithMaintenanceWindow-request-WindowId"></a>
The ID of the maintenance window the target should be registered with.
Type: String
Length Constraints: Fixed length of 20.
Pattern: `^mw-[0-9a-f]{17}$`
Required: Yes

## Response Syntax
<a name="API_RegisterTargetWithMaintenanceWindow_ResponseSyntax"></a>

```
{
   "WindowTargetId": "string"
}
```

## Response Elements
<a name="API_RegisterTargetWithMaintenanceWindow_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [WindowTargetId](#API_RegisterTargetWithMaintenanceWindow_ResponseSyntax) **   <a name="systemsmanager-RegisterTargetWithMaintenanceWindow-response-WindowTargetId"></a>
The ID of the target definition in this maintenance window.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[0-9a-fA-F]{8}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{12}$`

## Errors
<a name="API_RegisterTargetWithMaintenanceWindow_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DoesNotExistException **
Error returned when the ID specified for a resource, such as a maintenance window or patch baseline, doesn't exist.
For information about resource quotas in AWS Systems Manager, see [Systems Manager service quotas](https://docs.aws.amazon.com/general/latest/gr/ssm.html#limits_ssm) in the *Amazon Web Services General Reference*.
HTTP Status Code: 400

 ** IdempotentParameterMismatch **
Error returned when an idempotent operation is retried and the parameters don't match the original call to the API with the same idempotency token.
HTTP Status Code: 400

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

 ** ResourceLimitExceededException **
Error returned when the caller has exceeded the default resource quotas. For example, too many maintenance windows or patch baselines have been created.
For information about resource quotas in Systems Manager, see [Systems Manager service quotas](https://docs.aws.amazon.com/general/latest/gr/ssm.html#limits_ssm) in the *Amazon Web Services General Reference*.
HTTP Status Code: 400

## Examples
<a name="API_RegisterTargetWithMaintenanceWindow_Examples"></a>

### Example
<a name="API_RegisterTargetWithMaintenanceWindow_Example_1"></a>

This example illustrates one usage of RegisterTargetWithMaintenanceWindow.

#### Sample Request
<a name="API_RegisterTargetWithMaintenanceWindow_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-east-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: AmazonSSM.RegisterTargetWithMaintenanceWindow
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/2.0.0 Python/3.7.5 Windows/10 botocore/2.0.0dev4
X-Amz-Date: 20240225T003144Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240225/us-east-2/ssm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target,Signature=39c3b3042cd2aEXAMPLE
Content-Length: 191

{
    "WindowId": "mw-0c50858d01EXAMPLE",
    "ResourceType": "INSTANCE",
    "Targets": [
        {
            "Key": "InstanceIds",
            "Values": [
                "i-07782c72faEXAMPLE"
            ]
        }
    ],
    "ClientToken": "aa1b2cde-27e3-42ff-9cac-99380EXAMPLE"
}
```

#### Sample Response
<a name="API_RegisterTargetWithMaintenanceWindow_Example_1_Response"></a>

```
{
    "WindowTargetId": "7f4813bb-df25-4e59-b34f-c9e83EXAMPLE"
}
```

## See Also
<a name="API_RegisterTargetWithMaintenanceWindow_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/RegisterTargetWithMaintenanceWindow)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/RegisterTargetWithMaintenanceWindow)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/RegisterTargetWithMaintenanceWindow)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/RegisterTargetWithMaintenanceWindow)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/RegisterTargetWithMaintenanceWindow)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/RegisterTargetWithMaintenanceWindow)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/RegisterTargetWithMaintenanceWindow)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/RegisterTargetWithMaintenanceWindow)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/RegisterTargetWithMaintenanceWindow)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/RegisterTargetWithMaintenanceWindow)
