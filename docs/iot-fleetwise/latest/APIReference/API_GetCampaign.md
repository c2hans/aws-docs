---
source_url: https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_GetCampaign.html
---

# GetCampaign
<a name="API_GetCampaign"></a>

**Important**
 AWS IoT FleetWise is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS IoT FleetWise availability change](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/iotfleetwise-availability-change.html).

 Retrieves information about a campaign.

## Request Syntax
<a name="API_GetCampaign_RequestSyntax"></a>

```
{
   "name": "{{string}}"
}
```

## Request Parameters
<a name="API_GetCampaign_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [name](#API_GetCampaign_RequestSyntax) **   <a name="iotfleetwise-GetCampaign-request-name"></a>
 The name of the campaign to retrieve information about.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z\d\-_:]+`
Required: Yes

## Response Syntax
<a name="API_GetCampaign_ResponseSyntax"></a>

```
{
   "arn": "string",
   "collectionScheme": { ... },
   "compression": "string",
   "creationTime": number,
   "dataDestinationConfigs": [
      { ... }
   ],
   "dataExtraDimensions": [ "string" ],
   "dataPartitions": [
      {
         "id": "string",
         "storageOptions": {
            "maximumSize": {
               "unit": "string",
               "value": number
            },
            "minimumTimeToLive": {
               "unit": "string",
               "value": number
            },
            "storageLocation": "string"
         },
         "uploadOptions": {
            "conditionLanguageVersion": number,
            "expression": "string"
         }
      }
   ],
   "description": "string",
   "diagnosticsMode": "string",
   "expiryTime": number,
   "lastModificationTime": number,
   "name": "string",
   "postTriggerCollectionDuration": number,
   "priority": number,
   "signalCatalogArn": "string",
   "signalsToCollect": [
      {
         "dataPartitionId": "string",
         "maxSampleCount": number,
         "minimumSamplingIntervalMs": number,
         "name": "string"
      }
   ],
   "signalsToFetch": [
      {
         "actions": [ "string" ],
         "conditionLanguageVersion": number,
         "fullyQualifiedName": "string",
         "signalFetchConfig": { ... }
      }
   ],
   "spoolingMode": "string",
   "startTime": number,
   "status": "string",
   "targetArn": "string"
}
```

## Response Elements
<a name="API_GetCampaign_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_GetCampaign_ResponseSyntax) **   <a name="iotfleetwise-GetCampaign-response-arn"></a>
 The Amazon Resource Name (ARN) of the campaign.
Type: String
Pattern: `arn:aws:iotfleetwise:[a-z0-9-]+:[0-9]{12}:campaign/[a-zA-Z\d\-_:]{1,100}`

 ** [collectionScheme](#API_GetCampaign_ResponseSyntax) **   <a name="iotfleetwise-GetCampaign-response-collectionScheme"></a>
 Information about the data collection scheme associated with the campaign.
Type: [CollectionScheme](API_CollectionScheme.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [compression](#API_GetCampaign_ResponseSyntax) **   <a name="iotfleetwise-GetCampaign-response-compression"></a>
 Whether to compress signals before transmitting data to AWS IoT FleetWise. If `OFF` is specified, the signals aren't compressed. If it's not specified, `SNAPPY` is used.
Type: String
Valid Values: `OFF | SNAPPY`

 ** [creationTime](#API_GetCampaign_ResponseSyntax) **   <a name="iotfleetwise-GetCampaign-response-creationTime"></a>
 The time the campaign was created in seconds since epoch (January 1, 1970 at midnight UTC time).
Type: Timestamp

 ** [dataDestinationConfigs](#API_GetCampaign_ResponseSyntax) **   <a name="iotfleetwise-GetCampaign-response-dataDestinationConfigs"></a>
The destination where the campaign sends data. You can send data to an MQTT topic, or store it in Amazon S3 or Amazon Timestream.
MQTT is the publish/subscribe messaging protocol used by AWS IoT to communicate with your devices.
Amazon S3 optimizes the cost of data storage and provides additional mechanisms to use vehicle data, such as data lakes, centralized data storage, data processing pipelines, and analytics.
You can use Amazon Timestream to access and analyze time series data, and Timestream to query vehicle data so that you can identify trends and patterns.
Type: Array of [DataDestinationConfig](API_DataDestinationConfig.md) objects
Array Members: Minimum number of 1 item. Maximum number of 3 items.

 ** [dataExtraDimensions](#API_GetCampaign_ResponseSyntax) **   <a name="iotfleetwise-GetCampaign-response-dataExtraDimensions"></a>
 A list of vehicle attributes associated with the campaign.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Length Constraints: Minimum length of 1. Maximum length of 150.
Pattern: `[a-zA-Z0-9_.]+`

 ** [dataPartitions](#API_GetCampaign_ResponseSyntax) **   <a name="iotfleetwise-GetCampaign-response-dataPartitions"></a>
The data partitions associated with the signals collected from the vehicle.
Type: Array of [DataPartition](API_DataPartition.md) objects
Array Members: Minimum number of 1 item. Maximum number of 20 items.

 ** [description](#API_GetCampaign_ResponseSyntax) **   <a name="iotfleetwise-GetCampaign-response-description"></a>
The description of the campaign.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\u0000-\u001F\u007F]+`

 ** [diagnosticsMode](#API_GetCampaign_ResponseSyntax) **   <a name="iotfleetwise-GetCampaign-response-diagnosticsMode"></a>
 Option for a vehicle to send diagnostic trouble codes to AWS IoT FleetWise.
Type: String
Valid Values: `OFF | SEND_ACTIVE_DTCS`

 ** [expiryTime](#API_GetCampaign_ResponseSyntax) **   <a name="iotfleetwise-GetCampaign-response-expiryTime"></a>
 The time the campaign expires, in seconds since epoch (January 1, 1970 at midnight UTC time). Vehicle data won't be collected after the campaign expires.
Type: Timestamp

 ** [lastModificationTime](#API_GetCampaign_ResponseSyntax) **   <a name="iotfleetwise-GetCampaign-response-lastModificationTime"></a>
The last time the campaign was modified.
Type: Timestamp

 ** [name](#API_GetCampaign_ResponseSyntax) **   <a name="iotfleetwise-GetCampaign-response-name"></a>
The name of the campaign.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z\d\-_:]+`

 ** [postTriggerCollectionDuration](#API_GetCampaign_ResponseSyntax) **   <a name="iotfleetwise-GetCampaign-response-postTriggerCollectionDuration"></a>
 How long (in seconds) to collect raw data after a triggering event initiates the collection.
Type: Long
Valid Range: Minimum value of 0. Maximum value of 4294967295.

 ** [priority](#API_GetCampaign_ResponseSyntax) **   <a name="iotfleetwise-GetCampaign-response-priority"></a>
 A number indicating the priority of one campaign over another campaign for a certain vehicle or fleet. A campaign with the lowest value is deployed to vehicles before any other campaigns.
Type: Integer
Valid Range: Minimum value of 0.

 ** [signalCatalogArn](#API_GetCampaign_ResponseSyntax) **   <a name="iotfleetwise-GetCampaign-response-signalCatalogArn"></a>
 The ARN of a signal catalog.
Type: String

 ** [signalsToCollect](#API_GetCampaign_ResponseSyntax) **   <a name="iotfleetwise-GetCampaign-response-signalsToCollect"></a>
 Information about a list of signals to collect data on.
Type: Array of [SignalInformation](API_SignalInformation.md) objects
Array Members: Minimum number of 0 items. Maximum number of 1000 items.

 ** [signalsToFetch](#API_GetCampaign_ResponseSyntax) **   <a name="iotfleetwise-GetCampaign-response-signalsToFetch"></a>
Information about a list of signals to fetch data from.
Type: Array of [SignalFetchInformation](API_SignalFetchInformation.md) objects
Array Members: Minimum number of 1 item. Maximum number of 2 items.

 ** [spoolingMode](#API_GetCampaign_ResponseSyntax) **   <a name="iotfleetwise-GetCampaign-response-spoolingMode"></a>
 Whether to store collected data after a vehicle lost a connection with the cloud. After a connection is re-established, the data is automatically forwarded to AWS IoT FleetWise.
Type: String
Valid Values: `OFF | TO_DISK`

 ** [startTime](#API_GetCampaign_ResponseSyntax) **   <a name="iotfleetwise-GetCampaign-response-startTime"></a>
 The time, in milliseconds, to deliver a campaign after it was approved.
Type: Timestamp

 ** [status](#API_GetCampaign_ResponseSyntax) **   <a name="iotfleetwise-GetCampaign-response-status"></a>
The state of the campaign. The status can be one of: `CREATING`, `WAITING_FOR_APPROVAL`, `RUNNING`, and `SUSPENDED`.
Type: String
Valid Values: `CREATING | WAITING_FOR_APPROVAL | RUNNING | SUSPENDED`

 ** [targetArn](#API_GetCampaign_ResponseSyntax) **   <a name="iotfleetwise-GetCampaign-response-targetArn"></a>
 The ARN of the vehicle or the fleet targeted by the campaign.
Type: String

## Errors
<a name="API_GetCampaign_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient permission to perform this action.
HTTP Status Code: 400

 ** InternalServerException **
The request couldn't be completed because the server temporarily failed.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the command.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The resource wasn't found.
 ** resourceId **
The identifier of the resource that wasn't found.
 ** resourceType **
The type of resource that wasn't found.
HTTP Status Code: 400

 ** ThrottlingException **
The request couldn't be completed due to throttling.
 ** quotaCode **
The quota identifier of the applied throttling rules for this request.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the command.
 ** serviceCode **
The code for the service that couldn't be completed due to throttling.
HTTP Status Code: 400

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
 ** fieldList **
The list of fields that fail to satisfy the constraints specified by an AWS service.
 ** reason **
The reason the input failed to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_GetCampaign_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotfleetwise-2021-06-17/GetCampaign)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotfleetwise-2021-06-17/GetCampaign)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotfleetwise-2021-06-17/GetCampaign)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotfleetwise-2021-06-17/GetCampaign)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotfleetwise-2021-06-17/GetCampaign)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotfleetwise-2021-06-17/GetCampaign)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotfleetwise-2021-06-17/GetCampaign)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotfleetwise-2021-06-17/GetCampaign)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iotfleetwise-2021-06-17/GetCampaign)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotfleetwise-2021-06-17/GetCampaign)
