---
source_url: https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_RfcCorrespondence.html
---

# RfcCorrespondence
<a name="API_RfcCorrespondence"></a>

The RFC correspondence structure.

## Contents
<a name="API_RfcCorrespondence_Contents"></a>

 ** Content **   <a name="amscm-Type-RfcCorrespondence-Content"></a>
The RFC correspondence content in plain text.
Type: String
Required: No

 ** CorrespondenceId **   <a name="amscm-Type-RfcCorrespondence-CorrespondenceId"></a>
The Unique Identifier(UUID) of the RFC correspondence.
Type: String
Required: No

 ** CreatedBy **   <a name="amscm-Type-RfcCorrespondence-CreatedBy"></a>
The Amazon Resource Name (ARN) of the user who created the correspondence.
Type: String
Required: No

 ** CreatedTime **   <a name="amscm-Type-RfcCorrespondence-CreatedTime"></a>
The date and time when the RFC correspondence was created.
Type: String
Required: No

 ** LinkedAttachments **   <a name="amscm-Type-RfcCorrespondence-LinkedAttachments"></a>
The list of `AttachmentId` identifiers that are linked to the RFC correspondence.
Type: Array of [LinkedAttachment](API_LinkedAttachment.md) objects
Required: No

 ** RfcId **   <a name="amscm-Type-RfcCorrespondence-RfcId"></a>
The `RfcId` of the RFC.
Type: String
Required: No

 ** UserType **   <a name="amscm-Type-RfcCorrespondence-UserType"></a>
The user type of the RFC correspondence, customer or AWS operator.
Type: [UserType](API_UserType.md) object
Required: No

## See Also
<a name="API_RfcCorrespondence_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amscm-2020-05-21/RfcCorrespondence)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amscm-2020-05-21/RfcCorrespondence)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amscm-2020-05-21/RfcCorrespondence)
