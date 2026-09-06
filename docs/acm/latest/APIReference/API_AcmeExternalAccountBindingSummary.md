---
source_url: https://docs.aws.amazon.com/acm/latest/APIReference/API_AcmeExternalAccountBindingSummary.html
---

# AcmeExternalAccountBindingSummary
<a name="API_AcmeExternalAccountBindingSummary"></a>

Contains summary information about an ACME external account binding.

## Contents
<a name="API_AcmeExternalAccountBindingSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AcmeEndpointArn **   <a name="ACM-Type-AcmeExternalAccountBindingSummary-AcmeEndpointArn"></a>
The Amazon Resource Name (ARN) of the ACME endpoint.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `arn:aws[a-z-]*:acm:[a-z0-9-]+:[0-9]{12}:acme-endpoint/[a-zA-Z0-9-]+`
Required: No

 ** AcmeExternalAccountBindingArn **   <a name="ACM-Type-AcmeExternalAccountBindingSummary-AcmeExternalAccountBindingArn"></a>
The Amazon Resource Name (ARN) of the ACME external account binding.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `arn:aws[a-z-]*:acm:[a-z0-9-]+:[0-9]{12}:acme-endpoint/[a-zA-Z0-9-]+/acme-external-account-binding/[a-zA-Z0-9-]+`
Required: No

 ** CreatedAt **   <a name="ACM-Type-AcmeExternalAccountBindingSummary-CreatedAt"></a>
The time at which the external account binding was created.
Type: Timestamp
Required: No

 ** ExpiresAt **   <a name="ACM-Type-AcmeExternalAccountBindingSummary-ExpiresAt"></a>
The time at which the external account binding expires.
Type: Timestamp
Required: No

 ** LastUsedAt **   <a name="ACM-Type-AcmeExternalAccountBindingSummary-LastUsedAt"></a>
The time at which the external account binding was last used.
Type: Timestamp
Required: No

 ** RevokedAt **   <a name="ACM-Type-AcmeExternalAccountBindingSummary-RevokedAt"></a>
The time at which the external account binding was revoked.
Type: Timestamp
Required: No

 ** RoleArn **   <a name="ACM-Type-AcmeExternalAccountBindingSummary-RoleArn"></a>
The Amazon Resource Name (ARN) of the IAM role associated with the external account binding.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws[a-z-]*:iam::[0-9]{12}:role/.+`
Required: No

 ** UpdatedAt **   <a name="ACM-Type-AcmeExternalAccountBindingSummary-UpdatedAt"></a>
The time at which the external account binding was last updated.
Type: Timestamp
Required: No

## See Also
<a name="API_AcmeExternalAccountBindingSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/acm-2015-12-08/AcmeExternalAccountBindingSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/acm-2015-12-08/AcmeExternalAccountBindingSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/acm-2015-12-08/AcmeExternalAccountBindingSummary)
