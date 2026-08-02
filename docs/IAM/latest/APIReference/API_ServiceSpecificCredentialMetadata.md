---
source_url: https://docs.aws.amazon.com/IAM/latest/APIReference/API_ServiceSpecificCredentialMetadata.html
---

# ServiceSpecificCredentialMetadata
<a name="API_ServiceSpecificCredentialMetadata"></a>

Contains additional details about a service-specific credential.

## Contents
<a name="API_ServiceSpecificCredentialMetadata_Contents"></a>

 ** CreateDate **
The date and time, in [ISO 8601 date-time format](http://www.iso.org/iso/iso8601), when the service-specific credential were created.
Type: Timestamp
Required: Yes

 ** ServiceName **
The name of the service associated with the service-specific credential.
Type: String
Required: Yes

 ** ServiceSpecificCredentialId **
The unique identifier for the service-specific credential.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 128.
Pattern: `[\w]+`
Required: Yes

 ** Status **
The status of the service-specific credential. `Active` means that the key is valid for API calls, while `Inactive` means it is not.
Type: String
Valid Values: `Active | Inactive | Expired`
Required: Yes

 ** UserName **
The name of the IAM user associated with the service-specific credential.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\w+=,.@-]+`
Required: Yes

 ** ExpirationDate **
The date and time when the service specific credential expires. This field is only present for Bedrock API keys and CloudWatch Logs API keys that were created with an expiration period.
Type: Timestamp
Required: No

 ** ServiceCredentialAlias **
For Bedrock API keys and CloudWatch Logs API keys, this is the public portion of the credential that includes the IAM user name and a suffix containing version and creation information.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 200.
Pattern: `[\w+=,.@-]+`
Required: No

 ** ServiceUserName **
The generated user name for the service-specific credential.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 200.
Pattern: `[\w+=,.@-]*`
Required: No

## See Also
<a name="API_ServiceSpecificCredentialMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-2010-05-08/ServiceSpecificCredentialMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-2010-05-08/ServiceSpecificCredentialMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-2010-05-08/ServiceSpecificCredentialMetadata)
