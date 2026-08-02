---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_ThingGroupMetadata.html
---

# ThingGroupMetadata
<a name="API_ThingGroupMetadata"></a>

Thing group metadata.

## Contents
<a name="API_ThingGroupMetadata_Contents"></a>

 ** creationDate **   <a name="iot-Type-ThingGroupMetadata-creationDate"></a>
The UNIX timestamp of when the thing group was created.
Type: Timestamp
Required: No

 ** parentGroupName **   <a name="iot-Type-ThingGroupMetadata-parentGroupName"></a>
The parent thing group name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9:_-]+`
Required: No

 ** rootToParentThingGroups **   <a name="iot-Type-ThingGroupMetadata-rootToParentThingGroups"></a>
The root parent thing group.
Type: Array of [GroupNameAndArn](API_GroupNameAndArn.md) objects
Required: No

## See Also
<a name="API_ThingGroupMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/ThingGroupMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/ThingGroupMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/ThingGroupMetadata)
