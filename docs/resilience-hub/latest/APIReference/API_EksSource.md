---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_EksSource.html
---

# EksSource
<a name="API_EksSource"></a>

The input source of the Amazon Elastic Kubernetes Service cluster.

## Contents
<a name="API_EksSource_Contents"></a>

 ** eksClusterArn **   <a name="resiliencehub-Type-EksSource-eksClusterArn"></a>
Amazon Resource Name (ARN) of the Amazon Elastic Kubernetes Service cluster. The format for this ARN is: arn:`aws`:eks:`region`:`account-id`:cluster/`cluster-name`. For more information about ARNs, see [ Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference* guide.
Type: String
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`
Required: Yes

 ** namespaces **   <a name="resiliencehub-Type-EksSource-namespaces"></a>
The list of namespaces located on your Amazon Elastic Kubernetes Service cluster.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-z0-9]([-a-z0-9]*[a-z0-9])?`
Required: Yes

## See Also
<a name="API_EksSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehub-2020-04-30/EksSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehub-2020-04-30/EksSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehub-2020-04-30/EksSource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
