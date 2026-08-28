---
source_url: https://docs.aws.amazon.com/tnb/latest/APIReference/API_ListSolFunctionInstanceInfo.html
---

# ListSolFunctionInstanceInfo
<a name="API_ListSolFunctionInstanceInfo"></a>

Lists information about a network function instance.

A network function instance is a function in a function package .

## Contents
<a name="API_ListSolFunctionInstanceInfo_Contents"></a>

 ** arn **   <a name="TNB-Type-ListSolFunctionInstanceInfo-arn"></a>
Network function instance ARN.
Type: String
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-b|aws-us-gov):tnb:([a-z]{2}(-(gov|isob|iso))?-(east|west|north|south|central){1,2}-[0-9]):\d{12}:(function-instance/fi-[a-f0-9]{17})`
Required: Yes

 ** id **   <a name="TNB-Type-ListSolFunctionInstanceInfo-id"></a>
Network function instance ID.
Type: String
Pattern: `fi-[a-f0-9]{17}`
Required: Yes

 ** instantiationState **   <a name="TNB-Type-ListSolFunctionInstanceInfo-instantiationState"></a>
Network function instance instantiation state.
Type: String
Valid Values: `INSTANTIATED | NOT_INSTANTIATED`
Required: Yes

 ** metadata **   <a name="TNB-Type-ListSolFunctionInstanceInfo-metadata"></a>
Network function instance metadata.
Type: [ListSolFunctionInstanceMetadata](API_ListSolFunctionInstanceMetadata.md) object
Required: Yes

 ** nsInstanceId **   <a name="TNB-Type-ListSolFunctionInstanceInfo-nsInstanceId"></a>
Network instance ID.
Type: String
Pattern: `ni-[a-f0-9]{17}`
Required: Yes

 ** vnfPkgId **   <a name="TNB-Type-ListSolFunctionInstanceInfo-vnfPkgId"></a>
Function package ID.
Type: String
Pattern: `fp-[a-f0-9]{17}`
Required: Yes

 ** instantiatedVnfInfo **   <a name="TNB-Type-ListSolFunctionInstanceInfo-instantiatedVnfInfo"></a>
Information about a network function.
A network instance is a single network created in AWS TNB that can be deployed and on which life-cycle operations (like terminate, update, and delete) can be performed.
Type: [GetSolInstantiatedVnfInfo](API_GetSolInstantiatedVnfInfo.md) object
Required: No

 ** vnfPkgName **   <a name="TNB-Type-ListSolFunctionInstanceInfo-vnfPkgName"></a>
Function package name.
Type: String
Required: No

## See Also
<a name="API_ListSolFunctionInstanceInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/tnb-2008-10-21/ListSolFunctionInstanceInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/tnb-2008-10-21/ListSolFunctionInstanceInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/tnb-2008-10-21/ListSolFunctionInstanceInfo)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Telco Network Builder. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query tnb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
