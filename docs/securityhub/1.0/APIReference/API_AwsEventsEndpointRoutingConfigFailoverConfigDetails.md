---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsEventsEndpointRoutingConfigFailoverConfigDetails.html
---

# AwsEventsEndpointRoutingConfigFailoverConfigDetails
<a name="API_AwsEventsEndpointRoutingConfigFailoverConfigDetails"></a>

 The failover configuration for an endpoint. This includes what triggers failover and what happens when it's triggered.

## Contents
<a name="API_AwsEventsEndpointRoutingConfigFailoverConfigDetails_Contents"></a>

 ** Primary **   <a name="securityhub-Type-AwsEventsEndpointRoutingConfigFailoverConfigDetails-Primary"></a>
 The main Region of the endpoint.
Type: [AwsEventsEndpointRoutingConfigFailoverConfigPrimaryDetails](API_AwsEventsEndpointRoutingConfigFailoverConfigPrimaryDetails.md) object
Required: No

 ** Secondary **   <a name="securityhub-Type-AwsEventsEndpointRoutingConfigFailoverConfigDetails-Secondary"></a>
 The Region that events are routed to when failover is triggered or event replication is enabled.
Type: [AwsEventsEndpointRoutingConfigFailoverConfigSecondaryDetails](API_AwsEventsEndpointRoutingConfigFailoverConfigSecondaryDetails.md) object
Required: No

## See Also
<a name="API_AwsEventsEndpointRoutingConfigFailoverConfigDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsEventsEndpointRoutingConfigFailoverConfigDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsEventsEndpointRoutingConfigFailoverConfigDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsEventsEndpointRoutingConfigFailoverConfigDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
