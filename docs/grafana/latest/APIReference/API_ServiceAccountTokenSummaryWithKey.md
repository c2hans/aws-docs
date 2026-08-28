---
source_url: https://docs.aws.amazon.com/grafana/latest/APIReference/API_ServiceAccountTokenSummaryWithKey.html
---

# ServiceAccountTokenSummaryWithKey
<a name="API_ServiceAccountTokenSummaryWithKey"></a>

A structure that contains the information about a service account token.

This structure is returned when creating the token. It is important to store the `key` that is returned, as it is not retrievable at a later time.

If you lose the key, you can delete and recreate the token, which will create a new key.

## Contents
<a name="API_ServiceAccountTokenSummaryWithKey_Contents"></a>

 ** id **   <a name="ManagedGrafana-Type-ServiceAccountTokenSummaryWithKey-id"></a>
The unique ID of the service account token.
Type: String
Required: Yes

 ** key **   <a name="ManagedGrafana-Type-ServiceAccountTokenSummaryWithKey-key"></a>
The key for the service account token. Used when making calls to the Grafana HTTP APIs to authenticate and authorize the requests.
Type: String
Required: Yes

 ** name **   <a name="ManagedGrafana-Type-ServiceAccountTokenSummaryWithKey-name"></a>
The name of the service account token.
Type: String
Required: Yes

## See Also
<a name="API_ServiceAccountTokenSummaryWithKey_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/grafana-2020-08-18/ServiceAccountTokenSummaryWithKey)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/grafana-2020-08-18/ServiceAccountTokenSummaryWithKey)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/grafana-2020-08-18/ServiceAccountTokenSummaryWithKey)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Grafana. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query grafana` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
