---
source_url: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/migration-env-and-system-props.html
---

# Environment variables and system properties changes
<a name="migration-env-and-system-props"></a>

| 1.x Environment Variable | 1.x System Property | 2.x Environment Variable | 2.x System Property |
| --- | --- | --- | --- |
| AWS\_ACCESS\_KEY\_IDAWS\_ACCESS\_KEY | aws.accessKeyId | AWS\_ACCESS\_KEY\_ID | aws.accessKeyId |
| AWS\_SECRET\_KEYAWS\_SECRET\_ACCESS\_KEY | aws.secretKey | AWS\_SECRET\_ACCESS\_KEY | aws.secretAccessKey |
| AWS\_SESSION\_TOKEN | aws.sessionToken | AWS\_SESSION\_TOKEN | aws.sessionToken |
| AWS\_REGION | aws.region | AWS\_REGION | aws.region |
| AWS\_CONFIG\_FILE |   | AWS\_CONFIG\_FILE | aws.configFile |
| AWS\_CREDENTIAL\_PROFILES\_FILE |   | AWS\_SHARED\_CREDENTIALS\_FILE | aws.sharedCredentialsFile |
| AWS\_PROFILE | aws.profile | AWS\_PROFILE | aws.profile |
| AWS\_EC2\_METADATA\_DISABLED | com.amazonaws.sdk.disableEc2Metadata | AWS\_EC2\_METADATA\_DISABLED | aws.disableEc2Metadata |
|   | com.amazonaws.sdk.ec2MetadataServiceEndpointOverride | AWS\_EC2\_METADATA\_SERVICE\_ENDPOINT | aws.ec2MetadataServiceEndpoint |
| AWS\_CONTAINER\_CREDENTIALS\_RELATIVE\_URI |   | AWS\_CONTAINER\_CREDENTIALS\_RELATIVE\_URI | aws.containerCredentialsPath |
| AWS\_CONTAINER\_CREDENTIALS\_FULL\_URI |   | AWS\_CONTAINER\_CREDENTIALS\_FULL\_URI | aws.containerCredentialsFullUri |
| AWS\_CONTAINER\_AUTHORIZATION\_TOKEN |   | AWS\_CONTAINER\_AUTHORIZATION\_TOKEN | aws.containerAuthorizationToken |
| AWS\_CBOR\_DISABLED | com.amazonaws.sdk.disableCbor | CBOR\_ENABLED | aws.cborEnabled |
| AWS\_ION\_BINARY\_DISABLE | com.amazonaws.sdk.disableIonBinary | BINARY\_ION\_ENABLED | aws.binaryIonEnabled |
| AWS\_EXECUTION\_ENV |   | AWS\_EXECUTION\_ENV | aws.executionEnvironment |
|   | com.amazonaws.sdk.disableCertChecking | Not supported ([Request feature](https://github.com/aws/aws-sdk-java-v2/issues/new)) | Not supported ([Request feature](https://github.com/aws/aws-sdk-java-v2/issues/new)) |
|   | com.amazonaws.sdk.enableDefaultMetrics | [Not supported](https://github.com/aws/aws-sdk-java-v2/issues/23) | [Not supported](https://github.com/aws/aws-sdk-java-v2/issues/23) |
|   | com.amazonaws.sdk.enableThrottledRetry | [Not supported](https://github.com/aws/aws-sdk-java-v2/issues/645) | [Not supported](https://github.com/aws/aws-sdk-java-v2/issues/645) |
|   | com.amazonaws.regions.RegionUtils.fileOverride | Not supported ([Request feature](https://github.com/aws/aws-sdk-java-v2/issues/new)) | Not supported ([Request feature](https://github.com/aws/aws-sdk-java-v2/issues/new)) |
|   | com.amazonaws.regions.RegionUtils.disableRemote | Not supported ([Request feature](https://github.com/aws/aws-sdk-java-v2/issues/new)) | Not supported ([Request feature](https://github.com/aws/aws-sdk-java-v2/issues/new)) |
|   | com.amazonaws.services.s3.disableImplicitGlobalClients | Not supported ([Request feature](https://github.com/aws/aws-sdk-java-v2/issues/new)) | Not supported ([Request feature](https://github.com/aws/aws-sdk-java-v2/issues/new)) |
|   | com.amazonaws.sdk.enableInRegionOptimizedMode | Not supported ([Request feature](https://github.com/aws/aws-sdk-java-v2/issues/new)) | Not supported ([Request feature](https://github.com/aws/aws-sdk-java-v2/issues/new)) |
