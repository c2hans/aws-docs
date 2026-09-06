---
source_url: https://docs.aws.amazon.com/cases/latest/APIReference/API_RelatedItemInputContent.html
---

# RelatedItemInputContent
<a name="API_connect-cases_RelatedItemInputContent"></a>

Represents the content of a related item to be created.

## Contents
<a name="API_connect-cases_RelatedItemInputContent_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** comment **   <a name="connect-Type-connect-cases_RelatedItemInputContent-comment"></a>
Represents the content of a comment to be returned to agents.
Type: [CommentContent](API_connect-cases_CommentContent.md) object
Required: No

 ** connectCase **   <a name="connect-Type-connect-cases_RelatedItemInputContent-connectCase"></a>
Represents the Connect Customer case to be created as a related item.
Type: [ConnectCaseInputContent](API_connect-cases_ConnectCaseInputContent.md) object
Required: No

 ** contact **   <a name="connect-Type-connect-cases_RelatedItemInputContent-contact"></a>
Object representing a contact in Connect Customer as an API request field.
Type: [Contact](API_connect-cases_Contact.md) object
Required: No

 ** custom **   <a name="connect-Type-connect-cases_RelatedItemInputContent-custom"></a>
Represents the content of a `Custom` type related item.
Type: [CustomInputContent](API_connect-cases_CustomInputContent.md) object
Required: No

 ** file **   <a name="connect-Type-connect-cases_RelatedItemInputContent-file"></a>
A file of related items.
Type: [FileContent](API_connect-cases_FileContent.md) object
Required: No

 ** sla **   <a name="connect-Type-connect-cases_RelatedItemInputContent-sla"></a>
Represents the content of an SLA to be created.
Type: [SlaInputContent](API_connect-cases_SlaInputContent.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

## See Also
<a name="API_connect-cases_RelatedItemInputContent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcases-2022-10-03/RelatedItemInputContent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcases-2022-10-03/RelatedItemInputContent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcases-2022-10-03/RelatedItemInputContent)
