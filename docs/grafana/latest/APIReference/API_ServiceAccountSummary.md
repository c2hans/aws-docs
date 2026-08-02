---
source_url: https://docs.aws.amazon.com/grafana/latest/APIReference/API_ServiceAccountSummary.html
---

# ServiceAccountSummary
<a name="API_ServiceAccountSummary"></a>

A structure that contains the information about one service account.

## Contents
<a name="API_ServiceAccountSummary_Contents"></a>

 ** grafanaRole **   <a name="ManagedGrafana-Type-ServiceAccountSummary-grafanaRole"></a>
The role of the service account, which sets the permission level used when calling Grafana APIs.
Type: String
Valid Values: `ADMIN | EDITOR | VIEWER`
Required: Yes

 ** id **   <a name="ManagedGrafana-Type-ServiceAccountSummary-id"></a>
The unique ID of the service account.
Type: String
Required: Yes

 ** isDisabled **   <a name="ManagedGrafana-Type-ServiceAccountSummary-isDisabled"></a>
Returns true if the service account is disabled. Service accounts can be disabled and enabled in the Amazon Managed Grafana console.
Type: String
Required: Yes

 ** name **   <a name="ManagedGrafana-Type-ServiceAccountSummary-name"></a>
The name of the service account.
Type: String
Required: Yes

## See Also
<a name="API_ServiceAccountSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/grafana-2020-08-18/ServiceAccountSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/grafana-2020-08-18/ServiceAccountSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/grafana-2020-08-18/ServiceAccountSummary)
