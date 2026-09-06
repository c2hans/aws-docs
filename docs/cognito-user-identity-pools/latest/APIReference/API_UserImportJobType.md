---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_UserImportJobType.html
---

# UserImportJobType
<a name="API_UserImportJobType"></a>

A user import job in a user pool. Describes the status of user import with a CSV file. For more information, see [Importing users into user pools from a CSV file](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-using-import-tool.html).

This data type is a request parameter of [CreateUserImportJob](API_CreateUserImportJob.md), [DescribeUserImportJob](API_DescribeUserImportJob.md), [ListUserImportJobs](API_ListUserImportJobs.md), [StartUserImportJob](API_StartUserImportJob.md), and [StopUserImportJob](API_StopUserImportJob.md).

## Contents
<a name="API_UserImportJobType_Contents"></a>

 ** CloudWatchLogsRoleArn **   <a name="CognitoUserPools-Type-UserImportJobType-CloudWatchLogsRoleArn"></a>
The role Amazon Resource Name (ARN) for the Amazon CloudWatch Logging role for the user import job. For more information, see "Creating the CloudWatch Logs IAM Role" in the Amazon Cognito Developer Guide.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[\w+=/,.@-]+:[\w+=/,.@-]+:([\w+=/,.@-]*)?:[0-9]+:[\w+=/,.@-]+(:[\w+=/,.@-]+)?(:[\w+=/,.@-]+)?`
Required: No

 ** CompletionDate **   <a name="CognitoUserPools-Type-UserImportJobType-CompletionDate"></a>
The date when the user import job was completed.
Type: Timestamp
Required: No

 ** CompletionMessage **   <a name="CognitoUserPools-Type-UserImportJobType-CompletionMessage"></a>
The message returned when the user import job is completed.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w]+`
Required: No

 ** CreationDate **   <a name="CognitoUserPools-Type-UserImportJobType-CreationDate"></a>
The date and time when the item was created. Amazon Cognito returns this timestamp in UNIX epoch time format. Your SDK might render the output in a human-readable format like ISO 8601 or a Java `Date` object.
Type: Timestamp
Required: No

 ** FailedUsers **   <a name="CognitoUserPools-Type-UserImportJobType-FailedUsers"></a>
The number of users that couldn't be imported.
Type: Long
Required: No

 ** ImportedUsers **   <a name="CognitoUserPools-Type-UserImportJobType-ImportedUsers"></a>
The number of users that were successfully imported.
Type: Long
Required: No

 ** JobId **   <a name="CognitoUserPools-Type-UserImportJobType-JobId"></a>
The ID of the user import job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 55.
Pattern: `import-[0-9a-zA-Z-]+`
Required: No

 ** JobName **   <a name="CognitoUserPools-Type-UserImportJobType-JobName"></a>
The friendly name of the user import job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w\s+=,.@-]+`
Required: No

 ** PasswordHashingAlgorithm **   <a name="CognitoUserPools-Type-UserImportJobType-PasswordHashingAlgorithm"></a>
The password hashing algorithm used to generate the hashes in the CSV file for this import job.
Valid values: `BCRYPT` \| `SCRYPT` \| `ARGON2ID` \| `PBKDF2_SHA256`
Type: String
Valid Values: `BCRYPT | SCRYPT | ARGON2ID | PBKDF2_SHA256`
Required: No

 ** PreSignedUrl **   <a name="CognitoUserPools-Type-UserImportJobType-PreSignedUrl"></a>
The pre-signed URL target for uploading the CSV file.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

 ** SkippedUsers **   <a name="CognitoUserPools-Type-UserImportJobType-SkippedUsers"></a>
The number of users that were skipped.
Type: Long
Required: No

 ** StartDate **   <a name="CognitoUserPools-Type-UserImportJobType-StartDate"></a>
The date when the user import job was started.
Type: Timestamp
Required: No

 ** Status **   <a name="CognitoUserPools-Type-UserImportJobType-Status"></a>
The status of the user import job. One of the following:
+  `Created` - The job was created but not started.
+  `Pending` - A transition state. You have started the job, but it has not begun importing users yet.
+  `InProgress` - The job has started, and users are being imported.
+  `Stopping` - You have stopped the job, but the job has not stopped importing users yet.
+  `Stopped` - You have stopped the job, and the job has stopped importing users.
+  `Succeeded` - The job has completed successfully.
+  `Failed` - The job has stopped due to an error.
+  `Expired` - You created a job, but did not start the job within 24-48 hours. All data associated with the job was deleted, and the job can't be started.
Type: String
Valid Values: `Created | Pending | InProgress | Stopping | Expired | Stopped | Failed | Succeeded`
Required: No

 ** UserPoolId **   <a name="CognitoUserPools-Type-UserImportJobType-UserPoolId"></a>
The ID of the user pool that the users are being imported into.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 55.
Pattern: `[\w-]+_[0-9a-zA-Z]+`
Required: No

## See Also
<a name="API_UserImportJobType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/UserImportJobType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/UserImportJobType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/UserImportJobType)
