---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_ResourceReplicationStatus.html
---

# ResourceReplicationStatus
<a name="API_ResourceReplicationStatus"></a>

Indicates whether a resource type is being replicated and kept in sync in a specific AWS Region of a Global Resiliency deployment.

## Contents
<a name="API_ResourceReplicationStatus_Contents"></a>

 ** Region **   <a name="connect-Type-ResourceReplicationStatus-Region"></a>
The AWS Region that the replication status applies to.
Type: String
Length Constraints: Minimum length of 8. Maximum length of 31.
Pattern: `[a-z]{2}(-[a-z]+){1,2}(-[0-9])?`
Required: Yes

 ** Status **   <a name="connect-Type-ResourceReplicationStatus-Status"></a>
The replication status of the resource type in the Region, such as `ENABLED`, `BLOCKED`, or `DISABLED`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

## See Also
<a name="API_ResourceReplicationStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/ResourceReplicationStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/ResourceReplicationStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/ResourceReplicationStatus)
