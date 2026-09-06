---
source_url: https://docs.aws.amazon.com/appflow/1.0/APIReference/API_FlowDefinition.html
---

# FlowDefinition
<a name="API_FlowDefinition"></a>

 The properties of the flow, such as its source, destination, trigger type, and so on.

## Contents
<a name="API_FlowDefinition_Contents"></a>

 ** createdAt **   <a name="appflow-Type-FlowDefinition-createdAt"></a>
 Specifies when the flow was created.
Type: Timestamp
Required: No

 ** createdBy **   <a name="appflow-Type-FlowDefinition-createdBy"></a>
 The ARN of the user who created the flow.
Type: String
Length Constraints: Maximum length of 256.
Pattern: `\S+`
Required: No

 ** description **   <a name="appflow-Type-FlowDefinition-description"></a>
 A user-entered description of the flow.
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `[\w!@#\-.?,\s]*`
Required: No

 ** destinationConnectorLabel **   <a name="appflow-Type-FlowDefinition-destinationConnectorLabel"></a>
The label of the destination connector in the flow.
Type: String
Length Constraints: Maximum length of 256.
Pattern: `[a-zA-Z0-9][\w!@#.-]+`
Required: No

 ** destinationConnectorType **   <a name="appflow-Type-FlowDefinition-destinationConnectorType"></a>
 Specifies the destination connector type, such as Salesforce, Amazon S3, Amplitude, and so on.
Type: String
Valid Values: `Salesforce | Singular | Slack | Redshift | S3 | Marketo | Googleanalytics | Zendesk | Servicenow | Datadog | Trendmicro | Snowflake | Dynatrace | Infornexus | Amplitude | Veeva | EventBridge | LookoutMetrics | Upsolver | Honeycode | CustomerProfiles | SAPOData | CustomConnector | Pardot`
Required: No

 ** flowArn **   <a name="appflow-Type-FlowDefinition-flowArn"></a>
 The flow's Amazon Resource Name (ARN).
Type: String
Length Constraints: Maximum length of 512.
Pattern: `arn:aws:appflow:.*:[0-9]+:.*`
Required: No

 ** flowName **   <a name="appflow-Type-FlowDefinition-flowName"></a>
 The specified name of the flow. Spaces are not allowed. Use underscores (\_) or hyphens (-) only.
Type: String
Length Constraints: Maximum length of 256.
Pattern: `[a-zA-Z0-9][\w!@#.-]+`
Required: No

 ** flowStatus **   <a name="appflow-Type-FlowDefinition-flowStatus"></a>
 Indicates the current status of the flow.
Type: String
Valid Values: `Active | Deprecated | Deleted | Draft | Errored | Suspended`
Required: No

 ** lastRunExecutionDetails **   <a name="appflow-Type-FlowDefinition-lastRunExecutionDetails"></a>
 Describes the details of the most recent flow run.
Type: [ExecutionDetails](API_ExecutionDetails.md) object
Required: No

 ** lastUpdatedAt **   <a name="appflow-Type-FlowDefinition-lastUpdatedAt"></a>
 Specifies when the flow was last updated.
Type: Timestamp
Required: No

 ** lastUpdatedBy **   <a name="appflow-Type-FlowDefinition-lastUpdatedBy"></a>
 Specifies the account user name that most recently updated the flow.
Type: String
Length Constraints: Maximum length of 256.
Pattern: `\S+`
Required: No

 ** sourceConnectorLabel **   <a name="appflow-Type-FlowDefinition-sourceConnectorLabel"></a>
The label of the source connector in the flow.
Type: String
Length Constraints: Maximum length of 256.
Pattern: `[a-zA-Z0-9][\w!@#.-]+`
Required: No

 ** sourceConnectorType **   <a name="appflow-Type-FlowDefinition-sourceConnectorType"></a>
 Specifies the source connector type, such as Salesforce, Amazon S3, Amplitude, and so on.
Type: String
Valid Values: `Salesforce | Singular | Slack | Redshift | S3 | Marketo | Googleanalytics | Zendesk | Servicenow | Datadog | Trendmicro | Snowflake | Dynatrace | Infornexus | Amplitude | Veeva | EventBridge | LookoutMetrics | Upsolver | Honeycode | CustomerProfiles | SAPOData | CustomConnector | Pardot`
Required: No

 ** tags **   <a name="appflow-Type-FlowDefinition-tags"></a>
 The tags used to organize, track, or control access for your flow.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[a-zA-Z+-=._:/]+$`
Value Length Constraints: Maximum length of 256.
Value Pattern: `[\s\w+-=\.:/@]*`
Required: No

 ** triggerType **   <a name="appflow-Type-FlowDefinition-triggerType"></a>
 Specifies the type of flow trigger. This can be `OnDemand`, `Scheduled`, or `Event`.
Type: String
Valid Values: `Scheduled | Event | OnDemand`
Required: No

## See Also
<a name="API_FlowDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appflow-2020-08-23/FlowDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appflow-2020-08-23/FlowDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appflow-2020-08-23/FlowDefinition)
