---
source_url: https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_MpaTeamAssociation.html
---

# MpaTeamAssociation
<a name="API_MpaTeamAssociation"></a>

The details of an MPA team association with a protected operation.

## Contents
<a name="API_MpaTeamAssociation_Contents"></a>

 ** Action **   <a name="paymentcryptography-Type-MpaTeamAssociation-Action"></a>
The protected operation associated with the MPA team.
Type: String
Valid Values: `IMPORT_ROOT_PUBLIC_KEY_CERTIFICATE`
Required: Yes

 ** AssociationState **   <a name="paymentcryptography-Type-MpaTeamAssociation-AssociationState"></a>
The state of the MPA team association.
Type: String
Valid Values: `ACTIVE | UPDATE_PENDING | DELETE_PENDING`
Required: Yes

 ** MpaTeamArn **   <a name="paymentcryptography-Type-MpaTeamAssociation-MpaTeamArn"></a>
The ARN of the MPA team.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws(-[^:]+)?:mpa:[a-z0-9-]{1,20}:[0-9]{12}:approval-team/[a-zA-Z0-9._-]+`
Required: Yes

 ** MpaStatus **   <a name="paymentcryptography-Type-MpaTeamAssociation-MpaStatus"></a>
The MPA session status for the association, if applicable.
Type: [MpaStatus](API_MpaStatus.md) object
Required: No

## See Also
<a name="API_MpaTeamAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/payment-cryptography-2021-09-14/MpaTeamAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/payment-cryptography-2021-09-14/MpaTeamAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/payment-cryptography-2021-09-14/MpaTeamAssociation)
