---
source_url: https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_EnhancedImageScanFinding.html
---

# EnhancedImageScanFinding
<a name="API_EnhancedImageScanFinding"></a>

The details of an enhanced image scan. This is returned when enhanced scanning is enabled for your private registry.

## Contents
<a name="API_EnhancedImageScanFinding_Contents"></a>

 ** awsAccountId **   <a name="ECR-Type-EnhancedImageScanFinding-awsAccountId"></a>
The AWS account ID associated with the image.
Type: String
Pattern: `[0-9]{12}`
Required: No

 ** description **   <a name="ECR-Type-EnhancedImageScanFinding-description"></a>
The description of the finding.
Type: String
Required: No

 ** exploitAvailable **   <a name="ECR-Type-EnhancedImageScanFinding-exploitAvailable"></a>
If a finding discovered in your environment has an exploit available.
Type: String
Required: No

 ** findingArn **   <a name="ECR-Type-EnhancedImageScanFinding-findingArn"></a>
The Amazon Resource Number (ARN) of the finding.
Type: String
Required: No

 ** firstObservedAt **   <a name="ECR-Type-EnhancedImageScanFinding-firstObservedAt"></a>
The date and time that the finding was first observed.
Type: Timestamp
Required: No

 ** fixAvailable **   <a name="ECR-Type-EnhancedImageScanFinding-fixAvailable"></a>
Details on whether a fix is available through a version update. This value can be `YES`, `NO`, or `PARTIAL`. A `PARTIAL` fix means that some, but not all, of the packages identified in the finding have fixes available through updated versions.
Type: String
Required: No

 ** lastObservedAt **   <a name="ECR-Type-EnhancedImageScanFinding-lastObservedAt"></a>
The date and time that the finding was last observed.
Type: Timestamp
Required: No

 ** packageVulnerabilityDetails **   <a name="ECR-Type-EnhancedImageScanFinding-packageVulnerabilityDetails"></a>
An object that contains the details of a package vulnerability finding.
Type: [PackageVulnerabilityDetails](API_PackageVulnerabilityDetails.md) object
Required: No

 ** remediation **   <a name="ECR-Type-EnhancedImageScanFinding-remediation"></a>
An object that contains the details about how to remediate a finding.
Type: [Remediation](API_Remediation.md) object
Required: No

 ** resources **   <a name="ECR-Type-EnhancedImageScanFinding-resources"></a>
Contains information on the resources involved in a finding.
Type: Array of [Resource](API_Resource.md) objects
Required: No

 ** score **   <a name="ECR-Type-EnhancedImageScanFinding-score"></a>
The Amazon Inspector score given to the finding.
Type: Double
Required: No

 ** scoreDetails **   <a name="ECR-Type-EnhancedImageScanFinding-scoreDetails"></a>
An object that contains details of the Amazon Inspector score.
Type: [ScoreDetails](API_ScoreDetails.md) object
Required: No

 ** severity **   <a name="ECR-Type-EnhancedImageScanFinding-severity"></a>
The severity of the finding.
Type: String
Required: No

 ** status **   <a name="ECR-Type-EnhancedImageScanFinding-status"></a>
The status of the finding.
Type: String
Required: No

 ** title **   <a name="ECR-Type-EnhancedImageScanFinding-title"></a>
The title of the finding.
Type: String
Required: No

 ** type **   <a name="ECR-Type-EnhancedImageScanFinding-type"></a>
The type of the finding.
Type: String
Required: No

 ** updatedAt **   <a name="ECR-Type-EnhancedImageScanFinding-updatedAt"></a>
The date and time the finding was last updated at.
Type: Timestamp
Required: No

## See Also
<a name="API_EnhancedImageScanFinding_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecr-2015-09-21/EnhancedImageScanFinding)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-2015-09-21/EnhancedImageScanFinding)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecr-2015-09-21/EnhancedImageScanFinding)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ECR. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECR` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
