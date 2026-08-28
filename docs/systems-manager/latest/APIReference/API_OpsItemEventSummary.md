---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_OpsItemEventSummary.html
---

# OpsItemEventSummary
<a name="API_OpsItemEventSummary"></a>

Summary information about an OpsItem event or that associated an OpsItem with a related item.

## Contents
<a name="API_OpsItemEventSummary_Contents"></a>

 ** CreatedBy **   <a name="systemsmanager-Type-OpsItemEventSummary-CreatedBy"></a>
Information about the user or resource that created the OpsItem event.
Type: [OpsItemIdentity](API_OpsItemIdentity.md) object
Required: No

 ** CreatedTime **   <a name="systemsmanager-Type-OpsItemEventSummary-CreatedTime"></a>
The date and time the OpsItem event was created.
Type: Timestamp
Required: No

 ** Detail **   <a name="systemsmanager-Type-OpsItemEventSummary-Detail"></a>
Specific information about the OpsItem event.
Type: String
Required: No

 ** DetailType **   <a name="systemsmanager-Type-OpsItemEventSummary-DetailType"></a>
The type of information provided as a detail.
Type: String
Required: No

 ** EventId **   <a name="systemsmanager-Type-OpsItemEventSummary-EventId"></a>
The ID of the OpsItem event.
Type: String
Required: No

 ** OpsItemId **   <a name="systemsmanager-Type-OpsItemEventSummary-OpsItemId"></a>
The ID of the OpsItem.
Type: String
Required: No

 ** Source **   <a name="systemsmanager-Type-OpsItemEventSummary-Source"></a>
The source of the OpsItem event.
Type: String
Required: No

## See Also
<a name="API_OpsItemEventSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/OpsItemEventSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/OpsItemEventSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/OpsItemEventSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
