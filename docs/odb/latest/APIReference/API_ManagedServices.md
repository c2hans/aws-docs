---
source_url: https://docs.aws.amazon.com/odb/latest/APIReference/API_ManagedServices.html
---

# ManagedServices
<a name="API_ManagedServices"></a>

The managed services configuration for the ODB network.

## Contents
<a name="API_ManagedServices_Contents"></a>

 ** crossRegionS3RestoreSourcesAccess **   <a name="odb-Type-ManagedServices-crossRegionS3RestoreSourcesAccess"></a>
The access configuration for the cross-Region Amazon S3 database restore source.
Type: Array of [CrossRegionS3RestoreSourcesAccess](API_CrossRegionS3RestoreSourcesAccess.md) objects
Required: No

 ** kmsAccess **   <a name="odb-Type-ManagedServices-kmsAccess"></a>
The AWS Key Management Service (KMS) access configuration.
Type: [KmsAccess](API_KmsAccess.md) object
Required: No

 ** managedS3BackupAccess **   <a name="odb-Type-ManagedServices-managedS3BackupAccess"></a>
The managed Amazon S3 backup access configuration.
Type: [ManagedS3BackupAccess](API_ManagedS3BackupAccess.md) object
Required: No

 ** managedServicesIpv4Cidrs **   <a name="odb-Type-ManagedServices-managedServicesIpv4Cidrs"></a>
The IPv4 CIDR blocks for the managed services.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 1024 items.
Required: No

 ** resourceGatewayArn **   <a name="odb-Type-ManagedServices-resourceGatewayArn"></a>
The Amazon Resource Name (ARN) of the resource gateway.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:(?:aws|aws-cn|aws-us-gov|aws-iso-{0,1}[a-z]{0,1}):[a-z0-9-]+:[a-z0-9-]*:[0-9]+:[a-z0-9-]+/[a-z0-9-_]{6,64}`
Required: No

 ** s3Access **   <a name="odb-Type-ManagedServices-s3Access"></a>
The Amazon S3 access configuration.
Type: [S3Access](API_S3Access.md) object
Required: No

 ** serviceNetworkArn **   <a name="odb-Type-ManagedServices-serviceNetworkArn"></a>
The Amazon Resource Name (ARN) of the service network.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:(?:aws|aws-cn|aws-us-gov|aws-iso-{0,1}[a-z]{0,1}):[a-z0-9-]+:[a-z0-9-]*:[0-9]+:[a-z0-9-]+/[a-z0-9-_]{6,64}`
Required: No

 ** serviceNetworkEndpoint **   <a name="odb-Type-ManagedServices-serviceNetworkEndpoint"></a>
The service network endpoint configuration.
Type: [ServiceNetworkEndpoint](API_ServiceNetworkEndpoint.md) object
Required: No

 ** stsAccess **   <a name="odb-Type-ManagedServices-stsAccess"></a>
The AWS Security Token Service (STS) access configuration.
Type: [StsAccess](API_StsAccess.md) object
Required: No

 ** zeroEtlAccess **   <a name="odb-Type-ManagedServices-zeroEtlAccess"></a>
The Zero-ETL access configuration.
Type: [ZeroEtlAccess](API_ZeroEtlAccess.md) object
Required: No

## See Also
<a name="API_ManagedServices_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/odb-2024-08-20/ManagedServices)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/odb-2024-08-20/ManagedServices)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/odb-2024-08-20/ManagedServices)
