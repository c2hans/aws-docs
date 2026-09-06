---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_ApplicationSummary.html
---

# ApplicationSummary
<a name="API_ApplicationSummary"></a>

Basic details of an OpenSearch application.

## Contents
<a name="API_ApplicationSummary_Contents"></a>

 ** arn **   <a name="opensearchservice-Type-ApplicationSummary-arn"></a>
The Amazon Resource Name (ARN) of the domain. See [Identifiers for IAM Entities ](https://docs.aws.amazon.com/IAM/latest/UserGuide/index.html) in *Using AWS Identity and Access Management* for more information.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `.*`
Required: No

 ** createdAt **   <a name="opensearchservice-Type-ApplicationSummary-createdAt"></a>
The timestamp when an OpenSearch application was created.
Type: Timestamp
Required: No

 ** endpoint **   <a name="opensearchservice-Type-ApplicationSummary-endpoint"></a>
The endpoint URL of an OpenSearch application.
Type: String
Required: No

 ** id **   <a name="opensearchservice-Type-ApplicationSummary-id"></a>
The unique identifier of an OpenSearch application.
Type: String
Pattern: `[a-z0-9]{3,30}`
Required: No

 ** lastUpdatedAt **   <a name="opensearchservice-Type-ApplicationSummary-lastUpdatedAt"></a>
The timestamp of the last update to an OpenSearch application.
Type: Timestamp
Required: No

 ** name **   <a name="opensearchservice-Type-ApplicationSummary-name"></a>
The name of an OpenSearch application.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 30.
Pattern: `[a-z][a-z0-9\-]+`
Required: No

 ** status **   <a name="opensearchservice-Type-ApplicationSummary-status"></a>
The current status of an OpenSearch application. Possible values: `CREATING`, `UPDATING`, `DELETING`, `FAILED`, `ACTIVE`, and `DELETED`.
Type: String
Valid Values: `CREATING | UPDATING | DELETING | ACTIVE | FAILED`
Required: No

## See Also
<a name="API_ApplicationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/ApplicationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/ApplicationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/ApplicationSummary)
