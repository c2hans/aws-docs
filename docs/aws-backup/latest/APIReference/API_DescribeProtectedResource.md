---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_DescribeProtectedResource.html
---

# DescribeProtectedResource
<a name="API_DescribeProtectedResource"></a>

Returns information about a saved resource, including the last time it was backed up, its Amazon Resource Name (ARN), and the AWS service type of the saved resource.

## Request Syntax
<a name="API_DescribeProtectedResource_RequestSyntax"></a>

```
GET /resources/{{resourceArn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeProtectedResource_RequestParameters"></a>

The request uses the following URI parameters.

 ** [resourceArn](#API_DescribeProtectedResource_RequestSyntax) **   <a name="Backup-DescribeProtectedResource-request-uri-ResourceArn"></a>
An Amazon Resource Name (ARN) that uniquely identifies a resource. The format of the ARN depends on the resource type.
Required: Yes

## Request Body
<a name="API_DescribeProtectedResource_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeProtectedResource_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "LastBackupTime": number,
   "LastBackupVaultArn": "string",
   "LastRecoveryPointArn": "string",
   "LatestRestoreExecutionTimeMinutes": number,
   "LatestRestoreJobCreationDate": number,
   "LatestRestoreRecoveryPointCreationDate": number,
   "ResourceArn": "string",
   "ResourceName": "string",
   "ResourceType": "string"
}
```

## Response Elements
<a name="API_DescribeProtectedResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [LastBackupTime](#API_DescribeProtectedResource_ResponseSyntax) **   <a name="Backup-DescribeProtectedResource-response-LastBackupTime"></a>
The date and time that a resource was last backed up, in Unix format and Coordinated Universal Time (UTC). The value of `LastBackupTime` is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.
Type: Timestamp

 ** [LastBackupVaultArn](#API_DescribeProtectedResource_ResponseSyntax) **   <a name="Backup-DescribeProtectedResource-response-LastBackupVaultArn"></a>
The ARN (Amazon Resource Name) of the backup vault that contains the most recent backup recovery point.
Type: String

 ** [LastRecoveryPointArn](#API_DescribeProtectedResource_ResponseSyntax) **   <a name="Backup-DescribeProtectedResource-response-LastRecoveryPointArn"></a>
The ARN (Amazon Resource Name) of the most recent recovery point.
Type: String

 ** [LatestRestoreExecutionTimeMinutes](#API_DescribeProtectedResource_ResponseSyntax) **   <a name="Backup-DescribeProtectedResource-response-LatestRestoreExecutionTimeMinutes"></a>
The time, in minutes, that the most recent restore job took to complete.
Type: Long

 ** [LatestRestoreJobCreationDate](#API_DescribeProtectedResource_ResponseSyntax) **   <a name="Backup-DescribeProtectedResource-response-LatestRestoreJobCreationDate"></a>
The creation date of the most recent restore job.
Type: Timestamp

 ** [LatestRestoreRecoveryPointCreationDate](#API_DescribeProtectedResource_ResponseSyntax) **   <a name="Backup-DescribeProtectedResource-response-LatestRestoreRecoveryPointCreationDate"></a>
The date the most recent recovery point was created.
Type: Timestamp

 ** [ResourceArn](#API_DescribeProtectedResource_ResponseSyntax) **   <a name="Backup-DescribeProtectedResource-response-ResourceArn"></a>
An ARN that uniquely identifies a resource. The format of the ARN depends on the resource type.
Type: String

 ** [ResourceName](#API_DescribeProtectedResource_ResponseSyntax) **   <a name="Backup-DescribeProtectedResource-response-ResourceName"></a>
The name of the resource that belongs to the specified backup.
Type: String

 ** [ResourceType](#API_DescribeProtectedResource_ResponseSyntax) **   <a name="Backup-DescribeProtectedResource-response-ResourceType"></a>
The type of AWS resource saved as a recovery point; for example, an Amazon EBS volume or an Amazon RDS database.
Type: String
Pattern: `^[a-zA-Z0-9\-\_\.]{1,50}$`

## Errors
<a name="API_DescribeProtectedResource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterValueException **
Indicates that something is wrong with a parameter's value. For example, the value is out of range.
 ** Context **

 ** Type **

HTTP Status Code: 400

 ** MissingParameterValueException **
Indicates that a required parameter is missing.
 ** Context **

 ** Type **

HTTP Status Code: 400

 ** ResourceNotFoundException **
A resource that is required for the action doesn't exist.
 ** Context **

 ** Type **

HTTP Status Code: 400

 ** ServiceUnavailableException **
The request failed due to a temporary failure of the server.
 ** Context **

 ** Type **

HTTP Status Code: 500

## See Also
<a name="API_DescribeProtectedResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/backup-2018-11-15/DescribeProtectedResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/backup-2018-11-15/DescribeProtectedResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-2018-11-15/DescribeProtectedResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/backup-2018-11-15/DescribeProtectedResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-2018-11-15/DescribeProtectedResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/backup-2018-11-15/DescribeProtectedResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/backup-2018-11-15/DescribeProtectedResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/backup-2018-11-15/DescribeProtectedResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/backup-2018-11-15/DescribeProtectedResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-2018-11-15/DescribeProtectedResource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Backup. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-backup` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
