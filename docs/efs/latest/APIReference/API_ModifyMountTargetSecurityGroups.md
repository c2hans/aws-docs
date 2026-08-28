---
source_url: https://docs.aws.amazon.com/efs/latest/APIReference/API_ModifyMountTargetSecurityGroups.html
---

# ModifyMountTargetSecurityGroups
<a name="API_ModifyMountTargetSecurityGroups"></a>

Modifies the set of security groups in effect for a mount target.

When you create a mount target, Amazon EFS also creates a new network interface. For more information, see [CreateMountTarget](API_CreateMountTarget.md). This operation replaces the security groups in effect for the network interface associated with a mount target, with the `SecurityGroups` provided in the request. This operation requires that the network interface of the mount target has been created and the lifecycle state of the mount target is not `deleted`.

The operation requires permissions for the following actions:
+  `elasticfilesystem:ModifyMountTargetSecurityGroups` action on the mount target's file system.
+  `ec2:ModifyNetworkInterfaceAttribute` action on the mount target's network interface.

## Request Syntax
<a name="API_ModifyMountTargetSecurityGroups_RequestSyntax"></a>

```
PUT /2015-02-01/mount-targets/{{MountTargetId}}/security-groups HTTP/1.1
Content-type: application/json

{
   "SecurityGroups": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_ModifyMountTargetSecurityGroups_RequestParameters"></a>

The request uses the following URI parameters.

 ** [MountTargetId](#API_ModifyMountTargetSecurityGroups_RequestSyntax) **   <a name="efs-ModifyMountTargetSecurityGroups-request-uri-MountTargetId"></a>
The ID of the mount target whose security groups you want to modify.
Length Constraints: Minimum length of 13. Maximum length of 45.
Pattern: `^fsmt-[0-9a-f]{8,40}$`
Required: Yes

## Request Body
<a name="API_ModifyMountTargetSecurityGroups_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [SecurityGroups](#API_ModifyMountTargetSecurityGroups_RequestSyntax) **   <a name="efs-ModifyMountTargetSecurityGroups-request-SecurityGroups"></a>
An array of VPC security group IDs.
Type: Array of strings
Array Members: Maximum number of 100 items.
Length Constraints: Minimum length of 11. Maximum length of 43.
Pattern: `^sg-[0-9a-f]{8,40}`
Required: No

## Response Syntax
<a name="API_ModifyMountTargetSecurityGroups_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_ModifyMountTargetSecurityGroups_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_ModifyMountTargetSecurityGroups_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequest **
Returned if the request is malformed or contains an error such as an invalid parameter value or a missing required parameter.
 ** ErrorCode **
The error code is a string that uniquely identifies an error condition. It is meant to be read and understood by programs that detect and handle errors by type.
 ** Message **
The error message contains a generic description of the error condition in English. It is intended for a human audience. Simple programs display the message directly to the end user if they encounter an error condition they don't know how or don't care to handle. Sophisticated programs with more exhaustive error handling and proper internationalization are more likely to ignore the error message.
HTTP Status Code: 400

 ** IncorrectMountTargetState **
Returned if the mount target is not in the correct state for the operation.
 ** ErrorCode **
The error code is a string that uniquely identifies an error condition. It is meant to be read and understood by programs that detect and handle errors by type.
 ** Message **
The error message contains a generic description of the error condition in English. It is intended for a human audience. Simple programs display the message directly to the end user if they encounter an error condition they don't know how or don't care to handle. Sophisticated programs with more exhaustive error handling and proper internationalization are more likely to ignore the error message.
HTTP Status Code: 409

 ** InternalServerError **
Returned if an error occurred on the server side.
 ** ErrorCode **
The error code is a string that uniquely identifies an error condition. It is meant to be read and understood by programs that detect and handle errors by type.
 ** Message **
The error message contains a generic description of the error condition in English. It is intended for a human audience. Simple programs display the message directly to the end user if they encounter an error condition they don't know how or don't care to handle. Sophisticated programs with more exhaustive error handling and proper internationalization are more likely to ignore the error message.
HTTP Status Code: 500

 ** MountTargetNotFound **
Returned if there is no mount target with the specified ID found in the caller's AWS account.
 ** ErrorCode **
The error code is a string that uniquely identifies an error condition. It is meant to be read and understood by programs that detect and handle errors by type.
 ** Message **
The error message contains a generic description of the error condition in English. It is intended for a human audience. Simple programs display the message directly to the end user if they encounter an error condition they don't know how or don't care to handle. Sophisticated programs with more exhaustive error handling and proper internationalization are more likely to ignore the error message.
HTTP Status Code: 404

 ** SecurityGroupLimitExceeded **
Returned if the number of `SecurityGroups` specified in the request is greater than the limit, which is based on account quota. Either delete some security groups or request that the account quota be raised. For more information, see [Amazon VPC Quotas](https://docs.aws.amazon.com/vpc/latest/userguide/amazon-vpc-limits.html) in the *Amazon VPC User Guide* (see the **Security Groups** table).
 ** ErrorCode **
The error code is a string that uniquely identifies an error condition. It is meant to be read and understood by programs that detect and handle errors by type.
 ** Message **
The error message contains a generic description of the error condition in English. It is intended for a human audience. Simple programs display the message directly to the end user if they encounter an error condition they don't know how or don't care to handle. Sophisticated programs with more exhaustive error handling and proper internationalization are more likely to ignore the error message.
HTTP Status Code: 400

 ** SecurityGroupNotFound **
Returned if one of the specified security groups doesn't exist in the subnet's virtual private cloud (VPC).
 ** ErrorCode **
The error code is a string that uniquely identifies an error condition. It is meant to be read and understood by programs that detect and handle errors by type.
 ** Message **
The error message contains a generic description of the error condition in English. It is intended for a human audience. Simple programs display the message directly to the end user if they encounter an error condition they don't know how or don't care to handle. Sophisticated programs with more exhaustive error handling and proper internationalization are more likely to ignore the error message.
HTTP Status Code: 400

## Examples
<a name="API_ModifyMountTargetSecurityGroups_Examples"></a>

### Replace a mount target's security groups
<a name="API_ModifyMountTargetSecurityGroups_Example_1"></a>

 The following example replaces security groups in effect for the network interface associated with a mount target.

#### Sample Request
<a name="API_ModifyMountTargetSecurityGroups_Example_1_Request"></a>

```
PUT /2015-02-01/mount-targets/fsmt-9a13661e/security-groups HTTP/1.1
Host: elasticfilesystem.us-west-2.amazonaws.com
x-amz-date: 20140620T223446Z
Authorization: <...>
Content-Type: application/json
Content-Length: 57

{
  "SecurityGroups" : [
  "sg-188d9f74"
  ]
}
```

#### Sample Response
<a name="API_ModifyMountTargetSecurityGroups_Example_1_Response"></a>

```
HTTP/1.1 204 No Content
x-amzn-RequestId: 01234567-89ab-cdef-0123-456789abcdef
```

## See Also
<a name="API_ModifyMountTargetSecurityGroups_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticfilesystem-2015-02-01/ModifyMountTargetSecurityGroups)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticfilesystem-2015-02-01/ModifyMountTargetSecurityGroups)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticfilesystem-2015-02-01/ModifyMountTargetSecurityGroups)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticfilesystem-2015-02-01/ModifyMountTargetSecurityGroups)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticfilesystem-2015-02-01/ModifyMountTargetSecurityGroups)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticfilesystem-2015-02-01/ModifyMountTargetSecurityGroups)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticfilesystem-2015-02-01/ModifyMountTargetSecurityGroups)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticfilesystem-2015-02-01/ModifyMountTargetSecurityGroups)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticfilesystem-2015-02-01/ModifyMountTargetSecurityGroups)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticfilesystem-2015-02-01/ModifyMountTargetSecurityGroups)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Elastic File System (EFS). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query efs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
