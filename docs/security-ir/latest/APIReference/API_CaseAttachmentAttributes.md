---
source_url: https://docs.aws.amazon.com/security-ir/latest/APIReference/API_CaseAttachmentAttributes.html
---

# CaseAttachmentAttributes
<a name="API_CaseAttachmentAttributes"></a>

## Contents
<a name="API_CaseAttachmentAttributes_Contents"></a>

 ** attachmentId **   <a name="securityir-Type-CaseAttachmentAttributes-attachmentId"></a>

Type: String
Pattern: `[0-9a-fA-F]{8}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{12}`
Required: Yes

 ** attachmentStatus **   <a name="securityir-Type-CaseAttachmentAttributes-attachmentStatus"></a>

Type: String
Valid Values: `Verified | Failed | Pending`
Required: Yes

 ** createdDate **   <a name="securityir-Type-CaseAttachmentAttributes-createdDate"></a>

Type: Timestamp
Required: Yes

 ** creator **   <a name="securityir-Type-CaseAttachmentAttributes-creator"></a>

Type: String
Pattern: `.*((^AWS Responder)|(^\d{12}$)|(^arn:([^:]*aws[^:]*):(?:(?:iam)::\d{12}:(?:user|role|group|root)(?:(?:/[^/]+)+)?|(?:sts)::\d{12}:assumed-role/[^/]+/[^/]+)$)|(^security-ir.amazonaws.com)).*`
Required: Yes

 ** fileName **   <a name="securityir-Type-CaseAttachmentAttributes-fileName"></a>

Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9._-]+`
Required: Yes

## See Also
<a name="API_CaseAttachmentAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/security-ir-2018-05-10/CaseAttachmentAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/security-ir-2018-05-10/CaseAttachmentAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/security-ir-2018-05-10/CaseAttachmentAttributes)
