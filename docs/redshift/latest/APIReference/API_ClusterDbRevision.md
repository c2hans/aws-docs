---
source_url: https://docs.aws.amazon.com/redshift/latest/APIReference/API_ClusterDbRevision.html
---

# ClusterDbRevision
<a name="API_ClusterDbRevision"></a>

Describes a `ClusterDbRevision`.

## Contents
<a name="API_ClusterDbRevision_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ClusterIdentifier **
The unique identifier of the cluster.
Type: String
Length Constraints: Maximum length of 2147483647.
Required: No

 ** CurrentDatabaseRevision **
A string representing the current cluster version.
Type: String
Length Constraints: Maximum length of 2147483647.
Required: No

 ** DatabaseRevisionReleaseDate **
The date on which the database revision was released.
Type: Timestamp
Required: No

 ** RevisionTargets.RevisionTarget.N **
A list of `RevisionTarget` objects, where each object describes the database revision that a cluster can be updated to.
Type: Array of [RevisionTarget](API_RevisionTarget.md) objects
Required: No

## See Also
<a name="API_ClusterDbRevision_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/ClusterDbRevision)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/ClusterDbRevision)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/ClusterDbRevision)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
