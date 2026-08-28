---
source_url: https://docs.aws.amazon.com/kms/latest/APIReference/API_RotationsListEntry.html
---

# RotationsListEntry
<a name="API_RotationsListEntry"></a>

Each entry contains information about one of the key materials associated with a KMS key.

## Contents
<a name="API_RotationsListEntry_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ExpirationModel **   <a name="KMS-Type-RotationsListEntry-ExpirationModel"></a>
Indicates if the key material is configured to automatically expire. There are two possible values for this field: `KEY_MATERIAL_EXPIRES` and `KEY_MATERIAL_DOES_NOT_EXPIRE`. For any key material that expires, the expiration date and time is indicated in `ValidTo`. This field is only present for symmetric encryption KMS keys with `EXTERNAL` origin.
Type: String
Valid Values: `KEY_MATERIAL_EXPIRES | KEY_MATERIAL_DOES_NOT_EXPIRE`
Required: No

 ** ImportState **   <a name="KMS-Type-RotationsListEntry-ImportState"></a>
Indicates if the key material is currently imported into AWS KMS. It has two possible values: `IMPORTED` or `PENDING_IMPORT`. This field is only present for symmetric encryption KMS keys with `EXTERNAL` origin.
Type: String
Valid Values: `IMPORTED | PENDING_IMPORT`
Required: No

 ** KeyId **   <a name="KMS-Type-RotationsListEntry-KeyId"></a>
Unique identifier of the key.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** KeyMaterialDescription **   <a name="KMS-Type-RotationsListEntry-KeyMaterialDescription"></a>
User-specified description of the key material. This field is only present for symmetric encryption KMS keys with `EXTERNAL` origin.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `^[a-zA-Z0-9:/_\s.-]+$`
Required: No

 ** KeyMaterialId **   <a name="KMS-Type-RotationsListEntry-KeyMaterialId"></a>
Unique identifier of the key material.
Type: String
Length Constraints: Fixed length of 64.
Pattern: `^[a-f0-9]+$`
Required: No

 ** KeyMaterialState **   <a name="KMS-Type-RotationsListEntry-KeyMaterialState"></a>
There are four possible values for this field: `CURRENT`, `NON_CURRENT`, `PENDING_MULTI_REGION_IMPORT_AND_ROTATION` and `PENDING_ROTATION`. AWS KMS uses `CURRENT` key material for both encryption and decryption and `NON_CURRENT` key material only for decryption. `PENDING_ROTATION` identifies key material that has been imported for on-demand key rotation but the rotation hasn't completed. The key material state `PENDING_MULTI_REGION_IMPORT_AND_ROTATION` is unique to multi-region, symmetric encryption keys with imported key material. It indicates key material that has been imported into the primary Region key but not all of the replica Region keys. When this key material is imported in to all of the replica Region keys, the key material state will change to `PENDING_ROTATION`. Key material in `PENDING_MULTI_REGION_IMPORT_AND_ROTATION` or `PENDING_ROTATION` state is not permanently associated with the KMS key. You can delete this key material and import different key material in its place. The `PENDING_MULTI_REGION_IMPORT_AND_ROTATION` and `PENDING_ROTATION` values are only used in symmetric encryption keys with imported key material. The other values, `CURRENT` and `NON_CURRENT`, are used for all KMS keys that support automatic or on-demand key rotation.
Type: String
Valid Values: `NON_CURRENT | CURRENT | PENDING_ROTATION | PENDING_MULTI_REGION_IMPORT_AND_ROTATION`
Required: No

 ** RotationDate **   <a name="KMS-Type-RotationsListEntry-RotationDate"></a>
Date and time that the key material rotation completed. Formatted as Unix time. This field is not present for the first key material or an imported key material in `PENDING_ROTATION` state.
Type: Timestamp
Required: No

 ** RotationType **   <a name="KMS-Type-RotationsListEntry-RotationType"></a>
Identifies whether the key material rotation was a scheduled [automatic rotation](https://docs.aws.amazon.com/kms/latest/developerguide/rotating-keys-enable-disable.html) or an [on-demand rotation](https://docs.aws.amazon.com/kms/latest/developerguide/rotating-keys-on-demand.html). This field is not present for the first key material or an imported key material in `PENDING_ROTATION` state.
Type: String
Valid Values: `AUTOMATIC | ON_DEMAND`
Required: No

 ** ValidTo **   <a name="KMS-Type-RotationsListEntry-ValidTo"></a>
Date and time at which the key material expires. This field is only present for symmetric encryption KMS keys with `EXTERNAL` origin in rotation list entries with an `ExpirationModel` value of `KEY_MATERIAL_EXPIRES`.
Type: Timestamp
Required: No

## See Also
<a name="API_RotationsListEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kms-2014-11-01/RotationsListEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kms-2014-11-01/RotationsListEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kms-2014-11-01/RotationsListEntry)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for KMS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
