---
source_url: https://docs.aws.amazon.com/kms/latest/APIReference/API_GrantListEntry.html
---

# GrantListEntry
<a name="API_GrantListEntry"></a>

Contains information about a grant.

## Contents
<a name="API_GrantListEntry_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Constraints **   <a name="KMS-Type-GrantListEntry-Constraints"></a>
The constraints on the grant, such as encryption context pairs or a SourceArn, that restrict the subsequent operations the grant allows.
Type: [GrantConstraints](API_GrantConstraints.md) object
Required: No

 ** CreationDate **   <a name="KMS-Type-GrantListEntry-CreationDate"></a>
The date and time when the grant was created.
Type: Timestamp
Required: No

 ** GranteePrincipal **   <a name="KMS-Type-GrantListEntry-GranteePrincipal"></a>
The identity that gets the permissions in the grant.
When a grant is created with the `GranteePrincipal` field, the `ListGrants` response usually contains the user or role designated as the grantee principal in the grant. However, if the grantee principal is an AWS service, the `GranteePrincipal` field contains an AWS [service principal](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html#principal-services), which might correspond to several different grantee principals, such as an IAM user, IAM role, or AWS account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^[\w+=,.@:/-]+$`
Required: No

 ** GranteeServicePrincipal **   <a name="KMS-Type-GrantListEntry-GranteeServicePrincipal"></a>
The AWS [service principal](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html#principal-services) that gets the permissions in the grant.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^([A-Za-z0-9\-]+)\.([A-Za-z0-9\-]+)(\.[A-Za-z0-9\-]+)+$`
Required: No

 ** GrantId **   <a name="KMS-Type-GrantListEntry-GrantId"></a>
The unique identifier for the grant.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** IssuingAccount **   <a name="KMS-Type-GrantListEntry-IssuingAccount"></a>
The AWS account under which the grant was issued.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^[\w+=,.@:/-]+$`
Required: No

 ** KeyId **   <a name="KMS-Type-GrantListEntry-KeyId"></a>
The unique identifier for the KMS key to which the grant applies.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** Name **   <a name="KMS-Type-GrantListEntry-Name"></a>
The friendly name that identifies the grant. If a name was provided in the [CreateGrant](API_CreateGrant.md) request, that name is returned. Otherwise this value is null.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^[a-zA-Z0-9:/_-]+$`
Required: No

 ** Operations **   <a name="KMS-Type-GrantListEntry-Operations"></a>
The list of operations permitted by the grant.
Type: Array of strings
Valid Values: `Decrypt | Encrypt | GenerateDataKey | GenerateDataKeyWithoutPlaintext | ReEncryptFrom | ReEncryptTo | Sign | Verify | GetPublicKey | CreateGrant | RetireGrant | DescribeKey | GenerateDataKeyPair | GenerateDataKeyPairWithoutPlaintext | GenerateMac | VerifyMac | DeriveSharedSecret`
Required: No

 ** RetiringPrincipal **   <a name="KMS-Type-GrantListEntry-RetiringPrincipal"></a>
The principal that can retire the grant.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^[\w+=,.@:/-]+$`
Required: No

 ** RetiringServicePrincipal **   <a name="KMS-Type-GrantListEntry-RetiringServicePrincipal"></a>
The AWS [service principal](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html#principal-services) that can retire the grant.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^([A-Za-z0-9\-]+)\.([A-Za-z0-9\-]+)(\.[A-Za-z0-9\-]+)+$`
Required: No

## See Also
<a name="API_GrantListEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kms-2014-11-01/GrantListEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kms-2014-11-01/GrantListEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kms-2014-11-01/GrantListEntry)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for KMS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
