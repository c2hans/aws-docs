---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_ReservedInstance.html
---

# ReservedInstance
<a name="API_ReservedInstance"></a>

Details of an OpenSearch Reserved Instance.

## Contents
<a name="API_ReservedInstance_Contents"></a>

 ** BillingSubscriptionId **   <a name="opensearchservice-Type-ReservedInstance-BillingSubscriptionId"></a>
The unique identifier of the billing subscription.
Type: Long
Required: No

 ** CurrencyCode **   <a name="opensearchservice-Type-ReservedInstance-CurrencyCode"></a>
The currency code for the offering.
Type: String
Required: No

 ** Duration **   <a name="opensearchservice-Type-ReservedInstance-Duration"></a>
The duration, in seconds, for which the OpenSearch instance is reserved.
Type: Integer
Required: No

 ** FixedPrice **   <a name="opensearchservice-Type-ReservedInstance-FixedPrice"></a>
The upfront fixed charge you will paid to purchase the specific Reserved Instance offering.
Type: Double
Required: No

 ** InstanceCount **   <a name="opensearchservice-Type-ReservedInstance-InstanceCount"></a>
The number of OpenSearch instances that have been reserved.
Type: Integer
Required: No

 ** InstanceType **   <a name="opensearchservice-Type-ReservedInstance-InstanceType"></a>
The OpenSearch instance type offered by theReserved Instance offering.
Type: String
Valid Values: `m3.medium.search | m3.large.search | m3.xlarge.search | m3.2xlarge.search | m4.large.search | m4.xlarge.search | m4.2xlarge.search | m4.4xlarge.search | m4.10xlarge.search | m5.large.search | m5.xlarge.search | m5.2xlarge.search | m5.4xlarge.search | m5.12xlarge.search | m5.24xlarge.search | r5.large.search | r5.xlarge.search | r5.2xlarge.search | r5.4xlarge.search | r5.12xlarge.search | r5.24xlarge.search | c5.large.search | c5.xlarge.search | c5.2xlarge.search | c5.4xlarge.search | c5.9xlarge.search | c5.18xlarge.search | t3.nano.search | t3.micro.search | t3.small.search | t3.medium.search | t3.large.search | t3.xlarge.search | t3.2xlarge.search | or1.medium.search | or1.large.search | or1.xlarge.search | or1.2xlarge.search | or1.4xlarge.search | or1.8xlarge.search | or1.12xlarge.search | or1.16xlarge.search | ultrawarm1.medium.search | ultrawarm1.large.search | ultrawarm1.xlarge.search | t2.micro.search | t2.small.search | t2.medium.search | r3.large.search | r3.xlarge.search | r3.2xlarge.search | r3.4xlarge.search | r3.8xlarge.search | i2.xlarge.search | i2.2xlarge.search | d2.xlarge.search | d2.2xlarge.search | d2.4xlarge.search | d2.8xlarge.search | c4.large.search | c4.xlarge.search | c4.2xlarge.search | c4.4xlarge.search | c4.8xlarge.search | r4.large.search | r4.xlarge.search | r4.2xlarge.search | r4.4xlarge.search | r4.8xlarge.search | r4.16xlarge.search | i3.large.search | i3.xlarge.search | i3.2xlarge.search | i3.4xlarge.search | i3.8xlarge.search | i3.16xlarge.search | r6g.large.search | r6g.xlarge.search | r6g.2xlarge.search | r6g.4xlarge.search | r6g.8xlarge.search | r6g.12xlarge.search | m6g.large.search | m6g.xlarge.search | m6g.2xlarge.search | m6g.4xlarge.search | m6g.8xlarge.search | m6g.12xlarge.search | c6g.large.search | c6g.xlarge.search | c6g.2xlarge.search | c6g.4xlarge.search | c6g.8xlarge.search | c6g.12xlarge.search | r6gd.large.search | r6gd.xlarge.search | r6gd.2xlarge.search | r6gd.4xlarge.search | r6gd.8xlarge.search | r6gd.12xlarge.search | r6gd.16xlarge.search | t4g.small.search | t4g.medium.search`
Required: No

 ** PaymentOption **   <a name="opensearchservice-Type-ReservedInstance-PaymentOption"></a>
The payment option as defined in the Reserved Instance offering.
Type: String
Valid Values: `ALL_UPFRONT | PARTIAL_UPFRONT | NO_UPFRONT`
Required: No

 ** RecurringCharges **   <a name="opensearchservice-Type-ReservedInstance-RecurringCharges"></a>
The recurring charge to your account, regardless of whether you create any domains using the Reserved Instance offering.
Type: Array of [RecurringCharge](API_RecurringCharge.md) objects
Required: No

 ** ReservationName **   <a name="opensearchservice-Type-ReservedInstance-ReservationName"></a>
The customer-specified identifier to track this reservation.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 64.
Pattern: `.*`
Required: No

 ** ReservedInstanceId **   <a name="opensearchservice-Type-ReservedInstance-ReservedInstanceId"></a>
The unique identifier for the reservation.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `\p{XDigit}{8}-\p{XDigit}{4}-\p{XDigit}{4}-\p{XDigit}{4}-\p{XDigit}{12}`
Required: No

 ** ReservedInstanceOfferingId **   <a name="opensearchservice-Type-ReservedInstance-ReservedInstanceOfferingId"></a>
The unique identifier of the Reserved Instance offering.
Type: String
Required: No

 ** StartTime **   <a name="opensearchservice-Type-ReservedInstance-StartTime"></a>
The date and time when the reservation was purchased.
Type: Timestamp
Required: No

 ** State **   <a name="opensearchservice-Type-ReservedInstance-State"></a>
The state of the Reserved Instance.
Type: String
Required: No

 ** UsagePrice **   <a name="opensearchservice-Type-ReservedInstance-UsagePrice"></a>
The hourly rate at which you're charged for the domain using this Reserved Instance.
Type: Double
Required: No

## See Also
<a name="API_ReservedInstance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/ReservedInstance)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/ReservedInstance)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/ReservedInstance)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
