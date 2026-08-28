---
source_url: https://docs.aws.amazon.com/savingsplans/latest/APIReference/API_SavingsPlan.html
---

# SavingsPlan
<a name="API_SavingsPlan"></a>

Information about a Savings Plan.

## Contents
<a name="API_SavingsPlan_Contents"></a>

 ** commitment **   <a name="savingsplans-Type-SavingsPlan-commitment"></a>
The hourly commitment amount in the specified currency.
Type: String
Required: No

 ** currency **   <a name="savingsplans-Type-SavingsPlan-currency"></a>
The currency.
Type: String
Valid Values: `CNY | USD | EUR`
Required: No

 ** description **   <a name="savingsplans-Type-SavingsPlan-description"></a>
The description.
Type: String
Required: No

 ** ec2InstanceFamily **   <a name="savingsplans-Type-SavingsPlan-ec2InstanceFamily"></a>
The EC2 instance family.
Type: String
Required: No

 ** end **   <a name="savingsplans-Type-SavingsPlan-end"></a>
The end time.
Type: String
Required: No

 ** offeringId **   <a name="savingsplans-Type-SavingsPlan-offeringId"></a>
The ID of the offering.
Type: String
Required: No

 ** paymentOption **   <a name="savingsplans-Type-SavingsPlan-paymentOption"></a>
The payment option.
Type: String
Valid Values: `All Upfront | Partial Upfront | No Upfront`
Required: No

 ** productTypes **   <a name="savingsplans-Type-SavingsPlan-productTypes"></a>
The product types.
Type: Array of strings
Valid Values: `EC2 | Fargate | Lambda | SageMaker | RDS | DSQL | DynamoDB | ElastiCache | DocDB | Neptune | Timestream | Keyspaces | DMS | OpenSearch`
Required: No

 ** recurringPaymentAmount **   <a name="savingsplans-Type-SavingsPlan-recurringPaymentAmount"></a>
The recurring payment amount.
Type: String
Required: No

 ** region **   <a name="savingsplans-Type-SavingsPlan-region"></a>
The AWS Region.
Type: String
Required: No

 ** returnableUntil **   <a name="savingsplans-Type-SavingsPlan-returnableUntil"></a>
The time until when a return for the Savings Plan can be requested. If the Savings Plan is not returnable, the field reflects the Savings Plans start time.
Type: String
Required: No

 ** savingsPlanArn **   <a name="savingsplans-Type-SavingsPlan-savingsPlanArn"></a>
The Amazon Resource Name (ARN) of the Savings Plan.
Type: String
Pattern: `arn:aws:[a-z]+:([a-z]{2}-[a-z]+-\d{1}|):(\d{12}):savingsplan\/([0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12})$`
Required: No

 ** savingsPlanId **   <a name="savingsplans-Type-SavingsPlan-savingsPlanId"></a>
The ID of the Savings Plan.
Type: String
Required: No

 ** savingsPlanType **   <a name="savingsplans-Type-SavingsPlan-savingsPlanType"></a>
The plan type.
Type: String
Valid Values: `Compute | EC2Instance | SageMaker | Database`
Required: No

 ** start **   <a name="savingsplans-Type-SavingsPlan-start"></a>
The start time.
Type: String
Required: No

 ** state **   <a name="savingsplans-Type-SavingsPlan-state"></a>
The current state.
Type: String
Valid Values: `payment-pending | payment-failed | active | retired | queued | queued-deleted | pending-return | returned`
Required: No

 ** tags **   <a name="savingsplans-Type-SavingsPlan-tags"></a>
One or more tags.
Type: String to string map
Required: No

 ** termDurationInSeconds **   <a name="savingsplans-Type-SavingsPlan-termDurationInSeconds"></a>
The duration of the term, in seconds.
Type: Long
Required: No

 ** upfrontPaymentAmount **   <a name="savingsplans-Type-SavingsPlan-upfrontPaymentAmount"></a>
The up-front payment amount.
Type: String
Required: No

## See Also
<a name="API_SavingsPlan_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/savingsplans-2019-06-28/SavingsPlan)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/savingsplans-2019-06-28/SavingsPlan)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/savingsplans-2019-06-28/SavingsPlan)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Savings Plans. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query savingsplans` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
