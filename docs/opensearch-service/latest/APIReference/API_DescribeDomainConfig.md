---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DescribeDomainConfig.html
---

# DescribeDomainConfig
<a name="API_DescribeDomainConfig"></a>

Returns the configuration of an Amazon OpenSearch Service domain.

## Request Syntax
<a name="API_DescribeDomainConfig_RequestSyntax"></a>

```
GET /2021-01-01/opensearch/domain/{{DomainName}}/config HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeDomainConfig_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DomainName](#API_DescribeDomainConfig_RequestSyntax) **   <a name="opensearchservice-DescribeDomainConfig-request-uri-DomainName"></a>
Name of the OpenSearch Service domain configuration that you want to describe.
Length Constraints: Minimum length of 3. Maximum length of 28.
Pattern: `[a-z][a-z0-9\-]+`
Required: Yes

## Request Body
<a name="API_DescribeDomainConfig_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeDomainConfig_ResponseSyntax"></a>

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
   }
}
```

## Response Elements
<a name="API_DescribeDomainConfig_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DomainConfig](#API_DescribeDomainConfig_ResponseSyntax) **   <a name="opensearchservice-DescribeDomainConfig-response-DomainConfig"></a>
Container for the configuration of the OpenSearch Service domain.
Type: [DomainConfig](API_DomainConfig.md) object

## Errors
<a name="API_DescribeDomainConfig_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BaseException **
An error occurred while processing the request.
 ** message **
A description of the error.
HTTP Status Code: 400

 ** InternalException **
Request processing failed because of an unknown error, exception, or internal failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
An exception for accessing or deleting a resource that doesn't exist.
HTTP Status Code: 409

 ** ValidationException **
An exception for accessing or deleting a resource that doesn't exist.
HTTP Status Code: 400

## Examples
<a name="API_DescribeDomainConfig_Examples"></a>

### Example
<a name="API_DescribeDomainConfig_Example_1"></a>

This example illustrates one usage of DescribeDomainConfig.

#### Sample Request
<a name="API_DescribeDomainConfig_Example_1_Request"></a>

```
GET /2021-01-01/opensearch/domain/movies/config HTTP/1.1
Host: es.us-east-1.amazonaws.com
Accept-Encoding: identity
User-Agent: aws-cli/2.15.13 Python/3.11.6 Windows/10 exe/AMD64 prompt/off command/opensearch.describe-domain-config
X-Amz-Date: 20240209T222604Z
X-Amz-Security-Token: IQoJb3JpZ2luX2VjEEcaCXVz==
Authorization: AWS4-HMAC-SHA256 Credential=ASIAU/20240209/us-east-1/es/aws4_request, SignedHeaders=host;x-amz-date;x-amz-security-token, Signature=9fe055358029051fbcedaf0b82da320529af57cc6efadc35fb9c187b65252704
```

#### Sample Response
<a name="API_DescribeDomainConfig_Example_1_Response"></a>

```
{
   "DomainConfig":{
      "AccessPolicies":{
         "Options":"{\"Version\":\"2012-10-17\",\"Statement\":[{\"Effect\":\"Allow\",\"Principal\":{\"AWS\":\"*\"},\"Action\":\"es:*\",\"Resource\":\"arn:aws:es:us-east-1:123456789012:domain/movies/*\"}]}",
         "Status":{
            "CreationDate":1.655753311082E9,
            "PendingDeletion":false,
            "State":"Active",
            "UpdateDate":1.655754278102E9,
            "UpdateVersion":7
         }
      },
      "AdvancedOptions":{
         "Options":{
            "indices.fielddata.cache.size":"20",
            "indices.query.bool.max_clause_count":"1024",
            "override_main_response_version":"true",
            "rest.action.multi.allow_explicit_index":"true"
         },
         "Status":{
            "CreationDate":1.655753311082E9,
            "PendingDeletion":false,
            "State":"Active",
            "UpdateDate":1.660244135078E9,
            "UpdateVersion":23
         }
      },
      "AdvancedSecurityOptions":{
         "Options":{
            "AnonymousAuthDisableDate":null,
            "AnonymousAuthEnabled":false,
            "Enabled":true,
            "InternalUserDatabaseEnabled":true,
            "SAMLOptions":null
         },
         "Status":{
            "CreationDate":1.655753311082E9,
            "PendingDeletion":false,
            "State":"Active",
            "UpdateDate":1.655754278102E9,
            "UpdateVersion":7
         }
      },
      "AutoTuneOptions":{
         "Options":{
            "DesiredState":"ENABLED",
            "MaintenanceSchedules":[

            ],
            "RollbackOnDisable":"NO_ROLLBACK",
            "UseOffPeakWindow":false
         },
         "Status":{
            "CreationDate":1.655753311082E9,
            "ErrorMessage":null,
            "PendingDeletion":false,
            "State":"ENABLE_IN_PROGRESS",
            "UpdateDate":1.655754278102E9,
            "UpdateVersion":7
         }
      },
      "AutomatedSnapshotPauseOptions":{
         "Options":{
            "Enabled":false,
            "State":"Disabled"
         },
         "Status":{
            "CreationDate":1.655753311082E9,
            "PendingDeletion":false,
            "State":"Active",
            "UpdateDate":1.655753311082E9,
            "UpdateVersion":7
         }
      },
      "ChangeProgressDetails":{
         "ChangeId":"c5cba9b5-1083-45a9-836e-bb2e1ccf4347",
         "LastUpdatedTime":1.682350123826E9,
         "Message":null,
         "StartTime":1.682348498501E9
      },
      "DeploymentStrategyOptions":{
         "Options":{
            "DeploymentStrategy":"Default"
         },
         "Status":{
            "CreationDate":1.655753311082E9,
            "PendingDeletion":false,
            "State":"Active",
            "UpdateDate":1.655754278102E9,
            "UpdateVersion":7
         }
      },
      "ClusterConfig":{
         "Options":{
            "ColdStorageOptions":{
               "Enabled":false
            },
            "DedicatedMasterCount":null,
            "DedicatedMasterEnabled":false,
            "DedicatedMasterType":null,
            "InstanceCount":3,
            "InstanceType":"t3.small.search",
            "WarmCount":null,
            "WarmEnabled":false,
            "WarmStorage":null,
            "WarmType":null,
            "ZoneAwarenessConfig":{
               "AvailabilityZoneCount":3
            },
            "ZoneAwarenessEnabled":true
         },
         "Status":{
            "CreationDate":1.655753311082E9,
            "PendingDeletion":false,
            "State":"Active",
            "UpdateDate":1.655754278102E9,
            "UpdateVersion":7
         }
      },
      "CognitoOptions":{
         "Options":{
            "Enabled":false,
            "IdentityPoolId":null,
            "RoleArn":null,
            "UserPoolId":null
         },
         "Status":{
            "CreationDate":1.707517564627E9,
            "PendingDeletion":false,
            "State":"Active",
            "UpdateDate":1.707517564627E9,
            "UpdateVersion":33
         }
      },
      "DomainEndpointOptions":{
         "Options":{
            "CustomEndpoint":null,
            "CustomEndpointCertificateArn":null,
            "CustomEndpointEnabled":false,
            "EnforceHTTPS":true,
            "TLSSecurityPolicy":"Policy-Min-TLS-1-0-2019-07"
         },
         "Status":{
            "CreationDate":1.655753311082E9,
            "PendingDeletion":false,
            "State":"Active",
            "UpdateDate":1.655754278102E9,
            "UpdateVersion":7
         }
      },
      "EBSOptions":{
         "Options":{
            "EBSEnabled":true,
            "Iops":null,
            "Throughput":null,
            "VolumeSize":10,
            "VolumeType":"gp2"
         },
         "Status":{
            "CreationDate":1.655753311082E9,
            "PendingDeletion":false,
            "State":"Active",
            "UpdateDate":1.655754278102E9,
            "UpdateVersion":7
         }
      },
      "EncryptionAtRestOptions":{
         "Options":{
            "Enabled":true,
            "KmsKeyId":"arn:aws:kms:us-east-1:123456789012:key/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
         },
         "Status":{
            "CreationDate":1.655753311082E9,
            "PendingDeletion":false,
            "State":"Active",
            "UpdateDate":1.655754278102E9,
            "UpdateVersion":7
         }
      },
      "EngineVersion":{
         "Options":"OpenSearch_1.3",
         "Status":{
            "CreationDate":1.655753311082E9,
            "PendingDeletion":false,
            "State":"Active",
            "UpdateDate":1.660245682561E9,
            "UpdateVersion":28
         }
      },
      "IPAddressType":{
         "Options":"ipv4",
         "Status":{
            "CreationDate":1.707517564625E9,
            "PendingDeletion":false,
            "State":"Active",
            "UpdateDate":1.707517564625E9,
            "UpdateVersion":33
         }
      },
      "LogPublishingOptions":{
         "Options":{

         },
         "Status":{
            "CreationDate":1.707517564636E9,
            "PendingDeletion":false,
            "State":"Active",
            "UpdateDate":1.707517564636E9,
            "UpdateVersion":33
         }
      },
      "ModifyingProperties":[

      ],
      "NodeToNodeEncryptionOptions":{
         "Options":{
            "Enabled":true
         },
         "Status":{
            "CreationDate":1.655753311082E9,
            "PendingDeletion":false,
            "State":"Active",
            "UpdateDate":1.655754278102E9,
            "UpdateVersion":7
         }
      },
      "OffPeakWindowOptions":{
         "Options":{
            "Enabled":false,
            "OffPeakWindow":{
               "WindowStartTime":{
                  "Hours":0,
                  "Minutes":0
               }
            }
         },
         "Status":{
            "CreationDate":1.707517564647E9,
            "PendingDeletion":false,
            "State":"Active",
            "UpdateDate":1.707517564647E9,
            "UpdateVersion":33
         }
      },
      "SnapshotOptions":{
         "Options":{
            "AutomatedSnapshotStartHour":0
         },
         "Status":{
            "CreationDate":1.655753311082E9,
            "PendingDeletion":false,
            "State":"Active",
            "UpdateDate":1.655754278102E9,
            "UpdateVersion":7
         }
      },
      "SoftwareUpdateOptions":{
         "Options":{
            "AutoSoftwareUpdateEnabled":false
         },
         "Status":{
            "CreationDate":1.707517564648E9,
            "PendingDeletion":false,
            "State":"Active",
            "UpdateDate":1.707517564648E9,
            "UpdateVersion":33
         }
      },
      "VPCOptions":{
         "Options":{
            "AvailabilityZones":null,
            "SecurityGroupIds":null,
            "SubnetIds":null,
            "VPCId":null
         },
         "Status":{
            "CreationDate":1.707517564626E9,
            "PendingDeletion":false,
            "State":"Active",
            "UpdateDate":1.707517564626E9,
            "UpdateVersion":33
         }
      }
   }
}
```

## See Also
<a name="API_DescribeDomainConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearch-2021-01-01/DescribeDomainConfig)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearch-2021-01-01/DescribeDomainConfig)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/DescribeDomainConfig)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearch-2021-01-01/DescribeDomainConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/DescribeDomainConfig)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearch-2021-01-01/DescribeDomainConfig)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearch-2021-01-01/DescribeDomainConfig)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearch-2021-01-01/DescribeDomainConfig)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/opensearch-2021-01-01/DescribeDomainConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/DescribeDomainConfig)
