---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_UpdateDomainConfig.html
---

# UpdateDomainConfig
<a name="API_UpdateDomainConfig"></a>

Modifies the cluster configuration of the specified Amazon OpenSearch Service domain.

## Request Syntax
<a name="API_UpdateDomainConfig_RequestSyntax"></a>

```
POST /2021-01-01/opensearch/domain/{{DomainName}}/config HTTP/1.1
Content-type: application/json

{
   "AccessPolicies": "{{string}}",
   "AdvancedOptions": {
      "{{string}}" : "{{string}}"
   },
   "AdvancedSecurityOptions": {
      "AnonymousAuthEnabled": {{boolean}},
      "Enabled": {{boolean}},
      "IAMFederationOptions": {
         "Enabled": {{boolean}},
         "RolesKey": "{{string}}",
         "SubjectKey": "{{string}}"
      },
      "InternalUserDatabaseEnabled": {{boolean}},
      "JWTOptions": {
         "Enabled": {{boolean}},
         "JwksUrl": "{{string}}",
         "PublicKey": "{{string}}",
         "RolesKey": "{{string}}",
         "SubjectKey": "{{string}}"
      },
      "MasterUserOptions": {
         "MasterUserARN": "{{string}}",
         "MasterUserName": "{{string}}",
         "MasterUserPassword": "{{string}}"
      },
      "SAMLOptions": {
         "Enabled": {{boolean}},
         "Idp": {
            "EntityId": "{{string}}",
            "MetadataContent": "{{string}}"
         },
         "MasterBackendRole": "{{string}}",
         "MasterUserName": "{{string}}",
         "RolesKey": "{{string}}",
         "SessionTimeoutMinutes": {{number}},
         "SubjectKey": "{{string}}"
      }
   },
   "AIMLOptions": {
      "NaturalLanguageQueryGenerationOptions": {
         "DesiredState": "{{string}}"
      },
      "S3VectorsEngine": {
         "Enabled": {{boolean}}
      },
      "ServerlessVectorAcceleration": {
         "Enabled": {{boolean}}
      }
   },
   "AutomatedSnapshotPauseOptions": {
      "Enabled": {{boolean}},
      "EndTime": {{number}},
      "StartTime": {{number}}
   },
   "AutoTuneOptions": {
      "DesiredState": "{{string}}",
      "MaintenanceSchedules": [
         {
            "CronExpressionForRecurrence": "{{string}}",
            "Duration": {
               "Unit": "{{string}}",
               "Value": {{number}}
            },
            "StartAt": {{number}}
         }
      ],
      "RollbackOnDisable": "{{string}}",
      "UseOffPeakWindow": {{boolean}}
   },
   "ClusterConfig": {
      "ColdStorageOptions": {
         "Enabled": {{boolean}}
      },
      "DedicatedMasterCount": {{number}},
      "DedicatedMasterEnabled": {{boolean}},
      "DedicatedMasterType": "{{string}}",
      "InstanceCount": {{number}},
      "InstanceType": "{{string}}",
      "MultiAZWithStandbyEnabled": {{boolean}},
      "NodeOptions": [
         {
            "NodeConfig": {
               "Count": {{number}},
               "Enabled": {{boolean}},
               "Type": "{{string}}"
            },
            "NodeType": "{{string}}"
         }
      ],
      "WarmCount": {{number}},
      "WarmEnabled": {{boolean}},
      "WarmType": "{{string}}",
      "ZoneAwarenessConfig": {
         "AvailabilityZoneCount": {{number}}
      },
      "ZoneAwarenessEnabled": {{boolean}}
   },
   "CognitoOptions": {
      "Enabled": {{boolean}},
      "IdentityPoolId": "{{string}}",
      "RoleArn": "{{string}}",
      "UserPoolId": "{{string}}"
   },
   "DeploymentStrategyOptions": {
      "DeploymentStrategy": "{{string}}"
   },
   "DomainEndpointOptions": {
      "CustomEndpoint": "{{string}}",
      "CustomEndpointCertificateArn": "{{string}}",
      "CustomEndpointEnabled": {{boolean}},
      "EnforceHTTPS": {{boolean}},
      "TLSSecurityPolicy": "{{string}}"
   },
   "DryRun": {{boolean}},
   "DryRunMode": "{{string}}",
   "EBSOptions": {
      "EBSEnabled": {{boolean}},
      "Iops": {{number}},
      "Throughput": {{number}},
      "VolumeSize": {{number}},
      "VolumeType": "{{string}}"
   },
   "EncryptionAtRestOptions": {
      "Enabled": {{boolean}},
      "KmsKeyId": "{{string}}"
   },
   "EngineMode": "{{string}}",
   "IdentityCenterOptions": {
      "EnabledAPIAccess": {{boolean}},
      "IdentityCenterInstanceARN": "{{string}}",
      "IdentityCenterInstanceRegion": "{{string}}",
      "RolesKey": "{{string}}",
      "SubjectKey": "{{string}}"
   },
   "IPAddressType": "{{string}}",
   "LogPublishingOptions": {
      "{{string}}" : {
         "CloudWatchLogsLogGroupArn": "{{string}}",
         "Enabled": {{boolean}}
      }
   },
   "NodeToNodeEncryptionOptions": {
      "Enabled": {{boolean}}
   },
   "OffPeakWindowOptions": {
      "Enabled": {{boolean}},
      "OffPeakWindow": {
         "WindowStartTime": {
            "Hours": {{number}},
            "Minutes": {{number}}
         }
      }
   },
   "SnapshotOptions": {
      "AutomatedSnapshotStartHour": {{number}}
   },
   "SoftwareUpdateOptions": {
      "AutoSoftwareUpdateEnabled": {{boolean}},
      "UseLatestServiceSoftwareForBlueGreen": {{boolean}}
   },
   "UseCase": "{{string}}",
   "VPCOptions": {
      "EgressEnabled": {{boolean}},
      "SecurityGroupIds": [ "{{string}}" ],
      "SubnetIds": [ "{{string}}" ]
   }
}
```

## URI Request Parameters
<a name="API_UpdateDomainConfig_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DomainName](#API_UpdateDomainConfig_RequestSyntax) **   <a name="opensearchservice-UpdateDomainConfig-request-uri-DomainName"></a>
The name of the domain that you're updating.
Length Constraints: Minimum length of 3. Maximum length of 28.
Pattern: `[a-z][a-z0-9\-]+`
Required: Yes

## Request Body
<a name="API_UpdateDomainConfig_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AccessPolicies](#API_UpdateDomainConfig_RequestSyntax) **   <a name="opensearchservice-UpdateDomainConfig-request-AccessPolicies"></a>
Identity and Access Management (IAM) access policy as a JSON-formatted string.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 102400.
Pattern: `.*`
Required: No

 ** [AdvancedOptions](#API_UpdateDomainConfig_RequestSyntax) **   <a name="opensearchservice-UpdateDomainConfig-request-AdvancedOptions"></a>
Key-value pairs to specify advanced configuration options. The following key-value pairs are supported:
+  `"rest.action.multi.allow_explicit_index": "true" | "false"` - Note the use of a string rather than a boolean. Specifies whether explicit references to indexes are allowed inside the body of HTTP requests. If you want to configure access policies for domain sub-resources, such as specific indexes and domain APIs, you must disable this property. Default is true.
+  `"indices.fielddata.cache.size": "80" ` - Note the use of a string rather than a boolean. Specifies the percentage of heap space allocated to field data. Default is unbounded.
+  `"indices.query.bool.max_clause_count": "1024"` - Note the use of a string rather than a boolean. Specifies the maximum number of clauses allowed in a Lucene boolean query. Default is 1,024. Queries with more than the permitted number of clauses result in a `TooManyClauses` error.
For more information, see [Advanced cluster parameters](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/createupdatedomains.html#createdomain-configure-advanced-options).
Type: String to string map
Required: No

 ** [AdvancedSecurityOptions](#API_UpdateDomainConfig_RequestSyntax) **   <a name="opensearchservice-UpdateDomainConfig-request-AdvancedSecurityOptions"></a>
Options for fine-grained access control.
Type: [AdvancedSecurityOptionsInput](API_AdvancedSecurityOptionsInput.md) object
Required: No

 ** [AIMLOptions](#API_UpdateDomainConfig_RequestSyntax) **   <a name="opensearchservice-UpdateDomainConfig-request-AIMLOptions"></a>
Options for all machine learning features for the specified domain.
Type: [AIMLOptionsInput](API_AIMLOptionsInput.md) object
Required: No

 ** [AutomatedSnapshotPauseOptions](#API_UpdateDomainConfig_RequestSyntax) **   <a name="opensearchservice-UpdateDomainConfig-request-AutomatedSnapshotPauseOptions"></a>
Specifies the automated snapshot pause options for the domain.
Suspending snapshots reduces data protection. You cannot restore your domain to points in time when snapshots are suspended. Use this feature only for short-term operational needs such as migrations or maintenance windows.
Maximum suspension duration: 3 days.
Type: [AutomatedSnapshotPauseRequestOptions](API_AutomatedSnapshotPauseRequestOptions.md) object
Required: No

 ** [AutoTuneOptions](#API_UpdateDomainConfig_RequestSyntax) **   <a name="opensearchservice-UpdateDomainConfig-request-AutoTuneOptions"></a>
Options for Auto-Tune.
Type: [AutoTuneOptions](API_AutoTuneOptions.md) object
Required: No

 ** [ClusterConfig](#API_UpdateDomainConfig_RequestSyntax) **   <a name="opensearchservice-UpdateDomainConfig-request-ClusterConfig"></a>
Changes that you want to make to the cluster configuration, such as the instance type and number of EC2 instances.
Type: [ClusterConfig](API_ClusterConfig.md) object
Required: No

 ** [CognitoOptions](#API_UpdateDomainConfig_RequestSyntax) **   <a name="opensearchservice-UpdateDomainConfig-request-CognitoOptions"></a>
Key-value pairs to configure Amazon Cognito authentication for OpenSearch Dashboards.
Type: [CognitoOptions](API_CognitoOptions.md) object
Required: No

 ** [DeploymentStrategyOptions](#API_UpdateDomainConfig_RequestSyntax) **   <a name="opensearchservice-UpdateDomainConfig-request-DeploymentStrategyOptions"></a>
Specifies the deployment strategy options for the domain.
Type: [DeploymentStrategyOptions](API_DeploymentStrategyOptions.md) object
Required: No

 ** [DomainEndpointOptions](#API_UpdateDomainConfig_RequestSyntax) **   <a name="opensearchservice-UpdateDomainConfig-request-DomainEndpointOptions"></a>
Additional options for the domain endpoint, such as whether to require HTTPS for all traffic.
Type: [DomainEndpointOptions](API_DomainEndpointOptions.md) object
Required: No

 ** [DryRun](#API_UpdateDomainConfig_RequestSyntax) **   <a name="opensearchservice-UpdateDomainConfig-request-DryRun"></a>
This flag, when set to True, specifies whether the `UpdateDomain` request should return the results of a dry run analysis without actually applying the change. A dry run determines what type of deployment the update will cause.
Type: Boolean
Required: No

 ** [DryRunMode](#API_UpdateDomainConfig_RequestSyntax) **   <a name="opensearchservice-UpdateDomainConfig-request-DryRunMode"></a>
The type of dry run to perform.
+  `Basic` only returns the type of deployment (blue/green or dynamic) that the update will cause.
+  `Verbose` runs an additional check to validate the changes you're making. For more information, see [Validating a domain update](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managedomains-configuration-changes#validation-check).
Type: String
Valid Values: `Basic | Verbose`
Required: No

 ** [EBSOptions](#API_UpdateDomainConfig_RequestSyntax) **   <a name="opensearchservice-UpdateDomainConfig-request-EBSOptions"></a>
The type and size of the EBS volume to attach to instances in the domain.
Type: [EBSOptions](API_EBSOptions.md) object
Required: No

 ** [EncryptionAtRestOptions](#API_UpdateDomainConfig_RequestSyntax) **   <a name="opensearchservice-UpdateDomainConfig-request-EncryptionAtRestOptions"></a>
Encryption at rest options for the domain.
Type: [EncryptionAtRestOptions](API_EncryptionAtRestOptions.md) object
Required: No

 ** [EngineMode](#API_UpdateDomainConfig_RequestSyntax) **   <a name="opensearchservice-UpdateDomainConfig-request-EngineMode"></a>
The engine mode for the domain. The engine mode can't be changed after the domain is created. For valid values, see `EngineMode`.
Type: String
Valid Values: `GENERAL | OPTIMIZED`
Required: No

 ** [IdentityCenterOptions](#API_UpdateDomainConfig_RequestSyntax) **   <a name="opensearchservice-UpdateDomainConfig-request-IdentityCenterOptions"></a>
Configuration settings for enabling and managing IAM Identity Center.
Type: [IdentityCenterOptionsInput](API_IdentityCenterOptionsInput.md) object
Required: No

 ** [IPAddressType](#API_UpdateDomainConfig_RequestSyntax) **   <a name="opensearchservice-UpdateDomainConfig-request-IPAddressType"></a>
Specify either dual stack or IPv4 as your IP address type. Dual stack allows you to share domain resources across IPv4 and IPv6 address types, and is the recommended option. If your IP address type is currently set to dual stack, you can't change it.
Type: String
Valid Values: `ipv4 | dualstack`
Required: No

 ** [LogPublishingOptions](#API_UpdateDomainConfig_RequestSyntax) **   <a name="opensearchservice-UpdateDomainConfig-request-LogPublishingOptions"></a>
Options to publish OpenSearch logs to Amazon CloudWatch Logs.
Type: String to [LogPublishingOption](API_LogPublishingOption.md) object map
Valid Keys: `INDEX_SLOW_LOGS | SEARCH_SLOW_LOGS | ES_APPLICATION_LOGS | AUDIT_LOGS`
Required: No

 ** [NodeToNodeEncryptionOptions](#API_UpdateDomainConfig_RequestSyntax) **   <a name="opensearchservice-UpdateDomainConfig-request-NodeToNodeEncryptionOptions"></a>
Node-to-node encryption options for the domain.
Type: [NodeToNodeEncryptionOptions](API_NodeToNodeEncryptionOptions.md) object
Required: No

 ** [OffPeakWindowOptions](#API_UpdateDomainConfig_RequestSyntax) **   <a name="opensearchservice-UpdateDomainConfig-request-OffPeakWindowOptions"></a>
Off-peak window options for the domain.
Type: [OffPeakWindowOptions](API_OffPeakWindowOptions.md) object
Required: No

 ** [SnapshotOptions](#API_UpdateDomainConfig_RequestSyntax) **   <a name="opensearchservice-UpdateDomainConfig-request-SnapshotOptions"></a>
Option to set the time, in UTC format, for the daily automated snapshot. Default value is `0` hours.
Type: [SnapshotOptions](API_SnapshotOptions.md) object
Required: No

 ** [SoftwareUpdateOptions](#API_UpdateDomainConfig_RequestSyntax) **   <a name="opensearchservice-UpdateDomainConfig-request-SoftwareUpdateOptions"></a>
Service software update options for the domain.
Type: [SoftwareUpdateOptions](API_SoftwareUpdateOptions.md) object
Required: No

 ** [UseCase](#API_UpdateDomainConfig_RequestSyntax) **   <a name="opensearchservice-UpdateDomainConfig-request-UseCase"></a>
The primary use case for the domain. For valid values, see `DomainUseCase`.
Type: String
Valid Values: `SEARCH | VECTOR | OBSERVABILITY | MIXED`
Required: No

 ** [VPCOptions](#API_UpdateDomainConfig_RequestSyntax) **   <a name="opensearchservice-UpdateDomainConfig-request-VPCOptions"></a>
Options to specify the subnets and security groups for a VPC endpoint. For more information, see [Launching your Amazon OpenSearch Service domains using a VPC](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/vpc.html).
Type: [VPCOptions](API_VPCOptions.md) object
Required: No

## Response Syntax
<a name="API_UpdateDomainConfig_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "DomainConfig": {
      "AccessPolicies": {
         "Options": "string",
         "Status": {
            "CreationDate": number,
            "PendingDeletion": boolean,
            "State": "string",
            "UpdateDate": number,
            "UpdateVersion": number
         }
      },
      "AdvancedOptions": {
         "Options": {
            "string" : "string"
         },
         "Status": {
            "CreationDate": number,
            "PendingDeletion": boolean,
            "State": "string",
            "UpdateDate": number,
            "UpdateVersion": number
         }
      },
      "AdvancedSecurityOptions": {
         "Options": {
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
         "Status": {
            "CreationDate": number,
            "PendingDeletion": boolean,
            "State": "string",
            "UpdateDate": number,
            "UpdateVersion": number
         }
      },
      "AIMLOptions": {
         "Options": {
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
         "Status": {
            "CreationDate": number,
            "PendingDeletion": boolean,
            "State": "string",
            "UpdateDate": number,
            "UpdateVersion": number
         }
      },
      "AutomatedSnapshotPauseOptions": {
         "Options": {
            "Enabled": boolean,
            "EndTime": number,
            "StartTime": number,
            "State": "string"
         },
         "Status": {
            "CreationDate": number,
            "PendingDeletion": boolean,
            "State": "string",
            "UpdateDate": number,
            "UpdateVersion": number
         }
      },
      "AutoTuneOptions": {
         "Options": {
            "DesiredState": "string",
            "MaintenanceSchedules": [
               {
                  "CronExpressionForRecurrence": "string",
                  "Duration": {
                     "Unit": "string",
                     "Value": number
                  },
                  "StartAt": number
               }
            ],
            "RollbackOnDisable": "string",
            "UseOffPeakWindow": boolean
         },
         "Status": {
            "CreationDate": number,
            "ErrorMessage": "string",
            "PendingDeletion": boolean,
            "State": "string",
            "UpdateDate": number,
            "UpdateVersion": number
         }
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
         "Options": {
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
         "Status": {
            "CreationDate": number,
            "PendingDeletion": boolean,
            "State": "string",
            "UpdateDate": number,
            "UpdateVersion": number
         }
      },
      "CognitoOptions": {
         "Options": {
            "Enabled": boolean,
            "IdentityPoolId": "string",
            "RoleArn": "string",
            "UserPoolId": "string"
         },
         "Status": {
            "CreationDate": number,
            "PendingDeletion": boolean,
            "State": "string",
            "UpdateDate": number,
            "UpdateVersion": number
         }
      },
      "DeploymentStrategyOptions": {
         "Options": {
            "DeploymentStrategy": "string"
         },
         "Status": {
            "CreationDate": number,
            "PendingDeletion": boolean,
            "State": "string",
            "UpdateDate": number,
            "UpdateVersion": number
         }
      },
      "DomainEndpointOptions": {
         "Options": {
            "CustomEndpoint": "string",
            "CustomEndpointCertificateArn": "string",
            "CustomEndpointEnabled": boolean,
            "EnforceHTTPS": boolean,
            "TLSSecurityPolicy": "string"
         },
         "Status": {
            "CreationDate": number,
            "PendingDeletion": boolean,
            "State": "string",
            "UpdateDate": number,
            "UpdateVersion": number
         }
      },
      "EBSOptions": {
         "Options": {
            "EBSEnabled": boolean,
            "Iops": number,
            "Throughput": number,
            "VolumeSize": number,
            "VolumeType": "string"
         },
         "Status": {
            "CreationDate": number,
            "PendingDeletion": boolean,
            "State": "string",
            "UpdateDate": number,
            "UpdateVersion": number
         }
      },
      "EncryptionAtRestOptions": {
         "Options": {
            "Enabled": boolean,
            "KmsKeyId": "string"
         },
         "Status": {
            "CreationDate": number,
            "PendingDeletion": boolean,
            "State": "string",
            "UpdateDate": number,
            "UpdateVersion": number
         }
      },
      "EngineMode": {
         "Options": "string",
         "Status": {
            "CreationDate": number,
            "PendingDeletion": boolean,
            "State": "string",
            "UpdateDate": number,
            "UpdateVersion": number
         }
      },
      "EngineVersion": {
         "Options": "string",
         "Status": {
            "CreationDate": number,
            "PendingDeletion": boolean,
            "State": "string",
            "UpdateDate": number,
            "UpdateVersion": number
         }
      },
      "IdentityCenterOptions": {
         "Options": {
            "EnabledAPIAccess": boolean,
            "IdentityCenterApplicationARN": "string",
            "IdentityCenterInstanceARN": "string",
            "IdentityCenterInstanceRegion": "string",
            "IdentityStoreId": "string",
            "RolesKey": "string",
            "SubjectKey": "string"
         },
         "Status": {
            "CreationDate": number,
            "PendingDeletion": boolean,
            "State": "string",
            "UpdateDate": number,
            "UpdateVersion": number
         }
      },
      "IPAddressType": {
         "Options": "string",
         "Status": {
            "CreationDate": number,
            "PendingDeletion": boolean,
            "State": "string",
            "UpdateDate": number,
            "UpdateVersion": number
         }
      },
      "LogPublishingOptions": {
         "Options": {
            "string" : {
               "CloudWatchLogsLogGroupArn": "string",
               "Enabled": boolean
            }
         },
         "Status": {
            "CreationDate": number,
            "PendingDeletion": boolean,
            "State": "string",
            "UpdateDate": number,
            "UpdateVersion": number
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
         "Options": {
            "Enabled": boolean
         },
         "Status": {
            "CreationDate": number,
            "PendingDeletion": boolean,
            "State": "string",
            "UpdateDate": number,
            "UpdateVersion": number
         }
      },
      "OffPeakWindowOptions": {
         "Options": {
            "Enabled": boolean,
            "OffPeakWindow": {
               "WindowStartTime": {
                  "Hours": number,
                  "Minutes": number
               }
            }
         },
         "Status": {
            "CreationDate": number,
            "PendingDeletion": boolean,
            "State": "string",
            "UpdateDate": number,
            "UpdateVersion": number
         }
      },
      "SnapshotOptions": {
         "Options": {
            "AutomatedSnapshotStartHour": number
         },
         "Status": {
            "CreationDate": number,
            "PendingDeletion": boolean,
            "State": "string",
            "UpdateDate": number,
            "UpdateVersion": number
         }
      },
      "SoftwareUpdateOptions": {
         "Options": {
            "AutoSoftwareUpdateEnabled": boolean,
            "UseLatestServiceSoftwareForBlueGreen": boolean
         },
         "Status": {
            "CreationDate": number,
            "PendingDeletion": boolean,
            "State": "string",
            "UpdateDate": number,
            "UpdateVersion": number
         }
      },
      "UseCase": {
         "Options": "string",
         "Status": {
            "CreationDate": number,
            "PendingDeletion": boolean,
            "State": "string",
            "UpdateDate": number,
            "UpdateVersion": number
         }
      },
      "VPCOptions": {
         "Options": {
            "AvailabilityZones": [ "string" ],
            "EgressEnabled": boolean,
            "SecurityGroupIds": [ "string" ],
            "SubnetIds": [ "string" ],
            "VPCId": "string"
         },
         "Status": {
            "CreationDate": number,
            "PendingDeletion": boolean,
            "State": "string",
            "UpdateDate": number,
            "UpdateVersion": number
         }
      }
   },
   "DryRunProgressStatus": {
      "CreationDate": "string",
      "DryRunId": "string",
      "DryRunStatus": "string",
      "UpdateDate": "string",
      "ValidationFailures": [
         {
            "Code": "string",
            "Message": "string"
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
<a name="API_UpdateDomainConfig_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DomainConfig](#API_UpdateDomainConfig_ResponseSyntax) **   <a name="opensearchservice-UpdateDomainConfig-response-DomainConfig"></a>
The status of the updated domain.
Type: [DomainConfig](API_DomainConfig.md) object

 ** [DryRunProgressStatus](#API_UpdateDomainConfig_ResponseSyntax) **   <a name="opensearchservice-UpdateDomainConfig-response-DryRunProgressStatus"></a>
The status of the dry run being performed on the domain, if any.
Type: [DryRunProgressStatus](API_DryRunProgressStatus.md) object

 ** [DryRunResults](#API_UpdateDomainConfig_ResponseSyntax) **   <a name="opensearchservice-UpdateDomainConfig-response-DryRunResults"></a>
Results of the dry run performed in the update domain request.
Type: [DryRunResults](API_DryRunResults.md) object

## Errors
<a name="API_UpdateDomainConfig_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BaseException **
An error occurred while processing the request.
 ** message **
A description of the error.
HTTP Status Code: 400

 ** InternalException **
Request processing failed because of an unknown error, exception, or internal failure.
HTTP Status Code: 500

 ** InvalidTypeException **
An exception for trying to create or access a sub-resource that's either invalid or not supported.
HTTP Status Code: 409

 ** LimitExceededException **
An exception for trying to create more than the allowed number of resources or sub-resources.
HTTP Status Code: 409

 ** ResourceNotFoundException **
An exception for accessing or deleting a resource that doesn't exist.
HTTP Status Code: 409

 ** ValidationException **
An exception for accessing or deleting a resource that doesn't exist.
HTTP Status Code: 400

## See Also
<a name="API_UpdateDomainConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearch-2021-01-01/UpdateDomainConfig)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearch-2021-01-01/UpdateDomainConfig)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/UpdateDomainConfig)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearch-2021-01-01/UpdateDomainConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/UpdateDomainConfig)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearch-2021-01-01/UpdateDomainConfig)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearch-2021-01-01/UpdateDomainConfig)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearch-2021-01-01/UpdateDomainConfig)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/opensearch-2021-01-01/UpdateDomainConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/UpdateDomainConfig)
