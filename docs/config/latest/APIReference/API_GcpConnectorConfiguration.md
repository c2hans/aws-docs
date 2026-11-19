---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_GcpConnectorConfiguration.html
---

# GcpConnectorConfiguration

The configuration details for connecting to Google Cloud.

## Contents
<a name="API_GcpConnectorConfiguration_Contents"></a>

 ** serviceAccountEmail **   <a name="config-Type-GcpConnectorConfiguration-serviceAccountEmail"></a>
The email address of the Google Cloud service account that AWS Config uses to access your Google Cloud resources. The format is `SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com`.
The project that contains this service account is the connector's management project. If the connector has no `gcpOrganizationId`, it can record only the management project.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^[a-z][a-z0-9\-]*@[a-z][a-z0-9\-]*[a-z0-9]\.iam\.gserviceaccount\.com$`
Required: Yes

 ** workloadIdentityPoolProvider **   <a name="config-Type-GcpConnectorConfiguration-workloadIdentityPoolProvider"></a>
The full resource name of the Google Cloud workload identity pool provider that trusts AWS Config. The format is `projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/providers/PROVIDER_ID`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `^projects/[0-9]+/locations/global/workloadIdentityPools/[^/]+/providers/[^/]+$`
Required: Yes

 ** gcpOrganizationId **   <a name="config-Type-GcpConnectorConfiguration-gcpOrganizationId"></a>
The ID of the Google Cloud organization that contains the connector's management project, which is the project of the service account in `serviceAccountEmail`.
Required if the management project belongs to an organization. A connector needs an organization ID to record an entire organization or more than one project. Omit it only if the management project doesn't belong to an organization. In that case, the connector can record only the management project.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Required: No

## See Also
<a name="API_GcpConnectorConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/GcpConnectorConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/GcpConnectorConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/GcpConnectorConfiguration)
