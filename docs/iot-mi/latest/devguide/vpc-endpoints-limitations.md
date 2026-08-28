---
source_url: https://docs.aws.amazon.com/iot-mi/latest/devguide/vpc-endpoints-limitations.html
---

# Limitations
<a name="vpc-endpoints-limitations"></a>
+  The [CreateAccountAssociation](https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_CreateAccountAssociation.html) API, is designed to perform OAuth with third-party cloud services, which requires the request to leave the Amazon network. This is important for customers using AWS PrivateLink to contain their traffic within the VPC, as AWS PrivateLink cannot provide complete end-to-end containment for this API call.
+ VPC endpoints for AWS IoT Managed Integrations are not available in AWS GovCloud (US) Regions.

For general VPC endpoint limitations, see [ Interface endpoint properties and limitations](https://docs.aws.amazon.com/vpc/latest/privatelink/vpce-interface.html#vpce-interface-limitations) in the *Amazon VPC User Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Managed integrations. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-mi` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
