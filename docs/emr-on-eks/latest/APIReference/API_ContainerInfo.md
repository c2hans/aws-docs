---
source_url: https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_ContainerInfo.html
---

# ContainerInfo
<a name="API_ContainerInfo"></a>

The information about the container used for a job run or a managed endpoint.

## Contents
<a name="API_ContainerInfo_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** eksInfo **   <a name="emroneks-Type-ContainerInfo-eksInfo"></a>
The information about the Amazon EKS cluster.
Type: [EksInfo](API_EksInfo.md) object
Required: No

## See Also
<a name="API_ContainerInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/emr-containers-2020-10-01/ContainerInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/emr-containers-2020-10-01/ContainerInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/emr-containers-2020-10-01/ContainerInfo)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR on EKS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr-on-eks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
