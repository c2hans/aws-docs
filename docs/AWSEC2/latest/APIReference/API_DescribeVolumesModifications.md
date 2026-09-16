---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeVolumesModifications.html
---

# DescribeVolumesModifications
<a name="API_DescribeVolumesModifications"></a>

Describes the most recent volume modification request for the specified EBS volumes.

For more information, see [ Monitor the progress of volume modifications](https://docs.aws.amazon.com/ebs/latest/userguide/monitoring-volume-modifications.html) in the *Amazon EBS User Guide*.

## Request Parameters
<a name="API_DescribeVolumesModifications_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **Filter.N**
The filters.
+  `modification-state` - The current modification state (modifying \| optimizing \| completed \| failed).
+  `original-iops` - The original IOPS rate of the volume.
+  `original-size` - The original size of the volume, in GiB.
+  `original-volume-type` - The original volume type of the volume (standard \| io1 \| io2 \| gp2 \| sc1 \| st1).
+  `originalMultiAttachEnabled` - Indicates whether Multi-Attach support was enabled (true \| false).
+  `start-time` - The modification start time.
+  `target-iops` - The target IOPS rate of the volume.
+  `target-size` - The target size of the volume, in GiB.
+  `target-volume-type` - The target volume type of the volume (standard \| io1 \| io2 \| gp2 \| sc1 \| st1).
+  `targetMultiAttachEnabled` - Indicates whether Multi-Attach support is to be enabled (true \| false).
+  `volume-id` - The ID of the volume.
Type: Array of [Filter](API_Filter.md) objects
Required: No

 **IncludeManagedResources**
Indicates whether to include managed resources in the output. If this parameter is set to `true`, the output includes resources that are managed by AWS services, even if managed resource visibility is set to hidden.
Type: Boolean
Required: No

 **MaxResults**
The maximum number of results (up to a limit of 500) to be returned in a paginated request. For more information, see [Pagination](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html#api-pagination).
Type: Integer
Required: No

 **NextToken**
The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.
Type: String
Required: No

 **VolumeId.N**
The IDs of the volumes.
Type: Array of strings
Required: No

## Response Elements
<a name="API_DescribeVolumesModifications_ResponseElements"></a>

The following elements are returned by the service.

 **nextToken**
The token to include in another request to get the next page of items. This value is `null` when there are no more items to return.
Type: String

 **requestId**
The ID of the request.
Type: String

 **volumeModificationSet**
Information about the volume modifications.
Type: Array of [VolumeModification](API_VolumeModification.md) objects

## Errors
<a name="API_DescribeVolumesModifications_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DescribeVolumesModifications_Examples"></a>

### Example 1
<a name="API_DescribeVolumesModifications_Example_1"></a>

This example displays volume status after modifications to size, type, IOPS provisioning, and Multi-Attach support.

#### Sample Request
<a name="API_DescribeVolumesModifications_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=DescribeVolumesModifications
&VolumeId.1=vol-0123456789EXAMPLE
&Version=2016-11-15
```

#### Sample Response
<a name="API_DescribeVolumesModifications_Example_1_Response"></a>

```
<DescribeVolumesModificationsResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
  <requestId>59dbff89-35bd-4eac-99ed-be587EXAMPLE</requestId>
  <volumeModificationSet>
    <item>
      <targetIops>10000</targetIops>
      <originalIops>300</originalIops>
      <modificationState>optimizing</modificationState>
      <targetSize>200</targetSize>
      <targetVolumeType>io1</targetVolumeType>
      <volumeId>vol-0123456789EXAMPLE</volumeId>
      <progress>40</progress>
      <startTime>2017-01-19T23:58:04.922Z</startTime>
      <originalSize>100</originalSize>
      <originalVolumeType>gp2</originalVolumeType>
      <originalMultiAttachEnabled>false</originalMultiAttachEnabled>
      <targetMultiAttachEnabled>true</targetMultiAttachEnabled>
    </item>
  </volumeModificationSet>
</DescribeVolumesModificationsResponse>
```

### Example 2
<a name="API_DescribeVolumesModifications_Example_2"></a>

This example displays information about all volumes in a Region with a modification state of optimizing or completed.

#### Sample Request
<a name="API_DescribeVolumesModifications_Example_2_Request"></a>

```
https://ec2.amazonaws.com/?Action=DescribeVolumesModifications
&Filter.1.Value.2=completed
&Filter.1.Value.1=optimizing
&Version=2016-11-15
&Filter.1.Name=modification-state
```

#### Sample Response
<a name="API_DescribeVolumesModifications_Example_2_Response"></a>

```
<DescribeVolumesModificationsResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
	<requestId>35fdf8d3-6ffa-46dc-8f8e-62fe70bc31a2</requestId>
	<volumeModificationSet>
		<item>
			<targetIops>10000</targetIops>
			<originalIops>100</originalIops>
			<modificationState>optimizing</modificationState>
			<targetSize>2000</targetSize>
			<targetVolumeType>io1</targetVolumeType>
			<volumeId>vol-06397e7a0eEXAMPLE</volumeId>
			<progress>3</progress>
			<startTime>2017-02-10T23:40:57.612Z</startTime>
			<originalSize>10</originalSize>
			<originalVolumeType>gp2</originalVolumeType>
		</item>
		<item>
			<targetIops>10000</targetIops>
			<originalIops>100</originalIops>
			<modificationState>completed</modificationState>
			<targetSize>200</targetSize>
			<targetVolumeType>io1</targetVolumeType>
			<volumeId>vol-bEXAMPLE</volumeId>
			<progress>100</progress>
			<startTime>2017-02-10T22:50:52.207Z</startTime>
			<endTime>2017-02-10T22:56:04.823Z</endTime>
			<originalSize>8</originalSize>
			<originalVolumeType>gp2</originalVolumeType>
		</item>
	</volumeModificationSet>
</DescribeVolumesModificationsResponse>
```

## See Also
<a name="API_DescribeVolumesModifications_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DescribeVolumesModifications)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DescribeVolumesModifications)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DescribeVolumesModifications)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DescribeVolumesModifications)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DescribeVolumesModifications)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DescribeVolumesModifications)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DescribeVolumesModifications)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DescribeVolumesModifications)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DescribeVolumesModifications)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DescribeVolumesModifications)
