---
source_url: https://docs.aws.amazon.com/omics/latest/api/API_RegistryMapping.html
---

# RegistryMapping
<a name="API_RegistryMapping"></a>

If you are using the ECR pull through cache feature, the registry mapping maps between the ECR repository and the upstream registry where container images are pulled and synchronized.

## Contents
<a name="API_RegistryMapping_Contents"></a>

 ** ecrAccountId **   <a name="omics-Type-RegistryMapping-ecrAccountId"></a>
Account ID of the account that owns the upstream container image.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `[0-9]+`
Required: No

 ** ecrRepositoryPrefix **   <a name="omics-Type-RegistryMapping-ecrRepositoryPrefix"></a>
The repository prefix to use in the ECR private repository.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: No

 ** upstreamRegistryUrl **   <a name="omics-Type-RegistryMapping-upstreamRegistryUrl"></a>
The URI of the upstream registry.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 750.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: No

 ** upstreamRepositoryPrefix **   <a name="omics-Type-RegistryMapping-upstreamRepositoryPrefix"></a>
The repository prefix of the corresponding repository in the upstream registry.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 30.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: No

## See Also
<a name="API_RegistryMapping_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/omics-2022-11-28/RegistryMapping)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/omics-2022-11-28/RegistryMapping)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/omics-2022-11-28/RegistryMapping)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS HealthOmics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query omics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
