---
source_url: https://docs.aws.amazon.com/prometheus/latest/APIReference/API_AlertManagerDefinitionDescription.html
---

# AlertManagerDefinitionDescription
<a name="API_AlertManagerDefinitionDescription"></a>

The details of an alert manager definition. It is the configuration for the alert manager, including information about receivers for routing alerts.

## Contents
<a name="API_AlertManagerDefinitionDescription_Contents"></a>

 ** createdAt **   <a name="prometheus-Type-AlertManagerDefinitionDescription-createdAt"></a>
The date and time that the alert manager definition was created.
Type: Timestamp
Required: Yes

 ** data **   <a name="prometheus-Type-AlertManagerDefinitionDescription-data"></a>
The actual alert manager definition.
For details about the alert manager definition, see [AlertManagedDefinitionData](https://docs.aws.amazon.com/prometheus/latest/APIReference/yaml-AlertManagerDefinitionData.html).
Type: Base64-encoded binary data object
Required: Yes

 ** modifiedAt **   <a name="prometheus-Type-AlertManagerDefinitionDescription-modifiedAt"></a>
The date and time that the alert manager definition was most recently changed.
Type: Timestamp
Required: Yes

 ** status **   <a name="prometheus-Type-AlertManagerDefinitionDescription-status"></a>
A structure that displays the current status of the alert manager definition..
Type: [AlertManagerDefinitionStatus](API_AlertManagerDefinitionStatus.md) object
Required: Yes

## See Also
<a name="API_AlertManagerDefinitionDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amp-2020-08-01/AlertManagerDefinitionDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amp-2020-08-01/AlertManagerDefinitionDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amp-2020-08-01/AlertManagerDefinitionDescription)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Service for Prometheus. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prometheus` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
