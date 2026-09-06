---
source_url: https://docs.aws.amazon.com/savingsplans/latest/APIReference/API_SavingsPlanOffering.html
---

# SavingsPlanOffering
<a name="API_SavingsPlanOffering"></a>

Information about a Savings Plan offering.

## Contents
<a name="API_SavingsPlanOffering_Contents"></a>

 ** currency **   <a name="savingsplans-Type-SavingsPlanOffering-currency"></a>
The currency.
Type: String
Valid Values: `CNY | USD | EUR`
Required: No

 ** description **   <a name="savingsplans-Type-SavingsPlanOffering-description"></a>
The description.
Type: String
Pattern: `^[a-zA-Z0-9_\- ]+$`
Required: No

 ** durationSeconds **   <a name="savingsplans-Type-SavingsPlanOffering-durationSeconds"></a>
The duration, in seconds.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** offeringId **   <a name="savingsplans-Type-SavingsPlanOffering-offeringId"></a>
The ID of the offering.
Type: String
Pattern: `[a-f0-9]+(-[a-f0-9]+)*`
Required: No

 ** operation **   <a name="savingsplans-Type-SavingsPlanOffering-operation"></a>
The specific AWS operation for the line item in the billing report.
Type: String
Length Constraints: Maximum length of 255.
Pattern: `^[a-zA-Z0-9_ \/.:-]*$`
Required: No

 ** paymentOption **   <a name="savingsplans-Type-SavingsPlanOffering-paymentOption"></a>
The payment option.
Type: String
Valid Values: `All Upfront | Partial Upfront | No Upfront`
Required: No

 ** planType **   <a name="savingsplans-Type-SavingsPlanOffering-planType"></a>
The plan type.
Type: String
Valid Values: `Compute | EC2Instance | SageMaker | Database`
Required: No

 ** productTypes **   <a name="savingsplans-Type-SavingsPlanOffering-productTypes"></a>
The product type.
Type: Array of strings
Valid Values: `EC2 | Fargate | Lambda | SageMaker | RDS | DSQL | DynamoDB | ElastiCache | DocDB | Neptune | Timestream | Keyspaces | DMS | OpenSearch`
Required: No

 ** properties **   <a name="savingsplans-Type-SavingsPlanOffering-properties"></a>
The properties.
Type: Array of [SavingsPlanOfferingProperty](API_SavingsPlanOfferingProperty.md) objects
Required: No

 ** serviceCode **   <a name="savingsplans-Type-SavingsPlanOffering-serviceCode"></a>
The service.
Type: String
Length Constraints: Maximum length of 255.
Pattern: `^[a-zA-Z]+$`
Required: No

 ** usageType **   <a name="savingsplans-Type-SavingsPlanOffering-usageType"></a>
The usage details of the line item in the billing report.
Type: String
Length Constraints: Maximum length of 255.
Pattern: `^[a-zA-Z0-9_ \/.:-]+$`
Required: No

## See Also
<a name="API_SavingsPlanOffering_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/savingsplans-2019-06-28/SavingsPlanOffering)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/savingsplans-2019-06-28/SavingsPlanOffering)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/savingsplans-2019-06-28/SavingsPlanOffering)
