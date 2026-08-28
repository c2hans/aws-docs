---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DocumentVersionInfo.html
---

# DocumentVersionInfo
<a name="API_DocumentVersionInfo"></a>

Version information about the document.

## Contents
<a name="API_DocumentVersionInfo_Contents"></a>

 ** CreatedDate **   <a name="systemsmanager-Type-DocumentVersionInfo-CreatedDate"></a>
The date the document was created.
Type: Timestamp
Required: No

 ** DisplayName **   <a name="systemsmanager-Type-DocumentVersionInfo-DisplayName"></a>
The friendly name of the SSM document. This value can differ for each version of the document. If you want to update this value, see [UpdateDocument](API_UpdateDocument.md).
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `^[\w\.\-\:\/ ]*$`
Required: No

 ** DocumentFormat **   <a name="systemsmanager-Type-DocumentVersionInfo-DocumentFormat"></a>
The document format, either JSON or YAML.
Type: String
Valid Values: `YAML | JSON | TEXT`
Required: No

 ** DocumentVersion **   <a name="systemsmanager-Type-DocumentVersionInfo-DocumentVersion"></a>
The document version.
Type: String
Pattern: `([$]LATEST|[$]DEFAULT|^[1-9][0-9]*$)`
Required: No

 ** IsDefaultVersion **   <a name="systemsmanager-Type-DocumentVersionInfo-IsDefaultVersion"></a>
An identifier for the default version of the document.
Type: Boolean
Required: No

 ** Name **   <a name="systemsmanager-Type-DocumentVersionInfo-Name"></a>
The document name.
Type: String
Pattern: `^[a-zA-Z0-9_\-.]{3,128}$`
Required: No

 ** ReviewStatus **   <a name="systemsmanager-Type-DocumentVersionInfo-ReviewStatus"></a>
The current status of the approval review for the latest version of the document.
Type: String
Valid Values: `APPROVED | NOT_REVIEWED | PENDING | REJECTED`
Required: No

 ** Status **   <a name="systemsmanager-Type-DocumentVersionInfo-Status"></a>
The status of the SSM document, such as `Creating`, `Active`, `Failed`, and `Deleting`.
Type: String
Valid Values: `Creating | Active | Updating | Deleting | Failed`
Required: No

 ** StatusInformation **   <a name="systemsmanager-Type-DocumentVersionInfo-StatusInformation"></a>
A message returned by AWS Systems Manager that explains the `Status` value. For example, a `Failed` status might be explained by the `StatusInformation` message, "The specified S3 bucket doesn't exist. Verify that the URL of the S3 bucket is correct."
Type: String
Required: No

 ** VersionName **   <a name="systemsmanager-Type-DocumentVersionInfo-VersionName"></a>
The version of the artifact associated with the document. For example, 12.6. This value is unique across all versions of a document, and can't be changed.
Type: String
Pattern: `^[a-zA-Z0-9_\-.]{1,128}$`
Required: No

## See Also
<a name="API_DocumentVersionInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/DocumentVersionInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/DocumentVersionInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/DocumentVersionInfo)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
