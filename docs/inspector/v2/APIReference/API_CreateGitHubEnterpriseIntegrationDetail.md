---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_CreateGitHubEnterpriseIntegrationDetail.html
---

# CreateGitHubEnterpriseIntegrationDetail

Contains the details required to create an integration with a GitHub Enterprise Server instance.

## Contents
<a name="API_CreateGitHubEnterpriseIntegrationDetail_Contents"></a>

 ** instanceUrl **   <a name="inspector2-Type-CreateGitHubEnterpriseIntegrationDetail-instanceUrl"></a>
The URL of the GitHub Enterprise Server instance.
Type: String
Pattern: `https://[-a-zA-Z0-9()@:%_+.~#?&//=]{1,1024}`
Required: Yes

 ** vpcConfiguration **   <a name="inspector2-Type-CreateGitHubEnterpriseIntegrationDetail-vpcConfiguration"></a>
The VPC configuration used to connect to the GitHub Enterprise Server instance in a private network. For publicly accessible instances, omit this field.
Type: [CodeSecurityIntegrationVpcConfiguration](API_CodeSecurityIntegrationVpcConfiguration.md) object
Required: No

## See Also
<a name="API_CreateGitHubEnterpriseIntegrationDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/CreateGitHubEnterpriseIntegrationDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/CreateGitHubEnterpriseIntegrationDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/CreateGitHubEnterpriseIntegrationDetail)
