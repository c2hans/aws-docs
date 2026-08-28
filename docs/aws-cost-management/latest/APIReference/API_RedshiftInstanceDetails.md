---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_RedshiftInstanceDetails.html
---

# RedshiftInstanceDetails
<a name="API_RedshiftInstanceDetails"></a>

Details about the Amazon Redshift reservations that AWS recommends that you purchase.

## Contents
<a name="API_RedshiftInstanceDetails_Contents"></a>

 ** CurrentGeneration **   <a name="awscostmanagement-Type-RedshiftInstanceDetails-CurrentGeneration"></a>
Determines whether the recommendation is for a current-generation instance.
Type: Boolean
Required: No

 ** Family **   <a name="awscostmanagement-Type-RedshiftInstanceDetails-Family"></a>
The instance family of the recommended reservation.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** NodeType **   <a name="awscostmanagement-Type-RedshiftInstanceDetails-NodeType"></a>
The type of node that AWS recommends.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** Region **   <a name="awscostmanagement-Type-RedshiftInstanceDetails-Region"></a>
The AWS Region of the recommended reservation.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** SizeFlexEligible **   <a name="awscostmanagement-Type-RedshiftInstanceDetails-SizeFlexEligible"></a>
Determines whether the recommended reservation is size flexible.
Type: Boolean
Required: No

## See Also
<a name="API_RedshiftInstanceDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ce-2017-10-25/RedshiftInstanceDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ce-2017-10-25/RedshiftInstanceDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ce-2017-10-25/RedshiftInstanceDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
