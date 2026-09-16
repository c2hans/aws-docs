---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_CreateResourceDataSync.html
---

# CreateResourceDataSync
<a name="API_CreateResourceDataSync"></a>

A resource data sync helps you view data from multiple sources in a single location. AWS Systems Manager offers two types of resource data sync: `SyncToDestination` and `SyncFromSource`.

You can configure Systems Manager Inventory to use the `SyncToDestination` type to synchronize Inventory data from multiple AWS Regions to a single Amazon Simple Storage Service (Amazon S3) bucket. For more information, see [Creating a resource data sync for Inventory](https://docs.aws.amazon.com/systems-manager/latest/userguide/inventory-create-resource-data-sync.html) in the * AWS Systems Manager User Guide*.

You can configure Systems Manager Explorer to use the `SyncFromSource` type to synchronize operational work items (OpsItems) and operational data (OpsData) from multiple AWS Regions to a single Amazon S3 bucket. This type can synchronize OpsItems and OpsData from multiple AWS accounts and AWS Regions or `EntireOrganization` by using AWS Organizations. For more information, see [Setting up Systems Manager Explorer to display data from multiple accounts and Regions](https://docs.aws.amazon.com/systems-manager/latest/userguide/Explorer-resource-data-sync.html) in the * AWS Systems Manager User Guide*.

A resource data sync is an asynchronous operation that returns immediately. After a successful initial sync is completed, the system continuously syncs data. To check the status of a sync, use the [ListResourceDataSync](API_ListResourceDataSync.md).

**Note**
By default, data isn't encrypted in Amazon S3. We strongly recommend that you enable encryption in Amazon S3 to ensure secure data storage. We also recommend that you secure access to the Amazon S3 bucket by creating a restrictive bucket policy.

## Request Syntax
<a name="API_CreateResourceDataSync_RequestSyntax"></a>

```
{
   "S3Destination": {
      "AWSKMSKeyARN": "{{string}}",
      "BucketName": "{{string}}",
      "DestinationDataSharing": {
         "DestinationDataSharingType": "{{string}}"
      },
      "Prefix": "{{string}}",
      "Region": "{{string}}",
      "SyncFormat": "{{string}}"
   },
   "SyncName": "{{string}}",
   "SyncSource": {
      "AwsOrganizationsSource": {
         "OrganizationalUnits": [
            {
               "OrganizationalUnitId": "{{string}}"
            }
         ],
         "OrganizationSourceType": "{{string}}"
      },
      "EnableAllOpsDataSources": {{boolean}},
      "IncludeFutureRegions": {{boolean}},
      "SourceRegions": [ "{{string}}" ],
      "SourceType": "{{string}}"
   },
   "SyncType": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateResourceDataSync_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [S3Destination](#API_CreateResourceDataSync_RequestSyntax) **   <a name="systemsmanager-CreateResourceDataSync-request-S3Destination"></a>
Amazon S3 configuration details for the sync. This parameter is required if the `SyncType` value is SyncToDestination.
Type: [ResourceDataSyncS3Destination](API_ResourceDataSyncS3Destination.md) object
Required: No

 ** [SyncName](#API_CreateResourceDataSync_RequestSyntax) **   <a name="systemsmanager-CreateResourceDataSync-request-SyncName"></a>
A name for the configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** [SyncSource](#API_CreateResourceDataSync_RequestSyntax) **   <a name="systemsmanager-CreateResourceDataSync-request-SyncSource"></a>
Specify information about the data sources to synchronize. This parameter is required if the `SyncType` value is SyncFromSource.
Type: [ResourceDataSyncSource](API_ResourceDataSyncSource.md) object
Required: No

 ** [SyncType](#API_CreateResourceDataSync_RequestSyntax) **   <a name="systemsmanager-CreateResourceDataSync-request-SyncType"></a>
Specify `SyncToDestination` to create a resource data sync that synchronizes data to an S3 bucket for Inventory. If you specify `SyncToDestination`, you must provide a value for `S3Destination`. Specify `SyncFromSource` to synchronize data from a single account and multiple Regions, or multiple AWS accounts and AWS Regions, as listed in AWS Organizations for Explorer. If you specify `SyncFromSource`, you must provide a value for `SyncSource`. The default value is `SyncToDestination`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

## Response Elements
<a name="API_CreateResourceDataSync_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_CreateResourceDataSync_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

 ** ResourceDataSyncAlreadyExistsException **
A sync configuration with the same name already exists.
HTTP Status Code: 400

 ** ResourceDataSyncCountExceededException **
You have exceeded the allowed maximum sync configurations.
HTTP Status Code: 400

 ** ResourceDataSyncInvalidConfigurationException **
The specified sync configuration is invalid.
HTTP Status Code: 400

## Examples
<a name="API_CreateResourceDataSync_Examples"></a>

### Example
<a name="API_CreateResourceDataSync_Example_1"></a>

This example illustrates one usage of CreateResourceDataSync.

#### Sample Request
<a name="API_CreateResourceDataSync_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-east-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: AmazonSSM.CreateResourceDataSync
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/1.17.12 Python/3.6.8 Darwin/18.7.0 botocore/1.14.12
X-Amz-Date: 20240327T173437Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240327/us-east-2/ssm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 186

{
    "SyncName": "Example",
    "S3Destination": {
        "BucketName": "amzn-s3-demo-bucket",
        "Prefix": "amzn-s3-demo-bucket-prefix",
        "SyncFormat": "JsonSerDe",
        "Region": "us-east-2"
    },
    "SyncType": "SyncToDestination"
}
```

#### Sample Response
<a name="API_CreateResourceDataSync_Example_1_Response"></a>

```
{}
```

## See Also
<a name="API_CreateResourceDataSync_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/CreateResourceDataSync)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/CreateResourceDataSync)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/CreateResourceDataSync)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/CreateResourceDataSync)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/CreateResourceDataSync)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/CreateResourceDataSync)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/CreateResourceDataSync)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/CreateResourceDataSync)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/CreateResourceDataSync)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/CreateResourceDataSync)
