---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DescribeDryRunProgress.html
---

# DescribeDryRunProgress
<a name="API_DescribeDryRunProgress"></a>

Describes the progress of a pre-update dry run analysis on an Amazon OpenSearch Service domain. For more information, see [Determining whether a change will cause a blue/green deployment](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managedomains-configuration-changes#dryrun).

## Request Syntax
<a name="API_DescribeDryRunProgress_RequestSyntax"></a>

```
GET /2021-01-01/opensearch/domain/{{DomainName}}/dryRun?dryRunId={{DryRunId}}&loadDryRunConfig={{LoadDryRunConfig}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeDryRunProgress_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DomainName](#API_DescribeDryRunProgress_RequestSyntax) **   <a name="opensearchservice-DescribeDryRunProgress-request-uri-DomainName"></a>
The name of the domain.
Length Constraints: Minimum length of 3. Maximum length of 28.
Pattern: `[a-z][a-z0-9\-]+`
Required: Yes

 ** [DryRunId](#API_DescribeDryRunProgress_RequestSyntax) **   <a name="opensearchservice-DescribeDryRunProgress-request-uri-DryRunId"></a>
The unique identifier of the dry run.
Length Constraints: Fixed length of 36.
Pattern: `\p{XDigit}{8}-\p{XDigit}{4}-\p{XDigit}{4}-\p{XDigit}{4}-\p{XDigit}{12}`

 ** [LoadDryRunConfig](#API_DescribeDryRunProgress_RequestSyntax) **   <a name="opensearchservice-DescribeDryRunProgress-request-uri-LoadDryRunConfig"></a>
Whether to include the configuration of the dry run in the response. The configuration specifies the updates that you're planning to make on the domain.

## Request Body
<a name="API_DescribeDryRunProgress_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeDryRunProgress_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "DryRunConfig": {
      "AccessPolicies": "string",
      "AdvancedOptions": {
         "string" : "string"
      },
      "AdvancedSecurityOptions": {
         "AnonymousAuthDisableDate": number,
         "AnonymousAuthEnabled": boolean,
         "Enabled": boolean,
         "IAMFederationOptions": {
            "Enabled": boolean,
            "RolesKey": "string",
            "SubjectKey": "string"
         },
         "InternalUserDatabaseEnabled": boolean,
         "JWTOptions": {
            "Enabled": boolean,
            "JwksUrl": "string",
            "PublicKey": "string",
            "RolesKey": "string",
            "SubjectKey": "string"
         },
         "SAMLOptions": {
            "Enabled": boolean,
            "Idp": {
               "EntityId": "string",
               "MetadataContent": "string"
            },
            "RolesKey": "string",
            "SessionTimeoutMinutes": number,
            "SubjectKey": "string"
         }
      },
      "AIMLOptions": {
         "NaturalLanguageQueryGenerationOptions": {
            "CurrentState": "string",
            "DesiredState": "string"
         },
         "S3VectorsEngine": {
            "Enabled": boolean
         },
         "ServerlessVectorAcceleration": {
            "Enabled": boolean
         }
      },
      "ARN": "string",
      "AutomatedSnapshotPauseOptions": {
         "Enabled": boolean,
         "EndTime": number,
         "StartTime": number,
         "State": "string"
      },
      "AutoTuneOptions": {
         "ErrorMessage": "string",
         "State": "string",
         "UseOffPeakWindow": boolean
      },
      "ChangeProgressDetails": {
         "ChangeId": "string",
         "ConfigChangeStatus": "string",
         "InitiatedBy": "string",
         "LastUpdatedTime": number,
         "Message": "string",
         "StartTime": number
      },
      "ClusterConfig": {
         "ColdStorageOptions": {
            "Enabled": boolean
         },
         "DedicatedMasterCount": number,
         "DedicatedMasterEnabled": boolean,
         "DedicatedMasterType": "string",
         "InstanceCount": number,
         "InstanceType": "string",
         "MultiAZWithStandbyEnabled": boolean,
         "NodeOptions": [
            {
               "NodeConfig": {
                  "Count": number,
                  "Enabled": boolean,
                  "Type": "string"
               },
               "NodeType": "string"
            }
         ],
         "WarmCount": number,
         "WarmEnabled": boolean,
         "WarmType": "string",
         "ZoneAwarenessConfig": {
            "AvailabilityZoneCount": number
         },
         "ZoneAwarenessEnabled": boolean
      },
      "CognitoOptions": {
         "Enabled": boolean,
         "IdentityPoolId": "string",
         "RoleArn": "string",
         "UserPoolId": "string"
      },
      "Created": boolean,
      "Deleted": boolean,
      "DeploymentStrategyOptions": {
         "DeploymentStrategy": "string"
      },
      "DomainEndpointOptions": {
         "CustomEndpoint": "string",
         "CustomEndpointCertificateArn": "string",
         "CustomEndpointEnabled": boolean,
         "EnforceHTTPS": boolean,
         "TLSSecurityPolicy": "string"
      },
      "DomainEndpointV2HostedZoneId": "string",
      "DomainId": "string",
      "DomainName": "string",
      "DomainProcessingStatus": "string",
      "EBSOptions": {
         "EBSEnabled": boolean,
         "Iops": number,
         "Throughput": number,
         "VolumeSize": number,
         "VolumeType": "string"
      },
      "EncryptionAtRestOptions": {
         "Enabled": boolean,
         "KmsKeyId": "string"
      },
      "Endpoint": "string",
      "Endpoints": {
         "string" : "string"
      },
      "EndpointV2": "string",
      "EngineMode": "string",
      "EngineVersion": "string",
      "IdentityCenterOptions": {
         "EnabledAPIAccess": boolean,
         "IdentityCenterApplicationARN": "string",
         "IdentityCenterInstanceARN": "string",
         "IdentityCenterInstanceRegion": "string",
         "IdentityStoreId": "string",
         "RolesKey": "string",
         "SubjectKey": "string"
      },
      "IPAddressType": "string",
      "LogPublishingOptions": {
         "string" : {
            "CloudWatchLogsLogGroupArn": "string",
            "Enabled": boolean
         }
      },
      "ModifyingProperties": [
         {
            "ActiveValue": "string",
            "Name": "string",
            "PendingValue": "string",
            "ValueType": "string"
         }
      ],
      "NodeToNodeEncryptionOptions": {
         "Enabled": boolean
      },
      "OffPeakWindowOptions": {
         "Enabled": boolean,
         "OffPeakWindow": {
            "WindowStartTime": {
               "Hours": number,
               "Minutes": number
            }
         }
      },
      "Processing": boolean,
      "ServiceSoftwareOptions": {
         "AutomatedUpdateDate": number,
         "Cancellable": boolean,
         "CurrentVersion": "string",
         "Description": "string",
         "NewVersion": "string",
         "OptionalDeployment": boolean,
         "UpdateAvailable": boolean,
         "UpdateStatus": "string"
      },
      "SnapshotOptions": {
         "AutomatedSnapshotStartHour": number
      },
      "SoftwareUpdateOptions": {
         "AutoSoftwareUpdateEnabled": boolean,
         "UseLatestServiceSoftwareForBlueGreen": boolean
      },
      "UpgradeProcessing": boolean,
      "UseCase": "string",
      "VPCOptions": {
         "AvailabilityZones": [ "string" ],
         "EgressEnabled": boolean,
         "SecurityGroupIds": [ "string" ],
         "SubnetIds": [ "string" ],
         "VPCId": "string"
      }
   },
   "DryRunProgressStatus": {
      "AcceptedWarnings": [ "string" ],
      "CreationDate": "string",
      "DryRunId": "string",
      "DryRunStatus": "string",
      "UpdateDate": "string",
      "ValidationFailures": [
         {
            "Code": "string",
            "Message": "string",
            "Severity": "string"
         }
      ]
   },
   "DryRunResults": {
      "DeploymentType": "string",
      "Message": "string"
   }
}
```

## Response Elements
<a name="API_DescribeDryRunProgress_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DryRunConfig](#API_DescribeDryRunProgress_ResponseSyntax) **   <a name="opensearchservice-DescribeDryRunProgress-response-DryRunConfig"></a>
Details about the changes you're planning to make on the domain.
Type: [DomainStatus](API_DomainStatus.md) object

 ** [DryRunProgressStatus](#API_DescribeDryRunProgress_ResponseSyntax) **   <a name="opensearchservice-DescribeDryRunProgress-response-DryRunProgressStatus"></a>
The current status of the dry run, including any validation errors.
Type: [DryRunProgressStatus](API_DryRunProgressStatus.md) object

 ** [DryRunResults](#API_DescribeDryRunProgress_ResponseSyntax) **   <a name="opensearchservice-DescribeDryRunProgress-response-DryRunResults"></a>
The results of the dry run.
Type: [DryRunResults](API_DryRunResults.md) object

## Errors
<a name="API_DescribeDryRunProgress_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BaseException **
An error occurred while processing the request.
 ** message **
A description of the error.
HTTP Status Code: 400

 ** DisabledOperationException **
An error occured because the client wanted to access an unsupported operation.
HTTP Status Code: 409

 ** InternalException **
Request processing failed because of an unknown error, exception, or internal failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
An exception for accessing or deleting a resource that doesn't exist.
HTTP Status Code: 409

 ** ValidationException **
An exception for accessing or deleting a resource that doesn't exist.
HTTP Status Code: 400

## See Also
<a name="API_DescribeDryRunProgress_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearch-2021-01-01/DescribeDryRunProgress)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearch-2021-01-01/DescribeDryRunProgress)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/DescribeDryRunProgress)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearch-2021-01-01/DescribeDryRunProgress)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/DescribeDryRunProgress)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearch-2021-01-01/DescribeDryRunProgress)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearch-2021-01-01/DescribeDryRunProgress)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearch-2021-01-01/DescribeDryRunProgress)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/opensearch-2021-01-01/DescribeDryRunProgress)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/DescribeDryRunProgress)
