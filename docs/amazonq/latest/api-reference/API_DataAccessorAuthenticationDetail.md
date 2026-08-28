---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DataAccessorAuthenticationDetail.html
---

# DataAccessorAuthenticationDetail
<a name="API_DataAccessorAuthenticationDetail"></a>

Contains the authentication configuration details for a data accessor. This structure defines how the ISV authenticates when accessing data through the data accessor.

## Contents
<a name="API_DataAccessorAuthenticationDetail_Contents"></a>

 ** authenticationType **   <a name="qbusiness-Type-DataAccessorAuthenticationDetail-authenticationType"></a>
The type of authentication to use for the data accessor. This determines how the ISV authenticates when accessing data. You can use one of two authentication types:
+  `AWS_IAM_IDC_TTI` - Authentication using IAM Identity Center Trusted Token Issuer (TTI). This authentication type allows the ISV to use a trusted token issuer to generate tokens for accessing the data.
+  `AWS_IAM_IDC_AUTH_CODE` - Authentication using IAM Identity Center authorization code flow. This authentication type uses the standard OAuth 2.0 authorization code flow for authentication.
Type: String
Valid Values: `AWS_IAM_IDC_TTI | AWS_IAM_IDC_AUTH_CODE`
Required: Yes

 ** authenticationConfiguration **   <a name="qbusiness-Type-DataAccessorAuthenticationDetail-authenticationConfiguration"></a>
The specific authentication configuration based on the authentication type.
Type: [DataAccessorAuthenticationConfiguration](API_DataAccessorAuthenticationConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** externalIds **   <a name="qbusiness-Type-DataAccessorAuthenticationDetail-externalIds"></a>
A list of external identifiers associated with this authentication configuration. These are used to correlate the data accessor with external systems.
Type: Array of strings
Array Members: Fixed number of 1 item.
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_-]*`
Required: No

## See Also
<a name="API_DataAccessorAuthenticationDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/DataAccessorAuthenticationDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/DataAccessorAuthenticationDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/DataAccessorAuthenticationDetail)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q Business. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonq` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
