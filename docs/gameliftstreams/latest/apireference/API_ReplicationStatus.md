---
source_url: https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_ReplicationStatus.html
---

# ReplicationStatus
<a name="API_ReplicationStatus"></a>

Represents the status of the replication of an application to a location. An application cannot be streamed from a location until it has finished replicating there.

## Contents
<a name="API_ReplicationStatus_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Location **   <a name="gameliftstreams-Type-ReplicationStatus-Location"></a>
 A location's name. For example, `us-east-1`. For a complete list of locations that Amazon GameLift Streams supports, refer to [Regions, quotas, and limitations](https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/regions-quotas.html) in the *Amazon GameLift Streams Developer Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `[a-zA-Z0-9-]+`
Required: No

 ** Status **   <a name="gameliftstreams-Type-ReplicationStatus-Status"></a>
The current status of the replication process.
Type: String
Valid Values: `REPLICATING | COMPLETED`
Required: No

## See Also
<a name="API_ReplicationStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gameliftstreams-2018-05-10/ReplicationStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gameliftstreams-2018-05-10/ReplicationStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gameliftstreams-2018-05-10/ReplicationStatus)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GameLift Streams. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query gameliftstreams` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
