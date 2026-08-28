---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ImportSnapshot.html
---

# ImportSnapshot
<a name="API_ImportSnapshot"></a>

Imports a disk into an EBS snapshot.

For more information, see [Importing a disk as a snapshot using VM Import/Export](https://docs.aws.amazon.com/vm-import/latest/userguide/vmimport-import-snapshot.html) in the *VM Import/Export User Guide*.

## Request Parameters
<a name="API_ImportSnapshot_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **ClientData**
The client-specific data.
Type: [ClientData](API_ClientData.md) object
Required: No

 **ClientToken**
Token to enable idempotency for VM import requests.
Type: String
Required: No

 **Description**
The description string for the import snapshot task.
Type: String
Required: No

 **DiskContainer**
Information about the disk container.
Type: [SnapshotDiskContainer](API_SnapshotDiskContainer.md) object
Required: No

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **Encrypted**
Specifies whether the destination snapshot of the imported image should be encrypted. The default KMS key for EBS is used unless you specify a non-default KMS key using `KmsKeyId`. For more information, see [Amazon EBS Encryption](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html) in the *Amazon Elastic Compute Cloud User Guide*.
Type: Boolean
Required: No

 **KmsKeyId**
An identifier for the symmetric KMS key to use when creating the encrypted snapshot. This parameter is only required if you want to use a non-default KMS key; if this parameter is not specified, the default KMS key for EBS is used. If a `KmsKeyId` is specified, the `Encrypted` flag must also be set.
The KMS key identifier may be provided in any of the following formats:
+ Key ID
+ Key alias
+ ARN using key ID. The ID ARN contains the `arn:aws:kms` namespace, followed by the Region of the key, the AWS account ID of the key owner, the `key` namespace, and then the key ID. For example, arn:aws:kms:*us-east-1*:*012345678910*:key/*abcd1234-a123-456a-a12b-a123b4cd56ef*.
+ ARN using key alias. The alias ARN contains the `arn:aws:kms` namespace, followed by the Region of the key, the AWS account ID of the key owner, the `alias` namespace, and then the key alias. For example, arn:aws:kms:*us-east-1*:*012345678910*:alias/*ExampleAlias*.
 AWS parses `KmsKeyId` asynchronously, meaning that the action you call may appear to complete even though you provided an invalid identifier. This action will eventually report failure.
The specified KMS key must exist in the Region that the snapshot is being copied to.
Amazon EBS does not support asymmetric KMS keys.
Type: String
Required: No

 **RoleName**
The name of the role to use when not using the default role, 'vmimport'.
Type: String
Required: No

 **TagSpecification.N**
The tags to apply to the import snapshot task during creation.
Type: Array of [TagSpecification](API_TagSpecification.md) objects
Required: No

## Response Elements
<a name="API_ImportSnapshot_ResponseElements"></a>

The following elements are returned by the service.

 **description**
A description of the import snapshot task.
Type: String

 **importTaskId**
The ID of the import snapshot task.
Type: String

 **requestId**
The ID of the request.
Type: String

 **snapshotTaskDetail**
Information about the import snapshot task.
Type: [SnapshotTaskDetail](API_SnapshotTaskDetail.md) object

 **tagSet**
Any tags assigned to the import snapshot task.
Type: Array of [Tag](API_Tag.md) objects

## Errors
<a name="API_ImportSnapshot_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_ImportSnapshot_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/ImportSnapshot)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/ImportSnapshot)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ImportSnapshot)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/ImportSnapshot)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ImportSnapshot)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/ImportSnapshot)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/ImportSnapshot)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/ImportSnapshot)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/ImportSnapshot)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ImportSnapshot)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
