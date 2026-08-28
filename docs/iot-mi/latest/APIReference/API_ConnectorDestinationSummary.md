---
source_url: https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_ConnectorDestinationSummary.html
---

# ConnectorDestinationSummary
<a name="API_ConnectorDestinationSummary"></a>

Structure containing summary information about a connector destination, which defines how a cloud-to-cloud connector connects to a customer's AWS account.

## Contents
<a name="API_ConnectorDestinationSummary_Contents"></a>

 ** CloudConnectorId **   <a name="managedintegrations-Type-ConnectorDestinationSummary-CloudConnectorId"></a>
The identifier of the cloud connector associated with this connector destination.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9-_]+`
Required: No

 ** Description **   <a name="managedintegrations-Type-ConnectorDestinationSummary-Description"></a>
A description of the connector destination.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[0-9A-Za-z_\- ]+`
Required: No

 ** Id **   <a name="managedintegrations-Type-ConnectorDestinationSummary-Id"></a>
The unique identifier of the connector destination.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9-_]+`
Required: No

 ** Name **   <a name="managedintegrations-Type-ConnectorDestinationSummary-Name"></a>
The display name of the connector destination.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[A-Za-z0-9-_ ]+`
Required: No

## See Also
<a name="API_ConnectorDestinationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-managed-integrations-2025-03-03/ConnectorDestinationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-managed-integrations-2025-03-03/ConnectorDestinationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-managed-integrations-2025-03-03/ConnectorDestinationSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Managed integrations. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-mi` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
