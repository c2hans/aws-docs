---
source_url: https://docs.aws.amazon.com/cloudhsm/latest/APIReference/API_DescribeBackups.html
---

# DescribeBackups
<a name="API_DescribeBackups"></a>

Gets information about backups of AWS CloudHSM clusters. Lists either the backups you own or the backups shared with you when the Shared parameter is true.

This is a paginated operation, which means that each response might contain only a subset of all the backups. When the response contains only a subset of backups, it includes a `NextToken` value. Use this value in a subsequent `DescribeBackups` request to get more backups. When you receive a response with no `NextToken` (or an empty or null value), that means there are no more backups to get.

 **Cross-account use:** Yes. Customers can describe backups in other AWS accounts that are shared with them.

## Request Syntax
<a name="API_DescribeBackups_RequestSyntax"></a>

```
{
   "Filters": {
      "{{string}}" : [ "{{string}}" ]
   },
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "Shared": {{boolean}},
   "SortAscending": {{boolean}}
}
```

## Request Parameters
<a name="API_DescribeBackups_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Filters](#API_DescribeBackups_RequestSyntax) **   <a name="CloudHSMV2-DescribeBackups-request-Filters"></a>
One or more filters to limit the items returned in the response.
Use the `backupIds` filter to return only the specified backups. Specify backups by their backup identifier (ID).
Use the `sourceBackupIds` filter to return only the backups created from a source backup. The `sourceBackupID` of a source backup is returned by the [CopyBackupToRegion](API_CopyBackupToRegion.md) operation.
Use the `clusterIds` filter to return only the backups for the specified clusters. Specify clusters by their cluster identifier (ID).
Use the `states` filter to return only backups that match the specified state.
Use the `neverExpires` filter to return backups filtered by the value in the `neverExpires` parameter. `True` returns all backups exempt from the backup retention policy. `False` returns all backups with a backup retention policy defined at the cluster.
Type: String to array of strings map
Map Entries: Maximum number of 30 items.
Key Pattern: `[a-zA-Z0-9_-]+`
Required: No

 ** [MaxResults](#API_DescribeBackups_RequestSyntax) **   <a name="CloudHSMV2-DescribeBackups-request-MaxResults"></a>
The maximum number of backups to return in the response. When there are more backups than the number you specify, the response contains a `NextToken` value.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50.
Required: No

 ** [NextToken](#API_DescribeBackups_RequestSyntax) **   <a name="CloudHSMV2-DescribeBackups-request-NextToken"></a>
The `NextToken` value that you received in the previous response. Use this value to get more backups.
Type: String
Length Constraints: Maximum length of 256.
Pattern: `.*`
Required: No

 ** [Shared](#API_DescribeBackups_RequestSyntax) **   <a name="CloudHSMV2-DescribeBackups-request-Shared"></a>
Describe backups that are shared with you.
By default when using this option, the command returns backups that have been shared using a standard AWS Resource Access Manager resource share. In order for a backup that was shared using the PutResourcePolicy command to be returned, the share must be promoted to a standard resource share using the AWS RAM [PromoteResourceShareCreatedFromPolicy](https://docs.aws.amazon.com/cli/latest/reference/ram/promote-resource-share-created-from-policy.html) API operation. For more information about sharing backups, see [ Working with shared backups](https://docs.aws.amazon.com/cloudhsm/latest/userguide/sharing.html) in the AWS CloudHSM User Guide.
Type: Boolean
Required: No

 ** [SortAscending](#API_DescribeBackups_RequestSyntax) **   <a name="CloudHSMV2-DescribeBackups-request-SortAscending"></a>
Designates whether or not to sort the return backups by ascending chronological order of generation.
Type: Boolean
Required: No

## Response Syntax
<a name="API_DescribeBackups_ResponseSyntax"></a>

```
{
   "Backups": [
      {
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
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_DescribeBackups_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Backups](#API_DescribeBackups_ResponseSyntax) **   <a name="CloudHSMV2-DescribeBackups-response-Backups"></a>
A list of backups.
Type: Array of [Backup](API_Backup.md) objects

 ** [NextToken](#API_DescribeBackups_ResponseSyntax) **   <a name="CloudHSMV2-DescribeBackups-response-NextToken"></a>
An opaque string that indicates that the response contains only a subset of backups. Use this value in a subsequent `DescribeBackups` request to get more backups.
Type: String
Length Constraints: Maximum length of 256.
Pattern: `.*`

## Errors
<a name="API_DescribeBackups_Errors"></a>

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

 ** CloudHsmTagException **
The request was rejected because of a tagging failure. Verify the tag conditions in all applicable policies, and then retry the request.
HTTP Status Code: 400

## See Also
<a name="API_DescribeBackups_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudhsmv2-2017-04-28/DescribeBackups)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudhsmv2-2017-04-28/DescribeBackups)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudhsmv2-2017-04-28/DescribeBackups)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudhsmv2-2017-04-28/DescribeBackups)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudhsmv2-2017-04-28/DescribeBackups)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudhsmv2-2017-04-28/DescribeBackups)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudhsmv2-2017-04-28/DescribeBackups)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudhsmv2-2017-04-28/DescribeBackups)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudhsmv2-2017-04-28/DescribeBackups)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudhsmv2-2017-04-28/DescribeBackups)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudHSM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudhsm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
