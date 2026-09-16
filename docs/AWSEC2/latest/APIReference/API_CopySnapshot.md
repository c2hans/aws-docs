---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CopySnapshot.html
---

# CopySnapshot
<a name="API_CopySnapshot"></a>

Creates an exact copy of an Amazon EBS snapshot.

The location of the source snapshot determines whether you can copy it or not, and the allowed destinations for the snapshot copy.
+ If the source snapshot is in a Region, you can copy it within that Region, to another Region, to an Outpost associated with that Region, or to a Local Zone in that Region.
+ If the source snapshot is in a Local Zone, you can copy it within that Local Zone, to another Local Zone in the same zone group, or to the parent Region of the Local Zone.
+ If the source snapshot is on an Outpost, you can't copy it.

When copying snapshots to a Region, the encryption outcome for the snapshot copy depends on the Amazon EBS encryption by default setting for the destination Region, the encryption status of the source snapshot, and the encryption parameters you specify in the request. For more information, see [ Encryption and snapshot copying](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-copy-snapshot.html#creating-encrypted-snapshots).

Snapshots copied to an Outpost must be encrypted. Unencrypted snapshots are not supported on Outposts. For more information, [ Amazon EBS local snapshots on Outposts](https://docs.aws.amazon.com/ebs/latest/userguide/snapshots-outposts.html#considerations).

**Note**
Snapshots copies have an arbitrary source volume ID. Do not use this volume ID for any purpose.

For more information, see [Copy an Amazon EBS snapshot](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-copy-snapshot.html) in the *Amazon EBS User Guide*.

## Request Parameters
<a name="API_CopySnapshot_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **CompletionDurationMinutes**
Not supported when copying snapshots to or from Local Zones or Outposts.
Specify a completion duration, in 15 minute increments, to initiate a time-based snapshot copy. Time-based snapshot copy operations complete within the specified duration. For more information, see [ Time-based copies](https://docs.aws.amazon.com/ebs/latest/userguide/time-based-copies.html).
If you do not specify a value, the snapshot copy operation is completed on a best-effort basis.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 2880.
Required: No

 **Description**
A description for the EBS snapshot.
Type: String
Required: No

 **DestinationAvailabilityZone**
The Local Zone, for example, `cn-north-1-pkx-1a` to which to copy the snapshot.
Only supported when copying a snapshot to a Local Zone.
Type: String
Required: No

 **DestinationOutpostArn**
The Amazon Resource Name (ARN) of the Outpost to which to copy the snapshot.
Only supported when copying a snapshot to an Outpost.
For more information, see [ Copy snapshots from an AWS Region to an Outpost](https://docs.aws.amazon.com/ebs/latest/userguide/snapshots-outposts.html#copy-snapshots) in the *Amazon EBS User Guide*.
Type: String
Required: No

 **DestinationRegion**
The destination Region to use in the `PresignedUrl` parameter of a snapshot copy operation. This parameter is only valid for specifying the destination Region in a `PresignedUrl` parameter, where it is required.
The snapshot copy is sent to the regional endpoint that you sent the HTTP request to (for example, `ec2.us-east-1.amazonaws.com`).
Type: String
Required: No

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **Encrypted**
To encrypt a copy of an unencrypted snapshot if encryption by default is not enabled, enable encryption using this parameter. Otherwise, omit this parameter. Copies of encrypted snapshots are encrypted, even if you omit this parameter and encryption by default is not enabled. You cannot set this parameter to false. For more information, see [Amazon EBS encryption](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-encryption.html) in the *Amazon EBS User Guide*.
Type: Boolean
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

 **PresignedUrl**
When you copy an encrypted source snapshot using the Amazon EC2 Query API, you must supply a pre-signed URL. This parameter is optional for unencrypted snapshots. For more information, see [Query requests](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html).
The `PresignedUrl` should use the snapshot source endpoint, the `CopySnapshot` action, and include the `SourceRegion`, `SourceSnapshotId`, and `DestinationRegion` parameters. The `PresignedUrl` must be signed using AWS Signature Version 4. Because EBS snapshots are stored in Amazon S3, the signing algorithm for this parameter uses the same logic that is described in [ Authenticating Requests: Using Query Parameters (AWS Signature Version 4)](https://docs.aws.amazon.com/AmazonS3/latest/API/sigv4-query-string-auth.html) in the *Amazon S3 API Reference*. An invalid or improperly signed `PresignedUrl` will cause the copy operation to fail asynchronously, and the snapshot will move to an `error` state.
Type: String
Required: No

 **SourceRegion**
The ID of the Region that contains the snapshot to be copied.
Type: String
Required: Yes

 **SourceSnapshotId**
The ID of the EBS snapshot to copy.
Type: String
Required: Yes

 **TagSpecification.N**
The tags to apply to the new snapshot.
Type: Array of [TagSpecification](API_TagSpecification.md) objects
Required: No

## Response Elements
<a name="API_CopySnapshot_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **snapshotId**
The ID of the new snapshot.
Type: String

 **tagSet**
Any tags applied to the new snapshot.
Type: Array of [Tag](API_Tag.md) objects

## Errors
<a name="API_CopySnapshot_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_CopySnapshot_Examples"></a>

### Create copy of an unencrypted snapshot in the same Region as the original
<a name="API_CopySnapshot_Example_1"></a>

This example request copies the snapshot in the us-west-1 Region with the ID `snap-1234567890abcdef0`.

#### Sample Request
<a name="API_CopySnapshot_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=CopySnapshot
&SourceRegion=us-west-1
&SourceSnapshotId=snap-1234567890abcdef0
&Description=My_snapshot
&AUTHPARAMS
```

#### Sample Response
<a name="API_CopySnapshot_Example_1_Response"></a>

```
<CopySnapshotResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
  <requestId>60bc441d-fa2c-494d-b155-5d6a3EXAMPLE</requestId>
  <snapshotId>snap-1234567890abcdef1</snapshotId>
</CopySnapshotResponse<
```

### Create a copy of an encrypted snapshot in a Region different from the original
<a name="API_CopySnapshot_Example_2"></a>

This example request copies an encrypted snapshot in the us-west-1 Region to the us-east-1 Region with the ID `snap-0987654321abcdef0`.

#### Sample Request
<a name="API_CopySnapshot_Example_2_Request"></a>

```
https://ec2.amazonaws.com/?SourceSnapshotId=snap-005a01bf6eEXAMPLE
&SourceRegion=us-west-1
&KmsKeyId=arn%3Aaws%3Akms%3Aus-west-2%3A210774411744%3Akey%2FfEXAMPLE-24bc-479b-a9da-7132eEXAMPLE
&Action=CopySnapshot
&Encrypted=true
&DestinationRegion=us-east-1
&AUTHPARAMS
```

#### Sample Response
<a name="API_CopySnapshot_Example_2_Response"></a>

```
<CopySnapshotResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
	<requestId>256f6c57-6648-4544-a79a-35a03EXAMPLE</requestId>
	<snapshotId>snap-0987654321abcdef0</snapshotId>
</CopySnapshotResponse>
```

## See Also
<a name="API_CopySnapshot_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/CopySnapshot)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/CopySnapshot)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CopySnapshot)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/CopySnapshot)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CopySnapshot)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/CopySnapshot)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/CopySnapshot)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/CopySnapshot)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/CopySnapshot)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CopySnapshot)
