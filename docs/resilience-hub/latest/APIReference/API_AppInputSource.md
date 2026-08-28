---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_AppInputSource.html
---

# AppInputSource
<a name="API_AppInputSource"></a>

The list of AWS Resilience Hub application input sources.

## Contents
<a name="API_AppInputSource_Contents"></a>

 ** importType **   <a name="resiliencehub-Type-AppInputSource-importType"></a>
The resource type of the input source.
Type: String
Valid Values: `CfnStack | Resource | AppRegistryApp | ResourceGroup | Terraform | EKS`
Required: Yes

 ** eksSourceClusterNamespace **   <a name="resiliencehub-Type-AppInputSource-eksSourceClusterNamespace"></a>
The namespace on your Amazon Elastic Kubernetes Service cluster.
Type: [EksSourceClusterNamespace](API_EksSourceClusterNamespace.md) object
Required: No

 ** resourceCount **   <a name="resiliencehub-Type-AppInputSource-resourceCount"></a>
The number of resources.
Type: Integer
Required: No

 ** sourceArn **   <a name="resiliencehub-Type-AppInputSource-sourceArn"></a>
The Amazon Resource Name (ARN) of the input source. For more information about ARNs, see [ Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference* guide.
Type: String
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`
Required: No

 ** sourceName **   <a name="resiliencehub-Type-AppInputSource-sourceName"></a>
The name of the input source.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** terraformSource **   <a name="resiliencehub-Type-AppInputSource-terraformSource"></a>
The name of the Terraform s3 state ﬁle.
Type: [TerraformSource](API_TerraformSource.md) object
Required: No

## See Also
<a name="API_AppInputSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehub-2020-04-30/AppInputSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehub-2020-04-30/AppInputSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehub-2020-04-30/AppInputSource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
