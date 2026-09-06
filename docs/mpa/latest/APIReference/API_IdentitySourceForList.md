---
source_url: https://docs.aws.amazon.com/mpa/latest/APIReference/API_IdentitySourceForList.html
---

# IdentitySourceForList
<a name="API_IdentitySourceForList"></a>

Contains details for an identity source. For more information, see [Identity source](https://docs.aws.amazon.com/mpa/latest/userguide/mpa-concepts.html) in the *Multi-party approval User Guide*.

## Contents
<a name="API_IdentitySourceForList_Contents"></a>

 ** CreationTime **   <a name="mpa-Type-IdentitySourceForList-CreationTime"></a>
Timestamp when the identity source was created.
Type: Timestamp
Required: No

 ** IdentitySourceArn **   <a name="mpa-Type-IdentitySourceForList-IdentitySourceArn"></a>
Amazon Resource Name (ARN) for the identity source.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Required: No

 ** IdentitySourceParameters **   <a name="mpa-Type-IdentitySourceForList-IdentitySourceParameters"></a>
A `IdentitySourceParametersForList` object. Contains details for the resource that provides identities to the identity source. For example, an IAM Identity Center instance.
Type: [IdentitySourceParametersForList](API_IdentitySourceParametersForList.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** IdentitySourceType **   <a name="mpa-Type-IdentitySourceForList-IdentitySourceType"></a>
The type of resource that provided identities to the identity source. For example, an IAM Identity Center instance.
Type: String
Valid Values: `IAM_IDENTITY_CENTER`
Required: No

 ** Status **   <a name="mpa-Type-IdentitySourceForList-Status"></a>
Status for the identity source. For example, if the identity source is `ACTIVE`.
Type: String
Valid Values: `CREATING | ACTIVE | DELETING | ERROR`
Required: No

 ** StatusCode **   <a name="mpa-Type-IdentitySourceForList-StatusCode"></a>
Status code of the identity source.
Type: String
Valid Values: `ACCESS_DENIED | DELETION_FAILED | IDC_INSTANCE_NOT_FOUND | IDC_INSTANCE_NOT_VALID`
Required: No

 ** StatusMessage **   <a name="mpa-Type-IdentitySourceForList-StatusMessage"></a>
Message describing the status for the identity source.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Required: No

## See Also
<a name="API_IdentitySourceForList_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mpa-2022-07-26/IdentitySourceForList)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mpa-2022-07-26/IdentitySourceForList)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mpa-2022-07-26/IdentitySourceForList)
