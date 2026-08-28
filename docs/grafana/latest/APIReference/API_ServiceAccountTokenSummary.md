---
source_url: https://docs.aws.amazon.com/grafana/latest/APIReference/API_ServiceAccountTokenSummary.html
---

# ServiceAccountTokenSummary
<a name="API_ServiceAccountTokenSummary"></a>

A structure that contains the information about a service account token.

## Contents
<a name="API_ServiceAccountTokenSummary_Contents"></a>

 ** createdAt **   <a name="ManagedGrafana-Type-ServiceAccountTokenSummary-createdAt"></a>
When the service account token was created.
Type: Timestamp
Required: Yes

 ** expiresAt **   <a name="ManagedGrafana-Type-ServiceAccountTokenSummary-expiresAt"></a>
When the service account token will expire.
Type: Timestamp
Required: Yes

 ** id **   <a name="ManagedGrafana-Type-ServiceAccountTokenSummary-id"></a>
The unique ID of the service account token.
Type: String
Required: Yes

 ** name **   <a name="ManagedGrafana-Type-ServiceAccountTokenSummary-name"></a>
The name of the service account token.
Type: String
Required: Yes

 ** lastUsedAt **   <a name="ManagedGrafana-Type-ServiceAccountTokenSummary-lastUsedAt"></a>
The last time the token was used to authorize a Grafana HTTP API.
Type: Timestamp
Required: No

## See Also
<a name="API_ServiceAccountTokenSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/grafana-2020-08-18/ServiceAccountTokenSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/grafana-2020-08-18/ServiceAccountTokenSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/grafana-2020-08-18/ServiceAccountTokenSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Grafana. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query grafana` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
