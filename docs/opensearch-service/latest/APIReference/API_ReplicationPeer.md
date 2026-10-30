---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_ReplicationPeer.html
---

# ReplicationPeer
<a name="API_ReplicationPeer"></a>

A domain that another domain replicates with, and the state of that relationship.

## Contents
<a name="API_ReplicationPeer_Contents"></a>

 ** PeerDomainArn **   <a name="opensearchservice-Type-ReplicationPeer-PeerDomainArn"></a>
The Amazon Resource Name (ARN) of the peer domain.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `arn:aws[a-z\-]*:[a-z]+:[a-z0-9\-]+:[0-9]+:domain\/[a-z0-9\-]+`
Required: No

 ** PeerRole **   <a name="opensearchservice-Type-ReplicationPeer-PeerRole"></a>
The peer's role in the relationship, either `PRIMARY` or `SECONDARY`.
Type: String
Valid Values: `PRIMARY | SECONDARY`
Required: No

 ** Status **   <a name="opensearchservice-Type-ReplicationPeer-Status"></a>
The state of the relationship:
+  `PENDING_SETUP` - replication is being established.
+  `ACTIVE` - replication is running.
+  `SWITCHING_OVER` - a planned promotion is in progress.
+  `FAILING_OVER` - an unplanned promotion is in progress.
+  `PENDING_REMOVAL` - replication is being stopped.
+  `DETACHED` - the relationship has ended.
+  `EJECTED` - a failover promoted the other domain. The former primary keeps the data it had when it was ejected and stays read-only until you remove the peer, or discard that data and pair again.
+  `FAILED` - setup or teardown could not complete. You can still remove the relationship.
A relationship that is removed successfully no longer appears in `Peers`.
Type: String
Valid Values: `PENDING_SETUP | ACTIVE | SWITCHING_OVER | FAILING_OVER | PENDING_REMOVAL | DETACHED | EJECTED | FAILED`
Required: No

 ** StatusMessage **   <a name="opensearchservice-Type-ReplicationPeer-StatusMessage"></a>
An explanation of why the relationship is in its current state, when more detail is available.
Type: String
Length Constraints: Maximum length of 2048.
Required: No

## See Also
<a name="API_ReplicationPeer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/ReplicationPeer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/ReplicationPeer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/ReplicationPeer)
