---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeStorageConfiguration.html
---

# DescribeStorageConfiguration
<a name="API_DescribeStorageConfiguration"></a>

Retrieves information about the storage configuration for AWS IoT SiteWise.

## Request Syntax
<a name="API_DescribeStorageConfiguration_RequestSyntax"></a>

```
GET /configuration/account/storage HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeStorageConfiguration_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DescribeStorageConfiguration_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeStorageConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "configurationStatus": {
      "error": {
         "code": "string",
         "message": "string"
      },
      "state": "string"
   },
   "disallowIngestNullNaN": boolean,
   "disassociatedDataStorage": "string",
   "lastUpdateDate": number,
   "multiLayerStorage": {
      "customerManagedS3Storage": {
         "roleArn": "string",
         "s3ResourceArn": "string"
      }
   },
   "retentionPeriod": {
      "numberOfDays": number,
      "unlimited": boolean
   },
   "storageType": "string",
   "warmTier": "string",
   "warmTierRetentionPeriod": {
      "numberOfDays": number,
      "unlimited": boolean
   }
}
```

## Response Elements
<a name="API_DescribeStorageConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [configurationStatus](#API_DescribeStorageConfiguration_ResponseSyntax) **   <a name="iotsitewise-DescribeStorageConfiguration-response-configurationStatus"></a>
Contains current status information for the configuration.
Type: [ConfigurationStatus](API_ConfigurationStatus.md) object

 ** [disallowIngestNullNaN](#API_DescribeStorageConfiguration_ResponseSyntax) **   <a name="iotsitewise-DescribeStorageConfiguration-response-disallowIngestNullNaN"></a>
Describes the configuration for ingesting NULL and NaN data. By default the feature is allowed. The feature is disallowed if the value is `true`.
Type: Boolean

 ** [disassociatedDataStorage](#API_DescribeStorageConfiguration_ResponseSyntax) **   <a name="iotsitewise-DescribeStorageConfiguration-response-disassociatedDataStorage"></a>
Contains the storage configuration for time series (data streams) that aren't associated with asset properties. The `disassociatedDataStorage` can be one of the following values:
+  `ENABLED` – AWS IoT SiteWise accepts time series that aren't associated with asset properties.
**Important**
After the `disassociatedDataStorage` is enabled, you can't disable it.
+  `DISABLED` – AWS IoT SiteWise doesn't accept time series (data streams) that aren't associated with asset properties.
For more information, see [Data streams](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/data-streams.html) in the * AWS IoT SiteWise User Guide*.
Type: String
Valid Values: `ENABLED | DISABLED`

 ** [lastUpdateDate](#API_DescribeStorageConfiguration_ResponseSyntax) **   <a name="iotsitewise-DescribeStorageConfiguration-response-lastUpdateDate"></a>
The date the storage configuration was last updated, in Unix epoch time.
Type: Timestamp

 ** [multiLayerStorage](#API_DescribeStorageConfiguration_ResponseSyntax) **   <a name="iotsitewise-DescribeStorageConfiguration-response-multiLayerStorage"></a>
Contains information about the storage destination.
Type: [MultiLayerStorage](API_MultiLayerStorage.md) object

 ** [retentionPeriod](#API_DescribeStorageConfiguration_ResponseSyntax) **   <a name="iotsitewise-DescribeStorageConfiguration-response-retentionPeriod"></a>
The number of days your data is kept in the hot tier. By default, your data is kept indefinitely in the hot tier.
Type: [RetentionPeriod](API_RetentionPeriod.md) object

 ** [storageType](#API_DescribeStorageConfiguration_ResponseSyntax) **   <a name="iotsitewise-DescribeStorageConfiguration-response-storageType"></a>
The storage tier that you specified for your data. The `storageType` parameter can be one of the following values:
+  `SITEWISE_DEFAULT_STORAGE` – AWS IoT SiteWise saves your data into the hot tier. The hot tier is a service-managed database.
+  `MULTI_LAYER_STORAGE` – AWS IoT SiteWise saves your data in both the cold tier and the hot tier. The cold tier is a customer-managed Amazon S3 bucket.
Type: String
Valid Values: `SITEWISE_DEFAULT_STORAGE | MULTI_LAYER_STORAGE`

 ** [warmTier](#API_DescribeStorageConfiguration_ResponseSyntax) **   <a name="iotsitewise-DescribeStorageConfiguration-response-warmTier"></a>
A service managed storage tier optimized for analytical queries. It stores periodically uploaded, buffered and historical data ingested with the CreaeBulkImportJob API.
Type: String
Valid Values: `ENABLED | DISABLED`

 ** [warmTierRetentionPeriod](#API_DescribeStorageConfiguration_ResponseSyntax) **   <a name="iotsitewise-DescribeStorageConfiguration-response-warmTierRetentionPeriod"></a>
Set this period to specify how long your data is stored in the warm tier before it is deleted. You can set this only if cold tier is enabled.
Type: [WarmTierRetentionPeriod](API_WarmTierRetentionPeriod.md) object

## Errors
<a name="API_DescribeStorageConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictingOperationException **
Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.
 ** resourceArn **
The ARN of the resource that conflicts with this operation.
 ** resourceId **
The ID of the resource that conflicts with this operation.
HTTP Status Code: 409

 ** InternalFailureException **
 AWS IoT SiteWise can't process your request right now. Try again later.
HTTP Status Code: 500

 ** InvalidRequestException **
The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.
HTTP Status Code: 400

 ** LimitExceededException **
You've reached the quota for a resource. For example, this can occur if you're trying to associate more than the allowed number of child assets or attempting to create more than the allowed number of properties for an asset model.
For more information, see [Quotas](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html) in the * AWS IoT SiteWise User Guide*.
HTTP Status Code: 410

 ** ResourceNotFoundException **
The requested resource can't be found.
HTTP Status Code: 404

 ** ThrottlingException **
Your request exceeded a rate limit. For example, you might have exceeded the number of AWS IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.
For more information, see [Quotas](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html) in the * AWS IoT SiteWise User Guide*.
HTTP Status Code: 429

## See Also
<a name="API_DescribeStorageConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotsitewise-2019-12-02/DescribeStorageConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotsitewise-2019-12-02/DescribeStorageConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/DescribeStorageConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotsitewise-2019-12-02/DescribeStorageConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/DescribeStorageConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotsitewise-2019-12-02/DescribeStorageConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotsitewise-2019-12-02/DescribeStorageConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotsitewise-2019-12-02/DescribeStorageConfiguration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iotsitewise-2019-12-02/DescribeStorageConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/DescribeStorageConfiguration)
