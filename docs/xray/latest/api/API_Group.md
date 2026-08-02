---
source_url: https://docs.aws.amazon.com/xray/latest/api/API_Group.html
---

# Group
<a name="API_Group"></a>

Details and metadata for a group.

## Contents
<a name="API_Group_Contents"></a>

 ** FilterExpression **   <a name="xray-Type-Group-FilterExpression"></a>
The filter expression defining the parameters to include traces.
Type: String
Required: No

 ** GroupARN **   <a name="xray-Type-Group-GroupARN"></a>
The Amazon Resource Name (ARN) of the group generated based on the GroupName.
Type: String
Required: No

 ** GroupName **   <a name="xray-Type-Group-GroupName"></a>
The unique case-sensitive name of the group.
Type: String
Required: No

 ** InsightsConfiguration **   <a name="xray-Type-Group-InsightsConfiguration"></a>
The structure containing configurations related to insights.
+ The InsightsEnabled boolean can be set to true to enable insights for the group or false to disable insights for the group.
+ The NotificationsEnabled boolean can be set to true to enable insights notifications through Amazon EventBridge for the group.
Type: [InsightsConfiguration](API_InsightsConfiguration.md) object
Required: No

## See Also
<a name="API_Group_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/xray-2016-04-12/Group)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/xray-2016-04-12/Group)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/xray-2016-04-12/Group)
