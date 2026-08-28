---
source_url: https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_CustomerMeCollectorInfo.html
---

# CustomerMeCollectorInfo
<a name="API_CustomerMeCollectorInfo"></a>

**Important**
 AWS Application Discovery Service is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Application Discovery Service availability change](https://docs.aws.amazon.com/application-discovery/latest/userguide/application-discovery-service-availability-change.html).

 The inventory data for installed Migration Evaluator collectors.

## Contents
<a name="API_CustomerMeCollectorInfo_Contents"></a>

 ** activeMeCollectors **   <a name="DiscServ-Type-CustomerMeCollectorInfo-activeMeCollectors"></a>
 The number of active Migration Evaluator collectors.
Type: Integer
Required: Yes

 ** denyListedMeCollectors **   <a name="DiscServ-Type-CustomerMeCollectorInfo-denyListedMeCollectors"></a>
 The number of deny-listed Migration Evaluator collectors.
Type: Integer
Required: Yes

 ** healthyMeCollectors **   <a name="DiscServ-Type-CustomerMeCollectorInfo-healthyMeCollectors"></a>
 The number of healthy Migration Evaluator collectors.
Type: Integer
Required: Yes

 ** shutdownMeCollectors **   <a name="DiscServ-Type-CustomerMeCollectorInfo-shutdownMeCollectors"></a>
 The number of Migration Evaluator collectors with `SHUTDOWN` status.
Type: Integer
Required: Yes

 ** totalMeCollectors **   <a name="DiscServ-Type-CustomerMeCollectorInfo-totalMeCollectors"></a>
 The total number of Migration Evaluator collectors.
Type: Integer
Required: Yes

 ** unhealthyMeCollectors **   <a name="DiscServ-Type-CustomerMeCollectorInfo-unhealthyMeCollectors"></a>
 The number of unhealthy Migration Evaluator collectors.
Type: Integer
Required: Yes

 ** unknownMeCollectors **   <a name="DiscServ-Type-CustomerMeCollectorInfo-unknownMeCollectors"></a>
 The number of unknown Migration Evaluator collectors.
Type: Integer
Required: Yes

## See Also
<a name="API_CustomerMeCollectorInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/discovery-2015-11-01/CustomerMeCollectorInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/discovery-2015-11-01/CustomerMeCollectorInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/discovery-2015-11-01/CustomerMeCollectorInfo)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Application Discovery Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query application-discovery` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
