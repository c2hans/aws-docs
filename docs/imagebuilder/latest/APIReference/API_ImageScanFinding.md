---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_ImageScanFinding.html
---

# ImageScanFinding
<a name="API_ImageScanFinding"></a>

Contains details about a vulnerability scan finding that Amazon Inspector generated for an image.

## Contents
<a name="API_ImageScanFinding_Contents"></a>

 ** awsAccountId **   <a name="imagebuilder-Type-ImageScanFinding-awsAccountId"></a>
The AWS account ID that's associated with the finding.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** description **   <a name="imagebuilder-Type-ImageScanFinding-description"></a>
The description of the finding.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** firstObservedAt **   <a name="imagebuilder-Type-ImageScanFinding-firstObservedAt"></a>
The date and time when the finding was first observed.
Type: Timestamp
Required: No

 ** fixAvailable **   <a name="imagebuilder-Type-ImageScanFinding-fixAvailable"></a>
Details about whether a fix is available for any of the packages that are identified in the finding through a version update. Valid values include:
+  `YES` – A fix is available for all of the packages identified in the finding.
+  `NO` – No fix is available.
+  `PARTIAL` – A fix is available for some, but not all, of the packages identified in the finding.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** imageBuildVersionArn **   <a name="imagebuilder-Type-ImageScanFinding-imageBuildVersionArn"></a>
The Amazon Resource Name (ARN) of the image build version that's associated with the finding.
Type: String
Pattern: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws(?:-[a-z-]+)?):image/[a-z0-9-_]+/[0-9]+\.[0-9]+\.[0-9]+/[0-9]+$`
Required: No

 ** imagePipelineArn **   <a name="imagebuilder-Type-ImageScanFinding-imagePipelineArn"></a>
The Amazon Resource Name (ARN) of the image pipeline that's associated with the finding.
Type: String
Pattern: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws):image-pipeline/[a-z0-9-_]+$`
Required: No

 ** inspectorScore **   <a name="imagebuilder-Type-ImageScanFinding-inspectorScore"></a>
The score that Amazon Inspector assigned for the finding.
Type: Double
Valid Range: Minimum value of 0.
Required: No

 ** inspectorScoreDetails **   <a name="imagebuilder-Type-ImageScanFinding-inspectorScoreDetails"></a>
An object that contains details of the Amazon Inspector score.
Type: [InspectorScoreDetails](API_InspectorScoreDetails.md) object
Required: No

 ** packageVulnerabilityDetails **   <a name="imagebuilder-Type-ImageScanFinding-packageVulnerabilityDetails"></a>
An object that contains the details of a package vulnerability finding.
Type: [PackageVulnerabilityDetails](API_PackageVulnerabilityDetails.md) object
Required: No

 ** remediation **   <a name="imagebuilder-Type-ImageScanFinding-remediation"></a>
An object that contains the details about how to remediate the finding.
Type: [Remediation](API_Remediation.md) object
Required: No

 ** severity **   <a name="imagebuilder-Type-ImageScanFinding-severity"></a>
The severity of the finding. For more information, see [Severity levels for Amazon Inspector findings](https://docs.aws.amazon.com/inspector/latest/user/findings-understanding-severity.html) in the *Amazon Inspector User Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** title **   <a name="imagebuilder-Type-ImageScanFinding-title"></a>
The title of the finding.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** type **   <a name="imagebuilder-Type-ImageScanFinding-type"></a>
The type of the finding. Image Builder looks for findings of the type `PACKAGE_VULNERABILITY` that apply to output images, and excludes other types.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** updatedAt **   <a name="imagebuilder-Type-ImageScanFinding-updatedAt"></a>
The timestamp when the finding was last updated.
Type: Timestamp
Required: No

## See Also
<a name="API_ImageScanFinding_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/ImageScanFinding)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/ImageScanFinding)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/ImageScanFinding)
