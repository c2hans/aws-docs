---
source_url: https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-multicloud-packages.html
---

# Azure and Google Cloud SDK packages

The Azure and Google Cloud actions, and `aws:executeScript` scripts, call the cloud with its SDK for Python. The `Package` input chooses which package of SDK libraries, and so which library versions, to use. Automation provides the following packages. For runbooks that use a package in an API action or a script, see [Create runbooks that call Azure and Google Cloud APIs](automation-multicloud-runbooks.md).

| Package | Contents | Use with | Runtimes for `aws:executeScript` |
| --- | --- | --- | --- |
| azure\_202610 | Azure SDK for Python management libraries (azure.mgmt.\*), some data-plane client libraries, azure.core, and azure.identity. The connector's token works only with the management libraries. | aws:executeAzureApi, aws:assertAzureResourceProperty, aws:waitForAzureResourceProperty, and aws:executeScript | python3.10, python3.11, and python3.12 |
| gcp\_202610 | Google Cloud client libraries for Python (google.cloud.\*), the Google API discovery client (googleapiclient), and google.auth. | aws:executeGcpApi, aws:assertGcpResourceProperty, aws:waitForGcpResourceProperty, and aws:executeScript | python3.10, python3.11, and python3.12 |

Keep the following in mind when you use the packages:
+ The Azure actions accept only an Azure package, and the Google Cloud actions accept only a Google Cloud package. If you specify another package, Automation rejects the runbook when you create it. If the package comes from a parameter, the step fails when it runs.
+ In `aws:executeScript`, the packages aren't currently supported with the PowerShell runtime. For more information, see [Use the Azure and Google Cloud SDKs in a script](automation-multicloud-runbooks.md#automation-multicloud-runbooks-sdk).
+ The package name includes the year and month it was introduced. Within a package, Automation can update a library to a newer minor or patch version, but not to a new major version. A new major version comes in a new package. For a library with a 0.x version, the table shows the minor version (for example, `0.16.x`), and Automation updates only its patch version. Each package has its own list of libraries and major versions in the following sections.
+ The API actions can call a service only if its library is in the package. For example, `Service: compute` uses `azure-mgmt-compute` in the Azure package and `google-cloud-compute` in the Google Cloud package. Not every library in the package can be used as a `Service`. The package also fixes each service's API version, so a REST API reference page for a newer API version can show parameters that the package doesn't accept. For more information about the libraries in each package, see the following sections.
+ `azure.identity` is included because other libraries depend on it. Its credential classes can't get a token in a step. To authenticate, use the connector's token, as shown in [Use the Azure and Google Cloud SDKs in a script](automation-multicloud-runbooks.md#automation-multicloud-runbooks-sdk).
+ In `aws:executeScript`, a package adds about 60 MB to 96 MB (compressed) to the script's runtime and uses part of its disk space. The first step that uses a package can take longer to start while Automation downloads the package.
+ A package also contains the libraries' dependencies, such as `requests`, `msal`, `protobuf`, and `grpcio`. Their versions can change within a package, so don't rely on them directly.

## Azure package libraries
<a name="automation-multicloud-packages-azure"></a>

### `azure_202610` libraries
<a name="automation-multicloud-packages-azure-202610"></a>

The following libraries in the `azure_202610` package are supported. Use this list to check that a library your script imports, or the library behind the `Service` that an API action calls, is supported, and which major version you get.

| Library | Major version |
| --- | --- |
| azure-appconfiguration | 1.x |
| azure-batch | 15.x |
| azure-core | 1.x |
| azure-cosmos | 4.x |
| azure-data-tables | 12.x |
| azure-eventhub | 5.x |
| azure-identity | 1.x |
| azure-keyvault-certificates | 4.x |
| azure-keyvault-keys | 4.x |
| azure-keyvault-secrets | 4.x |
| azure-mgmt-advisor | 9.x |
| azure-mgmt-alertsmanagement | 1.x |
| azure-mgmt-apimanagement | 5.x |
| azure-mgmt-appconfiguration | 5.x |
| azure-mgmt-applicationinsights | 4.x |
| azure-mgmt-attestation | 2.x |
| azure-mgmt-authorization | 4.x |
| azure-mgmt-azurearcdata | 1.x |
| azure-mgmt-batch | 19.x |
| azure-mgmt-billing | 8.x |
| azure-mgmt-cdn | 14.x |
| azure-mgmt-chaos | 2.x |
| azure-mgmt-cognitiveservices | 14.x |
| azure-mgmt-commerce | 6.x |
| azure-mgmt-communication | 3.x |
| azure-mgmt-compute | 38.x |
| azure-mgmt-confluent | 2.x |
| azure-mgmt-consumption | 11.x |
| azure-mgmt-containerinstance | 10.x |
| azure-mgmt-containerregistry | 15.x |
| azure-mgmt-core | 1.x |
| azure-mgmt-cosmosdb | 10.x |
| azure-mgmt-dashboard | 2.x |
| azure-mgmt-databox | 4.x |
| azure-mgmt-databricks | 3.x |
| azure-mgmt-datafactory | 10.x |
| azure-mgmt-datamigration | 10.x |
| azure-mgmt-datashare | 1.x |
| azure-mgmt-digitaltwins | 7.x |
| azure-mgmt-dns | 9.x |
| azure-mgmt-dnsresolver | 1.x |
| azure-mgmt-edgeorder | 3.x |
| azure-mgmt-eventgrid | 10.x |
| azure-mgmt-eventhub | 12.x |
| azure-mgmt-fluidrelay | 1.x |
| azure-mgmt-frontdoor | 2.x |
| azure-mgmt-hdinsight | 9.x |
| azure-mgmt-healthcareapis | 2.x |
| azure-mgmt-hybridcompute | 10.x |
| azure-mgmt-hybridnetwork | 2.x |
| azure-mgmt-keyvault | 14.x |
| azure-mgmt-kusto | 4.x |
| azure-mgmt-loganalytics | 14.x |
| azure-mgmt-logic | 10.x |
| azure-mgmt-maintenance | 2.x |
| azure-mgmt-maps | 2.x |
| azure-mgmt-monitor | 7.x |
| azure-mgmt-mysqlflexibleservers | 1.x |
| azure-mgmt-netapp | 17.x |
| azure-mgmt-network | 33.x |
| azure-mgmt-nginx | 4.x |
| azure-mgmt-notificationhubs | 8.x |
| azure-mgmt-operationsmanagement | 1.x |
| azure-mgmt-peering | 2.x |
| azure-mgmt-postgresqlflexibleservers | 2.x |
| azure-mgmt-privatedns | 2.x |
| azure-mgmt-purview | 1.x |
| azure-mgmt-recoveryservicessiterecovery | 2.x |
| azure-mgmt-redis | 14.x |
| azure-mgmt-redisenterprise | 3.x |
| azure-mgmt-resource | 26.x |
| azure-mgmt-search | 9.x |
| azure-mgmt-servicebus | 10.x |
| azure-mgmt-servicefabric | 2.x |
| azure-mgmt-servicefabricmanagedclusters | 3.x |
| azure-mgmt-signalr | 1.x |
| azure-mgmt-sql | 4.x |
| azure-mgmt-sqlvirtualmachine | 1.x |
| azure-mgmt-storage | 25.x |
| azure-mgmt-storagecache | 4.x |
| azure-mgmt-streamanalytics | 1.x |
| azure-mgmt-synapse | 2.x |
| azure-mgmt-trafficmanager | 2.x |
| azure-mgmt-web | 11.x |
| azure-mgmt-webpubsub | 2.x |
| azure-monitor-opentelemetry | 1.x |
| azure-monitor-query | 2.x |
| azure-search-documents | 12.x |
| azure-servicebus | 7.x |
| azure-storage-blob | 12.x |
| azure-storage-file-datalake | 12.x |
| azure-storage-file-share | 12.x |
| azure-storage-queue | 12.x |
| azure-synapse-artifacts | 0.22.x |
| azure-synapse-spark | 0.7.x |

## Google Cloud package libraries
<a name="automation-multicloud-packages-gcp"></a>

### `gcp_202610` libraries
<a name="automation-multicloud-packages-gcp-202610"></a>

The following libraries in the `gcp_202610` package are supported. Use this list to check that a library your script imports, or the library behind the `Service` that an API action calls, is supported, and which major version you get.

| Library | Major version |
| --- | --- |
| google-api-core | 2.x |
| google-api-python-client | 2.x |
| google-auth | 2.x |
| google-auth-httplib2 | 0.4.x |
| google-auth-oauthlib | 1.x |
| google-cloud-access-approval | 1.x |
| google-cloud-advisorynotifications | 0.7.x |
| google-cloud-alloydb | 0.11.x |
| google-cloud-api-gateway | 1.x |
| google-cloud-api-keys | 0.9.x |
| google-cloud-apigee-connect | 1.x |
| google-cloud-apihub | 0.7.x |
| google-cloud-apiregistry | 0.3.x |
| google-cloud-apphub | 0.5.x |
| google-cloud-appoptimize | 0.2.x |
| google-cloud-artifact-registry | 1.x |
| google-cloud-asset | 4.x |
| google-cloud-auditmanager | 0.3.x |
| google-cloud-backupdr | 0.10.x |
| google-cloud-bare-metal-solution | 1.x |
| google-cloud-batch | 0.22.x |
| google-cloud-beyondcorp-appconnections | 0.8.x |
| google-cloud-beyondcorp-appconnectors | 0.8.x |
| google-cloud-beyondcorp-appgateways | 0.8.x |
| google-cloud-biglake | 0.5.x |
| google-cloud-biglake-hive | 0.3.x |
| google-cloud-bigquery-analyticshub | 0.9.x |
| google-cloud-bigquery-biglake | 0.8.x |
| google-cloud-bigquery-connection | 1.x |
| google-cloud-bigquery-data-exchange | 0.9.x |
| google-cloud-bigquery-datapolicies | 0.10.x |
| google-cloud-bigquery-datatransfer | 3.x |
| google-cloud-bigquery-migration | 0.15.x |
| google-cloud-bigquery-reservation | 1.x |
| google-cloud-billing | 1.x |
| google-cloud-binary-authorization | 1.x |
| google-cloud-capacityplanner | 0.5.x |
| google-cloud-certificate-manager | 1.x |
| google-cloud-cloudsecuritycompliance | 0.8.x |
| google-cloud-compute | 1.x |
| google-cloud-confidentialcomputing | 0.11.x |
| google-cloud-config | 0.7.x |
| google-cloud-configdelivery | 0.5.x |
| google-cloud-container | 2.x |
| google-cloud-core | 2.x |
| google-cloud-data-fusion | 1.x |
| google-cloud-databasecenter | 0.9.x |
| google-cloud-datacatalog | 3.x |
| google-cloud-datacatalog-lineage | 0.7.x |
| google-cloud-datacatalog-lineage-configmanagement | 0.3.x |
| google-cloud-dataform | 0.11.x |
| google-cloud-dataplex | 2.x |
| google-cloud-dataproc | 5.x |
| google-cloud-dataproc-metastore | 1.x |
| google-cloud-datastream | 1.x |
| google-cloud-deploy | 2.x |
| google-cloud-developerconnect | 0.6.x |
| google-cloud-dlp | 3.x |
| google-cloud-dms | 1.x |
| google-cloud-dns | 0.37.x |
| google-cloud-domains | 1.x |
| google-cloud-edgecontainer | 0.8.x |
| google-cloud-edgenetwork | 0.5.x |
| google-cloud-essential-contacts | 1.x |
| google-cloud-eventarc | 1.x |
| google-cloud-filestore | 1.x |
| google-cloud-financialservices | 0.4.x |
| google-cloud-firestore | 2.x |
| google-cloud-functions | 1.x |
| google-cloud-gdchardwaremanagement | 0.5.x |
| google-cloud-gke-backup | 0.8.x |
| google-cloud-gke-hub | 1.x |
| google-cloud-hypercomputecluster | 0.4.x |
| google-cloud-iam | 2.x |
| google-cloud-iap | 1.x |
| google-cloud-kms | 3.x |
| google-cloud-kms-inventory | 0.6.x |
| google-cloud-licensemanager | 0.4.x |
| google-cloud-locationfinder | 0.4.x |
| google-cloud-lustre | 0.4.x |
| google-cloud-managed-identities | 1.x |
| google-cloud-managedkafka | 0.4.x |
| google-cloud-managedkafka-schemaregistry | 0.4.x |
| google-cloud-memcache | 1.x |
| google-cloud-memorystore | 0.5.x |
| google-cloud-migrationcenter | 0.4.x |
| google-cloud-modelarmor | 0.7.x |
| google-cloud-monitoring | 2.x |
| google-cloud-monitoring-dashboards | 3.x |
| google-cloud-netapp | 0.10.x |
| google-cloud-network-connectivity | 2.x |
| google-cloud-network-management | 1.x |
| google-cloud-network-security | 0.13.x |
| google-cloud-network-services | 0.10.x |
| google-cloud-notebooks | 1.x |
| google-cloud-oracledatabase | 0.6.x |
| google-cloud-org-policy | 1.x |
| google-cloud-os-config | 1.x |
| google-cloud-parallelstore | 0.6.x |
| google-cloud-parametermanager | 0.4.x |
| google-cloud-policysimulator | 0.4.x |
| google-cloud-private-catalog | 0.12.x |
| google-cloud-privilegedaccessmanager | 0.4.x |
| google-cloud-pubsub | 2.x |
| google-cloud-quotas | 0.6.x |
| google-cloud-recaptcha-enterprise | 1.x |
| google-cloud-recommender | 2.x |
| google-cloud-redis | 2.x |
| google-cloud-redis-cluster | 0.5.x |
| google-cloud-resource-manager | 1.x |
| google-cloud-run | 0.16.x |
| google-cloud-saasplatform-saasservicemgmt | 0.7.x |
| google-cloud-scheduler | 2.x |
| google-cloud-secret-manager | 2.x |
| google-cloud-securesourcemanager | 0.6.x |
| google-cloud-securitycenter | 1.x |
| google-cloud-securitycentermanagement | 0.5.x |
| google-cloud-service-directory | 1.x |
| google-cloud-service-usage | 1.x |
| google-cloud-servicehealth | 0.5.x |
| google-cloud-spanner | 3.x |
| google-cloud-storage | 3.x |
| google-cloud-storage-control | 1.x |
| google-cloud-storage-transfer | 1.x |
| google-cloud-storagebatchoperations | 0.8.x |
| google-cloud-storageinsights | 0.5.x |
| google-cloud-support | 0.5.x |
| google-cloud-tasks | 2.x |
| google-cloud-tpu | 1.x |
| google-cloud-trace | 1.x |
| google-cloud-vm-migration | 1.x |
| google-cloud-vmwareengine | 1.x |
| google-cloud-vpc-access | 1.x |
| google-cloud-websecurityscanner | 1.x |
| google-cloud-workflows | 1.x |
| google-cloud-workloadmanager | 0.2.x |
| google-cloud-workstations | 0.8.x |
| google-crc32c | 1.x |
| google-resumable-media | 2.x |
| googleapis-common-protos | 1.x |
| grafeas | 1.x |
| grpc-google-iam-v1 | 0.14.x |
| proto-plus | 1.x |

## Related topics
<a name="automation-multicloud-packages-related"></a>

For more information about using these packages, see the following topics:
+ [Use the Azure and Google Cloud SDKs in a script](automation-multicloud-runbooks.md#automation-multicloud-runbooks-sdk)
+ [`aws:executeAzureApi` – Call and run Azure API operations](automation-action-executeAzureApi.md)
+ [`aws:executeGcpApi` – Call and run Google Cloud API operations](automation-action-executeGcpApi.md)
