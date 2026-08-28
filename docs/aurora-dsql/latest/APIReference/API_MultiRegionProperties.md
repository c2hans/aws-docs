---
source_url: https://docs.aws.amazon.com/aurora-dsql/latest/APIReference/API_MultiRegionProperties.html
---

# MultiRegionProperties
<a name="API_MultiRegionProperties"></a>

Defines the structure for multi-Region cluster configurations, containing the witness region and linked cluster settings.

## Contents
<a name="API_MultiRegionProperties_Contents"></a>

 ** clusters **   <a name="auroradsql-Type-MultiRegionProperties-clusters"></a>
The set of peered clusters that form the multi-Region cluster configuration. Each peered cluster represents a database instance in a different Region.
Type: Array of strings
Pattern: `arn:aws(-[^:]+)?:dsql:[a-z0-9-]{1,20}:[0-9]{12}:cluster/[a-z0-9]{26}`
Required: No

 ** witnessRegion **   <a name="auroradsql-Type-MultiRegionProperties-witnessRegion"></a>
The Region that serves as the witness region for a multi-Region cluster. The witness Region helps maintain cluster consistency and quorum.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 50.
Required: No

## See Also
<a name="API_MultiRegionProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dsql-2018-05-10/MultiRegionProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dsql-2018-05-10/MultiRegionProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dsql-2018-05-10/MultiRegionProperties)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Aurora DSQL. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aurora-dsql` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
