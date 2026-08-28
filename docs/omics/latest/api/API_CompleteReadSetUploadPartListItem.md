---
source_url: https://docs.aws.amazon.com/omics/latest/api/API_CompleteReadSetUploadPartListItem.html
---

# CompleteReadSetUploadPartListItem
<a name="API_CompleteReadSetUploadPartListItem"></a>

 Part of the response to the CompleteReadSetUpload API, including metadata.

## Contents
<a name="API_CompleteReadSetUploadPartListItem_Contents"></a>

 ** checksum **   <a name="omics-Type-CompleteReadSetUploadPartListItem-checksum"></a>
 A unique identifier used to confirm that parts are being added to the correct upload.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: Yes

 ** partNumber **   <a name="omics-Type-CompleteReadSetUploadPartListItem-partNumber"></a>
 A number identifying the part in a read set upload.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 10000.
Required: Yes

 ** partSource **   <a name="omics-Type-CompleteReadSetUploadPartListItem-partSource"></a>
 The source file of the part being uploaded.
Type: String
Valid Values: `SOURCE1 | SOURCE2`
Required: Yes

## See Also
<a name="API_CompleteReadSetUploadPartListItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/omics-2022-11-28/CompleteReadSetUploadPartListItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/omics-2022-11-28/CompleteReadSetUploadPartListItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/omics-2022-11-28/CompleteReadSetUploadPartListItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS HealthOmics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query omics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
