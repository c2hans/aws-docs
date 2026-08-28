---
source_url: https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_ContainerProvider.html
---

# ContainerProvider
<a name="API_ContainerProvider"></a>

The information about the container provider.

## Contents
<a name="API_ContainerProvider_Contents"></a>

 ** id **   <a name="emroneks-Type-ContainerProvider-id"></a>
The ID of the container cluster.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[0-9A-Za-z][A-Za-z0-9\-_]*`
Required: Yes

 ** type **   <a name="emroneks-Type-ContainerProvider-type"></a>
The type of the container provider. Amazon EKS is the only supported type as of now.
Type: String
Valid Values: `EKS`
Required: Yes

 ** info **   <a name="emroneks-Type-ContainerProvider-info"></a>
The information about the container cluster.
Type: [ContainerInfo](API_ContainerInfo.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

## See Also
<a name="API_ContainerProvider_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/emr-containers-2020-10-01/ContainerProvider)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/emr-containers-2020-10-01/ContainerProvider)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/emr-containers-2020-10-01/ContainerProvider)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR on EKS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr-on-eks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
