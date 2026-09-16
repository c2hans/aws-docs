---
source_url: https://docs.aws.amazon.com/efs/latest/APIReference/API_CreateAccessPoint.html
---

# CreateAccessPoint
<a name="API_CreateAccessPoint"></a>

Creates an EFS access point. An access point is an application-specific view into an EFS file system that applies an operating system user and group, and a file system path, to any file system request made through the access point. The operating system user and group override any identity information provided by the NFS client. The file system path is exposed as the access point's root directory. Applications using the access point can only access data in the application's own directory and any subdirectories. A file system can have a maximum of 10,000 access points unless you request an increase. To learn more, see [Mounting a file system using EFS access points](https://docs.aws.amazon.com/efs/latest/ug/efs-access-points.html).

**Note**
If multiple requests to create access points on the same file system are sent in quick succession, and the file system is near the limit of access points, you may experience a throttling response for these requests. This is to ensure that the file system does not exceed the stated access point limit.

This operation requires permissions for the `elasticfilesystem:CreateAccessPoint` action.

Access points can be tagged on creation. If tags are specified in the creation action, IAM performs additional authorization on the `elasticfilesystem:TagResource` action to verify if users have permissions to create tags. Therefore, you must grant explicit permissions to use the `elasticfilesystem:TagResource` action. For more information, see [Granting permissions to tag resources during creation](https://docs.aws.amazon.com/efs/latest/ug/using-tags-efs.html#supported-iam-actions-tagging.html).

## Request Syntax
<a name="API_CreateAccessPoint_RequestSyntax"></a>

```
POST /2015-02-01/access-points HTTP/1.1
Content-type: application/json

{
   "ClientToken": "{{string}}",
   "FileSystemId": "{{string}}",
   "PosixUser": {
      "Gid": {{number}},
      "SecondaryGids": [ {{number}} ],
      "Uid": {{number}}
   },
   "RootDirectory": {
      "CreationInfo": {
         "OwnerGid": {{number}},
         "OwnerUid": {{number}},
         "Permissions": "{{string}}"
      },
      "Path": "{{string}}"
   },
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_CreateAccessPoint_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateAccessPoint_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ClientToken](#API_CreateAccessPoint_RequestSyntax) **   <a name="efs-CreateAccessPoint-request-ClientToken"></a>
A string of up to 64 ASCII characters that Amazon EFS uses to ensure idempotent creation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `.+`
Required: Yes

 ** [FileSystemId](#API_CreateAccessPoint_RequestSyntax) **   <a name="efs-CreateAccessPoint-request-FileSystemId"></a>
The ID of the EFS file system that the access point provides access to.
Type: String
Length Constraints: Maximum length of 128.
Pattern: `^(arn:aws[-a-z]*:elasticfilesystem:[0-9a-z-:]+:file-system/fs-[0-9a-f]{8,40}|fs-[0-9a-f]{8,40})$`
Required: Yes

 ** [PosixUser](#API_CreateAccessPoint_RequestSyntax) **   <a name="efs-CreateAccessPoint-request-PosixUser"></a>
The operating system user and group applied to all file system requests made using the access point.
Type: [PosixUser](API_PosixUser.md) object
Required: No

 ** [RootDirectory](#API_CreateAccessPoint_RequestSyntax) **   <a name="efs-CreateAccessPoint-request-RootDirectory"></a>
Specifies the directory on the EFS file system that the access point exposes as the root directory of your file system to NFS clients using the access point. The clients using the access point can only access the root directory and below. If the `RootDirectory` > `Path` specified does not exist, Amazon EFS creates it and applies the `CreationInfo` settings when a client connects to an access point. When specifying a `RootDirectory`, you must provide the `Path`, and the `CreationInfo`.
Amazon EFS creates a root directory only if you have provided the CreationInfo: OwnUid, OwnGID, and permissions for the directory. If you do not provide this information, Amazon EFS does not create the root directory. If the root directory does not exist, attempts to mount using the access point will fail.
Type: [RootDirectory](API_RootDirectory.md) object
Required: No

 ** [Tags](#API_CreateAccessPoint_RequestSyntax) **   <a name="efs-CreateAccessPoint-request-Tags"></a>
Creates tags associated with the access point. Each tag is a key-value pair, each key must be unique. For more information, see [Tagging AWS resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) in the * AWS General Reference Guide*.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## Response Syntax
<a name="API_CreateAccessPoint_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "AccessPointArn": "string",
   "AccessPointId": "string",
   "ClientToken": "string",
   "FileSystemId": "string",
   "LifeCycleState": "string",
   "Name": "string",
   "OwnerId": "string",
   "PosixUser": {
      "Gid": number,
      "SecondaryGids": [ number ],
      "Uid": number
   },
   "RootDirectory": {
      "CreationInfo": {
         "OwnerGid": number,
         "OwnerUid": number,
         "Permissions": "string"
      },
      "Path": "string"
   },
   "Tags": [
      {
         "Key": "string",
         "Value": "string"
      }
   ]
}
```

## Response Elements
<a name="API_CreateAccessPoint_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AccessPointArn](#API_CreateAccessPoint_ResponseSyntax) **   <a name="efs-CreateAccessPoint-response-AccessPointArn"></a>
The unique Amazon Resource Name (ARN) associated with the access point.
Type: String
Length Constraints: Maximum length of 128.
Pattern: `^arn:aws[-a-z]*:elasticfilesystem:[0-9a-z-:]+:access-point/fsap-[0-9a-f]{8,40}$`

 ** [AccessPointId](#API_CreateAccessPoint_ResponseSyntax) **   <a name="efs-CreateAccessPoint-response-AccessPointId"></a>
The ID of the access point, assigned by Amazon EFS.
Type: String
Length Constraints: Maximum length of 128.
Pattern: `^(arn:aws[-a-z]*:elasticfilesystem:[0-9a-z-:]+:access-point/fsap-[0-9a-f]{8,40}|fsap-[0-9a-f]{8,40})$`

 ** [ClientToken](#API_CreateAccessPoint_ResponseSyntax) **   <a name="efs-CreateAccessPoint-response-ClientToken"></a>
The opaque string specified in the request to ensure idempotent creation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `.+`

 ** [FileSystemId](#API_CreateAccessPoint_ResponseSyntax) **   <a name="efs-CreateAccessPoint-response-FileSystemId"></a>
The ID of the EFS file system that the access point applies to.
Type: String
Length Constraints: Maximum length of 128.
Pattern: `^(arn:aws[-a-z]*:elasticfilesystem:[0-9a-z-:]+:file-system/fs-[0-9a-f]{8,40}|fs-[0-9a-f]{8,40})$`

 ** [LifeCycleState](#API_CreateAccessPoint_ResponseSyntax) **   <a name="efs-CreateAccessPoint-response-LifeCycleState"></a>
Identifies the lifecycle phase of the access point.
Type: String
Valid Values: `creating | available | updating | deleting | deleted | error`

 ** [Name](#API_CreateAccessPoint_ResponseSyntax) **   <a name="efs-CreateAccessPoint-response-Name"></a>
The name of the access point. This is the value of the `Name` tag.
Type: String

 ** [OwnerId](#API_CreateAccessPoint_ResponseSyntax) **   <a name="efs-CreateAccessPoint-response-OwnerId"></a>
Identifies the AWS account that owns the access point resource.
Type: String
Length Constraints: Maximum length of 14.
Pattern: `^(\d{12})|(\d{4}-\d{4}-\d{4})$`

 ** [PosixUser](#API_CreateAccessPoint_ResponseSyntax) **   <a name="efs-CreateAccessPoint-response-PosixUser"></a>
The full POSIX identity, including the user ID, group ID, and secondary group IDs on the access point that is used for all file operations by NFS clients using the access point.
Type: [PosixUser](API_PosixUser.md) object

 ** [RootDirectory](#API_CreateAccessPoint_ResponseSyntax) **   <a name="efs-CreateAccessPoint-response-RootDirectory"></a>
The directory on the EFS file system that the access point exposes as the root directory to NFS clients using the access point.
Type: [RootDirectory](API_RootDirectory.md) object

 ** [Tags](#API_CreateAccessPoint_ResponseSyntax) **   <a name="efs-CreateAccessPoint-response-Tags"></a>
The tags associated with the access point, presented as an array of Tag objects.
Type: Array of [Tag](API_Tag.md) objects

## Errors
<a name="API_CreateAccessPoint_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessPointAlreadyExists **
Returned if the access point that you are trying to create already exists, with the creation token you provided in the request.
 ** ErrorCode **
The error code is a string that uniquely identifies an error condition. It is meant to be read and understood by programs that detect and handle errors by type.
 ** Message **
The error message contains a generic description of the error condition in English. It is intended for a human audience. Simple programs display the message directly to the end user if they encounter an error condition they don't know how or don't care to handle. Sophisticated programs with more exhaustive error handling and proper internationalization are more likely to ignore the error message.
HTTP Status Code: 409

 ** AccessPointLimitExceeded **
Returned if the AWS account has already created the maximum number of access points allowed per file system. For more informaton, see [https://docs.aws.amazon.com/efs/latest/ug/limits.html#limits-efs-resources-per-account-per-region](https://docs.aws.amazon.com/efs/latest/ug/limits.html#limits-efs-resources-per-account-per-region).
 ** ErrorCode **
The error code is a string that uniquely identifies an error condition. It is meant to be read and understood by programs that detect and handle errors by type.
 ** Message **
The error message contains a generic description of the error condition in English. It is intended for a human audience. Simple programs display the message directly to the end user if they encounter an error condition they don't know how or don't care to handle. Sophisticated programs with more exhaustive error handling and proper internationalization are more likely to ignore the error message.
HTTP Status Code: 403

 ** BadRequest **
Returned if the request is malformed or contains an error such as an invalid parameter value or a missing required parameter.
 ** ErrorCode **
The error code is a string that uniquely identifies an error condition. It is meant to be read and understood by programs that detect and handle errors by type.
 ** Message **
The error message contains a generic description of the error condition in English. It is intended for a human audience. Simple programs display the message directly to the end user if they encounter an error condition they don't know how or don't care to handle. Sophisticated programs with more exhaustive error handling and proper internationalization are more likely to ignore the error message.
HTTP Status Code: 400

 ** FileSystemNotFound **
Returned if the specified `FileSystemId` value doesn't exist in the requester's AWS account.
 ** ErrorCode **
The error code is a string that uniquely identifies an error condition. It is meant to be read and understood by programs that detect and handle errors by type.
 ** Message **
The error message contains a generic description of the error condition in English. It is intended for a human audience. Simple programs display the message directly to the end user if they encounter an error condition they don't know how or don't care to handle. Sophisticated programs with more exhaustive error handling and proper internationalization are more likely to ignore the error message.
HTTP Status Code: 404

 ** IncorrectFileSystemLifeCycleState **
Returned if the file system's lifecycle state is not "available".
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

 ** ThrottlingException **
Returned when the `CreateAccessPoint` API action is called too quickly and the number of Access Points on the file system is nearing the [limit of 120](https://docs.aws.amazon.com/efs/latest/ug/limits.html#limits-efs-resources-per-account-per-region).
 ** ErrorCode **
The error code is a string that uniquely identifies an error condition. It is meant to be read and understood by programs that detect and handle errors by type.
 ** Message **
The error message contains a generic description of the error condition in English. It is intended for a human audience. Simple programs display the message directly to the end user if they encounter an error condition they don't know how or don't care to handle. Sophisticated programs with more exhaustive error handling and proper internationalization are more likely to ignore the error message.
HTTP Status Code: 429

## See Also
<a name="API_CreateAccessPoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticfilesystem-2015-02-01/CreateAccessPoint)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticfilesystem-2015-02-01/CreateAccessPoint)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticfilesystem-2015-02-01/CreateAccessPoint)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticfilesystem-2015-02-01/CreateAccessPoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticfilesystem-2015-02-01/CreateAccessPoint)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticfilesystem-2015-02-01/CreateAccessPoint)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticfilesystem-2015-02-01/CreateAccessPoint)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticfilesystem-2015-02-01/CreateAccessPoint)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/elasticfilesystem-2015-02-01/CreateAccessPoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticfilesystem-2015-02-01/CreateAccessPoint)
