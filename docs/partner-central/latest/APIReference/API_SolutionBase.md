---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_SolutionBase.html
---

# SolutionBase
<a name="API_SolutionBase"></a>

Specifies minimal information for the solution offered to solve the customer's business problem.

## Contents
<a name="API_SolutionBase_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Catalog **   <a name="AWSPartnerCentral-Type-SolutionBase-Catalog"></a>
Specifies the catalog in which the solution is hosted, either `AWS` or `Sandbox`. This helps partners differentiate between live solutions and those in testing environments.
Type: String
Pattern: `[a-zA-Z]+`
Required: Yes

 ** Category **   <a name="AWSPartnerCentral-Type-SolutionBase-Category"></a>
Specifies the solution category, which helps to categorize and organize the solutions partners offer. Valid values: `Software Product` \| `Consulting Service` \| `Hardware Product` \| `Communications Product` \| `Professional Service` \| `Managed Service` \| `Value-Added Resale AWS Service` \| `Distribution Service` \| `Training Service` \| `Merger and Acquisition Advising Service`.
Type: String
Required: Yes

 ** CreatedDate **   <a name="AWSPartnerCentral-Type-SolutionBase-CreatedDate"></a>
Indicates the solution creation date. This is useful to track and audit.
Type: Timestamp
Required: Yes

 ** Id **   <a name="AWSPartnerCentral-Type-SolutionBase-Id"></a>
Enables the association of solutions (offerings) to opportunities.
Type: String
Pattern: `S-[0-9]{1,19}`
Required: Yes

 ** Name **   <a name="AWSPartnerCentral-Type-SolutionBase-Name"></a>
Specifies the solution name.
Type: String
Required: Yes

 ** Status **   <a name="AWSPartnerCentral-Type-SolutionBase-Status"></a>
Specifies the solution's current status, which indicates its state in the system. Valid values: `Active` \| `Inactive` \| `Draft`. The status helps partners and AWS track the solution's lifecycle and availability. Filter for `Active` solutions for association to an opportunity.
Type: String
Valid Values: `Active | Inactive | Draft`
Required: Yes

 ** Arn **   <a name="AWSPartnerCentral-Type-SolutionBase-Arn"></a>
 The SolutionBase structure provides essential information about a solution.
Type: String
Pattern: `S-[0-9]{1,19}`
Required: No

 ** AwsMarketplaceSolutionArn **   <a name="AWSPartnerCentral-Type-SolutionBase-AwsMarketplaceSolutionArn"></a>
The Amazon Resource Name (ARN) of the AWS Marketplace solution associated with this partner solution.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 2048.
Pattern: `arn:.*`
Required: No

## See Also
<a name="API_SolutionBase_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/SolutionBase)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/SolutionBase)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/SolutionBase)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Partner Central. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query partner-central` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
