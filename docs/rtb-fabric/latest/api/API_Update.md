---
source_url: https://docs.aws.amazon.com/rtb-fabric/latest/api/API_Update.html
---

# Update

An accepted configuration change and its status.

## Contents
<a name="API_Update_Contents"></a>

 ** createdAt **   <a name="rtbfabric-Type-Update-createdAt"></a>
The timestamp of when the update was created.
Type: Timestamp
Required: Yes

 ** status **   <a name="rtbfabric-Type-Update-status"></a>
The status of the update.
Type: String
Valid Values: `IN_PROGRESS | SUCCESSFUL | FAILED`
Required: Yes

 ** target **   <a name="rtbfabric-Type-Update-target"></a>
The resource that the update targeted.
Type: [UpdateTarget](API_UpdateTarget.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** type **   <a name="rtbfabric-Type-Update-type"></a>
The type of change. Currently, every update is a LINK\_FLOW\_UPDATE from PutLinkFlows.
Type: String
Valid Values: `GATEWAY_CONFIG_UPDATE | LINK_CONFIG_UPDATE | LINK_FLOW_UPDATE | ROUTING_RULE_UPDATE`
Required: Yes

 ** updateId **   <a name="rtbfabric-Type-Update-updateId"></a>
The unique identifier of the update.
Type: String
Length Constraints: Minimum length of 8. Maximum length of 64.
Pattern: `update-[a-z0-9]{1,57}`
Required: Yes

 ** errorDetails **   <a name="rtbfabric-Type-Update-errorDetails"></a>
The causes of the failure. Present only when the update has failed.
Type: Array of [ErrorDetail](API_ErrorDetail.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

 ** parameters **   <a name="rtbfabric-Type-Update-parameters"></a>
The changes that the update requested.
Type: [UpdateParameters](API_UpdateParameters.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

## See Also
<a name="API_Update_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rtbfabric-2023-05-15/Update)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rtbfabric-2023-05-15/Update)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rtbfabric-2023-05-15/Update)
