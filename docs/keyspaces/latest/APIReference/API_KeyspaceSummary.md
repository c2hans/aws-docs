---
source_url: https://docs.aws.amazon.com/keyspaces/latest/APIReference/API_KeyspaceSummary.html
---

# KeyspaceSummary
<a name="API_KeyspaceSummary"></a>

Represents the properties of a keyspace.

## Contents
<a name="API_KeyspaceSummary_Contents"></a>

 ** keyspaceName **   <a name="keyspaces-Type-KeyspaceSummary-keyspaceName"></a>
The name of the keyspace.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 48.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_]{0,47}`
Required: Yes

 ** replicationStrategy **   <a name="keyspaces-Type-KeyspaceSummary-replicationStrategy"></a>
 This property specifies if a keyspace is a single Region keyspace or a multi-Region keyspace. The available values are `SINGLE_REGION` or `MULTI_REGION`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Valid Values: `SINGLE_REGION | MULTI_REGION`
Required: Yes

 ** resourceArn **   <a name="keyspaces-Type-KeyspaceSummary-resourceArn"></a>
The unique identifier of the keyspace in the format of an Amazon Resource Name (ARN).
Type: String
Length Constraints: Minimum length of 20. Maximum length of 1000.
Pattern: `arn:(aws[a-zA-Z0-9-]*):cassandra:.+.*`
Required: Yes

 ** replicationRegions **   <a name="keyspaces-Type-KeyspaceSummary-replicationRegions"></a>
 If the `replicationStrategy` of the keyspace is `MULTI_REGION`, a list of replication Regions is returned.
Type: Array of strings
Array Members: Minimum number of 2 items.
Length Constraints: Minimum length of 2. Maximum length of 25.
Required: No

## See Also
<a name="API_KeyspaceSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/keyspaces-2022-02-10/KeyspaceSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/keyspaces-2022-02-10/KeyspaceSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/keyspaces-2022-02-10/KeyspaceSummary)
