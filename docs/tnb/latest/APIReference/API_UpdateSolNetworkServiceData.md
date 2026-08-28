---
source_url: https://docs.aws.amazon.com/tnb/latest/APIReference/API_UpdateSolNetworkServiceData.html
---

# UpdateSolNetworkServiceData
<a name="API_UpdateSolNetworkServiceData"></a>

Information parameters and/or the configurable properties for a network descriptor used for update.

## Contents
<a name="API_UpdateSolNetworkServiceData_Contents"></a>

 ** nsdInfoId **   <a name="TNB-Type-UpdateSolNetworkServiceData-nsdInfoId"></a>
ID of the network service descriptor.
Type: String
Pattern: `np-[a-f0-9]{17}`
Required: Yes

 ** additionalParamsForNs **   <a name="TNB-Type-UpdateSolNetworkServiceData-additionalParamsForNs"></a>
Values for the configurable properties declared in the network service descriptor.
Type: JSON value
Required: No

## See Also
<a name="API_UpdateSolNetworkServiceData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/tnb-2008-10-21/UpdateSolNetworkServiceData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/tnb-2008-10-21/UpdateSolNetworkServiceData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/tnb-2008-10-21/UpdateSolNetworkServiceData)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Telco Network Builder. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query tnb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
