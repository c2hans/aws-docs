---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_CollectionFilters.html
---

# CollectionFilters
<a name="API_CollectionFilters"></a>

A list of filter keys that you can use for LIST, UPDATE, and DELETE requests to OpenSearch Serverless collections.

## Contents
<a name="API_CollectionFilters_Contents"></a>

 ** collectionGroupName **   <a name="opensearchserverless-Type-CollectionFilters-collectionGroupName"></a>
The name of the collection group to filter by.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 32.
Pattern: `[a-z][a-z0-9-]+`
Required: No

 ** name **   <a name="opensearchserverless-Type-CollectionFilters-name"></a>
The name of the collection.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 64.
Pattern: `[a-z][a-z0-9-]+`
Required: No

 ** status **   <a name="opensearchserverless-Type-CollectionFilters-status"></a>
The current status of the collection.
Type: String
Valid Values: `CREATING | UPDATING | DELETING | ACTIVE | FAILED | UPDATE_FAILED`
Required: No

## See Also
<a name="API_CollectionFilters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearchserverless-2021-11-01/CollectionFilters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearchserverless-2021-11-01/CollectionFilters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearchserverless-2021-11-01/CollectionFilters)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Serverless. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
