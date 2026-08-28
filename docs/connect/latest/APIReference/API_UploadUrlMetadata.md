---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_UploadUrlMetadata.html
---

# UploadUrlMetadata
<a name="API_UploadUrlMetadata"></a>

Fields required when uploading an attached file.

## Contents
<a name="API_UploadUrlMetadata_Contents"></a>

 ** HeadersToInclude **   <a name="connect-Type-UploadUrlMetadata-HeadersToInclude"></a>
A map of headers that should be provided when uploading the attached file.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** Url **   <a name="connect-Type-UploadUrlMetadata-Url"></a>
A pre-signed S3 URL that should be used for uploading the attached file.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.
Required: No

 ** UrlExpiry **   <a name="connect-Type-UploadUrlMetadata-UrlExpiry"></a>
The expiration time of the URL in ISO timestamp. It's specified in ISO 8601 format: `yyyy-MM-ddThh:mm:ss.SSSZ`. For example, `2019-11-08T02:41:28.172Z`.
Type: String
Required: No

## See Also
<a name="API_UploadUrlMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/UploadUrlMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/UploadUrlMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/UploadUrlMetadata)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
