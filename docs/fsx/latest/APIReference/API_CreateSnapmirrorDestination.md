---
source_url: https://docs.aws.amazon.com/fsx/latest/APIReference/API_CreateSnapmirrorDestination.html
---

# CreateSnapmirrorDestination

Specifies the destination endpoint of the Amazon FSx for NetApp ONTAP SnapMirror relationship that you are creating.

## Contents
<a name="API_CreateSnapmirrorDestination_Contents"></a>

 ** VolumeId **   <a name="FSx-Type-CreateSnapmirrorDestination-VolumeId"></a>
Specifies the ID of the destination volume.
Type: String
Length Constraints: Fixed length of 23.
Pattern: `^(fsvol-[0-9a-f]{17,})$`
Required: Yes

## See Also
<a name="API_CreateSnapmirrorDestination_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/CreateSnapmirrorDestination)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/CreateSnapmirrorDestination)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/CreateSnapmirrorDestination)
