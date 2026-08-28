---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CopyImage.html
---

# CopyImage
<a name="API_CopyImage"></a>

Initiates an AMI copy operation. You must specify the source AMI ID and both the source and destination locations. The copy operation must be initiated in the destination Region.

**CopyImage supports the following source to destination copies:**
+ Region to Region
+ Region to Outpost
+ Parent Region to Local Zone
+ Local Zone to parent Region
+ Between Local Zones with the same parent Region (only supported for certain Local Zones)

**CopyImage does not support the following source to destination copies:**
+ Local Zone to non-parent Regions
+ Between Local Zones with different parent Regions
+ Local Zone to Outpost
+ Outpost to Local Zone
+ Outpost to Region
+ Between Outposts
+ Within same Outpost
+ Cross-partition copies (use [CreateStoreImageTask](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateStoreImageTask.html) instead)

**Destination specification**
+ Region to Region: The destination Region is the Region in which you initiate the copy operation.
+ Region to Outpost: Specify the destination using the `DestinationOutpostArn` parameter (the ARN of the Outpost)
+ Region to Local Zone, and Local Zone to Local Zone copies: Specify the destination using the `DestinationAvailabilityZone` parameter (the name of the destination Local Zone) or `DestinationAvailabilityZoneId` parameter (the ID of the destination Local Zone).

**Snapshot encryption**
+ Region to Outpost: Backing snapshots copied to an Outpost are encrypted by default using the default encryption key for the Region or the key that you specify. Outposts do not support unencrypted snapshots.
+ Region to Local Zone, and Local Zone to Local Zone: Not all Local Zones require encrypted snapshots. In Local Zones that require encrypted snapshots, backing snapshots are automatically encrypted during copy. In Local Zones where encryption is not required, snapshots retain their original encryption state (encrypted or unencrypted) by default.

For more information, including the required permissions for copying an AMI, see [Copy an Amazon EC2 AMI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/CopyingAMIs.html) in the *Amazon EC2 User Guide*.

## Request Parameters
<a name="API_CopyImage_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **ClientToken**
Unique, case-sensitive identifier you provide to ensure idempotency of the request. For more information, see [Ensuring idempotency in Amazon EC2 API requests](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html) in the *Amazon EC2 API Reference*.
Type: String
Required: No

 **CopyImageTags**
Specifies whether to copy your user-defined AMI tags to the new AMI.
The following tags are not be copied:
+ System tags (prefixed with `aws:`)
+ For public and shared AMIs, user-defined tags that are attached by other AWS accounts
Default: Your user-defined AMI tags are not copied.
Type: Boolean
Required: No

 **Description**
A description for the new AMI.
Type: String
Required: No

 **DestinationAvailabilityZone**
The Local Zone for the new AMI (for example, `cn-north-1-pkx-1a`).
Only one of `DestinationAvailabilityZone`, `DestinationAvailabilityZoneId`, or `DestinationOutpostArn` can be specified.
Type: String
Required: No

 **DestinationAvailabilityZoneId**
The ID of the Local Zone for the new AMI (for example, `cnn1-pkx1-az1`).
Only one of `DestinationAvailabilityZone`, `DestinationAvailabilityZoneId`, or `DestinationOutpostArn` can be specified.
Type: String
Required: No

 **DestinationOutpostArn**
The Amazon Resource Name (ARN) of the Outpost for the new AMI.
Only specify this parameter when copying an AMI from an AWS Region to an Outpost. The AMI must be in the Region of the destination Outpost. You can't copy an AMI from an Outpost to a Region, from one Outpost to another, or within the same Outpost.
For more information, see [Copy AMIs from an AWS Region to an Outpost](https://docs.aws.amazon.com/ebs/latest/userguide/snapshots-outposts.html#copy-amis) in the *Amazon EBS User Guide*.
Only one of `DestinationAvailabilityZone`, `DestinationAvailabilityZoneId`, or `DestinationOutpostArn` can be specified.
Type: String
Required: No

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **Encrypted**
Specifies whether to encrypt the snapshots of the copied image.
You can encrypt a copy of an unencrypted snapshot, but you cannot create an unencrypted copy of an encrypted snapshot. The default KMS key for Amazon EBS is used unless you specify a non-default AWS Key Management Service (AWS KMS) KMS key using `KmsKeyId`. For more information, see [Use encryption with EBS-backed AMIs](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIEncryption.html) in the *Amazon EC2 User Guide*.
Type: Boolean
Required: No

 **KmsKeyId**
The identifier of the symmetric AWS Key Management Service (AWS KMS) KMS key to use when creating encrypted volumes. If this parameter is not specified, your AWS managed KMS key for Amazon EBS is used. If you specify a KMS key, you must also set the encrypted state to `true`.
You can specify a KMS key using any of the following:
+ Key ID. For example, 1234abcd-12ab-34cd-56ef-1234567890ab.
+ Key alias. For example, alias/ExampleAlias.
+ Key ARN. For example, arn:aws:kms:us-east-1:012345678910:key/1234abcd-12ab-34cd-56ef-1234567890ab.
+ Alias ARN. For example, arn:aws:kms:us-east-1:012345678910:alias/ExampleAlias.
 AWS authenticates the KMS key asynchronously. Therefore, if you specify an identifier that is not valid, the action can appear to complete, but eventually fails.
The specified KMS key must exist in the destination Region.
Amazon EBS does not support asymmetric KMS keys.
Type: String
Required: No

 **Name**
The name of the new AMI.
Type: String
Required: Yes

 **SnapshotCopyCompletionDurationMinutes**
Specify a completion duration, in 15 minute increments, to initiate a time-based AMI copy. The specified completion duration applies to each of the snapshots associated with the AMI. Each snapshot associated with the AMI will be completed within the specified completion duration, with copy throughput automatically adjusted for each snapshot based on its size to meet the timing target.
If you do not specify a value, the AMI copy operation is completed on a best-effort basis.
This parameter is not supported when copying an AMI to or from a Local Zone, or to an Outpost.
For more information, see [Time-based copies for Amazon EBS snapshots and EBS-backed AMIs](https://docs.aws.amazon.com/ebs/latest/userguide/time-based-copies.html).
Type: Long
Required: No

 **SourceImageId**
The ID of the AMI to copy.
Type: String
Required: Yes

 **SourceRegion**
The name of the Region that contains the AMI to copy.
Type: String
Required: Yes

 **TagSpecification.N**
The tags to apply to the new AMI and new snapshots. You can tag the AMI, the snapshots, or both.
+ To tag the new AMI, the value for `ResourceType` must be `image`.
+ To tag the new snapshots, the value for `ResourceType` must be `snapshot`. The same tag is applied to all the new snapshots.
If you specify other values for `ResourceType`, the request fails.
To tag an AMI or snapshot after it has been created, see [CreateTags](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateTags.html).
Type: Array of [TagSpecification](API_TagSpecification.md) objects
Required: No

## Response Elements
<a name="API_CopyImage_ResponseElements"></a>

The following elements are returned by the service.

 **imageId**
The ID of the new AMI.
Type: String

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_CopyImage_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_CopyImage_Examples"></a>

### Example
<a name="API_CopyImage_Example_1"></a>

This example request copies the AMI in `us-west-2` with the ID `ami-1a2b3c4d`, naming the new AMI `My-Standard-AMI`.

#### Sample Request
<a name="API_CopyImage_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=CopyImage
&SourceRegion=us-west-2
&SourceImageId=ami-1a2b3c4d
&Name=My-Standard-AMI
&Description=This%20is%20the%20new%20version%20of%20My-Standard-AMI
&ClientToken=550e8400-e29b-41d4-a716-446655440000
&AUTHPARAMS
```

#### Sample Response
<a name="API_CopyImage_Example_1_Response"></a>

```
<CopyImageResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
   <requestId>60bc441d-fa2c-494d-b155-5d6a3EXAMPLE</requestId>
   <imageId>ami-4d3c2b1a</imageId>
</CopyImageResponse>
```

## See Also
<a name="API_CopyImage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/CopyImage)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/CopyImage)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CopyImage)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/CopyImage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CopyImage)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/CopyImage)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/CopyImage)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/CopyImage)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/CopyImage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CopyImage)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
