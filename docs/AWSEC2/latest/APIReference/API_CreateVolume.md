---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateVolume.html
---

# CreateVolume
<a name="API_CreateVolume"></a>

Creates an EBS volume that can be attached to an instance in the same Availability Zone.

You can create a new empty volume or restore a volume from an EBS snapshot. Any AWS Marketplace product codes from the snapshot are propagated to the volume.

You can create encrypted volumes. Encrypted volumes must be attached to instances that support Amazon EBS encryption. Volumes that are created from encrypted snapshots are also automatically encrypted. For more information, see [Amazon EBS encryption](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-encryption.html) in the *Amazon EBS User Guide*.

You can tag your volumes during creation. For more information, see [Tag your Amazon EC2 resources](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html) in the *Amazon EC2 User Guide*.

For more information, see [Create an Amazon EBS volume](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-creating-volume.html) in the *Amazon EBS User Guide*.

## Request Parameters
<a name="API_CreateVolume_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **AvailabilityZone**
The ID of the Availability Zone in which to create the volume. For example, `us-east-1a`.
Either `AvailabilityZone` or `AvailabilityZoneId` must be specified, but not both.
Type: String
Required: No

 **AvailabilityZoneId**
The ID of the Availability Zone in which to create the volume. For example, `use1-az1`.
Either `AvailabilityZone` or `AvailabilityZoneId` must be specified, but not both.
Type: String
Required: No

 **ClientToken**
Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see [Ensure Idempotency](https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html).
Type: String
Required: No

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **Encrypted**
Indicates whether the volume should be encrypted. The effect of setting the encryption state to `true` depends on the volume origin (new or from a snapshot), starting encryption state, ownership, and whether encryption by default is enabled. For more information, see [Encryption by default](https://docs.aws.amazon.com/ebs/latest/userguide/work-with-ebs-encr.html#encryption-by-default) in the *Amazon EBS User Guide*.
Encrypted Amazon EBS volumes must be attached to instances that support Amazon EBS encryption. For more information, see [Supported instance types](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-encryption-requirements.html#ebs-encryption_supported_instances).
Type: Boolean
Required: No

 **Iops**
The number of I/O operations per second (IOPS) to provision for the volume. Required for `io1` and `io2` volumes. Optional for `gp3` volumes. Omit for all other volume types.
Valid ranges:
+ gp3: `3,000 `(*default*)` - 80,000` IOPS
+ io1: `100 - 64,000` IOPS
+ io2: `100 - 256,000` IOPS
 [ Instances built on the Nitro System](https://docs.aws.amazon.com/ec2/latest/instancetypes/ec2-nitro-instances.html) can support up to 256,000 IOPS. Other instances can support up to 32,000 IOPS.
Type: Integer
Required: No

 **KmsKeyId**
The identifier of the AWS KMS key to use for Amazon EBS encryption. If this parameter is not specified, your AWS KMS key for Amazon EBS is used. If `KmsKeyId` is specified, the encrypted state must be `true`.
You can specify the KMS key using any of the following:
+ Key ID. For example, 1234abcd-12ab-34cd-56ef-1234567890ab.
+ Key alias. For example, alias/ExampleAlias.
+ Key ARN. For example, arn:aws:kms:us-east-1:012345678910:key/1234abcd-12ab-34cd-56ef-1234567890ab.
+ Alias ARN. For example, arn:aws:kms:us-east-1:012345678910:alias/ExampleAlias.
 AWS authenticates the KMS key asynchronously. Therefore, if you specify an ID, alias, or ARN that is not valid, the action can appear to complete, but eventually fails.
Type: String
Required: No

 **MultiAttachEnabled**
Indicates whether to enable Amazon EBS Multi-Attach. If you enable Multi-Attach, you can attach the volume to up to 16 [Instances built on the Nitro System](https://docs.aws.amazon.com/ec2/latest/instancetypes/ec2-nitro-instances.html) in the same Availability Zone. This parameter is supported with `io1` and `io2` volumes only. For more information, see [ Amazon EBS Multi-Attach](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volumes-multi.html) in the *Amazon EBS User Guide*.
Type: Boolean
Required: No

 **Operator**
Reserved for internal use.
Type: [OperatorRequest](API_OperatorRequest.md) object
Required: No

 **OutpostArn**
The Amazon Resource Name (ARN) of the Outpost on which to create the volume.
If you intend to use a volume with an instance running on an outpost, then you must create the volume on the same outpost as the instance. You can't use a volume created in an AWS Region with an instance on an AWS outpost, or the other way around.
Type: String
Required: No

 **Size**
The size of the volume, in GiBs. You must specify either a snapshot ID or a volume size. If you specify a snapshot, the default is the snapshot size, and you can specify a volume size that is equal to or larger than the snapshot size.
Valid sizes:
+ gp2: `1 - 16,384` GiB
+ gp3: `1 - 65,536` GiB
+ io1: `4 - 16,384` GiB
+ io2: `4 - 65,536` GiB
+ st1 and sc1: `125 - 16,384` GiB
+ standard: `1 - 1024` GiB
Type: Integer
Required: No

 **SnapshotId**
The snapshot from which to create the volume. You must specify either a snapshot ID or a volume size.
Type: String
Required: No

 **TagSpecification.N**
The tags to apply to the volume during creation.
Type: Array of [TagSpecification](API_TagSpecification.md) objects
Required: No

 **Throughput**
The throughput to provision for the volume, in MiB/s. Supported for `gp3` volumes only. Omit for all other volume types.
Valid Range: `125 - 2000` MiB/s
Type: Integer
Required: No

 **VolumeInitializationRate**
Specifies the Amazon EBS Provisioned Rate for Volume Initialization (volume initialization rate), in MiB/s, at which to download the snapshot blocks from Amazon S3 to the volume. This is also known as *volume initialization*. Specifying a volume initialization rate ensures that the volume is initialized at a predictable and consistent rate after creation.
This parameter is supported only for volumes created from snapshots. Omit this parameter if:
+ You want to create the volume using fast snapshot restore. You must specify a snapshot that is enabled for fast snapshot restore. In this case, the volume is fully initialized at creation.
**Note**
If you specify a snapshot that is enabled for fast snapshot restore and a volume initialization rate, the volume will be initialized at the specified rate instead of fast snapshot restore.
+ You want to create a volume that is initialized at the default rate.
For more information, see [ Initialize Amazon EBS volumes](https://docs.aws.amazon.com/ebs/latest/userguide/initalize-volume.html) in the *Amazon EC2 User Guide*.
Valid range: 100 - 300 MiB/s
Type: Integer
Required: No

 **VolumeType**
The volume type. This parameter can be one of the following values:
+ General Purpose SSD: `gp2` \| `gp3`
+ Provisioned IOPS SSD: `io1` \| `io2`
+ Throughput Optimized HDD: `st1`
+ Cold HDD: `sc1`
+ Magnetic: `standard`
Throughput Optimized HDD (`st1`) and Cold HDD (`sc1`) volumes can't be used as boot volumes.
For more information, see [Amazon EBS volume types](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volume-types.html) in the *Amazon EBS User Guide*.
Default: `gp2`
Type: String
Valid Values: `standard | io1 | io2 | gp2 | sc1 | st1 | gp3`
Required: No

## Response Elements
<a name="API_CreateVolume_ResponseElements"></a>

The following elements are returned by the service.

 **attachmentSet**
This parameter is not returned by CreateVolume.
Information about the volume attachments.
Type: Array of [VolumeAttachment](API_VolumeAttachment.md) objects

 **availabilityZone**
The Availability Zone for the volume.
Type: String

 **availabilityZoneId**
The ID of the Availability Zone for the volume.
Type: String

 **createTime**
The time stamp when volume creation was initiated.
Type: Timestamp

 **encrypted**
Indicates whether the volume is encrypted.
Type: Boolean

 **fastRestored**
This parameter is not returned by CreateVolume.
Indicates whether the volume was created using fast snapshot restore.
Type: Boolean

 **iops**
The number of I/O operations per second (IOPS). For `gp3`, `io1`, and `io2` volumes, this represents the number of IOPS that are provisioned for the volume. For `gp2` volumes, this represents the baseline performance of the volume and the rate at which the volume accumulates I/O credits for bursting.
Type: Integer

 **kmsKeyId**
The Amazon Resource Name (ARN) of the AWS KMS key that was used to protect the volume encryption key for the volume.
Type: String

 **multiAttachEnabled**
Indicates whether Amazon EBS Multi-Attach is enabled.
Type: Boolean

 **operator**
The service provider that manages the volume.
Type: [OperatorResponse](API_OperatorResponse.md) object

 **outpostArn**
The Amazon Resource Name (ARN) of the Outpost.
Type: String

 **requestId**
The ID of the request.
Type: String

 **size**
The size of the volume, in GiBs.
Type: Integer

 **snapshotId**
The snapshot from which the volume was created, if applicable.
Type: String

 **sourceVolumeId**
The ID of the source volume from which the volume copy was created. Only for volume copies.
Type: String

 **sseType**
This parameter is not returned by CreateVolume.
Reserved for future use.
Type: String
Valid Values: `sse-ebs | sse-kms | none`

 **status**
The volume state.
Type: String
Valid Values: `creating | available | in-use | deleting | deleted | error`

 **tagSet**
Any tags assigned to the volume.
Type: Array of [Tag](API_Tag.md) objects

 **throughput**
The throughput that the volume supports, in MiB/s.
Type: Integer

 **volumeId**
The ID of the volume.
Type: String

 **volumeInitializationRate**
The Amazon EBS Provisioned Rate for Volume Initialization (volume initialization rate) specified for the volume during creation, in MiB/s. If no volume initialization rate was specified, the value is `null`.
Type: Integer

 **volumeType**
The volume type.
Type: String
Valid Values: `standard | io1 | io2 | gp2 | sc1 | st1 | gp3`

## Errors
<a name="API_CreateVolume_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_CreateVolume_Examples"></a>

### Example 1
<a name="API_CreateVolume_Example_1"></a>

This example request creates an 150 GiB Multi-Attach enabled `io1` volume in the `us-east-1a` Availability Zone.

#### Sample Request
<a name="API_CreateVolume_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=CreateVolume
&VolumeType=io1
&Size=150
&Iops=7500
&AvailabilityZone=us-east-1a
&MultiAttachEnabled=true
&AUTHPARAMS
```

#### Sample Response
<a name="API_CreateVolume_Example_1_Response"></a>

```
<CreateVolumeResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
  <requestId>59dbff89-35bd-4eac-99ed-be587EXAMPLE</requestId>
  <volumeId>vol-1234567890abcdef0</volumeId>
  <size>150</size>
  <iops>7500</iops>
  <snapshotId/>
  <availabilityZone>us-east-1a</availabilityZone>
  <status>creating</status>
  <createTime>YYYY-MM-DDTHH:MM:SS.000Z</createTime>
  <volumeType>io1;</volumeType>
  <encrypted>true</encrypted>
  <multiAttachEnabled>true</multiAttachEnabled>
</CreateVolumeResponse>
```

### Example 2
<a name="API_CreateVolume_Example_2"></a>

This example request creates an 80 GiB encrypted volume in the Availability Zone `us-east-1a`.

#### Sample Request
<a name="API_CreateVolume_Example_2_Request"></a>

```
https://ec2.amazonaws.com/?Action=CreateVolume
&Size=80
&AvailabilityZone=us-east-1a
&Encrypted=true
&AUTHPARAMS
```

#### Sample Response
<a name="API_CreateVolume_Example_2_Response"></a>

```
<CreateVolumeResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>248f69ab-c7a9-4ad2-8e7c-b7556EXAMPLE</requestId>
    <volumeId>vol-08bf1d00afabcdef0</volumeId>
    <size>80</size>
    <snapshotId></snapshotId>
    <availabilityZone>us-east-1a</availabilityZone>
    <status>creating</status>
    <createTime>2020-11-30T10:39:56.000Z</createTime>
    <volumeType>gp2</volumeType>
    <iops>189</iops>
    <encrypted>true</encrypted>
    <kmsKeyId>arn:aws:kms:us-east-1:123456789012:key/237eb1a7-2fa1-44dc-b95e-6c526EXAMPLE</kmsKeyId>
    <tagSet/>
    <multiAttachEnabled>false</multiAttachEnabled>
</CreateVolumeResponse>
```

### Example 3
<a name="API_CreateVolume_Example_3"></a>

This example request creates a volume and applies a tag with a key of `stack` and a value of `production`.

#### Sample Request
<a name="API_CreateVolume_Example_3_Request"></a>

```
https://ec2.amazonaws.com/?Action=CreateVolume
&Size=80
&AvailabilityZone=us-east-1a
&TagSpecification.1.ResourceType=volume
&TagSpecification.1.Tag.1.Key=stack
&TagSpecification.1.Tag.1.Value=production
&AUTHPARAMS
```

#### Sample Response
<a name="API_CreateVolume_Example_3_Response"></a>

```
<CreateVolumeResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>bb216d10-54b9-4bc2-958d-fcfe2EXAMPLE</requestId>
    <volumeId>vol-043c91f2fa4abcdef</volumeId>
    <size>80</size>
    <snapshotId></snapshotId>
    <availabilityZone>us-east-1a</availabilityZone>
    <status>creating</status>
    <createTime>2020-11-30T10:47:43.000Z</createTime>
    <volumeType>gp2</volumeType>
    <iops>189</iops>
    <encrypted>true</encrypted>
    <kmsKeyId>arn:aws:kms:us-east-1:123456789012:key/237eb1a7-2fa1-44dc-b95e-6c526EXAMPLE</kmsKeyId>
    <tagSet>
        <item>
            <key>stack</key>
            <value>production</value>
        </item>
    </tagSet>
    <multiAttachEnabled>false</multiAttachEnabled>
</CreateVolumeResponse>
```

## See Also
<a name="API_CreateVolume_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/CreateVolume)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/CreateVolume)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CreateVolume)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/CreateVolume)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CreateVolume)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/CreateVolume)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/CreateVolume)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/CreateVolume)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/CreateVolume)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CreateVolume)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
