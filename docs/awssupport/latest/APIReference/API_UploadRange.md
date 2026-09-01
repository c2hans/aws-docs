---
source_url: https://docs.aws.amazon.com/awssupport/latest/APIReference/API_UploadRange.html
---

# UploadRange
<a name="API_UploadRange"></a>

The range of part indexes for which to return presigned upload URLs from [GetAttachmentUploadLinks](API_GetAttachmentUploadLinks.md).

## Contents
<a name="API_UploadRange_Contents"></a>

 ** startIndex **   <a name="AWSSupport-Type-UploadRange-startIndex"></a>
The starting part index of the range, inclusive. Part indexes start at 1.
Type: Integer
Valid Range: Minimum value of 1.

 ** endIndex **   <a name="AWSSupport-Type-UploadRange-endIndex"></a>
The ending part index of the range, exclusive. The range is half-open: `startIndex` is inclusive and `endIndex` is exclusive. For example, a range with `startIndex` of 1 and `endIndex` of 4 requests URLs for parts 1, 2, and 3. The range size (`endIndex` - `startIndex`) must not exceed 10. If you omit `endIndex`, the service defaults to `startIndex` \+ 10, capped by the total number of parts.
Type: Integer
Valid Range: Minimum value of 2.

## See Also
<a name="API_UploadRange_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/support-2013-04-15/UploadRange)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/support-2013-04-15/UploadRange)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/support-2013-04-15/UploadRange)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Support. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query awssupport` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
