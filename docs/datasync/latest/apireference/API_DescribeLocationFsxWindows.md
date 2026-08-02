---
source_url: https://docs.aws.amazon.com/datasync/latest/apireference/API_DescribeLocationFsxWindows.html
---

# DescribeLocationFsxWindows
<a name="API_DescribeLocationFsxWindows"></a>

Provides details about how an AWS DataSync transfer location for an Amazon FSx for Windows File Server file system is configured.

## Request Syntax
<a name="API_DescribeLocationFsxWindows_RequestSyntax"></a>

```
{
   "LocationArn": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeLocationFsxWindows_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [LocationArn](#API_DescribeLocationFsxWindows_RequestSyntax) **   <a name="DataSync-DescribeLocationFsxWindows-request-LocationArn"></a>
Specifies the Amazon Resource Name (ARN) of the FSx for Windows File Server location.
Type: String
Length Constraints: Maximum length of 128.
Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):datasync:[a-z\-0-9]+:[0-9]{12}:location/loc-[0-9a-z]{17}$`
Required: Yes

## Response Syntax
<a name="API_DescribeLocationFsxWindows_ResponseSyntax"></a>

```
{
   "CmkSecretConfig": {
      "KmsKeyArn": "string",
      "SecretArn": "string"
   },
   "CreationTime": number,
   "CustomSecretConfig": {
      "SecretAccessRoleArn": "string",
      "SecretArn": "string"
   },
   "Domain": "string",
   "LocationArn": "string",
   "LocationUri": "string",
   "ManagedSecretConfig": {
      "SecretArn": "string"
   },
   "SecurityGroupArns": [ "string" ],
   "User": "string"
}
```

## Response Elements
<a name="API_DescribeLocationFsxWindows_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CmkSecretConfig](#API_DescribeLocationFsxWindows_ResponseSyntax) **   <a name="DataSync-DescribeLocationFsxWindows-response-CmkSecretConfig"></a>
Describes configuration information for a DataSync-managed secret, such as a `Password` that DataSync uses to access a specific storage location, with a customer-managed AWS KMS key.
Type: [CmkSecretConfig](API_CmkSecretConfig.md) object

 ** [CreationTime](#API_DescribeLocationFsxWindows_ResponseSyntax) **   <a name="DataSync-DescribeLocationFsxWindows-response-CreationTime"></a>
The time that the FSx for Windows File Server location was created.
Type: Timestamp

 ** [CustomSecretConfig](#API_DescribeLocationFsxWindows_ResponseSyntax) **   <a name="DataSync-DescribeLocationFsxWindows-response-CustomSecretConfig"></a>
Describes configuration information for a customer-managed secret, such as a `Password` that DataSync uses to access a specific storage location, with a customer-managed AWS Identity and Access Management (IAM) role that provides access to the secret.
Type: [CustomSecretConfig](API_CustomSecretConfig.md) object

 ** [Domain](#API_DescribeLocationFsxWindows_ResponseSyntax) **   <a name="DataSync-DescribeLocationFsxWindows-response-Domain"></a>
The name of the Microsoft Active Directory domain that the FSx for Windows File Server file system belongs to.
Type: String
Length Constraints: Maximum length of 253.
Pattern: `^[A-Za-z0-9]((\.|-+)?[A-Za-z0-9]){0,252}$`

 ** [LocationArn](#API_DescribeLocationFsxWindows_ResponseSyntax) **   <a name="DataSync-DescribeLocationFsxWindows-response-LocationArn"></a>
The ARN of the FSx for Windows File Server location.
Type: String
Length Constraints: Maximum length of 128.
Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):datasync:[a-z\-0-9]+:[0-9]{12}:location/loc-[0-9a-z]{17}$`

 ** [LocationUri](#API_DescribeLocationFsxWindows_ResponseSyntax) **   <a name="DataSync-DescribeLocationFsxWindows-response-LocationUri"></a>
The uniform resource identifier (URI) of the FSx for Windows File Server location.
Type: String
Length Constraints: Maximum length of 4360.
Pattern: `^(efs|nfs|s3|smb|hdfs|fsx[a-z0-9-]+)://[a-zA-Z0-9.:/\-]+$`

 ** [ManagedSecretConfig](#API_DescribeLocationFsxWindows_ResponseSyntax) **   <a name="DataSync-DescribeLocationFsxWindows-response-ManagedSecretConfig"></a>
Describes configuration information for a DataSync-managed secret, such as a `Password` that DataSync uses to access a specific storage location. DataSync uses the default AWS-managed KMS key to encrypt this secret in AWS Secrets Manager.
Type: [ManagedSecretConfig](API_ManagedSecretConfig.md) object

 ** [SecurityGroupArns](#API_DescribeLocationFsxWindows_ResponseSyntax) **   <a name="DataSync-DescribeLocationFsxWindows-response-SecurityGroupArns"></a>
The ARNs of the Amazon EC2 security groups that provide access to your file system's preferred subnet.
For information about configuring security groups for file system access, see the [https://docs.aws.amazon.com/fsx/latest/WindowsGuide/limit-access-security-groups.html](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/limit-access-security-groups.html).
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Length Constraints: Maximum length of 128.
Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):ec2:[a-z\-0-9]*:[0-9]{12}:security-group/sg-[a-f0-9]+$`

 ** [User](#API_DescribeLocationFsxWindows_ResponseSyntax) **   <a name="DataSync-DescribeLocationFsxWindows-response-User"></a>
The user with the permissions to mount and access the FSx for Windows File Server file system.
Type: String
Length Constraints: Maximum length of 104.
Pattern: `^[^\x22\x5B\x5D/\\:;|=,+*?\x3C\x3E]{1,104}$`

## Errors
<a name="API_DescribeLocationFsxWindows_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalException **
This exception is thrown when an error occurs in the AWS DataSync service.
HTTP Status Code: 500

 ** InvalidRequestException **
This exception is thrown when the client submits a malformed request.
HTTP Status Code: 400

## See Also
<a name="API_DescribeLocationFsxWindows_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datasync-2018-11-09/DescribeLocationFsxWindows)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datasync-2018-11-09/DescribeLocationFsxWindows)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datasync-2018-11-09/DescribeLocationFsxWindows)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datasync-2018-11-09/DescribeLocationFsxWindows)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datasync-2018-11-09/DescribeLocationFsxWindows)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datasync-2018-11-09/DescribeLocationFsxWindows)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datasync-2018-11-09/DescribeLocationFsxWindows)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datasync-2018-11-09/DescribeLocationFsxWindows)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datasync-2018-11-09/DescribeLocationFsxWindows)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datasync-2018-11-09/DescribeLocationFsxWindows)
