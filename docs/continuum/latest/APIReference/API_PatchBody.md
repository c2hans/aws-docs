---
source_url: https://docs.aws.amazon.com/continuum/latest/APIReference/API_PatchBody.html
---

# PatchBody
<a name="API_PatchBody"></a>

Projected content for a PATCH artifact: the remediation patch for one repository, with the descriptors needed to verify and apply it and the state of its delivery to the customer's own bucket or repository.

## Contents
<a name="API_PatchBody_Contents"></a>

 ** patch **   <a name="continuum-Type-PatchBody-patch"></a>
The patch.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 5242880.
Required: Yes

 ** patchSha256 **   <a name="continuum-Type-PatchBody-patchSha256"></a>
The patch Sha256.
Type: String
Length Constraints: Fixed length of 64.
Pattern: `[0-9a-f]{64}`
Required: Yes

 ** sizeBytes **   <a name="continuum-Type-PatchBody-sizeBytes"></a>
The size Bytes.
Type: Long
Required: Yes

 ** delivery **   <a name="continuum-Type-PatchBody-delivery"></a>
Delivery of a patch to a destination the customer owns: an object in the environment's source bucket or a pull request in the source repository.
Type: [PatchDelivery](API_PatchDelivery.md) object
Required: No

 ** format **   <a name="continuum-Type-PatchBody-format"></a>
The format.
Type: String
Valid Values: `GIT_MAILBOX_PATCH | GIT_BINARY_DIFF | GIT_DIFF`
Required: No

 ** repositoryName **   <a name="continuum-Type-PatchBody-repositoryName"></a>
The repository Name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_-]+`
Required: No

## See Also
<a name="API_PatchBody_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/continuum-2022-07-26/PatchBody)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/continuum-2022-07-26/PatchBody)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/continuum-2022-07-26/PatchBody)
