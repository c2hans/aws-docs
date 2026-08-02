---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_RDSDBStorageRecommendationOption.html
---

# RDSDBStorageRecommendationOption
<a name="API_RDSDBStorageRecommendationOption"></a>

 Describes the recommendation options for DB storage.

## Contents
<a name="API_RDSDBStorageRecommendationOption_Contents"></a>

 ** estimatedMonthlyVolumeIOPsCostVariation **   <a name="computeoptimizer-Type-RDSDBStorageRecommendationOption-estimatedMonthlyVolumeIOPsCostVariation"></a>
 The projected level of variation in monthly I/O costs for the DB storage recommendation option.
Type: String
Valid Values: `None | Low | Medium | High`
Required: No

 ** rank **   <a name="computeoptimizer-Type-RDSDBStorageRecommendationOption-rank"></a>
 The rank identifier of the DB storage recommendation option.
Type: Integer
Required: No

 ** savingsOpportunity **   <a name="computeoptimizer-Type-RDSDBStorageRecommendationOption-savingsOpportunity"></a>
Describes the savings opportunity for recommendations of a given resource type or for the recommendation option of an individual resource.
Savings opportunity represents the estimated monthly savings you can achieve by implementing a given Compute Optimizer recommendation.
Savings opportunity data requires that you opt in to Cost Explorer, as well as activate **Receive Amazon EC2 resource recommendations** in the Cost Explorer preferences page. That creates a connection between Cost Explorer and Compute Optimizer. With this connection, Cost Explorer generates savings estimates considering the price of existing resources, the price of recommended resources, and historical usage data. Estimated monthly savings reflects the projected dollar savings associated with each of the recommendations generated. For more information, see [Enabling Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-enable.html) and [Optimizing your cost with Rightsizing Recommendations](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-rightsizing.html) in the *Cost Management User Guide*.
Type: [SavingsOpportunity](API_SavingsOpportunity.md) object
Required: No

 ** savingsOpportunityAfterDiscounts **   <a name="computeoptimizer-Type-RDSDBStorageRecommendationOption-savingsOpportunityAfterDiscounts"></a>
 Describes the savings opportunity for DB storage recommendations or for the recommendation option.
 Savings opportunity represents the estimated monthly savings after applying Savings Plans discounts. You can achieve this by implementing a given Compute Optimizer recommendation.
Type: [RDSStorageSavingsOpportunityAfterDiscounts](API_RDSStorageSavingsOpportunityAfterDiscounts.md) object
Required: No

 ** storageConfiguration **   <a name="computeoptimizer-Type-RDSDBStorageRecommendationOption-storageConfiguration"></a>
 The recommended storage configuration.
Type: [DBStorageConfiguration](API_DBStorageConfiguration.md) object
Required: No

## See Also
<a name="API_RDSDBStorageRecommendationOption_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-2019-11-01/RDSDBStorageRecommendationOption)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-2019-11-01/RDSDBStorageRecommendationOption)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-2019-11-01/RDSDBStorageRecommendationOption)
