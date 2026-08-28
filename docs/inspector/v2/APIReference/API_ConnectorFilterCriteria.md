---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_ConnectorFilterCriteria.html
---

# ConnectorFilterCriteria
<a name="API_ConnectorFilterCriteria"></a>

Contains the filter criteria for narrowing the results returned by a `ListConnectors` request. You can filter by connector ARN, AWS account ID, AWS Config connector ARN, connector type, or cloud provider.

## Contents
<a name="API_ConnectorFilterCriteria_Contents"></a>

 ** accounts **   <a name="inspector2-Type-ConnectorFilterCriteria-accounts"></a>
Filter by AWS account IDs.
Type: Array of [StringFilter](API_StringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** awsConfigConnectorArns **   <a name="inspector2-Type-ConnectorFilterCriteria-awsConfigConnectorArns"></a>
Filter by AWS Config connector ARNs.
Type: Array of [AwsConfigConnectorArnFilter](API_AwsConfigConnectorArnFilter.md) objects
Array Members: Minimum number of 0 items. Maximum number of 1 item.
Required: No

 ** connectorArns **   <a name="inspector2-Type-ConnectorFilterCriteria-connectorArns"></a>
Filter by connector ARNs.
Type: Array of [ConnectorArnFilter](API_ConnectorArnFilter.md) objects
Array Members: Minimum number of 0 items. Maximum number of 25 items.
Required: No

 ** connectorType **   <a name="inspector2-Type-ConnectorFilterCriteria-connectorType"></a>
Filter by connector type.
Type: Array of [ConnectorTypeFilter](API_ConnectorTypeFilter.md) objects
Array Members: Minimum number of 0 items. Maximum number of 1 item.
Required: No

 ** provider **   <a name="inspector2-Type-ConnectorFilterCriteria-provider"></a>
Filter by cloud provider.
Type: Array of [ProviderFilter](API_ProviderFilter.md) objects
Array Members: Minimum number of 0 items. Maximum number of 1 item.
Required: No

## See Also
<a name="API_ConnectorFilterCriteria_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/ConnectorFilterCriteria)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/ConnectorFilterCriteria)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/ConnectorFilterCriteria)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Inspector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
