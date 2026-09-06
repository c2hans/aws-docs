---
source_url: https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_RegisteredAzureIdentityDetails.html
---

# RegisteredAzureIdentityDetails
<a name="API_RegisteredAzureIdentityDetails"></a>

Details specific to a registered Azure identity using AWS Outbound Identity Federation.

## Contents
<a name="API_RegisteredAzureIdentityDetails_Contents"></a>

 ** clientId **   <a name="devopsagent-Type-RegisteredAzureIdentityDetails-clientId"></a>
The client ID of the service principal or managed identity used for authentication.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 36.
Pattern: `[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}`
Required: Yes

 ** tenantId **   <a name="devopsagent-Type-RegisteredAzureIdentityDetails-tenantId"></a>
The Azure Active Directory tenant ID for the identity.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 36.
Pattern: `[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}`
Required: Yes

 ** webIdentityRoleArn **   <a name="devopsagent-Type-RegisteredAzureIdentityDetails-webIdentityRoleArn"></a>
The role ARN to be assumed by DevOps Agent for requesting Web Identity Token.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `arn:aws:iam::\d{12}:role/[a-zA-Z0-9+=,.@_/-]+`
Required: Yes

 ** webIdentityTokenAudiences **   <a name="devopsagent-Type-RegisteredAzureIdentityDetails-webIdentityTokenAudiences"></a>
The audiences for the Web Identity Token.
Type: Array of strings
Required: Yes

## See Also
<a name="API_RegisteredAzureIdentityDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-agent-2026-01-01/RegisteredAzureIdentityDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-agent-2026-01-01/RegisteredAzureIdentityDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-agent-2026-01-01/RegisteredAzureIdentityDetails)
