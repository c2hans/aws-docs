---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DescribeDomains.html
---

# DescribeDomains
<a name="API_DescribeDomains"></a>

Returns domain configuration information about the specified Amazon OpenSearch Service domains.

## Request Syntax
<a name="API_DescribeDomains_RequestSyntax"></a>

```
POST /2021-01-01/opensearch/domain-info HTTP/1.1
Content-type: application/json

{
   "DomainNames": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_DescribeDomains_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DescribeDomains_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [DomainNames](#API_DescribeDomains_RequestSyntax) **   <a name="opensearchservice-DescribeDomains-request-DomainNames"></a>
Array of OpenSearch Service domain names that you want information about. You must specify at least one domain name.
Type: Array of strings
Length Constraints: Minimum length of 3. Maximum length of 28.
Pattern: `[a-z][a-z0-9\-]+`
Required: Yes

## Response Syntax
<a name="API_DescribeDomains_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "DomainStatusList": [
      {
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
   ]
}
```

## Response Elements
<a name="API_DescribeDomains_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DomainStatusList](#API_DescribeDomains_ResponseSyntax) **   <a name="opensearchservice-DescribeDomains-response-DomainStatusList"></a>
The status of the requested domains.
Type: Array of [DomainStatus](API_DomainStatus.md) objects

## Errors
<a name="API_DescribeDomains_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BaseException **
An error occurred while processing the request.
 ** message **
A description of the error.
HTTP Status Code: 400

 ** InternalException **
Request processing failed because of an unknown error, exception, or internal failure.
HTTP Status Code: 500

 ** ValidationException **
An exception for accessing or deleting a resource that doesn't exist.
HTTP Status Code: 400

## Examples
<a name="API_DescribeDomains_Examples"></a>

### Example
<a name="API_DescribeDomains_Example_1"></a>

This example illustrates one usage of DescribeDomains.

#### Sample Request
<a name="API_DescribeDomains_Example_1_Request"></a>

```
POST /2021-01-01/opensearch/domain-info HTTP/1.1
Host: es.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Type: application/json
User-Agent: aws-cli/2.15.13 Python/3.11.6 Windows/10 exe/AMD64 prompt/off command/opensearch.describe-domains
X-Amz-Date: 20240209T222038Z
X-Amz-Security-Token: IQoJb3JpZ2luX2VjEEcaCXVz==
Authorization: AWS4-HMAC-SHA256 Credential=ASIAU/20240209/us-east-1/es/aws4_request, SignedHeaders=content-type;host;x-amz-date;x-amz-security-token, Signature=584535086b2616bb3c1acf1bab39229d2d079327c05c84a0b65b76bed909ed15
Content-Length: 32

{"DomainNames": ["amazonrocks"]}
```

#### Sample Response
<a name="API_DescribeDomains_Example_1_Response"></a>

```
{
   "DomainStatusList":[
      {
         "ARN":"arn:aws:es:us-east-1:123456789012:domain/amazonrocks",
         "AccessPolicies":"{\"Version\":\"2012-10-17\",\"Statement\":[{\"Effect\":\"Allow\",\"Principal\":{\"AWS\":\"*\"},\"Action\":\"es:*\",\"Resource\":\"arn:aws:es:us-east-1:123456789012:domain/amazonrocks/*\"}]}",
         "AdvancedOptions":{
            "indices.fielddata.cache.size":"20",
            "indices.query.bool.max_clause_count":"1024",
            "override_main_response_version":"true",
            "rest.action.multi.allow_explicit_index":"true"
         },
         "AdvancedSecurityOptions":{
            "AnonymousAuthDisableDate":null,
            "AnonymousAuthEnabled":false,
            "Enabled":true,
            "InternalUserDatabaseEnabled":true,
            "SAMLOptions":null
         },
         "AutoTuneOptions":{
            "ErrorMessage":null,
            "State":"ENABLED",
            "UseOffPeakWindow":false
         },
         "ChangeProgressDetails":{
            "ChangeId":"42e55b10-16d3-4a49-a54f-0cf5e9a42244",
            "LastUpdatedTime":1.682458752907E9,
            "Message":null,
            "StartTime":1.682456512645E9
         },
         "ClusterConfig":{
            "ColdStorageOptions":{
               "Enabled":false
            },
            "DedicatedMasterCount":null,
            "DedicatedMasterEnabled":false,
            "DedicatedMasterType":null,
            "InstanceCount":3,
            "InstanceType":"r6g.large.search",
            "WarmCount":null,
            "WarmEnabled":false,
            "WarmStorage":null,
            "WarmType":null,
            "ZoneAwarenessConfig":{
               "AvailabilityZoneCount":3
            },
            "ZoneAwarenessEnabled":true
         },
         "CognitoOptions":{
            "Enabled":false,
            "IdentityPoolId":null,
            "RoleArn":null,
            "UserPoolId":null
         },
         "Created":true,
         "Deleted":false,
         "DomainEndpointOptions":{
            "CustomEndpoint":null,
            "CustomEndpointCertificateArn":null,
            "CustomEndpointEnabled":false,
            "EnforceHTTPS":true,
            "TLSSecurityPolicy":"Policy-Min-TLS-1-0-2019-07"
         },
         "DomainId":"123456789012/amazonrocks",
         "DomainName":"amazonrocks",
         "DomainProcessingStatus":"Active",
         "EBSOptions":{
            "EBSEnabled":true,
            "Iops":null,
            "Throughput":null,
            "VolumeSize":10,
            "VolumeType":"gp2"
         },
         "EncryptionAtRestOptions":{
            "Enabled":true,
            "KmsKeyId":"arn:aws:kms:us-east-1:123456789012:key/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
         },
         "Endpoint":"search-amazonrocks-scuclckuu7bjkhxo6du557d4da.us-east-1.es.amazonaws.com",
         "Endpoints":null,
         "EngineVersion":"OpenSearch_1.3",
         "IPAddressType":"ipv4",
         "LogPublishingOptions":null,
         "ModifyingProperties":[

         ],
         "NodeToNodeEncryptionOptions":{
            "Enabled":true
         },
         "OffPeakWindowOptions":{
            "Enabled":false,
            "OffPeakWindow":{
               "WindowStartTime":{
                  "Hours":0,
                  "Minutes":0
               }
            }
         },
         "Processing":false,
         "ServiceSoftwareOptions":{
            "AutomatedUpdateDate":0.0,
            "Cancellable":false,
            "CurrentVersion":"R20221114-P3",
            "Description":"A newer release OpenSearch_1_3_R20230928-P3 is available.",
            "NewVersion":"OpenSearch_1_3_R20230928-P3",
            "OptionalDeployment":true,
            "UpdateAvailable":true,
            "UpdateStatus":"ELIGIBLE"
         },
         "SnapshotOptions":{
            "AutomatedSnapshotStartHour":null
         },
         "SoftwareUpdateOptions":{
            "AutoSoftwareUpdateEnabled":false
         },
         "UpgradeProcessing":false,
         "VPCOptions":null
      }
   ]
}
```

## See Also
<a name="API_DescribeDomains_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearch-2021-01-01/DescribeDomains)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearch-2021-01-01/DescribeDomains)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/DescribeDomains)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearch-2021-01-01/DescribeDomains)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/DescribeDomains)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearch-2021-01-01/DescribeDomains)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearch-2021-01-01/DescribeDomains)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearch-2021-01-01/DescribeDomains)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/opensearch-2021-01-01/DescribeDomains)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/DescribeDomains)
