---
source_url: https://docs.aws.amazon.com/redshift/latest/APIReference/API_TaggedResource.html
---

# TaggedResource
<a name="API_TaggedResource"></a>

A tag and its associated resource.

## Contents
<a name="API_TaggedResource_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ResourceName **
The Amazon Resource Name (ARN) with which the tag is associated, for example: `arn:aws:redshift:us-east-2:123456789:cluster:t1`.
Type: String
Length Constraints: Maximum length of 2147483647.
Required: No

 ** ResourceType **
The type of resource with which the tag is associated. Valid resource types are:
+ Cluster
+ CIDR/IP
+ EC2 security group
+ Snapshot
+ Cluster security group
+ Subnet group
+ HSM connection
+ HSM certificate
+ Parameter group
For more information about Amazon Redshift resource types and constructing ARNs, go to [Constructing an Amazon Redshift Amazon Resource Name (ARN)](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-iam-access-control-overview.html#redshift-iam-access-control-specify-actions) in the Amazon Redshift Cluster Management Guide.
Type: String
Length Constraints: Maximum length of 2147483647.
Required: No

 ** Tag **
The tag for the resource.
Type: [Tag](API_Tag.md) object
Required: No

## See Also
<a name="API_TaggedResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/TaggedResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/TaggedResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/TaggedResource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
