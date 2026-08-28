---
source_url: https://docs.aws.amazon.com/savingsplans/latest/APIReference/API_SavingsPlanRate.html
---

# SavingsPlanRate
<a name="API_SavingsPlanRate"></a>

Information about a Savings Plan rate.

## Contents
<a name="API_SavingsPlanRate_Contents"></a>

 ** currency **   <a name="savingsplans-Type-SavingsPlanRate-currency"></a>
The currency.
Type: String
Valid Values: `CNY | USD | EUR`
Required: No

 ** operation **   <a name="savingsplans-Type-SavingsPlanRate-operation"></a>
The specific AWS operation for the line item in the billing report.
Type: String
Length Constraints: Maximum length of 255.
Pattern: `^[a-zA-Z0-9_ \/.:-]*$`
Required: No

 ** productType **   <a name="savingsplans-Type-SavingsPlanRate-productType"></a>
The product type.
Type: String
Valid Values: `EC2 | Fargate | Lambda | SageMaker | RDS | DSQL | DynamoDB | ElastiCache | DocDB | Neptune | Timestream | Keyspaces | DMS | OpenSearch`
Required: No

 ** properties **   <a name="savingsplans-Type-SavingsPlanRate-properties"></a>
The properties.
Type: Array of [SavingsPlanRateProperty](API_SavingsPlanRateProperty.md) objects
Required: No

 ** rate **   <a name="savingsplans-Type-SavingsPlanRate-rate"></a>
The rate.
Type: String
Required: No

 ** serviceCode **   <a name="savingsplans-Type-SavingsPlanRate-serviceCode"></a>
The service.
Type: String
Valid Values: `AmazonEC2 | AmazonECS | AmazonEKS | AWSLambda | AmazonSageMaker | AmazonRDS | AuroraDSQL | AmazonDynamoDB | AmazonElastiCache | AmazonDocDB | AmazonNeptune | AmazonTimestream | AmazonMCS | AWSDatabaseMigrationSvc | AmazonES`
Required: No

 ** unit **   <a name="savingsplans-Type-SavingsPlanRate-unit"></a>
The unit.
Type: String
Valid Values: `Hrs | Lambda-GB-Second | Request | ACU-Hr | ReadRequestUnits | WriteRequestUnits | ReadCapacityUnit-Hrs | WriteCapacityUnit-Hrs | ReplicatedWriteRequestUnits | ReplicatedWriteCapacityUnit-Hrs | GB-Hours | DPU | ElastiCacheProcessingUnit | DCU-Hr | NCU-hr | OCU-hours | Jobs`
Required: No

 ** usageType **   <a name="savingsplans-Type-SavingsPlanRate-usageType"></a>
The usage details of the line item in the billing report.
Type: String
Length Constraints: Maximum length of 255.
Pattern: `^[a-zA-Z0-9_ \/.:-]+$`
Required: No

## See Also
<a name="API_SavingsPlanRate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/savingsplans-2019-06-28/SavingsPlanRate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/savingsplans-2019-06-28/SavingsPlanRate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/savingsplans-2019-06-28/SavingsPlanRate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Savings Plans. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query savingsplans` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
