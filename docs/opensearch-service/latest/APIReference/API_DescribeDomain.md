---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DescribeDomain.html
---

# DescribeDomain
<a name="API_DescribeDomain"></a>

Describes the domain configuration for the specified Amazon OpenSearch Service domain, including the domain ID, domain service endpoint, and domain ARN.

## Request Syntax
<a name="API_DescribeDomain_RequestSyntax"></a>

```
GET /2021-01-01/opensearch/domain/{{DomainName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeDomain_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DomainName](#API_DescribeDomain_RequestSyntax) **   <a name="opensearchservice-DescribeDomain-request-uri-DomainName"></a>
The name of the domain that you want information about.
Length Constraints: Minimum length of 3. Maximum length of 28.
Pattern: `[a-z][a-z0-9\-]+`
Required: Yes

## Request Body
<a name="API_DescribeDomain_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeDomain_ResponseSyntax"></a>

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
<a name="API_DescribeDomain_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DomainStatus](#API_DescribeDomain_ResponseSyntax) **   <a name="opensearchservice-DescribeDomain-response-DomainStatus"></a>
List that contains the status of each specified OpenSearch Service domain.
Type: [DomainStatus](API_DomainStatus.md) object

## Errors
<a name="API_DescribeDomain_Errors"></a>

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
<a name="API_DescribeDomain_Examples"></a>

### Example
<a name="API_DescribeDomain_Example_1"></a>

This example illustrates one usage of DescribeDomain.

#### Sample Request
<a name="API_DescribeDomain_Example_1_Request"></a>

```
GET /2021-01-01/opensearch/domain/movies HTTP/1.1
Host: es.us-east-1.amazonaws.com
Accept-Encoding: identity
User-Agent: aws-cli/2.15.13 Python/3.11.6 Windows/10 exe/AMD64 prompt/off command/opensearch.describe-domain
X-Amz-Date: 20240209T222243Z
X-Amz-Security-Token: IQoJb3JpZ2luX2VjEEcaCXVz==
Authorization: AWS4-HMAC-SHA256 Credential=ASIAU/20240209/us-east-1/es/aws4_request, SignedHeaders=host;x-amz-date;x-amz-security-token, Signature=30d6a7dc73d1e649559866aff99b074e516e06e5e0b5d94f103ef608356c7d4e
```

#### Sample Response
<a name="API_DescribeDomain_Example_1_Response"></a>

```
{
   "DomainStatus":{
      "ARN":"arn:aws:es:us-east-1:123456789012:domain/movies",
      "AccessPolicies":"{\"Version\":\"2012-10-17\",\"Statement\":[{\"Effect\":\"Allow\",\"Principal\":{\"AWS\":\"*\"},\"Action\":\"es:*\",\"Resource\":\"arn:aws:es:us-east-1:123456789012:domain/movies/*\"}]}",
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
         "State":"ENABLE_IN_PROGRESS",
         "UseOffPeakWindow":false
      },
      "AutomatedSnapshotPauseOptions":{
         "Enabled":false,
         "State":"Disabled"
      },
      "ChangeProgressDetails":{
         "ChangeId":"c5cba9b5-1083-45a9-836e-bb2e1ccf4347",
         "LastUpdatedTime":1.682350123826E9,
         "Message":null,
         "StartTime":1.682348498501E9
      },
      "ClusterConfig":{
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
      "CognitoOptions":{
         "Enabled":false,
         "IdentityPoolId":null,
         "RoleArn":null,
         "UserPoolId":null
      },
      "Created":true,
      "Deleted":false,
      "DeploymentStrategyOptions":{
         "DeploymentStrategy":"Default"
      },
      "DomainEndpointOptions":{
         "CustomEndpoint":null,
         "CustomEndpointCertificateArn":null,
         "CustomEndpointEnabled":false,
         "EnforceHTTPS":true,
         "TLSSecurityPolicy":"Policy-Min-TLS-1-0-2019-07"
      },
      "DomainId":"123456789012/movies",
      "DomainName":"movies",
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
      "Endpoint":"search-movies-o36agaraperqwzp7s7vv6xfzwa.us-east-1.es.amazonaws.com",
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
}
```

## See Also
<a name="API_DescribeDomain_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearch-2021-01-01/DescribeDomain)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearch-2021-01-01/DescribeDomain)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/DescribeDomain)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearch-2021-01-01/DescribeDomain)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/DescribeDomain)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearch-2021-01-01/DescribeDomain)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearch-2021-01-01/DescribeDomain)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearch-2021-01-01/DescribeDomain)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/opensearch-2021-01-01/DescribeDomain)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/DescribeDomain)
