---
source_url: https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_FieldLevelEncryptionSummary.html
---

# FieldLevelEncryptionSummary
<a name="API_FieldLevelEncryptionSummary"></a>

A summary of a field-level encryption item.

## Contents
<a name="API_FieldLevelEncryptionSummary_Contents"></a>

 ** Id **   <a name="cloudfront-Type-FieldLevelEncryptionSummary-Id"></a>
The unique ID of a field-level encryption item.
Type: String
Required: Yes

 ** LastModifiedTime **   <a name="cloudfront-Type-FieldLevelEncryptionSummary-LastModifiedTime"></a>
The last time that the summary of field-level encryption items was modified.
Type: Timestamp
Required: Yes

 ** Comment **   <a name="cloudfront-Type-FieldLevelEncryptionSummary-Comment"></a>
An optional comment about the field-level encryption item. The comment cannot be longer than 128 characters.
Type: String
Required: No

 ** ContentTypeProfileConfig **   <a name="cloudfront-Type-FieldLevelEncryptionSummary-ContentTypeProfileConfig"></a>
A summary of a content type-profile mapping.
Type: [ContentTypeProfileConfig](API_ContentTypeProfileConfig.md) object
Required: No

 ** QueryArgProfileConfig **   <a name="cloudfront-Type-FieldLevelEncryptionSummary-QueryArgProfileConfig"></a>
A summary of a query argument-profile mapping.
Type: [QueryArgProfileConfig](API_QueryArgProfileConfig.md) object
Required: No

## See Also
<a name="API_FieldLevelEncryptionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/FieldLevelEncryptionSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/FieldLevelEncryptionSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/FieldLevelEncryptionSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudfront` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
