---
source_url: https://docs.aws.amazon.com/tnb/latest/APIReference/API_ValidateSolFunctionPackageContentMetadata.html
---

# ValidateSolFunctionPackageContentMetadata
<a name="API_ValidateSolFunctionPackageContentMetadata"></a>

Validates function package content metadata.

A function package is a .zip file in CSAR (Cloud Service Archive) format that contains a network function (an ETSI standard telecommunication application) and function package descriptor that uses the TOSCA standard to describe how the network functions should run on your network.

## Contents
<a name="API_ValidateSolFunctionPackageContentMetadata_Contents"></a>

 ** vnfd **   <a name="TNB-Type-ValidateSolFunctionPackageContentMetadata-vnfd"></a>
Metadata for function package artifacts.
Artifacts are the contents of the package descriptor file and the state of the package.
Type: [FunctionArtifactMeta](API_FunctionArtifactMeta.md) object
Required: No

## See Also
<a name="API_ValidateSolFunctionPackageContentMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/tnb-2008-10-21/ValidateSolFunctionPackageContentMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/tnb-2008-10-21/ValidateSolFunctionPackageContentMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/tnb-2008-10-21/ValidateSolFunctionPackageContentMetadata)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Telco Network Builder. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query tnb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
