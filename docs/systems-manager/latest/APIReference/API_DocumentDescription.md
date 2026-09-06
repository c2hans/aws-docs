---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DocumentDescription.html
---

# DocumentDescription
<a name="API_DocumentDescription"></a>

Describes an AWS Systems Manager document (SSM document).

## Contents
<a name="API_DocumentDescription_Contents"></a>

 ** ApprovedVersion **   <a name="systemsmanager-Type-DocumentDescription-ApprovedVersion"></a>
The version of the document currently approved for use in the organization.
Type: String
Pattern: `([$]LATEST|[$]DEFAULT|^[1-9][0-9]*$)`
Required: No

 ** AttachmentsInformation **   <a name="systemsmanager-Type-DocumentDescription-AttachmentsInformation"></a>
Details about the document attachments, including names, locations, sizes, and so on.
Type: Array of [AttachmentInformation](API_AttachmentInformation.md) objects
Required: No

 ** Author **   <a name="systemsmanager-Type-DocumentDescription-Author"></a>
The user in your organization who created the document.
Type: String
Required: No

 ** Category **   <a name="systemsmanager-Type-DocumentDescription-Category"></a>
The classification of a document to help you identify and categorize its use.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 3 items.
Length Constraints: Maximum length of 128.
Required: No

 ** CategoryEnum **   <a name="systemsmanager-Type-DocumentDescription-CategoryEnum"></a>
The value that identifies a document's category.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 3 items.
Length Constraints: Maximum length of 128.
Required: No

 ** CreatedDate **   <a name="systemsmanager-Type-DocumentDescription-CreatedDate"></a>
The date when the document was created.
Type: Timestamp
Required: No

 ** DefaultVersion **   <a name="systemsmanager-Type-DocumentDescription-DefaultVersion"></a>
The default version.
Type: String
Pattern: `([$]LATEST|[$]DEFAULT|^[1-9][0-9]*$)`
Required: No

 ** Description **   <a name="systemsmanager-Type-DocumentDescription-Description"></a>
A description of the document.
Type: String
Required: No

 ** DisplayName **   <a name="systemsmanager-Type-DocumentDescription-DisplayName"></a>
The friendly name of the SSM document. This value can differ for each version of the document. If you want to update this value, see [UpdateDocument](API_UpdateDocument.md).
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `^[\w\.\-\:\/ ]*$`
Required: No

 ** DocumentFormat **   <a name="systemsmanager-Type-DocumentDescription-DocumentFormat"></a>
The document format, either JSON or YAML.
Type: String
Valid Values: `YAML | JSON | TEXT`
Required: No

 ** DocumentType **   <a name="systemsmanager-Type-DocumentDescription-DocumentType"></a>
The type of document.
Type: String
Valid Values: `Command | Policy | Automation | Session | Package | ApplicationConfiguration | ApplicationConfigurationSchema | DeploymentStrategy | ChangeCalendar | Automation.ChangeTemplate | ProblemAnalysis | ProblemAnalysisTemplate | CloudFormation | ConformancePackTemplate | QuickSetup | ManualApprovalPolicy | AutoApprovalPolicy`
Required: No

 ** DocumentVersion **   <a name="systemsmanager-Type-DocumentDescription-DocumentVersion"></a>
The document version.
Type: String
Pattern: `([$]LATEST|[$]DEFAULT|^[1-9][0-9]*$)`
Required: No

 ** Hash **   <a name="systemsmanager-Type-DocumentDescription-Hash"></a>
The Sha256 or Sha1 hash created by the system when the document was created.
Sha1 hashes have been deprecated.
Type: String
Length Constraints: Maximum length of 256.
Required: No

 ** HashType **   <a name="systemsmanager-Type-DocumentDescription-HashType"></a>
The hash type of the document. Valid values include `Sha256` or `Sha1`.
Sha1 hashes have been deprecated.
Type: String
Valid Values: `Sha256 | Sha1`
Required: No

 ** LatestVersion **   <a name="systemsmanager-Type-DocumentDescription-LatestVersion"></a>
The latest version of the document.
Type: String
Pattern: `([$]LATEST|[$]DEFAULT|^[1-9][0-9]*$)`
Required: No

 ** Name **   <a name="systemsmanager-Type-DocumentDescription-Name"></a>
The name of the SSM document.
Type: String
Pattern: `^[a-zA-Z0-9_\-.:/]{3,128}$`
Required: No

 ** Owner **   <a name="systemsmanager-Type-DocumentDescription-Owner"></a>
The Amazon Web Services user that created the document.
Type: String
Required: No

 ** Parameters **   <a name="systemsmanager-Type-DocumentDescription-Parameters"></a>
A description of the parameters for a document.
Type: Array of [DocumentParameter](API_DocumentParameter.md) objects
Required: No

 ** PendingReviewVersion **   <a name="systemsmanager-Type-DocumentDescription-PendingReviewVersion"></a>
The version of the document that is currently under review.
Type: String
Pattern: `([$]LATEST|[$]DEFAULT|^[1-9][0-9]*$)`
Required: No

 ** PlatformTypes **   <a name="systemsmanager-Type-DocumentDescription-PlatformTypes"></a>
The list of operating system (OS) platforms compatible with this SSM document.
Type: Array of strings
Valid Values: `Windows | Linux | MacOS`
Required: No

 ** Requires **   <a name="systemsmanager-Type-DocumentDescription-Requires"></a>
A list of SSM documents required by a document. For example, an `ApplicationConfiguration` document requires an `ApplicationConfigurationSchema` document.
Type: Array of [DocumentRequires](API_DocumentRequires.md) objects
Array Members: Minimum number of 1 item.
Required: No

 ** ReviewInformation **   <a name="systemsmanager-Type-DocumentDescription-ReviewInformation"></a>
Details about the review of a document.
Type: Array of [ReviewInformation](API_ReviewInformation.md) objects
Array Members: Minimum number of 1 item.
Required: No

 ** ReviewStatus **   <a name="systemsmanager-Type-DocumentDescription-ReviewStatus"></a>
The current status of the review.
Type: String
Valid Values: `APPROVED | NOT_REVIEWED | PENDING | REJECTED`
Required: No

 ** SchemaVersion **   <a name="systemsmanager-Type-DocumentDescription-SchemaVersion"></a>
The schema version.
Type: String
Pattern: `([0-9]+)\.([0-9]+)`
Required: No

 ** Sha1 **   <a name="systemsmanager-Type-DocumentDescription-Sha1"></a>
The SHA1 hash of the document, which you can use for verification.
Type: String
Required: No

 ** Status **   <a name="systemsmanager-Type-DocumentDescription-Status"></a>
The status of the SSM document.
Type: String
Valid Values: `Creating | Active | Updating | Deleting | Failed`
Required: No

 ** StatusInformation **   <a name="systemsmanager-Type-DocumentDescription-StatusInformation"></a>
A message returned by AWS Systems Manager that explains the `Status` value. For example, a `Failed` status might be explained by the `StatusInformation` message, "The specified S3 bucket doesn't exist. Verify that the URL of the S3 bucket is correct."
Type: String
Required: No

 ** Tags **   <a name="systemsmanager-Type-DocumentDescription-Tags"></a>
The tags, or metadata, that have been applied to the document.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Maximum number of 1000 items.
Required: No

 ** TargetType **   <a name="systemsmanager-Type-DocumentDescription-TargetType"></a>
The target type which defines the kinds of resources the document can run on. For example, `/AWS::EC2::Instance`. For a list of valid resource types, see [AWS resource and property types reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html) in the * AWS CloudFormation User Guide*.
Type: String
Length Constraints: Maximum length of 200.
Pattern: `^\/[\w\.\-\:\/]*$`
Required: No

 ** VersionName **   <a name="systemsmanager-Type-DocumentDescription-VersionName"></a>
The version of the artifact associated with the document.
Type: String
Pattern: `^[a-zA-Z0-9_\-.]{1,128}$`
Required: No

## See Also
<a name="API_DocumentDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/DocumentDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/DocumentDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/DocumentDescription)
