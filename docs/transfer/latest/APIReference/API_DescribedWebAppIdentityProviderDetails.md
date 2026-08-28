---
source_url: https://docs.aws.amazon.com/transfer/latest/APIReference/API_DescribedWebAppIdentityProviderDetails.html
---

# DescribedWebAppIdentityProviderDetails
<a name="API_DescribedWebAppIdentityProviderDetails"></a>

Returns a structure that contains the identity provider details for your web app.

## Contents
<a name="API_DescribedWebAppIdentityProviderDetails_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** IdentityCenterConfig **   <a name="TransferFamily-Type-DescribedWebAppIdentityProviderDetails-IdentityCenterConfig"></a>
Returns a structure for your identity provider details. This structure contains the instance ARN and role being used for the web app.
Type: [DescribedIdentityCenterConfig](API_DescribedIdentityCenterConfig.md) object
Required: No

## See Also
<a name="API_DescribedWebAppIdentityProviderDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transfer-2018-11-05/DescribedWebAppIdentityProviderDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transfer-2018-11-05/DescribedWebAppIdentityProviderDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transfer-2018-11-05/DescribedWebAppIdentityProviderDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Transfer Family. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query transfer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
