---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_LensUpgradeSummary.html
---

# LensUpgradeSummary
<a name="API_LensUpgradeSummary"></a>

Lens upgrade summary return object.

## Contents
<a name="API_LensUpgradeSummary_Contents"></a>

 ** CurrentLensVersion **   <a name="wellarchitected-Type-LensUpgradeSummary-CurrentLensVersion"></a>
The current version of the lens.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Required: No

 ** LatestLensVersion **   <a name="wellarchitected-Type-LensUpgradeSummary-LatestLensVersion"></a>
The latest version of the lens.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Required: No

 ** LensAlias **   <a name="wellarchitected-Type-LensUpgradeSummary-LensAlias"></a>
The alias of the lens.
For AWS official lenses, this is either the lens alias, such as `serverless`, or the lens ARN, such as `arn:aws:wellarchitected:us-east-1::lens/serverless`. Note that some operations (such as ExportLens and CreateLensShare) are not permitted on AWS official lenses.
For custom lenses, this is the lens ARN, such as `arn:aws:wellarchitected:us-west-2:123456789012:lens/0123456789abcdef01234567890abcdef`.
Each lens is identified by its [LensSummary:LensAlias](API_LensSummary.md#wellarchitected-Type-LensSummary-LensAlias).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** LensArn **   <a name="wellarchitected-Type-LensUpgradeSummary-LensArn"></a>
The ARN for the lens.
Type: String
Required: No

 ** ResourceArn **   <a name="wellarchitected-Type-LensUpgradeSummary-ResourceArn"></a>
 `ResourceArn` of the lens being upgraded
Type: String
Length Constraints: Minimum length of 50. Maximum length of 250.
Pattern: `arn:aws(-us-gov|-iso(-[a-z])?|-cn)?:wellarchitected:[a-z]{2}(-gov|-iso([a-z])?)?-[a-z]+-\d:\d{12}:(review-template)/[a-f0-9]{32}`
Required: No

 ** ResourceName **   <a name="wellarchitected-Type-LensUpgradeSummary-ResourceName"></a>
The name of the workload.
The name must be unique within an account within an AWS Region. Spaces and capitalization are ignored when checking for uniqueness.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 100.
Required: No

 ** WorkloadId **   <a name="wellarchitected-Type-LensUpgradeSummary-WorkloadId"></a>
The ID assigned to the workload. This ID is unique within an AWS Region.
Type: String
Length Constraints: Fixed length of 32.
Pattern: `[0-9a-f]{32}`
Required: No

 ** WorkloadName **   <a name="wellarchitected-Type-LensUpgradeSummary-WorkloadName"></a>
The name of the workload.
The name must be unique within an account within an AWS Region. Spaces and capitalization are ignored when checking for uniqueness.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 100.
Required: No

## See Also
<a name="API_LensUpgradeSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/LensUpgradeSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/LensUpgradeSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/LensUpgradeSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected Tool. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
