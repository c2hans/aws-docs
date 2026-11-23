---
source_url: https://docs.aws.amazon.com/rtb-fabric/latest/api/API_UpdateSummary.html
---

# UpdateSummary

A summary of an update.

## Contents
<a name="API_UpdateSummary_Contents"></a>

 ** createdAt **   <a name="rtbfabric-Type-UpdateSummary-createdAt"></a>
The timestamp of when the update was created.
Type: Timestamp
Required: Yes

 ** status **   <a name="rtbfabric-Type-UpdateSummary-status"></a>
The status of the update.
Type: String
Valid Values: `IN_PROGRESS | SUCCESSFUL | FAILED`
Required: Yes

 ** type **   <a name="rtbfabric-Type-UpdateSummary-type"></a>
The type of change.
Type: String
Valid Values: `GATEWAY_CONFIG_UPDATE | LINK_CONFIG_UPDATE | LINK_FLOW_UPDATE | ROUTING_RULE_UPDATE`
Required: Yes

 ** updateId **   <a name="rtbfabric-Type-UpdateSummary-updateId"></a>
The unique identifier of the update.
Type: String
Length Constraints: Minimum length of 8. Maximum length of 64.
Pattern: `update-[a-z0-9]{1,57}`
Required: Yes

## See Also
<a name="API_UpdateSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rtbfabric-2023-05-15/UpdateSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rtbfabric-2023-05-15/UpdateSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rtbfabric-2023-05-15/UpdateSummary)
