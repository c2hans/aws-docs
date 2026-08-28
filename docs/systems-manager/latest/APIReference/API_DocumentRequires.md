---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DocumentRequires.html
---

# DocumentRequires
<a name="API_DocumentRequires"></a>

An SSM document required by the current document.

## Contents
<a name="API_DocumentRequires_Contents"></a>

 ** Name **   <a name="systemsmanager-Type-DocumentRequires-Name"></a>
The name of the required SSM document. The name can be an Amazon Resource Name (ARN).
Type: String
Pattern: `^[a-zA-Z0-9_\-.:/]{3,128}$`
Required: Yes

 ** RequireType **   <a name="systemsmanager-Type-DocumentRequires-RequireType"></a>
The document type of the required SSM document.
Type: String
Length Constraints: Maximum length of 128.
Pattern: `^[a-zA-Z0-9_\-.]{1,128}$`
Required: No

 ** Version **   <a name="systemsmanager-Type-DocumentRequires-Version"></a>
The document version required by the current document.
Type: String
Pattern: `([$]LATEST|[$]DEFAULT|^[1-9][0-9]*$)`
Required: No

 ** VersionName **   <a name="systemsmanager-Type-DocumentRequires-VersionName"></a>
An optional field specifying the version of the artifact associated with the document. For example, 12.6. This value is unique across all versions of a document, and can't be changed.
Type: String
Pattern: `^[a-zA-Z0-9_\-.]{1,128}$`
Required: No

## See Also
<a name="API_DocumentRequires_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/DocumentRequires)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/DocumentRequires)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/DocumentRequires)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
