---
source_url: https://docs.aws.amazon.com/odb/latest/APIReference/API_GetCloudAutonomousVmCluster.html
---

# GetCloudAutonomousVmCluster
<a name="API_GetCloudAutonomousVmCluster"></a>

Gets information about a specific Autonomous VM cluster.

## Request Syntax
<a name="API_GetCloudAutonomousVmCluster_RequestSyntax"></a>

```
{
   "cloudAutonomousVmClusterId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetCloudAutonomousVmCluster_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [cloudAutonomousVmClusterId](#API_GetCloudAutonomousVmCluster_RequestSyntax) **   <a name="odb-GetCloudAutonomousVmCluster-request-cloudAutonomousVmClusterId"></a>
The unique identifier of the Autonomous VM cluster to retrieve information about.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 64.
Pattern: `[a-zA-Z0-9_~.-]+`
Required: Yes

## Response Syntax
<a name="API_GetCloudAutonomousVmCluster_ResponseSyntax"></a>

```
{
   "cloudAutonomousVmCluster": {
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
}
```

## Response Elements
<a name="API_GetCloudAutonomousVmCluster_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [cloudAutonomousVmCluster](#API_GetCloudAutonomousVmCluster_ResponseSyntax) **   <a name="odb-GetCloudAutonomousVmCluster-response-cloudAutonomousVmCluster"></a>
The details of the requested Autonomous VM cluster.
Type: [CloudAutonomousVmCluster](API_CloudAutonomousVmCluster.md) object

## Errors
<a name="API_GetCloudAutonomousVmCluster_Errors"></a>

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
<a name="API_GetCloudAutonomousVmCluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/odb-2024-08-20/GetCloudAutonomousVmCluster)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/odb-2024-08-20/GetCloudAutonomousVmCluster)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/odb-2024-08-20/GetCloudAutonomousVmCluster)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/odb-2024-08-20/GetCloudAutonomousVmCluster)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/odb-2024-08-20/GetCloudAutonomousVmCluster)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/odb-2024-08-20/GetCloudAutonomousVmCluster)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/odb-2024-08-20/GetCloudAutonomousVmCluster)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/odb-2024-08-20/GetCloudAutonomousVmCluster)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/odb-2024-08-20/GetCloudAutonomousVmCluster)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/odb-2024-08-20/GetCloudAutonomousVmCluster)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Oracle Database@AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query odb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
