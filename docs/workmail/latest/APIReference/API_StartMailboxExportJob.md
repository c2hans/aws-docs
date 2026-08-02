---
source_url: https://docs.aws.amazon.com/workmail/latest/APIReference/API_StartMailboxExportJob.html
---

# StartMailboxExportJob
<a name="API_StartMailboxExportJob"></a>

**Important**
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).

Starts a mailbox export job to export MIME-format email messages and calendar items from the specified mailbox to the specified Amazon Simple Storage Service (Amazon S3) bucket. For more information, see [Exporting mailbox content](https://docs.aws.amazon.com/workmail/latest/adminguide/mail-export.html) in the *WorkMail Administrator Guide*.

## Request Syntax
<a name="API_StartMailboxExportJob_RequestSyntax"></a>

```
{
   "ClientToken": "{{string}}",
   "Description": "{{string}}",
   "EntityId": "{{string}}",
   "KmsKeyArn": "{{string}}",
   "OrganizationId": "{{string}}",
   "RoleArn": "{{string}}",
   "S3BucketName": "{{string}}",
   "S3Prefix": "{{string}}"
}
```

## Request Parameters
<a name="API_StartMailboxExportJob_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClientToken](#API_StartMailboxExportJob_RequestSyntax) **   <a name="workmail-StartMailboxExportJob-request-ClientToken"></a>
The idempotency token for the client request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\x21-\x7e]+`
Required: Yes

 ** [Description](#API_StartMailboxExportJob_RequestSyntax) **   <a name="workmail-StartMailboxExportJob-request-Description"></a>
The mailbox export job description.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1023.
Pattern: `[\S\s]*`
Required: No

 ** [EntityId](#API_StartMailboxExportJob_RequestSyntax) **   <a name="workmail-StartMailboxExportJob-request-EntityId"></a>
The identifier of the user or resource associated with the mailbox.
The identifier can accept *UserId or ResourceId*, *Username or Resourcename*, or *email*. The following identity formats are available:
+ Entity ID: 12345678-1234-1234-1234-123456789012, r-0123456789a0123456789b0123456789 , or S-1-1-12-1234567890-123456789-123456789-1234
+ Email address: entity@domain.tld
+ Entity name: entity
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9._%+@-]+`
Required: Yes

 ** [KmsKeyArn](#API_StartMailboxExportJob_RequestSyntax) **   <a name="workmail-StartMailboxExportJob-request-KmsKeyArn"></a>
The Amazon Resource Name (ARN) of the symmetric AWS Key Management Service (AWS KMS) key that encrypts the exported mailbox content.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws:kms:[a-z0-9-]*:[a-z0-9-]+:[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,1023}`
Required: Yes

 ** [OrganizationId](#API_StartMailboxExportJob_RequestSyntax) **   <a name="workmail-StartMailboxExportJob-request-OrganizationId"></a>
The identifier associated with the organization.
Type: String
Length Constraints: Fixed length of 34.
Pattern: `^m-[0-9a-f]{32}$`
Required: Yes

 ** [RoleArn](#API_StartMailboxExportJob_RequestSyntax) **   <a name="workmail-StartMailboxExportJob-request-RoleArn"></a>
The ARN of the AWS Identity and Access Management (IAM) role that grants write permission to the S3 bucket.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws:iam:[a-z0-9-]*:[a-z0-9-]+:[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,1023}`
Required: Yes

 ** [S3BucketName](#API_StartMailboxExportJob_RequestSyntax) **   <a name="workmail-StartMailboxExportJob-request-S3BucketName"></a>
The name of the S3 bucket.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[A-Za-z0-9.-]+`
Required: Yes

 ** [S3Prefix](#API_StartMailboxExportJob_RequestSyntax) **   <a name="workmail-StartMailboxExportJob-request-S3Prefix"></a>
The S3 bucket prefix.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1023.
Pattern: `[A-Za-z0-9!_.*'()/-]+`
Required: Yes

## Response Syntax
<a name="API_StartMailboxExportJob_ResponseSyntax"></a>

```
{
   "JobId": "string"
}
```

## Response Elements
<a name="API_StartMailboxExportJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [JobId](#API_StartMailboxExportJob_ResponseSyntax) **   <a name="workmail-StartMailboxExportJob-response-JobId"></a>
The job ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[A-Za-z0-9-]+`

## Errors
<a name="API_StartMailboxExportJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** EntityNotFoundException **
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).
The identifier supplied for the user, group, or resource does not exist in your organization.
HTTP Status Code: 400

 ** InvalidParameterException **
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).
One or more of the input parameters don't match the service's restrictions.
HTTP Status Code: 400

 ** LimitExceededException **
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).
The request exceeds the limit of the resource.
HTTP Status Code: 400

 ** OrganizationNotFoundException **
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).
An operation received a valid organization identifier that either doesn't belong or exist in the system.
HTTP Status Code: 400

 ** OrganizationStateException **
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).
The organization must have a valid state to perform certain operations on the organization or its members.
HTTP Status Code: 400

## See Also
<a name="API_StartMailboxExportJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workmail-2017-10-01/StartMailboxExportJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workmail-2017-10-01/StartMailboxExportJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workmail-2017-10-01/StartMailboxExportJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workmail-2017-10-01/StartMailboxExportJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workmail-2017-10-01/StartMailboxExportJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workmail-2017-10-01/StartMailboxExportJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workmail-2017-10-01/StartMailboxExportJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workmail-2017-10-01/StartMailboxExportJob)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/workmail-2017-10-01/StartMailboxExportJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workmail-2017-10-01/StartMailboxExportJob)
