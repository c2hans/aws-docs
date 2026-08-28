---
source_url: https://docs.aws.amazon.com/tnb/latest/APIReference/API_GetSolVnfInfo.html
---

# GetSolVnfInfo
<a name="API_GetSolVnfInfo"></a>

Information about the network function.

A network function instance is a function in a function package .

## Contents
<a name="API_GetSolVnfInfo_Contents"></a>

 ** vnfcResourceInfo **   <a name="TNB-Type-GetSolVnfInfo-vnfcResourceInfo"></a>
Compute info used by the network function instance.
Type: Array of [GetSolVnfcResourceInfo](API_GetSolVnfcResourceInfo.md) objects
Required: No

 ** vnfState **   <a name="TNB-Type-GetSolVnfInfo-vnfState"></a>
State of the network function instance.
Type: String
Valid Values: `STARTED | STOPPED`
Required: No

## See Also
<a name="API_GetSolVnfInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/tnb-2008-10-21/GetSolVnfInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/tnb-2008-10-21/GetSolVnfInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/tnb-2008-10-21/GetSolVnfInfo)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Telco Network Builder. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query tnb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
