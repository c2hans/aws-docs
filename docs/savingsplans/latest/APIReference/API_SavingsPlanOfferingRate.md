---
source_url: https://docs.aws.amazon.com/savingsplans/latest/APIReference/API_SavingsPlanOfferingRate.html
---

# SavingsPlanOfferingRate
<a name="API_SavingsPlanOfferingRate"></a>

Information about a Savings Plan offering rate.

## Contents
<a name="API_SavingsPlanOfferingRate_Contents"></a>

 ** operation **   <a name="savingsplans-Type-SavingsPlanOfferingRate-operation"></a>
The specific AWS operation for the line item in the billing report.
Type: String
Length Constraints: Maximum length of 255.
Pattern: `^[a-zA-Z0-9_ \/.:-]*$`
Required: No

 ** productType **   <a name="savingsplans-Type-SavingsPlanOfferingRate-productType"></a>
The product type.
Type: String
Valid Values: `EC2 | Fargate | Lambda | SageMaker | RDS | DSQL | DynamoDB | ElastiCache | DocDB | Neptune | Timestream | Keyspaces | DMS | OpenSearch`
Required: No

 ** properties **   <a name="savingsplans-Type-SavingsPlanOfferingRate-properties"></a>
The properties.
Type: Array of [SavingsPlanOfferingRateProperty](API_SavingsPlanOfferingRateProperty.md) objects
Required: No

 ** rate **   <a name="savingsplans-Type-SavingsPlanOfferingRate-rate"></a>
The Savings Plan rate.
Type: String
Required: No

 ** savingsPlanOffering **   <a name="savingsplans-Type-SavingsPlanOfferingRate-savingsPlanOffering"></a>
The Savings Plan offering.
Type: [ParentSavingsPlanOffering](API_ParentSavingsPlanOffering.md) object
Required: No

 ** serviceCode **   <a name="savingsplans-Type-SavingsPlanOfferingRate-serviceCode"></a>
The service.
Type: String
Valid Values: `AmazonEC2 | AmazonECS | AmazonEKS | AWSLambda | AmazonSageMaker | AmazonRDS | AuroraDSQL | AmazonDynamoDB | AmazonElastiCache | AmazonDocDB | AmazonNeptune | AmazonTimestream | AmazonMCS | AWSDatabaseMigrationSvc | AmazonES`
Required: No

 ** unit **   <a name="savingsplans-Type-SavingsPlanOfferingRate-unit"></a>
The unit.
Type: String
Valid Values: `Hrs | Lambda-GB-Second | Request | ACU-Hr | ReadRequestUnits | WriteRequestUnits | ReadCapacityUnit-Hrs | WriteCapacityUnit-Hrs | ReplicatedWriteRequestUnits | ReplicatedWriteCapacityUnit-Hrs | GB-Hours | DPU | ElastiCacheProcessingUnit | DCU-Hr | NCU-hr | OCU-hours | Jobs`
Required: No

 ** usageType **   <a name="savingsplans-Type-SavingsPlanOfferingRate-usageType"></a>
The usage details of the line item in the billing report.
Type: String
Length Constraints: Maximum length of 255.
Pattern: `^[a-zA-Z0-9_ \/.:-]+$`
Required: No

## See Also
<a name="API_SavingsPlanOfferingRate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/savingsplans-2019-06-28/SavingsPlanOfferingRate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/savingsplans-2019-06-28/SavingsPlanOfferingRate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/savingsplans-2019-06-28/SavingsPlanOfferingRate)
