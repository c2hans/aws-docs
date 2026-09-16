---
source_url: https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_EksLabelSelector.html
---

# EksLabelSelector
<a name="API_EksLabelSelector"></a>

A label selector that filters the Kubernetes objects discovered from an Amazon EKS input source. An object must satisfy both matchLabels and matchExpressions to match the selector. A selector with neither matches every object. The selector must render to 2,048 characters or fewer in Kubernetes label selector syntax.

## Contents
<a name="API_EksLabelSelector_Contents"></a>

 ** matchExpressions **   <a name="ngresiliencehub-Type-EksLabelSelector-matchExpressions"></a>
The label requirements that an object must satisfy. All requirements in the list must match for the object to be selected.
Type: Array of [EksLabelSelectorRequirement](API_EksLabelSelectorRequirement.md) objects
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Required: No

 ** matchLabels **   <a name="ngresiliencehub-Type-EksLabelSelector-matchLabels"></a>
The label key-value pairs that an object must have. All pairs must match for the object to be selected.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 20 items.
Key Length Constraints: Minimum length of 1. Maximum length of 317.
Key Pattern: `([a-z0-9]([-a-z0-9.]*[a-z0-9])?/)?[A-Za-z0-9]([-A-Za-z0-9_.]*[A-Za-z0-9])?`
Value Length Constraints: Minimum length of 0. Maximum length of 63.
Value Pattern: `([A-Za-z0-9]([-A-Za-z0-9_.]*[A-Za-z0-9])?)?`
Required: No

## See Also
<a name="API_EksLabelSelector_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehubv2-2026-02-17/EksLabelSelector)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehubv2-2026-02-17/EksLabelSelector)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehubv2-2026-02-17/EksLabelSelector)
