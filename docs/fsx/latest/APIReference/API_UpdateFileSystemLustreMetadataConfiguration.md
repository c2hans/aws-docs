---
source_url: https://docs.aws.amazon.com/fsx/latest/APIReference/API_UpdateFileSystemLustreMetadataConfiguration.html
---

# UpdateFileSystemLustreMetadataConfiguration
<a name="API_UpdateFileSystemLustreMetadataConfiguration"></a>

The Lustre metadata performance configuration update for an Amazon FSx for Lustre file system using a `PERSISTENT_2` deployment type. You can request an increase in your file system's Metadata IOPS and/or switch your file system's metadata configuration mode. For more information, see [Managing metadata performance](https://docs.aws.amazon.com/fsx/latest/LustreGuide/managing-metadata-performance.html) in the *Amazon FSx for Lustre User Guide*.

## Contents
<a name="API_UpdateFileSystemLustreMetadataConfiguration_Contents"></a>

 ** Iops **   <a name="FSx-Type-UpdateFileSystemLustreMetadataConfiguration-Iops"></a>
(USER\_PROVISIONED mode only) Specifies the number of Metadata IOPS to provision for your file system.
+ For SSD file systems, valid values are `1500`, `3000`, `6000`, `12000`, and multiples of `12000` up to a maximum of `192000`.
+ For Intelligent-Tiering file systems, valid values are `6000`, `12000`, and multiples of `12000` up to a maximum of `192000`.
The value you provide must be greater than or equal to the current number of Metadata IOPS provisioned for the file system. You can't provision fewer Metadata IOPS than AUTOMATIC mode provisions for your file system.
Type: Integer
Valid Range: Minimum value of 1500. Maximum value of 192000.
Required: No

 ** Mode **   <a name="FSx-Type-UpdateFileSystemLustreMetadataConfiguration-Mode"></a>
The metadata configuration mode for provisioning Metadata IOPS for an FSx for Lustre file system using a `PERSISTENT_2` deployment type.
+ To increase the Metadata IOPS or to switch from AUTOMATIC mode, specify `USER_PROVISIONED` as the value for this parameter. Then use the Iops parameter to provide a Metadata IOPS value that is greater than or equal to the current number of Metadata IOPS provisioned for the file system.
+ To switch from USER\_PROVISIONED mode, specify `AUTOMATIC` as the value for this parameter, but do not input a value for Iops.
**Note**
FSx for Lustre rejects a switch to AUTOMATIC mode when your current Metadata IOPS value is greater than what AUTOMATIC mode provisions, because decreasing Metadata IOPS is not supported. To unblock the switch, increase storage capacity for SSD file systems, or throughput capacity for Intelligent-Tiering file systems, until AUTOMATIC mode provisions at least your current Metadata IOPS.
Type: String
Valid Values: `AUTOMATIC | USER_PROVISIONED`
Required: No

## See Also
<a name="API_UpdateFileSystemLustreMetadataConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/UpdateFileSystemLustreMetadataConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/UpdateFileSystemLustreMetadataConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/UpdateFileSystemLustreMetadataConfiguration)
