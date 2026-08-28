---
source_url: https://docs.aws.amazon.com/evs/latest/APIReference/API_InstanceTypeEsxVersionsInfo.html
---

# InstanceTypeEsxVersionsInfo
<a name="API_InstanceTypeEsxVersionsInfo"></a>

Information about ESX versions offered for each EC2 instance type.

## Contents
<a name="API_InstanceTypeEsxVersionsInfo_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** esxVersions **   <a name="evs-Type-InstanceTypeEsxVersionsInfo-esxVersions"></a>
The list of ESX versions offered for this instance type.
Type: Array of strings
Required: Yes

 ** instanceType **   <a name="evs-Type-InstanceTypeEsxVersionsInfo-instanceType"></a>
The EC2 instance type.
Type: String
Valid Values: `i4i.metal | i7i.metal-24xl | i7i.metal-48xl`
Required: Yes

## See Also
<a name="API_InstanceTypeEsxVersionsInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/evs-2023-07-27/InstanceTypeEsxVersionsInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/evs-2023-07-27/InstanceTypeEsxVersionsInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/evs-2023-07-27/InstanceTypeEsxVersionsInfo)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Elastic VMware Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query evs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
