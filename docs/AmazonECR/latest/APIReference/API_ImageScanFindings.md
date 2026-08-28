---
source_url: https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_ImageScanFindings.html
---

# ImageScanFindings
<a name="API_ImageScanFindings"></a>

The details of an image scan.

## Contents
<a name="API_ImageScanFindings_Contents"></a>

 ** enhancedFindings **   <a name="ECR-Type-ImageScanFindings-enhancedFindings"></a>
Details about the enhanced scan findings from Amazon Inspector.
Type: Array of [EnhancedImageScanFinding](API_EnhancedImageScanFinding.md) objects
Required: No

 ** findings **   <a name="ECR-Type-ImageScanFindings-findings"></a>
The findings from the image scan.
Type: Array of [ImageScanFinding](API_ImageScanFinding.md) objects
Required: No

 ** findingSeverityCounts **   <a name="ECR-Type-ImageScanFindings-findingSeverityCounts"></a>
The image vulnerability counts, sorted by severity.
Type: String to integer map
Valid Keys: `INFORMATIONAL | LOW | MEDIUM | HIGH | CRITICAL | UNDEFINED`
Valid Range: Minimum value of 0.
Required: No

 ** imageScanCompletedAt **   <a name="ECR-Type-ImageScanFindings-imageScanCompletedAt"></a>
The time of the last completed image scan.
Type: Timestamp
Required: No

 ** vulnerabilitySourceUpdatedAt **   <a name="ECR-Type-ImageScanFindings-vulnerabilitySourceUpdatedAt"></a>
The time when the vulnerability data was last scanned.
Type: Timestamp
Required: No

## See Also
<a name="API_ImageScanFindings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecr-2015-09-21/ImageScanFindings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-2015-09-21/ImageScanFindings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecr-2015-09-21/ImageScanFindings)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ECR. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECR` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
