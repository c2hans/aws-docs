---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DocumentIdentifier.html
---

# DocumentIdentifier
<a name="API_DocumentIdentifier"></a>

Describes the name of a SSM document.

## Contents
<a name="API_DocumentIdentifier_Contents"></a>

 ** Author **   <a name="systemsmanager-Type-DocumentIdentifier-Author"></a>
The user in your organization who created the document.
Type: String
Required: No

 ** CreatedDate **   <a name="systemsmanager-Type-DocumentIdentifier-CreatedDate"></a>
The date the SSM document was created.
Type: Timestamp
Required: No

 ** DisplayName **   <a name="systemsmanager-Type-DocumentIdentifier-DisplayName"></a>
An optional field where you can specify a friendly name for the SSM document. This value can differ for each version of the document. If you want to update this value, see [UpdateDocument](API_UpdateDocument.md).
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `^[\w\.\-\:\/ ]*$`
Required: No

 ** DocumentFormat **   <a name="systemsmanager-Type-DocumentIdentifier-DocumentFormat"></a>
The document format, either JSON or YAML.
Type: String
Valid Values: `YAML | JSON | TEXT`
Required: No

 ** DocumentType **   <a name="systemsmanager-Type-DocumentIdentifier-DocumentType"></a>
The document type.
Type: String
Valid Values: `Command | Policy | Automation | Session | Package | ApplicationConfiguration | ApplicationConfigurationSchema | DeploymentStrategy | ChangeCalendar | Automation.ChangeTemplate | ProblemAnalysis | ProblemAnalysisTemplate | CloudFormation | ConformancePackTemplate | QuickSetup | ManualApprovalPolicy | AutoApprovalPolicy`
Required: No

 ** DocumentVersion **   <a name="systemsmanager-Type-DocumentIdentifier-DocumentVersion"></a>
The document version.
Type: String
Pattern: `([$]LATEST|[$]DEFAULT|^[1-9][0-9]*$)`
Required: No

 ** Name **   <a name="systemsmanager-Type-DocumentIdentifier-Name"></a>
The name of the SSM document.
Type: String
Pattern: `^[a-zA-Z0-9_\-.:/]{3,128}$`
Required: No

 ** Owner **   <a name="systemsmanager-Type-DocumentIdentifier-Owner"></a>
The Amazon Web Services user that created the document.
Type: String
Required: No

 ** PlatformTypes **   <a name="systemsmanager-Type-DocumentIdentifier-PlatformTypes"></a>
The operating system platform.
Type: Array of strings
Valid Values: `Windows | Linux | MacOS`
Required: No

 ** Requires **   <a name="systemsmanager-Type-DocumentIdentifier-Requires"></a>
A list of SSM documents required by a document. For example, an `ApplicationConfiguration` document requires an `ApplicationConfigurationSchema` document.
Type: Array of [DocumentRequires](API_DocumentRequires.md) objects
Array Members: Minimum number of 1 item.
Required: No

 ** ReviewStatus **   <a name="systemsmanager-Type-DocumentIdentifier-ReviewStatus"></a>
The current status of a document review.
Type: String
Valid Values: `APPROVED | NOT_REVIEWED | PENDING | REJECTED`
Required: No

 ** SchemaVersion **   <a name="systemsmanager-Type-DocumentIdentifier-SchemaVersion"></a>
The schema version.
Type: String
Pattern: `([0-9]+)\.([0-9]+)`
Required: No

 ** Tags **   <a name="systemsmanager-Type-DocumentIdentifier-Tags"></a>
The tags, or metadata, that have been applied to the document.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Maximum number of 1000 items.
Required: No

 ** TargetType **   <a name="systemsmanager-Type-DocumentIdentifier-TargetType"></a>
The target type which defines the kinds of resources the document can run on. For example, `/AWS::EC2::Instance`. For a list of valid resource types, see [AWS resource and property types reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html) in the * AWS CloudFormation User Guide*.
Type: String
Length Constraints: Maximum length of 200.
Pattern: `^\/[\w\.\-\:\/]*$`
Required: No

 ** VersionName **   <a name="systemsmanager-Type-DocumentIdentifier-VersionName"></a>
An optional field specifying the version of the artifact associated with the document. For example, 12.6. This value is unique across all versions of a document, and can't be changed.
Type: String
Pattern: `^[a-zA-Z0-9_\-.]{1,128}$`
Required: No

## See Also
<a name="API_DocumentIdentifier_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/DocumentIdentifier)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/DocumentIdentifier)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/DocumentIdentifier)
