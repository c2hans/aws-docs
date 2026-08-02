---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_LicenseRecommendationOption.html
---

# LicenseRecommendationOption
<a name="API_LicenseRecommendationOption"></a>

 Describes the recommendation options for licenses.

## Contents
<a name="API_LicenseRecommendationOption_Contents"></a>

 ** licenseEdition **   <a name="computeoptimizer-Type-LicenseRecommendationOption-licenseEdition"></a>
 The recommended edition of the license for the application that runs on the instance.
Type: String
Valid Values: `Enterprise | Standard | Free | NoLicenseEditionFound`
Required: No

 ** licenseModel **   <a name="computeoptimizer-Type-LicenseRecommendationOption-licenseModel"></a>
 The recommended license type associated with the instance.
Type: String
Valid Values: `LicenseIncluded | BringYourOwnLicense`
Required: No

 ** operatingSystem **   <a name="computeoptimizer-Type-LicenseRecommendationOption-operatingSystem"></a>
 The operating system of a license recommendation option.
Type: String
Required: No

 ** rank **   <a name="computeoptimizer-Type-LicenseRecommendationOption-rank"></a>
 The rank of the license recommendation option.
 The top recommendation option is ranked as `1`.
Type: Integer
Required: No

 ** savingsOpportunity **   <a name="computeoptimizer-Type-LicenseRecommendationOption-savingsOpportunity"></a>
Describes the savings opportunity for recommendations of a given resource type or for the recommendation option of an individual resource.
Savings opportunity represents the estimated monthly savings you can achieve by implementing a given Compute Optimizer recommendation.
Savings opportunity data requires that you opt in to Cost Explorer, as well as activate **Receive Amazon EC2 resource recommendations** in the Cost Explorer preferences page. That creates a connection between Cost Explorer and Compute Optimizer. With this connection, Cost Explorer generates savings estimates considering the price of existing resources, the price of recommended resources, and historical usage data. Estimated monthly savings reflects the projected dollar savings associated with each of the recommendations generated. For more information, see [Enabling Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-enable.html) and [Optimizing your cost with Rightsizing Recommendations](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-rightsizing.html) in the *Cost Management User Guide*.
Type: [SavingsOpportunity](API_SavingsOpportunity.md) object
Required: No

## See Also
<a name="API_LicenseRecommendationOption_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-2019-11-01/LicenseRecommendationOption)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-2019-11-01/LicenseRecommendationOption)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-2019-11-01/LicenseRecommendationOption)
