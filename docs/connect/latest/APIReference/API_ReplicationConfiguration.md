---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_ReplicationConfiguration.html
---

# ReplicationConfiguration
<a name="API_ReplicationConfiguration"></a>

Details about the status of the replication of a source Connect Customer instance across AWS Regions. Use these details to understand the general status of a given replication. For information about why a replication process may fail, see [Why a ReplicateInstance call fails](https://docs.aws.amazon.com/connect/latest/adminguide/create-replica-connect-instance.html#why-replicateinstance-fails) in the *Create a replica of your existing Connect Customer instance* topic in the *Connect Customer Administrator Guide*.

## Contents
<a name="API_ReplicationConfiguration_Contents"></a>

 ** GlobalSignInEndpoint **   <a name="connect-Type-ReplicationConfiguration-GlobalSignInEndpoint"></a>
The URL that is used to sign-in to your Connect Customer instance according to your traffic distribution group configuration. For more information about sign-in and traffic distribution groups, see [Important things to know](https://docs.aws.amazon.com/connect/latest/adminguide/setup-traffic-distribution-groups.html) in the *Create traffic distribution groups* topic in the *Connect Customer Administrator Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** ReplicationStatusSummaryList **   <a name="connect-Type-ReplicationConfiguration-ReplicationStatusSummaryList"></a>
A list of replication status summaries. The summaries contain details about the replication of configuration information for Connect Customer resources, for each AWS Region.
Type: Array of [ReplicationStatusSummary](API_ReplicationStatusSummary.md) objects
Array Members: Minimum number of 0 items. Maximum number of 11 items.
Required: No

 ** SourceRegion **   <a name="connect-Type-ReplicationConfiguration-SourceRegion"></a>
The AWS Region where the source Connect Customer instance was created. This is the Region where the [ReplicateInstance](https://docs.aws.amazon.com/connect/latest/APIReference/API_ReplicateInstance.html) API was called to start the replication process.
Type: String
Length Constraints: Minimum length of 8. Maximum length of 31.
Pattern: `[a-z]{2}(-[a-z]+){1,2}(-[0-9])?`
Required: No

## See Also
<a name="API_ReplicationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/ReplicationConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/ReplicationConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/ReplicationConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
