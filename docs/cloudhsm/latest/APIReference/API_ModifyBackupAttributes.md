---
source_url: https://docs.aws.amazon.com/cloudhsm/latest/APIReference/API_ModifyBackupAttributes.html
---

# ModifyBackupAttributes
<a name="API_ModifyBackupAttributes"></a>

Modifies attributes for AWS CloudHSM backup.

 **Cross-account use:** No. You cannot perform this operation on an AWS CloudHSM backup in a different AWS account.

## Request Syntax
<a name="API_ModifyBackupAttributes_RequestSyntax"></a>

```
{
   "BackupId": "{{string}}",
   "NeverExpires": {{boolean}}
}
```

## Request Parameters
<a name="API_ModifyBackupAttributes_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [BackupId](#API_ModifyBackupAttributes_RequestSyntax) **   <a name="CloudHSMV2-ModifyBackupAttributes-request-BackupId"></a>
The identifier (ID) of the backup to modify. To find the ID of a backup, use the [DescribeBackups](API_DescribeBackups.md) operation.
Type: String
Pattern: `backup-[2-7a-zA-Z]{11,16}`
Required: Yes

 ** [NeverExpires](#API_ModifyBackupAttributes_RequestSyntax) **   <a name="CloudHSMV2-ModifyBackupAttributes-request-NeverExpires"></a>
Specifies whether the service should exempt a backup from the retention policy for the cluster. `True` exempts a backup from the retention policy. `False` means the service applies the backup retention policy defined at the cluster.
Type: Boolean
Required: Yes

## Response Syntax
<a name="API_ModifyBackupAttributes_ResponseSyntax"></a>

```
{
   "Backup": {
      "BackupArn": "string",
      "BackupId": "string",
      "BackupState": "string",
      "ClusterId": "string",
      "CopyTimestamp": number,
      "CreateTimestamp": number,
      "DeleteTimestamp": number,
      "HsmType": "string",
      "Mode": "string",
      "NeverExpires": boolean,
      "SourceBackup": "string",
      "SourceCluster": "string",
      "SourceRegion": "string",
      "TagList": [
         {
            "Key": "string",
            "Value": "string"
         }
      ]
   }
}
```

## Response Elements
<a name="API_ModifyBackupAttributes_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Backup](#API_ModifyBackupAttributes_ResponseSyntax) **   <a name="CloudHSMV2-ModifyBackupAttributes-response-Backup"></a>
Contains information about a backup of an AWS CloudHSM cluster. All backup objects contain the `BackupId`, `BackupState`, `ClusterId`, and `CreateTimestamp` parameters. Backups that were copied into a destination region additionally contain the `CopyTimestamp`, `SourceBackup`, `SourceCluster`, and `SourceRegion` parameters. A backup that is pending deletion will include the `DeleteTimestamp` parameter.
Type: [Backup](API_Backup.md) object

## Errors
<a name="API_ModifyBackupAttributes_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** CloudHsmAccessDeniedException **
The request was rejected because the requester does not have permission to perform the requested operation.
HTTP Status Code: 400

 ** CloudHsmInternalFailureException **
The request was rejected because of an AWS CloudHSM internal failure. The request can be retried.
HTTP Status Code: 500

 ** CloudHsmInvalidRequestException **
The request was rejected because it is not a valid request.
HTTP Status Code: 400

 ** CloudHsmResourceNotFoundException **
The request was rejected because it refers to a resource that cannot be found.
HTTP Status Code: 400

 ** CloudHsmServiceException **
The request was rejected because an error occurred.
HTTP Status Code: 400

## See Also
<a name="API_ModifyBackupAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudhsmv2-2017-04-28/ModifyBackupAttributes)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudhsmv2-2017-04-28/ModifyBackupAttributes)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudhsmv2-2017-04-28/ModifyBackupAttributes)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudhsmv2-2017-04-28/ModifyBackupAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudhsmv2-2017-04-28/ModifyBackupAttributes)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudhsmv2-2017-04-28/ModifyBackupAttributes)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudhsmv2-2017-04-28/ModifyBackupAttributes)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudhsmv2-2017-04-28/ModifyBackupAttributes)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudhsmv2-2017-04-28/ModifyBackupAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudhsmv2-2017-04-28/ModifyBackupAttributes)
