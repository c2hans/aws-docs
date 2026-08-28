---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_ReferenceSummary.html
---

# ReferenceSummary
<a name="API_ReferenceSummary"></a>

Contains summary information about a reference. `ReferenceSummary` contains only one non null field between the URL and attachment based on the reference type.

## Contents
<a name="API_ReferenceSummary_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** Attachment **   <a name="connect-Type-ReferenceSummary-Attachment"></a>
Information about the reference when the `referenceType` is `ATTACHMENT`. Otherwise, null.
Type: [AttachmentReference](API_AttachmentReference.md) object
Required: No

 ** Date **   <a name="connect-Type-ReferenceSummary-Date"></a>
Information about a reference when the `referenceType` is `DATE`. Otherwise, null.
Type: [DateReference](API_DateReference.md) object
Required: No

 ** Email **   <a name="connect-Type-ReferenceSummary-Email"></a>
Information about a reference when the `referenceType` is `EMAIL`. Otherwise, null.
Type: [EmailReference](API_EmailReference.md) object
Required: No

 ** EmailMessage **   <a name="connect-Type-ReferenceSummary-EmailMessage"></a>
Information about the reference when the referenceType is `EMAIL_MESSAGE`. Otherwise, null.
Type: [EmailMessageReference](API_EmailMessageReference.md) object
Required: No

 ** EmailMessagePlainText **   <a name="connect-Type-ReferenceSummary-EmailMessagePlainText"></a>
Information about the reference when the referenceType is `EMAIL_MESSAGE`. Otherwise, null.
Type: [EmailMessageReference](API_EmailMessageReference.md) object
Required: No

 ** EmailMessagePlainTextRedacted **   <a name="connect-Type-ReferenceSummary-EmailMessagePlainTextRedacted"></a>
Information about the reference when the referenceType is `EMAIL_MESSAGE`. Otherwise, null.
Type: [EmailMessageReference](API_EmailMessageReference.md) object
Required: No

 ** EmailMessageRedacted **   <a name="connect-Type-ReferenceSummary-EmailMessageRedacted"></a>
Information about the reference when the referenceType is `EMAIL_MESSAGE`. Otherwise, null.
Type: [EmailMessageReference](API_EmailMessageReference.md) object
Required: No

 ** Number **   <a name="connect-Type-ReferenceSummary-Number"></a>
Information about a reference when the `referenceType` is `NUMBER`. Otherwise, null.
Type: [NumberReference](API_NumberReference.md) object
Required: No

 ** String **   <a name="connect-Type-ReferenceSummary-String"></a>
Information about a reference when the `referenceType` is `STRING`. Otherwise, null.
Type: [StringReference](API_StringReference.md) object
Required: No

 ** Url **   <a name="connect-Type-ReferenceSummary-Url"></a>
Information about the reference when the `referenceType` is `URL`. Otherwise, null.
Type: [UrlReference](API_UrlReference.md) object
Required: No

## See Also
<a name="API_ReferenceSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/ReferenceSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/ReferenceSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/ReferenceSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
