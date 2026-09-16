---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_CreateDomain.html
---

# CreateDomain
<a name="API_CreateDomain"></a>

Creates an Amazon OpenSearch Service domain. For more information, see [Creating and managing Amazon OpenSearch Service domains](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/createupdatedomains.html).

## Request Syntax
<a name="API_CreateDomain_RequestSyntax"></a>

```
POST /2021-01-01/opensearch/domain HTTP/1.1
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
   "DomainName": "{{string}}",
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
   "EngineVersion": "{{string}}",
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
   "TagList": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "UseCase": "{{string}}",
   "VPCOptions": {
      "EgressEnabled": {{boolean}},
      "SecurityGroupIds": [ "{{string}}" ],
      "SubnetIds": [ "{{string}}" ]
   }
}
```

## URI Request Parameters
<a name="API_CreateDomain_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateDomain_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AccessPolicies](#API_CreateDomain_RequestSyntax) **   <a name="opensearchservice-CreateDomain-request-AccessPolicies"></a>
Identity and Access Management (IAM) policy document specifying the access policies for the new domain.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 102400.
Pattern: `.*`
Required: No

 ** [AdvancedOptions](#API_CreateDomain_RequestSyntax) **   <a name="opensearchservice-CreateDomain-request-AdvancedOptions"></a>
Key-value pairs to specify advanced configuration options. The following key-value pairs are supported:
+  `"rest.action.multi.allow_explicit_index": "true" | "false"` - Note the use of a string rather than a boolean. Specifies whether explicit references to indexes are allowed inside the body of HTTP requests. If you want to configure access policies for domain sub-resources, such as specific indexes and domain APIs, you must disable this property. Default is true.
+  `"indices.fielddata.cache.size": "80" ` - Note the use of a string rather than a boolean. Specifies the percentage of heap space allocated to field data. Default is unbounded.
+  `"indices.query.bool.max_clause_count": "1024"` - Note the use of a string rather than a boolean. Specifies the maximum number of clauses allowed in a Lucene boolean query. Default is 1,024. Queries with more than the permitted number of clauses result in a `TooManyClauses` error.
+  `"override_main_response_version": "true" | "false"` - Note the use of a string rather than a boolean. Specifies whether the domain reports its version as 7.10 to allow Elasticsearch OSS clients and plugins to continue working with it. Default is false when creating a domain and true when upgrading a domain.
For more information, see [Advanced cluster parameters](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/createupdatedomains.html#createdomain-configure-advanced-options).
Type: String to string map
Required: No

 ** [AdvancedSecurityOptions](#API_CreateDomain_RequestSyntax) **   <a name="opensearchservice-CreateDomain-request-AdvancedSecurityOptions"></a>
Options for fine-grained access control.
Type: [AdvancedSecurityOptionsInput](API_AdvancedSecurityOptionsInput.md) object
Required: No

 ** [AIMLOptions](#API_CreateDomain_RequestSyntax) **   <a name="opensearchservice-CreateDomain-request-AIMLOptions"></a>
Options for all machine learning features for the specified domain.
Type: [AIMLOptionsInput](API_AIMLOptionsInput.md) object
Required: No

 ** [AutomatedSnapshotPauseOptions](#API_CreateDomain_RequestSyntax) **   <a name="opensearchservice-CreateDomain-request-AutomatedSnapshotPauseOptions"></a>
Specifies the automated snapshot pause options for the domain.
Suspending snapshots reduces data protection. You cannot restore your domain to points in time when snapshots are suspended. Use this feature only for short-term operational needs such as migrations or maintenance windows.
Maximum suspension duration: 3 days.
Type: [AutomatedSnapshotPauseRequestOptions](API_AutomatedSnapshotPauseRequestOptions.md) object
Required: No

 ** [AutoTuneOptions](#API_CreateDomain_RequestSyntax) **   <a name="opensearchservice-CreateDomain-request-AutoTuneOptions"></a>
Options for Auto-Tune.
Type: [AutoTuneOptionsInput](API_AutoTuneOptionsInput.md) object
Required: No

 ** [ClusterConfig](#API_CreateDomain_RequestSyntax) **   <a name="opensearchservice-CreateDomain-request-ClusterConfig"></a>
Container for the cluster configuration of a domain.
Type: [ClusterConfig](API_ClusterConfig.md) object
Required: No

 ** [CognitoOptions](#API_CreateDomain_RequestSyntax) **   <a name="opensearchservice-CreateDomain-request-CognitoOptions"></a>
Key-value pairs to configure Amazon Cognito authentication. For more information, see [Configuring Amazon Cognito authentication for OpenSearch Dashboards](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/cognito-auth.html).
Type: [CognitoOptions](API_CognitoOptions.md) object
Required: No

 ** [DeploymentStrategyOptions](#API_CreateDomain_RequestSyntax) **   <a name="opensearchservice-CreateDomain-request-DeploymentStrategyOptions"></a>
Specifies the deployment strategy options for the domain.
Type: [DeploymentStrategyOptions](API_DeploymentStrategyOptions.md) object
Required: No

 ** [DomainEndpointOptions](#API_CreateDomain_RequestSyntax) **   <a name="opensearchservice-CreateDomain-request-DomainEndpointOptions"></a>
Additional options for the domain endpoint, such as whether to require HTTPS for all traffic.
Type: [DomainEndpointOptions](API_DomainEndpointOptions.md) object
Required: No

 ** [DomainName](#API_CreateDomain_RequestSyntax) **   <a name="opensearchservice-CreateDomain-request-DomainName"></a>
Name of the OpenSearch Service domain to create. Domain names are unique across the domains owned by an account within an AWS Region.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 28.
Pattern: `[a-z][a-z0-9\-]+`
Required: Yes

 ** [EBSOptions](#API_CreateDomain_RequestSyntax) **   <a name="opensearchservice-CreateDomain-request-EBSOptions"></a>
Container for the parameters required to enable EBS-based storage for an OpenSearch Service domain.
Type: [EBSOptions](API_EBSOptions.md) object
Required: No

 ** [EncryptionAtRestOptions](#API_CreateDomain_RequestSyntax) **   <a name="opensearchservice-CreateDomain-request-EncryptionAtRestOptions"></a>
Key-value pairs to enable encryption at rest.
Type: [EncryptionAtRestOptions](API_EncryptionAtRestOptions.md) object
Required: No

 ** [EngineMode](#API_CreateDomain_RequestSyntax) **   <a name="opensearchservice-CreateDomain-request-EngineMode"></a>
The engine mode for the domain. For valid values and requirements, see `EngineMode`.
Type: String
Valid Values: `GENERAL | OPTIMIZED`
Required: No

 ** [EngineVersion](#API_CreateDomain_RequestSyntax) **   <a name="opensearchservice-CreateDomain-request-EngineVersion"></a>
String of format Elasticsearch\_X.Y or OpenSearch\_X.Y to specify the engine version for the OpenSearch Service domain. For example, `OpenSearch_1.0` or `Elasticsearch_7.9`. For more information, see [Creating and managing Amazon OpenSearch Service domains](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/createupdatedomains.html#createdomains).
Type: String
Length Constraints: Minimum length of 14. Maximum length of 18.
Pattern: `^Elasticsearch_[0-9]{1}\.[0-9]{1,2}$|^OpenSearch_[0-9]{1,2}\.[0-9]{1,2}$`
Required: No

 ** [IdentityCenterOptions](#API_CreateDomain_RequestSyntax) **   <a name="opensearchservice-CreateDomain-request-IdentityCenterOptions"></a>
Configuration options for enabling and managing IAM Identity Center integration within a domain.
Type: [IdentityCenterOptionsInput](API_IdentityCenterOptionsInput.md) object
Required: No

 ** [IPAddressType](#API_CreateDomain_RequestSyntax) **   <a name="opensearchservice-CreateDomain-request-IPAddressType"></a>
Specify either dual stack or IPv4 as your IP address type. Dual stack allows you to share domain resources across IPv4 and IPv6 address types, and is the recommended option. If you set your IP address type to dual stack, you can't change your address type later.
Type: String
Valid Values: `ipv4 | dualstack`
Required: No

 ** [LogPublishingOptions](#API_CreateDomain_RequestSyntax) **   <a name="opensearchservice-CreateDomain-request-LogPublishingOptions"></a>
Key-value pairs to configure log publishing.
Type: String to [LogPublishingOption](API_LogPublishingOption.md) object map
Valid Keys: `INDEX_SLOW_LOGS | SEARCH_SLOW_LOGS | ES_APPLICATION_LOGS | AUDIT_LOGS`
Required: No

 ** [NodeToNodeEncryptionOptions](#API_CreateDomain_RequestSyntax) **   <a name="opensearchservice-CreateDomain-request-NodeToNodeEncryptionOptions"></a>
Enables node-to-node encryption.
Type: [NodeToNodeEncryptionOptions](API_NodeToNodeEncryptionOptions.md) object
Required: No

 ** [OffPeakWindowOptions](#API_CreateDomain_RequestSyntax) **   <a name="opensearchservice-CreateDomain-request-OffPeakWindowOptions"></a>
Specifies a daily 10-hour time block during which OpenSearch Service can perform configuration changes on the domain, including service software updates and Auto-Tune enhancements that require a blue/green deployment. If no options are specified, the default start time of 10:00 P.M. local time (for the Region that the domain is created in) is used.
Type: [OffPeakWindowOptions](API_OffPeakWindowOptions.md) object
Required: No

 ** [SnapshotOptions](#API_CreateDomain_RequestSyntax) **   <a name="opensearchservice-CreateDomain-request-SnapshotOptions"></a>
DEPRECATED. Container for the parameters required to configure automated snapshots of domain indexes.
Type: [SnapshotOptions](API_SnapshotOptions.md) object
Required: No

 ** [SoftwareUpdateOptions](#API_CreateDomain_RequestSyntax) **   <a name="opensearchservice-CreateDomain-request-SoftwareUpdateOptions"></a>
Software update options for the domain.
Type: [SoftwareUpdateOptions](API_SoftwareUpdateOptions.md) object
Required: No

 ** [TagList](#API_CreateDomain_RequestSyntax) **   <a name="opensearchservice-CreateDomain-request-TagList"></a>
List of tags to add to the domain upon creation.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** [UseCase](#API_CreateDomain_RequestSyntax) **   <a name="opensearchservice-CreateDomain-request-UseCase"></a>
The primary use case for the domain. For valid values, see `DomainUseCase`.
Type: String
Valid Values: `SEARCH | VECTOR | OBSERVABILITY | MIXED`
Required: No

 ** [VPCOptions](#API_CreateDomain_RequestSyntax) **   <a name="opensearchservice-CreateDomain-request-VPCOptions"></a>
Container for the values required to configure VPC access domains. If you don't specify these values, OpenSearch Service creates the domain with a public endpoint. For more information, see [Launching your Amazon OpenSearch Service domains using a VPC](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/vpc.html).
Type: [VPCOptions](API_VPCOptions.md) object
Required: No

## Response Syntax
<a name="API_CreateDomain_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "DomainStatus": {
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
   }
}
```

## Response Elements
<a name="API_CreateDomain_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DomainStatus](#API_CreateDomain_ResponseSyntax) **   <a name="opensearchservice-CreateDomain-response-DomainStatus"></a>
The status of the newly created domain.
Type: [DomainStatus](API_DomainStatus.md) object

## Errors
<a name="API_CreateDomain_Errors"></a>

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

 ** InvalidTypeException **
An exception for trying to create or access a sub-resource that's either invalid or not supported.
HTTP Status Code: 409

 ** LimitExceededException **
An exception for trying to create more than the allowed number of resources or sub-resources.
HTTP Status Code: 409

 ** ResourceAlreadyExistsException **
An exception for creating a resource that already exists.
HTTP Status Code: 409

 ** ValidationException **
An exception for accessing or deleting a resource that doesn't exist.
HTTP Status Code: 400

## Examples
<a name="API_CreateDomain_Examples"></a>

### Example
<a name="API_CreateDomain_Example_1"></a>

This example illustrates one usage of CreateDomain.

#### Sample Request
<a name="API_CreateDomain_Example_1_Request"></a>

```
POST /2021-01-01/opensearch/domain HTTP/1.1
Host: es.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Type: application/json
User-Agent: aws-cli/2.15.0 Python/3.11.6 Darwin/23.3.0 exe/x86_64 prompt/off command/opensearch.create-domain
X-Amz-Date: 20240212T202032Z
X-Amz-Security-Token: IQoJb3JpZ2luX2VjEI3wEaCXVz==
Authorization: AWS4-HMAC-SHA256 Credential=ASIAU/20240212/us-east-1/es/aws4_request, SignedHeaders=content-type;host;x-amz-date;x-amz-security-token, Signature=dfbf9b8975a263d23a24fead9c4a409a6c7ef1c42e67c96252bf9bb794d1ea52
Content-Length: 645
{"DomainName": "my-domain", "EngineVersion": "OpenSearch_2.11", "ClusterConfig": {"InstanceType": "r6g.xlarge.search", "InstanceCount": 10, "DedicatedMasterEnabled": true, "DedicatedMasterType": "r6g.large.search", "DedicatedMasterCount": 3}, "EBSOptions": {"EBSEnabled": true, "VolumeType": "io1", "VolumeSize": 100, "Iops": 1000}, "AccessPolicies": "{\"Version\": \"2012-10-17\", \"Statement\": [ { \"Effect\": \"Allow\", \"Principal\": { \"AWS\": \"arn:aws:iam::123456789012:root\" }, \"Action\": \"es:*\", \"Resource\": \"arn:aws:es:us-east-1:123456789012:domain/my-domain/*\" } ] }", "AutoTuneOptions": {"DesiredState": "ENABLED"}}
```

#### Sample Response
<a name="API_CreateDomain_Example_1_Response"></a>

```
{
	"DomainStatus": {
		"ARN": "arn:aws:es:us-east-1:123456789012:domain/my-domain",
		"AccessPolicies": "{\"Version\":\"2012-10-17\",\"Statement\":[{\"Effect\":\"Allow\",\"Principal\":{\"AWS\":\"arn:aws:iam::478253424788:root\"},\"Action\":\"es:*\",\"Resource\":\"arn:aws:es:us-east-1:123456789012:domain/my-domain/*\"}]}",
		"AdvancedOptions": {
			"override_main_response_version": "false",
			"rest.action.multi.allow_explicit_index": "true"
		},
		"AdvancedSecurityOptions": {
			"AnonymousAuthDisableDate": null,
			"AnonymousAuthEnabled": false,
			"Enabled": false,
			"InternalUserDatabaseEnabled": false,
			"SAMLOptions": null
		},
		"AutoTuneOptions": {
			"ErrorMessage": null,
			"State": "ENABLE_IN_PROGRESS",
			"UseOffPeakWindow": false
		},
		"AutomatedSnapshotPauseOptions": {
			"Enabled": false,
			"State": "Disabled"
		},
		"ChangeProgressDetails": {
			"ChangeId": "388f35e8-5d0c-44ae-bcd1-ffd468df9908",
			"ConfigChangeStatus": "Pending",
			"InitiatedBy": "CUSTOMER",
			"LastUpdatedTime": 1.707769234762E9,
			"Message": null,
			"StartTime": 1.707769234762E9
		},
		"ClusterConfig": {
			"ColdStorageOptions": {
				"Enabled": false
			},
			"DedicatedMasterCount": 3,
			"DedicatedMasterEnabled": true,
			"DedicatedMasterType": "r6g.large.search",
			"InstanceCount": 10,
			"InstanceType": "r6g.xlarge.search",
			"MultiAZWithStandbyEnabled": false,
			"WarmCount": null,
			"WarmEnabled": false,
			"WarmStorage": null,
			"WarmType": null,
			"ZoneAwarenessConfig": null,
			"ZoneAwarenessEnabled": false
		},
		"CognitoOptions": {
			"Enabled": false,
			"IdentityPoolId": null,
			"RoleArn": null,
			"UserPoolId": null
		},
		"Created": true,
		"Deleted": false,
		"DeploymentStrategyOptions": {
			"DeploymentStrategy": "Default"
		},
		"DomainEndpointOptions": {
			"CustomEndpoint": null,
			"CustomEndpointCertificateArn": null,
			"CustomEndpointEnabled": false,
			"EnforceHTTPS": false,
			"TLSSecurityPolicy": "Policy-Min-TLS-1-0-2019-07"
		},
		"DomainId": "123456789012/my-domain",
		"DomainName": "my-domain",
		"DomainProcessingStatus": "Creating",
		"EBSOptions": {
			"EBSEnabled": true,
			"Iops": 1000,
			"Throughput": null,
			"VolumeSize": 100,
			"VolumeType": "io1"
		},
		"EncryptionAtRestOptions": {
			"Enabled": false,
			"KmsKeyId": null
		},
		"Endpoint": null,
		"Endpoints": null,
		"EngineVersion": "OpenSearch_2.11",
		"IPAddressType": "ipv4",
		"LogPublishingOptions": null,
		"ModifyingProperties": [{
			"ActiveValue": "",
			"Name": "AccessPolicies",
			"PendingValue": "{\"Version\":\"2012-10-17\",\"Statement\":[{\"Effect\":\"Allow\",\"Principal\":{\"AWS\":\"123456789012\"},\"Action\":\"es:*\",\"Resource\":\"arn:aws:es:us-east-1:123456789012:domain/my-domain/*\"}]}",
			"ValueType": "STRINGIFIED_JSON"
		}, {
			"ActiveValue": "",
			"Name": "AdvancedOptions",
			"PendingValue": "{\"override_main_response_version\":\"false\",\"rest.action.multi.allow_explicit_index\":\"true\"}",
			"ValueType": "STRINGIFIED_JSON"
		}, {
			"ActiveValue": "",
			"Name": "AdvancedSecurityOptions.AnonymousAuthDisableDate",
			"PendingValue": "false",
			"ValueType": "PLAIN_TEXT"
		}, {
			"ActiveValue": "",
			"Name": "AdvancedSecurityOptions.AnonymousAuthEnabled",
			"PendingValue": "false",
			"ValueType": "PLAIN_TEXT"
		}, {
			"ActiveValue": "",
			"Name": "AdvancedSecurityOptions.InternalUserDatabaseEnabled",
			"PendingValue": "false",
			"ValueType": "PLAIN_TEXT"
		}, {
			"ActiveValue": "",
			"Name": "AdvancedSecurityOptions.MasterUserOptions",
			"PendingValue": "false",
			"ValueType": "PLAIN_TEXT"
		}, {
			"ActiveValue": "",
			"Name": "AdvancedSecurityOptions.SAMLOptions",
			"PendingValue": "false",
			"ValueType": "PLAIN_TEXT"
		}, {
			"ActiveValue": "",
			"Name": "AutomatedSnapshotPauseOptions",
			"PendingValue": "{\"Enabled\":false}",
			"ValueType": "STRINGIFIED_JSON"
		}, {
			"ActiveValue": "",
			"Name": "ClusterConfig.ColdStorageOptions",
			"PendingValue": "{\"Enabled\":false}",
			"ValueType": "STRINGIFIED_JSON"
		}, {
			"ActiveValue": "",
			"Name": "ClusterConfig.DedicatedMasterCount",
			"PendingValue": "3",
			"ValueType": "PLAIN_TEXT"
		}, {
			"ActiveValue": "",
			"Name": "ClusterConfig.DedicatedMasterEnabled",
			"PendingValue": "true",
			"ValueType": "PLAIN_TEXT"
		}, {
			"ActiveValue": "",
			"Name": "ClusterConfig.DedicatedMasterType",
			"PendingValue": "r6g.large.search",
			"ValueType": "PLAIN_TEXT"
		}, {
			"ActiveValue": "",
			"Name": "ClusterConfig.InstanceCount",
			"PendingValue": "10",
			"ValueType": "PLAIN_TEXT"
		}, {
			"ActiveValue": "",
			"Name": "ClusterConfig.InstanceType",
			"PendingValue": "r6g.xlarge.search",
			"ValueType": "PLAIN_TEXT"
		}, {
			"ActiveValue": "",
			"Name": "ClusterConfig.MultiAZWithStandbyEnabled",
			"PendingValue": "false",
			"ValueType": "PLAIN_TEXT"
		}, {
			"ActiveValue": "",
			"Name": "ClusterConfig.WarmCount",
			"PendingValue": "",
			"ValueType": "STRINGIFIED_JSON"
		}, {
			"ActiveValue": "",
			"Name": "ClusterConfig.WarmEnabled",
			"PendingValue": "false",
			"ValueType": "PLAIN_TEXT"
		}, {
			"ActiveValue": "",
			"Name": "ClusterConfig.WarmStorage",
			"PendingValue": "",
			"ValueType": "STRINGIFIED_JSON"
		}, {
			"ActiveValue": "",
			"Name": "ClusterConfig.WarmType",
			"PendingValue": "",
			"ValueType": "STRINGIFIED_JSON"
		}, {
			"ActiveValue": "",
			"Name": "ClusterConfig.ZoneAwarenessEnabled",
			"PendingValue": "false",
			"ValueType": "PLAIN_TEXT"
		}, {
			"ActiveValue": "",
			"Name": "EngineVersion",
			"PendingValue": "OpenSearch_2.11",
			"ValueType": "PLAIN_TEXT"
		}, {
			"ActiveValue": "",
			"Name": "IPAddressType",
			"PendingValue": "ipv4",
			"ValueType": "PLAIN_TEXT"
		}, {
			"ActiveValue": "",
			"Name": "TAGS",
			"PendingValue": "",
			"ValueType": "STRINGIFIED_JSON"
		}, {
			"ActiveValue": "",
			"Name": "DomainEndpointOptions",
			"PendingValue": "{\"CustomEndpointEnabled\":false,\"EnforceHTTPS\":false,\"TLSSecurityPolicy\":\"Policy-Min-TLS-1-0-2019-07\"}",
			"ValueType": "STRINGIFIED_JSON"
		}, {
			"ActiveValue": "",
			"Name": "EBSOptions",
			"PendingValue": "{\"EBSEnabled\":true,\"Iops\":1000,\"VolumeSize\":100,\"VolumeType\":\"io1\"}",
			"ValueType": "STRINGIFIED_JSON"
		}, {
			"ActiveValue": "",
			"Name": "EncryptionAtRestOptions",
			"PendingValue": "{\"Enabled\":false}",
			"ValueType": "STRINGIFIED_JSON"
		}, {
			"ActiveValue": "",
			"Name": "NodeToNodeEncryptionOptions",
			"PendingValue": "{\"Enabled\":false}",
			"ValueType": "STRINGIFIED_JSON"
		}, {
			"ActiveValue": "",
			"Name": "OffPeakWindowOptions",
			"PendingValue": "{\"Enabled\":true,\"OffPeakWindow\":{\"WindowStartTime\":{\"Hours\":3,\"Minutes\":0}}}",
			"ValueType": "STRINGIFIED_JSON"
		}, {
			"ActiveValue": "",
			"Name": "SnapshotOptions",
			"PendingValue": "{\"AutomatedSnapshotStartHour\":0}",
			"ValueType": "STRINGIFIED_JSON"
		}, {
			"ActiveValue": "",
			"Name": "SoftwareUpdateOptions",
			"PendingValue": "{\"AutoSoftwareUpdateEnabled\":false}",
			"ValueType": "STRINGIFIED_JSON"
		}, {
			"ActiveValue": "",
			"Name": "AutoTuneOptions",
			"PendingValue": "{\"desiredState\":\"ENABLED\",\"rollbackOnDisable\":\"NO_ROLLBACK\",\"state\":\"ENABLE_IN_PROGRESS\",\"rollbackState\":\"ROLLBACK_OFF\",\"maintenanceSchedules\":[],\"useOffPeakWindow\":false}",
			"ValueType": "STRINGIFIED_JSON"
		}, {
			"ActiveValue": "",
			"Name": "DeploymentStrategyOptions",
			"PendingValue": "{\"DeploymentStrategy\":\"Default\"}",
			"ValueType": "STRINGIFIED_JSON"
		}],
		"NodeToNodeEncryptionOptions": {
			"Enabled": false
		},
		"OffPeakWindowOptions": {
			"Enabled": true,
			"OffPeakWindow": {
				"WindowStartTime": {
					"Hours": 3,
					"Minutes": 0
				}
			}
		},
		"Processing": true,
		"ServiceSoftwareOptions": {
			"AutomatedUpdateDate": 0.0,
			"Cancellable": false,
			"CurrentVersion": "",
			"Description": "There is no software update available for this domain.",
			"NewVersion": "",
			"OptionalDeployment": true,
			"UpdateAvailable": false,
			"UpdateStatus": "COMPLETED"
		},
		"SnapshotOptions": {
			"AutomatedSnapshotStartHour": 0
		},
		"SoftwareUpdateOptions": {
			"AutoSoftwareUpdateEnabled": false
		},
		"UpgradeProcessing": false,
		"VPCOptions": null
	}
}
```

## See Also
<a name="API_CreateDomain_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearch-2021-01-01/CreateDomain)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearch-2021-01-01/CreateDomain)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/CreateDomain)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearch-2021-01-01/CreateDomain)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/CreateDomain)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearch-2021-01-01/CreateDomain)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearch-2021-01-01/CreateDomain)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearch-2021-01-01/CreateDomain)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/opensearch-2021-01-01/CreateDomain)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/CreateDomain)
