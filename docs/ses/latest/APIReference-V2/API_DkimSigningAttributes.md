---
source_url: https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_DkimSigningAttributes.html
---

# DkimSigningAttributes
<a name="API_DkimSigningAttributes"></a>

An object that contains configuration for Bring Your Own DKIM (BYODKIM), or, for Easy DKIM

## Contents
<a name="API_DkimSigningAttributes_Contents"></a>

 ** DomainSigningAttributesOrigin **   <a name="SES-Type-DkimSigningAttributes-DomainSigningAttributesOrigin"></a>
The attribute to use for configuring DKIM for the identity depends on the operation:

1. For `PutEmailIdentityDkimSigningAttributes`:
   + None of the values are allowed - use the [`SigningAttributesOrigin`](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_PutEmailIdentityDkimSigningAttributes.html#SES-PutEmailIdentityDkimSigningAttributes-request-SigningAttributesOrigin) parameter instead

1. For `CreateEmailIdentity` when replicating a parent identity's DKIM configuration:
   + Allowed values: All values except `AWS_SES` and `EXTERNAL`
+  `AWS_SES` – Configure DKIM for the identity by using Easy DKIM.
+  `EXTERNAL` – Configure DKIM for the identity by using Bring Your Own DKIM (BYODKIM).
+  `AWS_SES_<REGION>` – Configure DKIM for the identity by replicating the signing attributes of a parent identity in another AWS Region, using [Deterministic Easy-DKIM (DEED)](https://docs.aws.amazon.com/ses/latest/dg/send-email-authentication-dkim-deed.html). Replace `<REGION>` with the AWS Region of the parent identity, in uppercase with each hyphen replaced by an underscore. You can specify any AWS Region in which Amazon SES supports DEED. For example, to replicate from a parent identity in `us-east-1`, specify `AWS_SES_US_EAST_1`.
**Note**
The parent identity must already exist in the specified AWS Region and have Easy DKIM configured.
Type: String
Valid Values: `AWS_SES | EXTERNAL | AWS_SES_AF_SOUTH_1 | AWS_SES_EU_NORTH_1 | AWS_SES_AP_SOUTH_1 | AWS_SES_EU_WEST_3 | AWS_SES_EU_WEST_2 | AWS_SES_EU_SOUTH_1 | AWS_SES_EU_WEST_1 | AWS_SES_AP_NORTHEAST_3 | AWS_SES_AP_NORTHEAST_2 | AWS_SES_ME_SOUTH_1 | AWS_SES_AP_NORTHEAST_1 | AWS_SES_IL_CENTRAL_1 | AWS_SES_SA_EAST_1 | AWS_SES_CA_CENTRAL_1 | AWS_SES_AP_SOUTHEAST_1 | AWS_SES_AP_SOUTHEAST_2 | AWS_SES_AP_SOUTHEAST_3 | AWS_SES_EU_CENTRAL_1 | AWS_SES_US_EAST_1 | AWS_SES_US_EAST_2 | AWS_SES_US_WEST_1 | AWS_SES_US_WEST_2 | AWS_SES_ME_CENTRAL_1 | AWS_SES_AP_SOUTH_2 | AWS_SES_EU_CENTRAL_2 | AWS_SES_AP_SOUTHEAST_5 | AWS_SES_CA_WEST_1 | AWS_SES_US_GOV_EAST_1 | AWS_SES_US_GOV_WEST_1`
Required: No

 ** DomainSigningPrivateKey **   <a name="SES-Type-DkimSigningAttributes-DomainSigningPrivateKey"></a>
[Bring Your Own DKIM] A private key that's used to generate a DKIM signature.
The private key must use 1024 or 2048-bit RSA encryption, and must be encoded using base64 encoding.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20480.
Pattern: `^[a-zA-Z0-9+\/]+={0,2}$`
Required: No

 ** DomainSigningSelector **   <a name="SES-Type-DkimSigningAttributes-DomainSigningSelector"></a>
[Bring Your Own DKIM] A string that's used to identify a public key in the DNS configuration for a domain.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9]))$`
Required: No

 ** NextSigningKeyLength **   <a name="SES-Type-DkimSigningAttributes-NextSigningKeyLength"></a>
[Easy DKIM] The key length of the future DKIM key pair to be generated. This can be changed at most once per day.
Type: String
Valid Values: `RSA_1024_BIT | RSA_2048_BIT`
Required: No

## See Also
<a name="API_DkimSigningAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/DkimSigningAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/DkimSigningAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/DkimSigningAttributes)
