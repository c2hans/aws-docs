---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_View.html
---

# View
<a name="API_View"></a>

A view resource object. Contains metadata and content necessary to render the view.

## Contents
<a name="API_View_Contents"></a>

 ** Arn **   <a name="connect-Type-View-Arn"></a>
The Amazon Resource Name (ARN) of the view.
Type: String
Required: No

 ** Content **   <a name="connect-Type-View-Content"></a>
View content containing all content necessary to render a view except for runtime input data.
Type: [ViewContent](API_ViewContent.md) object
Required: No

 ** CreatedTime **   <a name="connect-Type-View-CreatedTime"></a>
The timestamp of when the view was created.
Type: Timestamp
Required: No

 ** Description **   <a name="connect-Type-View-Description"></a>
The description of the view.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `^([\p{L}\p{N}_.:\/=+\-@,()']+[\p{L}\p{Z}\p{N}_.:\/=+\-@,()']*)$`
Required: No

 ** Id **   <a name="connect-Type-View-Id"></a>
The identifier of the view.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Pattern: `^[a-zA-Z0-9\_\-:\/$]+$`
Required: No

 ** LastModifiedTime **   <a name="connect-Type-View-LastModifiedTime"></a>
Latest timestamp of the `UpdateViewContent` or `CreateViewVersion` operations.
Type: Timestamp
Required: No

 ** Name **   <a name="connect-Type-View-Name"></a>
The name of the view.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^([\p{L}\p{N}_.:\/=+\-@()']+[\p{L}\p{Z}\p{N}_.:\/=+\-@()']*)$`
Required: No

 ** Status **   <a name="connect-Type-View-Status"></a>
Indicates the view status as either `SAVED` or `PUBLISHED`. The `PUBLISHED` status will initiate validation on the content.
Type: String
Valid Values: `PUBLISHED | SAVED`
Required: No

 ** Tags **   <a name="connect-Type-View-Tags"></a>
The tags associated with the view resource (not specific to view version).
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[\p{L}\p{Z}\p{N}_.:/=+\-@]*$`
Value Length Constraints: Maximum length of 256.
Required: No

 ** Type **   <a name="connect-Type-View-Type"></a>
The type of the view - `CUSTOMER_MANAGED`.
Type: String
Valid Values: `CUSTOMER_MANAGED | AWS_MANAGED`
Required: No

 ** Version **   <a name="connect-Type-View-Version"></a>
Current version of the view.
Type: Integer
Required: No

 ** VersionDescription **   <a name="connect-Type-View-VersionDescription"></a>
The description of the version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `^([\p{L}\p{N}_.:\/=+\-@,()']+[\p{L}\p{Z}\p{N}_.:\/=+\-@,()']*)$`
Required: No

 ** ViewContentSha256 **   <a name="connect-Type-View-ViewContentSha256"></a>
Indicates the checksum value of the latest published view content.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9]$`
Required: No

## See Also
<a name="API_View_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/View)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/View)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/View)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
