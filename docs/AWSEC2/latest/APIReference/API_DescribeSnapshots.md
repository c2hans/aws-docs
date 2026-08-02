---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeSnapshots.html
---

# DescribeSnapshots
<a name="API_DescribeSnapshots"></a>

Describes the specified EBS snapshots available to you or all of the EBS snapshots available to you.

The snapshots available to you include public snapshots, private snapshots that you own, and private snapshots owned by other AWS accounts for which you have explicit create volume permissions.

The create volume permissions fall into the following categories:
+  *public*: The owner of the snapshot granted create volume permissions for the snapshot to the `all` group. All AWS accounts have create volume permissions for these snapshots.
+  *explicit*: The owner of the snapshot granted create volume permissions to a specific AWS account.
+  *implicit*: An AWS account has implicit create volume permissions for all snapshots it owns.

The list of snapshots returned can be filtered by specifying snapshot IDs, snapshot owners, or AWS accounts with create volume permissions. If no options are specified, Amazon EC2 returns all snapshots for which you have create volume permissions.

If you specify one or more snapshot IDs, only snapshots that have the specified IDs are returned. If you specify an invalid snapshot ID, an error is returned. If you specify a snapshot ID for which you do not have access, it is not included in the returned results.

If you specify one or more snapshot owners using the `OwnerIds` option, only snapshots from the specified owners and for which you have access are returned. The results can include the AWS account IDs of the specified owners, `amazon` for snapshots owned by Amazon, or `self` for snapshots that you own.

If you specify a list of restorable users, only snapshots with create snapshot permissions for those users are returned. You can specify AWS account IDs (if you own the snapshots), `self` for snapshots for which you own or have explicit permissions, or `all` for public snapshots.

If you are describing a long list of snapshots, we recommend that you paginate the output to make the list more manageable. For more information, see [Pagination](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html#api-pagination).

To get the state of fast snapshot restores for a snapshot, use [DescribeFastSnapshotRestores](API_DescribeFastSnapshotRestores.md).

For more information about EBS snapshots, see [Amazon EBS snapshots](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-snapshots.html) in the *Amazon EBS User Guide*.

**Important**
We strongly recommend using only paginated requests. Unpaginated requests are susceptible to throttling and timeouts.

## Request Parameters
<a name="API_DescribeSnapshots_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **Filter.N**
The filters.
+  `description` - A description of the snapshot.
+  `encrypted` - Indicates whether the snapshot is encrypted (`true` \| `false`)
+  `owner-alias` - The owner alias, from an Amazon-maintained list (`amazon`). This is not the user-configured AWS account alias set using the IAM console. We recommend that you use the related parameter instead of this filter.
+  `owner-id` - The AWS account ID of the owner. We recommend that you use the related parameter instead of this filter.
+  `progress` - The progress of the snapshot, as a percentage (for example, 80%).
+  `snapshot-id` - The snapshot ID.
+  `start-time` - The time stamp when the snapshot was initiated.
+  `status` - The status of the snapshot (`pending` \| `completed` \| `error`).
+  `storage-tier` - The storage tier of the snapshot (`archive` \| `standard`).
+  `transfer-type` - The type of operation used to create the snapshot (`time-based` \| `standard`).
+  `tag`:<key> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key `Owner` and the value `TeamA`, specify `tag:Owner` for the filter name and `TeamA` for the filter value.
+  `tag-key` - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value.
+  `volume-id` - The ID of the volume the snapshot is for.
+  `volume-size` - The size of the volume, in GiB.
Type: Array of [Filter](API_Filter.md) objects
Required: No

 **MaxResults**
The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output. For more information, see [Pagination](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html#api-pagination).
Type: Integer
Required: No

 **NextToken**
The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.
Type: String
Required: No

 **Owner.N**
Scopes the results to snapshots with the specified owners. You can specify a combination of AWS account IDs, `self`, and `amazon`.
Type: Array of strings
Required: No

 **RestorableBy.N**
The IDs of the AWS accounts that can create volumes from the snapshot.
Type: Array of strings
Required: No

 **SnapshotId.N**
The snapshot IDs.
Default: Describes the snapshots for which you have create volume permissions.
Type: Array of strings
Required: No

## Response Elements
<a name="API_DescribeSnapshots_ResponseElements"></a>

The following elements are returned by the service.

 **nextToken**
The token to include in another request to get the next page of items. This value is `null` when there are no more items to return.
Type: String

 **requestId**
The ID of the request.
Type: String

 **snapshotSet**
Information about the snapshots.
Type: Array of [Snapshot](API_Snapshot.md) objects

## Errors
<a name="API_DescribeSnapshots_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DescribeSnapshots_Examples"></a>

### Example
<a name="API_DescribeSnapshots_Example_1"></a>

This example describes a snapshot with an ID of `snap-1234567890abcdef0`.

#### Sample Request
<a name="API_DescribeSnapshots_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=DescribeSnapshots
&SnapshotId=snap-1234567890abcdef0
&AUTHPARAMS
```

#### Sample Response
<a name="API_DescribeSnapshots_Example_1_Response"></a>

```
<DescribeSnapshotsResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
  <requestId>12345678-1234-1234-1234-3755ba4b9fa6</requestId>
  <snapshotSet>
    <item>
      <snapshotId>snap-0abcdef1234567890</snapshotId>
      <volumeId>vol-01234567890abcdef</volumeId>
      <status>completed</status>
      <startTime>2025-02-03T23:53:18.195Z</startTime>
      <progress>100%</progress>
      <ownerId>123456789012</ownerId>
      <volumeSize>8</volumeSize>
      <description>My root volume snapshot</description>
      <tagSet>
        <item>
          <key>purpose</key>
          <value>production_backup</value>
        </item>
      </tagSet>
      <encrypted>true</encrypted>
      <kmsKeyId>arn:aws:kms:us-east-1:123456789012:key/12345678-abcd-9876-ab12-cd56f438c90b</kmsKeyId>
      <storageTier>standard</storageTier>
      <transferType>standard</transferType>
      <completionTime>2025-02-03T23:56:27.864Z</completionTime>
      <fullSnapshotSizeInBytes>1770520576</fullSnapshotSizeInBytes>
    </item>
  </snapshotSet>
</DescribeSnapshotsResponse>
```

### Example
<a name="API_DescribeSnapshots_Example_2"></a>

This example filters the response to include only snapshots with the `pending` status, and a tag with the key `Owner` and the value `DbAdmin`.

#### Sample Request
<a name="API_DescribeSnapshots_Example_2_Request"></a>

```
https://ec2.amazonaws.com/?Action=DescribeSnapshots
&Filter.1.Name=status
&Filter.1.Value.1=pending
&Filter.2.Name=tag:Owner
&Filter.2.Value.1=DbAdmin
&AUTHPARAMS
```

## See Also
<a name="API_DescribeSnapshots_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DescribeSnapshots)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DescribeSnapshots)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DescribeSnapshots)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DescribeSnapshots)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DescribeSnapshots)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DescribeSnapshots)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DescribeSnapshots)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DescribeSnapshots)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DescribeSnapshots)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DescribeSnapshots)
