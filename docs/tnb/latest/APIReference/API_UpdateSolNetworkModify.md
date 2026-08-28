---
source_url: https://docs.aws.amazon.com/tnb/latest/APIReference/API_UpdateSolNetworkModify.html
---

# UpdateSolNetworkModify
<a name="API_UpdateSolNetworkModify"></a>

Information parameters and/or the configurable properties for a network function.

A network function instance is a function in a function package .

## Contents
<a name="API_UpdateSolNetworkModify_Contents"></a>

 ** vnfConfigurableProperties **   <a name="TNB-Type-UpdateSolNetworkModify-vnfConfigurableProperties"></a>
Provides values for the configurable properties declared in the function package descriptor.
Type: JSON value
Required: Yes

 ** vnfInstanceId **   <a name="TNB-Type-UpdateSolNetworkModify-vnfInstanceId"></a>
ID of the network function instance.
A network function instance is a function in a function package .
Type: String
Pattern: `fi-[a-f0-9]{17}`
Required: Yes

## See Also
<a name="API_UpdateSolNetworkModify_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/tnb-2008-10-21/UpdateSolNetworkModify)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/tnb-2008-10-21/UpdateSolNetworkModify)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/tnb-2008-10-21/UpdateSolNetworkModify)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Telco Network Builder. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query tnb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
