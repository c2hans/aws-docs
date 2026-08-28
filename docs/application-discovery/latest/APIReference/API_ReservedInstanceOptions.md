---
source_url: https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_ReservedInstanceOptions.html
---

# ReservedInstanceOptions
<a name="API_ReservedInstanceOptions"></a>

**Important**
 AWS Application Discovery Service is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Application Discovery Service availability change](https://docs.aws.amazon.com/application-discovery/latest/userguide/application-discovery-service-availability-change.html).

 Used to provide Reserved Instance preferences for the recommendation.

## Contents
<a name="API_ReservedInstanceOptions_Contents"></a>

 ** offeringClass **   <a name="DiscServ-Type-ReservedInstanceOptions-offeringClass"></a>
 The flexibility to change the instance types needed for your Reserved Instance.
Type: String
Valid Values: `STANDARD | CONVERTIBLE`
Required: Yes

 ** purchasingOption **   <a name="DiscServ-Type-ReservedInstanceOptions-purchasingOption"></a>
 The payment plan to use for your Reserved Instance.
Type: String
Valid Values: `ALL_UPFRONT | PARTIAL_UPFRONT | NO_UPFRONT`
Required: Yes

 ** termLength **   <a name="DiscServ-Type-ReservedInstanceOptions-termLength"></a>
 The preferred duration of the Reserved Instance term.
Type: String
Valid Values: `ONE_YEAR | THREE_YEAR`
Required: Yes

## See Also
<a name="API_ReservedInstanceOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/discovery-2015-11-01/ReservedInstanceOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/discovery-2015-11-01/ReservedInstanceOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/discovery-2015-11-01/ReservedInstanceOptions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Application Discovery Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query application-discovery` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
