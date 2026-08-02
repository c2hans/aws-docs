---
source_url: https://docs.aws.amazon.com/keyspaces/latest/APIReference/API_ReplicationSpecification.html
---

# ReplicationSpecification
<a name="API_ReplicationSpecification"></a>

 The replication specification of the keyspace includes:
+  `regionList` - the AWS Regions where the keyspace is replicated in.
+  `replicationStrategy` - the required value is `SINGLE_REGION` or `MULTI_REGION`.

## Contents
<a name="API_ReplicationSpecification_Contents"></a>

 ** replicationStrategy **   <a name="keyspaces-Type-ReplicationSpecification-replicationStrategy"></a>
 The `replicationStrategy` of a keyspace, the required value is `SINGLE_REGION` or `MULTI_REGION`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Valid Values: `SINGLE_REGION | MULTI_REGION`
Required: Yes

 ** regionList **   <a name="keyspaces-Type-ReplicationSpecification-regionList"></a>
 The `regionList` contains the AWS Regions where the keyspace is replicated in.
Type: Array of strings
Array Members: Minimum number of 2 items.
Length Constraints: Minimum length of 2. Maximum length of 25.
Required: No

## See Also
<a name="API_ReplicationSpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/keyspaces-2022-02-10/ReplicationSpecification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/keyspaces-2022-02-10/ReplicationSpecification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/keyspaces-2022-02-10/ReplicationSpecification)
