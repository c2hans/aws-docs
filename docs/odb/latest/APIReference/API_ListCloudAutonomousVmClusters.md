---
source_url: https://docs.aws.amazon.com/odb/latest/APIReference/API_ListCloudAutonomousVmClusters.html
---

# ListCloudAutonomousVmClusters
<a name="API_ListCloudAutonomousVmClusters"></a>

Lists all Autonomous VM clusters in a specified Cloud Exadata infrastructure.

## Request Syntax
<a name="API_ListCloudAutonomousVmClusters_RequestSyntax"></a>

```
{
   "cloudExadataInfrastructureId": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListCloudAutonomousVmClusters_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [cloudExadataInfrastructureId](#API_ListCloudAutonomousVmClusters_RequestSyntax) **   <a name="odb-ListCloudAutonomousVmClusters-request-cloudExadataInfrastructureId"></a>
The unique identifier of the Cloud Exadata Infrastructure that hosts the Autonomous VM clusters to be listed.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 2048.
Pattern: `(arn:(?:aws|aws-cn|aws-us-gov|aws-iso-{0,1}[a-z]{0,1}):[a-z0-9-]+:[a-z0-9-]*:[0-9]+:[a-z0-9-]+/[a-zA-Z0-9_~.-]{6,64}|[a-zA-Z0-9_~.-]{6,64})`
Required: No

 ** [maxResults](#API_ListCloudAutonomousVmClusters_RequestSyntax) **   <a name="odb-ListCloudAutonomousVmClusters-request-maxResults"></a>
The maximum number of items to return per page.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [nextToken](#API_ListCloudAutonomousVmClusters_RequestSyntax) **   <a name="odb-ListCloudAutonomousVmClusters-request-nextToken"></a>
The pagination token to continue listing from.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.
Required: No

## Response Syntax
<a name="API_ListCloudAutonomousVmClusters_ResponseSyntax"></a>

```
{
   "cloudAutonomousVmClusters": [
      {
         "autonomousDataStoragePercentage": number,
         "autonomousDataStorageSizeInTBs": number,
         "availableAutonomousDataStorageSizeInTBs": number,
         "availableContainerDatabases": number,
         "availableCpus": number,
         "cloudAutonomousVmClusterArn": "string",
         "cloudAutonomousVmClusterId": "string",
         "cloudExadataInfrastructureArn": "string",
         "cloudExadataInfrastructureId": "string",
         "computeModel": "string",
         "cpuCoreCount": number,
         "cpuCoreCountPerNode": number,
         "cpuPercentage": number,
         "createdAt": "string",
         "dataStorageSizeInGBs": number,
         "dataStorageSizeInTBs": number,
         "dbNodeStorageSizeInGBs": number,
         "dbServers": [ "string" ],
         "description": "string",
         "displayName": "string",
         "domain": "string",
         "exadataStorageInTBsLowestScaledValue": number,
         "hostname": "string",
         "iamRoles": [
            {
               "awsIntegration": "string",
               "iamRoleArn": "string",
               "status": "string",
               "statusReason": "string"
            }
         ],
         "isMtlsEnabledVmCluster": boolean,
         "licenseModel": "string",
         "maintenanceWindow": {
            "customActionTimeoutInMins": number,
            "daysOfWeek": [
               {
                  "name": "string"
               }
            ],
            "hoursOfDay": [ number ],
            "isCustomActionTimeoutEnabled": boolean,
            "leadTimeInWeeks": number,
            "months": [
               {
                  "name": "string"
               }
            ],
            "patchingMode": "string",
            "preference": "string",
            "skipRu": boolean,
            "weeksOfMonth": [ number ]
         },
         "maxAcdsLowestScaledValue": number,
         "memoryPerOracleComputeUnitInGBs": number,
         "memorySizeInGBs": number,
         "nodeCount": number,
         "nonProvisionableAutonomousContainerDatabases": number,
         "ocid": "string",
         "ociResourceAnchorName": "string",
         "ociUrl": "string",
         "odbNetworkArn": "string",
         "odbNetworkId": "string",
         "percentProgress": number,
         "provisionableAutonomousContainerDatabases": number,
         "provisionedAutonomousContainerDatabases": number,
         "provisionedCpus": number,
         "reclaimableCpus": number,
         "reservedCpus": number,
         "scanListenerPortNonTls": number,
         "scanListenerPortTls": number,
         "shape": "string",
         "status": "string",
         "statusReason": "string",
         "timeDatabaseSslCertificateExpires": "string",
         "timeOrdsCertificateExpires": "string",
         "timeZone": "string",
         "totalContainerDatabases": number
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListCloudAutonomousVmClusters_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [cloudAutonomousVmClusters](#API_ListCloudAutonomousVmClusters_ResponseSyntax) **   <a name="odb-ListCloudAutonomousVmClusters-response-cloudAutonomousVmClusters"></a>
The list of Autonomous VM clusters in the specified Cloud Exadata Infrastructure.
Type: Array of [CloudAutonomousVmClusterSummary](API_CloudAutonomousVmClusterSummary.md) objects

 ** [nextToken](#API_ListCloudAutonomousVmClusters_ResponseSyntax) **   <a name="odb-ListCloudAutonomousVmClusters-response-nextToken"></a>
The pagination token to continue listing from.
Type: String

## Errors
<a name="API_ListCloudAutonomousVmClusters_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.
HTTP Status Code: 400

 ** InternalServerException **
Occurs when there is an internal failure in the Oracle Database@AWS service. Wait and try again.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request after an internal server error.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.
 ** resourceId **
The identifier of the resource that was not found.
 ** resourceType **
The type of resource that was not found.
HTTP Status Code: 400

 ** ThrottlingException **
The request was denied due to request throttling.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request after being throttled.
HTTP Status Code: 400

 ** ValidationException **
The request has failed validation because it is missing required fields or has invalid inputs.
 ** fieldList **
A list of fields that failed validation.
 ** reason **
The reason why the validation failed.
HTTP Status Code: 400

## See Also
<a name="API_ListCloudAutonomousVmClusters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/odb-2024-08-20/ListCloudAutonomousVmClusters)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/odb-2024-08-20/ListCloudAutonomousVmClusters)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/odb-2024-08-20/ListCloudAutonomousVmClusters)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/odb-2024-08-20/ListCloudAutonomousVmClusters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/odb-2024-08-20/ListCloudAutonomousVmClusters)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/odb-2024-08-20/ListCloudAutonomousVmClusters)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/odb-2024-08-20/ListCloudAutonomousVmClusters)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/odb-2024-08-20/ListCloudAutonomousVmClusters)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/odb-2024-08-20/ListCloudAutonomousVmClusters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/odb-2024-08-20/ListCloudAutonomousVmClusters)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Oracle Database@AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query odb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
