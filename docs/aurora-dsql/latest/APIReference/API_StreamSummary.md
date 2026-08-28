---
source_url: https://docs.aws.amazon.com/aurora-dsql/latest/APIReference/API_StreamSummary.html
---

# StreamSummary
<a name="API_StreamSummary"></a>

Summary information about a stream.

## Contents
<a name="API_StreamSummary_Contents"></a>

 ** arn **   <a name="auroradsql-Type-StreamSummary-arn"></a>
The ARN of the stream.
Type: String
Pattern: `arn:aws(-[^:]+)?:dsql:[a-z0-9-]{1,20}:[0-9]{12}:cluster/[a-z0-9]{26}/stream/[a-z0-9]{26}`
Required: Yes

 ** clusterIdentifier **   <a name="auroradsql-Type-StreamSummary-clusterIdentifier"></a>
The ID of the cluster.
Type: String
Pattern: `[a-z0-9]{26}`
Required: Yes

 ** creationTime **   <a name="auroradsql-Type-StreamSummary-creationTime"></a>
The timestamp when the stream was created.
Type: Timestamp
Required: Yes

 ** status **   <a name="auroradsql-Type-StreamSummary-status"></a>
The current status of the stream.
Type: String
Valid Values: `CREATING | ACTIVE | DELETING | DELETED | FAILED | IMPAIRED`
Required: Yes

 ** streamIdentifier **   <a name="auroradsql-Type-StreamSummary-streamIdentifier"></a>
The ID of the stream.
Type: String
Pattern: `[a-z0-9]{26}`
Required: Yes

## See Also
<a name="API_StreamSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dsql-2018-05-10/StreamSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dsql-2018-05-10/StreamSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dsql-2018-05-10/StreamSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Aurora DSQL. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aurora-dsql` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
