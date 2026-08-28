---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_ElasticsearchAction.html
---

# ElasticsearchAction
<a name="API_ElasticsearchAction"></a>

Describes an action that writes data to an Amazon OpenSearch Service domain.

**Note**
The `Elasticsearch` action can only be used by existing rule actions. To create a new rule action or to update an existing rule action, use the `OpenSearch` rule action instead. For more information, see [OpenSearchAction](https://docs.aws.amazon.com/iot/latest/apireference/API_OpenSearchAction.html).

## Contents
<a name="API_ElasticsearchAction_Contents"></a>

 ** endpoint **   <a name="iot-Type-ElasticsearchAction-endpoint"></a>
The endpoint of your OpenSearch domain.
Type: String
Pattern: `https?://.*`
Required: Yes

 ** id **   <a name="iot-Type-ElasticsearchAction-id"></a>
The unique identifier for the document you are storing.
Type: String
Required: Yes

 ** index **   <a name="iot-Type-ElasticsearchAction-index"></a>
The index where you want to store your data.
Type: String
Required: Yes

 ** roleArn **   <a name="iot-Type-ElasticsearchAction-roleArn"></a>
The IAM role ARN that has access to OpenSearch.
Type: String
Required: Yes

 ** type **   <a name="iot-Type-ElasticsearchAction-type"></a>
The type of document you are storing.
Type: String
Required: Yes

## See Also
<a name="API_ElasticsearchAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/ElasticsearchAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/ElasticsearchAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/ElasticsearchAction)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
