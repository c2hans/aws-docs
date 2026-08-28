---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_AccountLimit.html
---

# AccountLimit
<a name="API_AccountLimit"></a>

A complex type that contains the type of limit that you specified in the request and the current value for that limit.

## Contents
<a name="API_AccountLimit_Contents"></a>

 ** Type **   <a name="Route53-Type-AccountLimit-Type"></a>
The limit that you requested. Valid values include the following:
+  **MAX\_HEALTH\_CHECKS\_BY\_OWNER**: The maximum number of health checks that you can create using the current account.
+  **MAX\_HOSTED\_ZONES\_BY\_OWNER**: The maximum number of hosted zones that you can create using the current account.
+  **MAX\_REUSABLE\_DELEGATION\_SETS\_BY\_OWNER**: The maximum number of reusable delegation sets that you can create using the current account.
+  **MAX\_TRAFFIC\_POLICIES\_BY\_OWNER**: The maximum number of traffic policies that you can create using the current account.
+  **MAX\_TRAFFIC\_POLICY\_INSTANCES\_BY\_OWNER**: The maximum number of traffic policy instances that you can create using the current account. (Traffic policy instances are referred to as traffic flow policy records in the Amazon Route 53 console.)
Type: String
Valid Values: `MAX_HEALTH_CHECKS_BY_OWNER | MAX_HOSTED_ZONES_BY_OWNER | MAX_TRAFFIC_POLICY_INSTANCES_BY_OWNER | MAX_REUSABLE_DELEGATION_SETS_BY_OWNER | MAX_TRAFFIC_POLICIES_BY_OWNER`
Required: Yes

 ** Value **   <a name="Route53-Type-AccountLimit-Value"></a>
The current value for the limit that is specified by [Type](https://docs.aws.amazon.com/Route53/latest/APIReference/API_AccountLimit.html#Route53-Type-AccountLimit-Type).
Type: Long
Valid Range: Minimum value of 1.
Required: Yes

## See Also
<a name="API_AccountLimit_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53-2013-04-01/AccountLimit)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-2013-04-01/AccountLimit)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53-2013-04-01/AccountLimit)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
