---
source_url: https://docs.aws.amazon.com/workmail/latest/APIReference/API_DescribeMailboxExportJob.html
---

# DescribeMailboxExportJob
<a name="API_DescribeMailboxExportJob"></a>

**Important**
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).

Describes the current status of a mailbox export job.

## Request Syntax
<a name="API_DescribeMailboxExportJob_RequestSyntax"></a>

```
{
   "JobId": "{{string}}",
   "OrganizationId": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeMailboxExportJob_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [JobId](#API_DescribeMailboxExportJob_RequestSyntax) **   <a name="workmail-DescribeMailboxExportJob-request-JobId"></a>
The mailbox export job ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[A-Za-z0-9-]+`
Required: Yes

 ** [OrganizationId](#API_DescribeMailboxExportJob_RequestSyntax) **   <a name="workmail-DescribeMailboxExportJob-request-OrganizationId"></a>
The organization ID.
Type: String
Length Constraints: Fixed length of 34.
Pattern: `^m-[0-9a-f]{32}$`
Required: Yes

## Response Syntax
<a name="API_DescribeMailboxExportJob_ResponseSyntax"></a>

```
{
   "Description": "string",
   "EndTime": number,
   "EntityId": "string",
   "ErrorInfo": "string",
   "EstimatedProgress": number,
   "KmsKeyArn": "string",
   "RoleArn": "string",
   "S3BucketName": "string",
   "S3Path": "string",
   "S3Prefix": "string",
   "StartTime": number,
   "State": "string"
}
```

## Response Elements
<a name="API_DescribeMailboxExportJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Description](#API_DescribeMailboxExportJob_ResponseSyntax) **   <a name="workmail-DescribeMailboxExportJob-response-Description"></a>
The mailbox export job description.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1023.
Pattern: `[\S\s]*`

 ** [EndTime](#API_DescribeMailboxExportJob_ResponseSyntax) **   <a name="workmail-DescribeMailboxExportJob-response-EndTime"></a>
The mailbox export job end timestamp.
Type: Timestamp

 ** [EntityId](#API_DescribeMailboxExportJob_ResponseSyntax) **   <a name="workmail-DescribeMailboxExportJob-response-EntityId"></a>
The identifier of the user or resource associated with the mailbox.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 256.

 ** [ErrorInfo](#API_DescribeMailboxExportJob_ResponseSyntax) **   <a name="workmail-DescribeMailboxExportJob-response-ErrorInfo"></a>
Error information for failed mailbox export jobs.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\S\s]*`

 ** [EstimatedProgress](#API_DescribeMailboxExportJob_ResponseSyntax) **   <a name="workmail-DescribeMailboxExportJob-response-EstimatedProgress"></a>
The estimated progress of the mailbox export job, in percentage points.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 100.

 ** [KmsKeyArn](#API_DescribeMailboxExportJob_ResponseSyntax) **   <a name="workmail-DescribeMailboxExportJob-response-KmsKeyArn"></a>
The Amazon Resource Name (ARN) of the symmetric AWS Key Management Service (AWS KMS) key that encrypts the exported mailbox content.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws:kms:[a-z0-9-]*:[a-z0-9-]+:[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,1023}`

 ** [RoleArn](#API_DescribeMailboxExportJob_ResponseSyntax) **   <a name="workmail-DescribeMailboxExportJob-response-RoleArn"></a>
The ARN of the AWS Identity and Access Management (IAM) role that grants write permission to the Amazon Simple Storage Service (Amazon S3) bucket.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws:iam:[a-z0-9-]*:[a-z0-9-]+:[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,1023}`

 ** [S3BucketName](#API_DescribeMailboxExportJob_ResponseSyntax) **   <a name="workmail-DescribeMailboxExportJob-response-S3BucketName"></a>
The name of the S3 bucket.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[A-Za-z0-9.-]+`

 ** [S3Path](#API_DescribeMailboxExportJob_ResponseSyntax) **   <a name="workmail-DescribeMailboxExportJob-response-S3Path"></a>
The path to the S3 bucket and file that the mailbox export job is exporting to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1023.
Pattern: `[A-Za-z0-9!_.*'()/-]+`

 ** [S3Prefix](#API_DescribeMailboxExportJob_ResponseSyntax) **   <a name="workmail-DescribeMailboxExportJob-response-S3Prefix"></a>
The S3 bucket prefix.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1023.
Pattern: `[A-Za-z0-9!_.*'()/-]+`

 ** [StartTime](#API_DescribeMailboxExportJob_ResponseSyntax) **   <a name="workmail-DescribeMailboxExportJob-response-StartTime"></a>
The mailbox export job start timestamp.
Type: Timestamp

 ** [State](#API_DescribeMailboxExportJob_ResponseSyntax) **   <a name="workmail-DescribeMailboxExportJob-response-State"></a>
The state of the mailbox export job.
Type: String
Valid Values: `RUNNING | COMPLETED | FAILED | CANCELLED`

## Errors
<a name="API_DescribeMailboxExportJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** EntityNotFoundException **
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).
The identifier supplied for the user, group, or resource does not exist in your organization.
HTTP Status Code: 400

 ** InvalidParameterException **
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).
One or more of the input parameters don't match the service's restrictions.
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
<a name="API_DescribeMailboxExportJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workmail-2017-10-01/DescribeMailboxExportJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workmail-2017-10-01/DescribeMailboxExportJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workmail-2017-10-01/DescribeMailboxExportJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workmail-2017-10-01/DescribeMailboxExportJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workmail-2017-10-01/DescribeMailboxExportJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workmail-2017-10-01/DescribeMailboxExportJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workmail-2017-10-01/DescribeMailboxExportJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workmail-2017-10-01/DescribeMailboxExportJob)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/workmail-2017-10-01/DescribeMailboxExportJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workmail-2017-10-01/DescribeMailboxExportJob)
