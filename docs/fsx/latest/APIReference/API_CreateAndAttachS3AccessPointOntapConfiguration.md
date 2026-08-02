---
source_url: https://docs.aws.amazon.com/fsx/latest/APIReference/API_CreateAndAttachS3AccessPointOntapConfiguration.html
---

# CreateAndAttachS3AccessPointOntapConfiguration
<a name="API_CreateAndAttachS3AccessPointOntapConfiguration"></a>

Specifies the FSx for ONTAP volume that the S3 access point will be attached to, and the file system user identity.

## Contents
<a name="API_CreateAndAttachS3AccessPointOntapConfiguration_Contents"></a>

 ** FileSystemIdentity **   <a name="FSx-Type-CreateAndAttachS3AccessPointOntapConfiguration-FileSystemIdentity"></a>
Specifies the file system user identity to use for authorizing file read and write requests that are made using this S3 access point.
Type: [OntapFileSystemIdentity](API_OntapFileSystemIdentity.md) object
Required: Yes

 ** VolumeId **   <a name="FSx-Type-CreateAndAttachS3AccessPointOntapConfiguration-VolumeId"></a>
The ID of the FSx for ONTAP volume to which you want the S3 access point attached.
Type: String
Length Constraints: Fixed length of 23.
Pattern: `^(fsvol-[0-9a-f]{17,})$`
Required: Yes

## See Also
<a name="API_CreateAndAttachS3AccessPointOntapConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/CreateAndAttachS3AccessPointOntapConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/CreateAndAttachS3AccessPointOntapConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/CreateAndAttachS3AccessPointOntapConfiguration)
