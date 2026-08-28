---
source_url: https://docs.aws.amazon.com/eks/latest/APIReference/API_AddonInfo.html
---

# AddonInfo
<a name="API_AddonInfo"></a>

Information about an add-on.

## Contents
<a name="API_AddonInfo_Contents"></a>

 ** addonName **   <a name="AmazonEKS-Type-AddonInfo-addonName"></a>
The name of the add-on.
Type: String
Required: No

 ** addonVersions **   <a name="AmazonEKS-Type-AddonInfo-addonVersions"></a>
An object representing information about available add-on versions and compatible Kubernetes versions.
Type: Array of [AddonVersionInfo](API_AddonVersionInfo.md) objects
Required: No

 ** defaultNamespace **   <a name="AmazonEKS-Type-AddonInfo-defaultNamespace"></a>
The default Kubernetes namespace where this addon is typically installed if no custom namespace is specified.
Type: String
Required: No

 ** marketplaceInformation **   <a name="AmazonEKS-Type-AddonInfo-marketplaceInformation"></a>
Information about the add-on from the AWS Marketplace.
Type: [MarketplaceInformation](API_MarketplaceInformation.md) object
Required: No

 ** owner **   <a name="AmazonEKS-Type-AddonInfo-owner"></a>
The owner of the add-on.
Type: String
Required: No

 ** publisher **   <a name="AmazonEKS-Type-AddonInfo-publisher"></a>
The publisher of the add-on.
Type: String
Required: No

 ** type **   <a name="AmazonEKS-Type-AddonInfo-type"></a>
The type of the add-on.
Type: String
Required: No

## See Also
<a name="API_AddonInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/AddonInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/AddonInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/AddonInfo)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EKS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query eks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
