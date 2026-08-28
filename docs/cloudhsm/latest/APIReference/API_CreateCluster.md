---
source_url: https://docs.aws.amazon.com/cloudhsm/latest/APIReference/API_CreateCluster.html
---

# CreateCluster
<a name="API_CreateCluster"></a>

Creates a new AWS CloudHSM cluster.

 **Cross-account use:** Yes. To perform this operation with an AWS CloudHSM backup in a different AWS account, specify the full backup ARN in the value of the SourceBackupId parameter.

## Request Syntax
<a name="API_CreateCluster_RequestSyntax"></a>

```
{
   "BackupRetentionPolicy": {
      "Type": "{{string}}",
      "Value": "{{string}}"
   },
   "HsmType": "{{string}}",
   "Mode": "{{string}}",
   "NetworkType": "{{string}}",
   "SourceBackupId": "{{string}}",
   "SubnetIds": [ "{{string}}" ],
   "TagList": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateCluster_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [BackupRetentionPolicy](#API_CreateCluster_RequestSyntax) **   <a name="CloudHSMV2-CreateCluster-request-BackupRetentionPolicy"></a>
A policy that defines how the service retains backups.
Type: [BackupRetentionPolicy](API_BackupRetentionPolicy.md) object
Required: No

 ** [HsmType](#API_CreateCluster_RequestSyntax) **   <a name="CloudHSMV2-CreateCluster-request-HsmType"></a>
The type of HSM to use in the cluster. The allowed values are `hsm1.medium` and `hsm2m.medium`.
Type: String
Length Constraints: Maximum length of 32.
Pattern: `((p|)hsm[0-9][a-z.]*\.[a-zA-Z]+)`
Required: Yes

 ** [Mode](#API_CreateCluster_RequestSyntax) **   <a name="CloudHSMV2-CreateCluster-request-Mode"></a>
The mode to use in the cluster. The allowed values are `FIPS` and `NON_FIPS`.
Type: String
Valid Values: `FIPS | NON_FIPS`
Required: No

 ** [NetworkType](#API_CreateCluster_RequestSyntax) **   <a name="CloudHSMV2-CreateCluster-request-NetworkType"></a>
The NetworkType to create a cluster with. The allowed values are `IPV4` and `DUALSTACK`.
Type: String
Valid Values: `IPV4 | DUALSTACK`
Required: No

 ** [SourceBackupId](#API_CreateCluster_RequestSyntax) **   <a name="CloudHSMV2-CreateCluster-request-SourceBackupId"></a>
The identifier (ID) or the Amazon Resource Name (ARN) of the cluster backup to restore. Use this value to restore the cluster from a backup instead of creating a new cluster. To find the backup ID or ARN, use [DescribeBackups](API_DescribeBackups.md). *If using a backup in another account, the full ARN must be supplied.*
Type: String
Pattern: `^(arn:aws(-(us-gov))?:cloudhsm:([a-z]{2}(-(gov|isob|iso))?-(east|west|north|south|central){1,2}-[0-9]{1}):[0-9]{12}:backup/)?backup-[2-7a-zA-Z]{11,16}`
Required: No

 ** [SubnetIds](#API_CreateCluster_RequestSyntax) **   <a name="CloudHSMV2-CreateCluster-request-SubnetIds"></a>
The identifiers (IDs) of the subnets where you are creating the cluster. You must specify at least one subnet. If you specify multiple subnets, they must meet the following criteria:
+ All subnets must be in the same virtual private cloud (VPC).
+ You can specify only one subnet per Availability Zone.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Pattern: `subnet-[0-9a-fA-F]{8,17}`
Required: Yes

 ** [TagList](#API_CreateCluster_RequestSyntax) **   <a name="CloudHSMV2-CreateCluster-request-TagList"></a>
Tags to apply to the AWS CloudHSM cluster during creation.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Required: No

## Response Syntax
<a name="API_CreateCluster_ResponseSyntax"></a>

```
{
   "Cluster": {
      "BackupPolicy": "string",
      "BackupRetentionPolicy": {
         "Type": "string",
         "Value": "string"
      },
      "Certificates": {
         "AwsHardwareCertificate": "string",
         "ClusterCertificate": "string",
         "ClusterCsr": "string",
         "HsmCertificate": "string",
         "ManufacturerHardwareCertificate": "string"
      },
      "ClusterId": "string",
      "CreateTimestamp": number,
      "Hsms": [
         {
            "AvailabilityZone": "string",
            "ClusterId": "string",
            "EniId": "string",
            "EniIp": "string",
            "EniIpV6": "string",
            "HsmId": "string",
            "HsmType": "string",
            "State": "string",
            "StateMessage": "string",
            "SubnetId": "string"
         }
      ],
      "HsmType": "string",
      "HsmTypeRollbackExpiration": number,
      "Mode": "string",
      "NetworkType": "string",
      "PreCoPassword": "string",
      "SecurityGroup": "string",
      "SourceBackupId": "string",
      "State": "string",
      "StateMessage": "string",
      "SubnetMapping": {
         "string" : "string"
      },
      "TagList": [
         {
            "Key": "string",
            "Value": "string"
         }
      ],
      "VpcId": "string"
   }
}
```

## Response Elements
<a name="API_CreateCluster_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Cluster](#API_CreateCluster_ResponseSyntax) **   <a name="CloudHSMV2-CreateCluster-response-Cluster"></a>
Information about the cluster that was created.
Type: [Cluster](API_Cluster.md) object

## Errors
<a name="API_CreateCluster_Errors"></a>

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
<a name="API_CreateCluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudhsmv2-2017-04-28/CreateCluster)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudhsmv2-2017-04-28/CreateCluster)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudhsmv2-2017-04-28/CreateCluster)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudhsmv2-2017-04-28/CreateCluster)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudhsmv2-2017-04-28/CreateCluster)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudhsmv2-2017-04-28/CreateCluster)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudhsmv2-2017-04-28/CreateCluster)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudhsmv2-2017-04-28/CreateCluster)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudhsmv2-2017-04-28/CreateCluster)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudhsmv2-2017-04-28/CreateCluster)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudHSM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudhsm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
