---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_FileUploadCardInput.html
---

# FileUploadCardInput
<a name="API_qapps_FileUploadCardInput"></a>

Represents a file upload card. It can optionally receive a `filename` and `fileId` to set a default file. If not received, the user must provide the file when the Q App runs.

## Contents
<a name="API_qapps_FileUploadCardInput_Contents"></a>

 ** id **   <a name="qbusiness-Type-qapps_FileUploadCardInput-id"></a>
The unique identifier of the file upload card.
Type: String
Pattern: `[\da-f]{8}-[\da-f]{4}-[45][\da-f]{3}-[89ABab][\da-f]{3}-[\da-f]{12}`
Required: Yes

 ** title **   <a name="qbusiness-Type-qapps_FileUploadCardInput-title"></a>
The title or label of the file upload card.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100.
Pattern: `[^{}\\"<>]+`
Required: Yes

 ** type **   <a name="qbusiness-Type-qapps_FileUploadCardInput-type"></a>
The type of the card.
Type: String
Valid Values: `text-input | q-query | file-upload | q-plugin | form-input`
Required: Yes

 ** allowOverride **   <a name="qbusiness-Type-qapps_FileUploadCardInput-allowOverride"></a>
A flag indicating if the user can override the default file for the upload card.
Type: Boolean
Required: No

 ** fileId **   <a name="qbusiness-Type-qapps_FileUploadCardInput-fileId"></a>
The identifier of a pre-uploaded file associated with the card.
Type: String
Pattern: `[\da-f]{8}-[\da-f]{4}-[45][\da-f]{3}-[89ABab][\da-f]{3}-[\da-f]{12}`
Required: No

 ** filename **   <a name="qbusiness-Type-qapps_FileUploadCardInput-filename"></a>
The default filename to use for the file upload card.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100.
Required: No

## See Also
<a name="API_qapps_FileUploadCardInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qapps-2023-11-27/FileUploadCardInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qapps-2023-11-27/FileUploadCardInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qapps-2023-11-27/FileUploadCardInput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q Business. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonq` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
