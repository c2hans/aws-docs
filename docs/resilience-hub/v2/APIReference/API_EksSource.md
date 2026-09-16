---
source_url: https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_EksSource.html
---

# EksSource
<a name="API_EksSource"></a>

Defines an Amazon EKS cluster and its namespaces as an input source for resource discovery.

## Contents
<a name="API_EksSource_Contents"></a>

 ** clusterArn **   <a name="ngresiliencehub-Type-EksSource-clusterArn"></a>
ARN identifier.
Type: String
Length Constraints: Minimum length of 31.
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`
Required: Yes

 ** namespaces **   <a name="ngresiliencehub-Type-EksSource-namespaces"></a>
The list of Kubernetes namespaces within the EKS cluster.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-z0-9]([-a-z0-9]*[a-z0-9])?`
Required: Yes

 ** labelSelector **   <a name="ngresiliencehub-Type-EksSource-labelSelector"></a>
Filters discovery to the Kubernetes objects whose labels match the selector. When omitted, all supported objects in the specified namespaces are discovered.
Type: [EksLabelSelector](API_EksLabelSelector.md) object
Required: No

## See Also
<a name="API_EksSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehubv2-2026-02-17/EksSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehubv2-2026-02-17/EksSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehubv2-2026-02-17/EksSource)
