---
source_url: https://docs.aws.amazon.com/cases/latest/APIReference/API_RelatedItemContent.html
---

# RelatedItemContent
<a name="API_connect-cases_RelatedItemContent"></a>

Represents the content of a particular type of related item.

## Contents
<a name="API_connect-cases_RelatedItemContent_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** comment **   <a name="connect-Type-connect-cases_RelatedItemContent-comment"></a>
Represents the content of a comment to be returned to agents.
Type: [CommentContent](API_connect-cases_CommentContent.md) object
Required: No

 ** connectCase **   <a name="connect-Type-connect-cases_RelatedItemContent-connectCase"></a>
Represents the Connect Customer case to be created as a related item.
Type: [ConnectCaseContent](API_connect-cases_ConnectCaseContent.md) object
Required: No

 ** contact **   <a name="connect-Type-connect-cases_RelatedItemContent-contact"></a>
Represents the content of a contact to be returned to agents.
Type: [ContactContent](API_connect-cases_ContactContent.md) object
Required: No

 ** custom **   <a name="connect-Type-connect-cases_RelatedItemContent-custom"></a>
Represents the content of a `Custom` type related item.
Type: [CustomContent](API_connect-cases_CustomContent.md) object
Required: No

 ** file **   <a name="connect-Type-connect-cases_RelatedItemContent-file"></a>
Represents the content of a File to be returned to agents.
Type: [FileContent](API_connect-cases_FileContent.md) object
Required: No

 ** sla **   <a name="connect-Type-connect-cases_RelatedItemContent-sla"></a>
Represents the content of an SLA to be returned to agents.
Type: [SlaContent](API_connect-cases_SlaContent.md) object
Required: No

## See Also
<a name="API_connect-cases_RelatedItemContent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcases-2022-10-03/RelatedItemContent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcases-2022-10-03/RelatedItemContent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcases-2022-10-03/RelatedItemContent)
