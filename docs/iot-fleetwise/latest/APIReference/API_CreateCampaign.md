---
source_url: https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_CreateCampaign.html
---

# CreateCampaign
<a name="API_CreateCampaign"></a>

**Important**
 AWS IoT FleetWise is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS IoT FleetWise availability change](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/iotfleetwise-availability-change.html).

Creates an orchestration of data collection rules. The AWS IoT FleetWise Edge Agent software running in vehicles uses campaigns to decide how to collect and transfer data to the cloud. You create campaigns in the cloud. After you or your team approve campaigns, AWS IoT FleetWise automatically deploys them to vehicles.

For more information, see [Collect and transfer data with campaigns](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/campaigns.html) in the * AWS IoT FleetWise Developer Guide*.

## Request Syntax
<a name="API_CreateCampaign_RequestSyntax"></a>

```
{
   "collectionScheme": { ... },
   "compression": "{{string}}",
   "dataDestinationConfigs": [
      { ... }
   ],
   "dataExtraDimensions": [ "{{string}}" ],
   "dataPartitions": [
      {
         "id": "{{string}}",
         "storageOptions": {
            "maximumSize": {
               "unit": "{{string}}",
               "value": {{number}}
            },
            "minimumTimeToLive": {
               "unit": "{{string}}",
               "value": {{number}}
            },
            "storageLocation": "{{string}}"
         },
         "uploadOptions": {
            "conditionLanguageVersion": {{number}},
            "expression": "{{string}}"
         }
      }
   ],
   "description": "{{string}}",
   "diagnosticsMode": "{{string}}",
   "expiryTime": {{number}},
   "name": "{{string}}",
   "postTriggerCollectionDuration": {{number}},
   "priority": {{number}},
   "signalCatalogArn": "{{string}}",
   "signalsToCollect": [
      {
         "dataPartitionId": "{{string}}",
         "maxSampleCount": {{number}},
         "minimumSamplingIntervalMs": {{number}},
         "name": "{{string}}"
      }
   ],
   "signalsToFetch": [
      {
         "actions": [ "{{string}}" ],
         "conditionLanguageVersion": {{number}},
         "fullyQualifiedName": "{{string}}",
         "signalFetchConfig": { ... }
      }
   ],
   "spoolingMode": "{{string}}",
   "startTime": {{number}},
   "tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "targetArn": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateCampaign_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [collectionScheme](#API_CreateCampaign_RequestSyntax) **   <a name="iotfleetwise-CreateCampaign-request-collectionScheme"></a>
 The data collection scheme associated with the campaign. You can specify a scheme that collects data based on time or an event.
Type: [CollectionScheme](API_CollectionScheme.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** [compression](#API_CreateCampaign_RequestSyntax) **   <a name="iotfleetwise-CreateCampaign-request-compression"></a>
Determines whether to compress signals before transmitting data to AWS IoT FleetWise. If you don't want to compress the signals, use `OFF`. If it's not specified, `SNAPPY` is used.
Default: `SNAPPY`
Type: String
Valid Values: `OFF | SNAPPY`
Required: No

 ** [dataDestinationConfigs](#API_CreateCampaign_RequestSyntax) **   <a name="iotfleetwise-CreateCampaign-request-dataDestinationConfigs"></a>
The destination where the campaign sends data. You can send data to an MQTT topic, or store it in Amazon S3 or Amazon Timestream.
MQTT is the publish/subscribe messaging protocol used by AWS IoT to communicate with your devices.
Amazon S3 optimizes the cost of data storage and provides additional mechanisms to use vehicle data, such as data lakes, centralized data storage, data processing pipelines, and analytics. AWS IoT FleetWise supports at-least-once file delivery to S3. Your vehicle data is stored on multiple AWS IoT FleetWise servers for redundancy and high availability.
You can use Amazon Timestream to access and analyze time series data, and Timestream to query vehicle data so that you can identify trends and patterns.
Type: Array of [DataDestinationConfig](API_DataDestinationConfig.md) objects
Array Members: Minimum number of 1 item. Maximum number of 3 items.
Required: No

 ** [dataExtraDimensions](#API_CreateCampaign_RequestSyntax) **   <a name="iotfleetwise-CreateCampaign-request-dataExtraDimensions"></a>
A list of vehicle attributes to associate with a campaign.
Enrich the data with specified vehicle attributes. For example, add `make` and `model` to the campaign, and AWS IoT FleetWise will associate the data with those attributes as dimensions in Amazon Timestream. You can then query the data against `make` and `model`.
Default: An empty array
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Length Constraints: Minimum length of 1. Maximum length of 150.
Pattern: `[a-zA-Z0-9_.]+`
Required: No

 ** [dataPartitions](#API_CreateCampaign_RequestSyntax) **   <a name="iotfleetwise-CreateCampaign-request-dataPartitions"></a>
The data partitions associated with the signals collected from the vehicle.
Type: Array of [DataPartition](API_DataPartition.md) objects
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Required: No

 ** [description](#API_CreateCampaign_RequestSyntax) **   <a name="iotfleetwise-CreateCampaign-request-description"></a>
An optional description of the campaign to help identify its purpose.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\u0000-\u001F\u007F]+`
Required: No

 ** [diagnosticsMode](#API_CreateCampaign_RequestSyntax) **   <a name="iotfleetwise-CreateCampaign-request-diagnosticsMode"></a>
Option for a vehicle to send diagnostic trouble codes to AWS IoT FleetWise. If you want to send diagnostic trouble codes, use `SEND_ACTIVE_DTCS`. If it's not specified, `OFF` is used.
Default: `OFF`
Type: String
Valid Values: `OFF | SEND_ACTIVE_DTCS`
Required: No

 ** [expiryTime](#API_CreateCampaign_RequestSyntax) **   <a name="iotfleetwise-CreateCampaign-request-expiryTime"></a>
The time the campaign expires, in seconds since epoch (January 1, 1970 at midnight UTC time). Vehicle data isn't collected after the campaign expires.
Default: 253402214400 (December 31, 9999, 00:00:00 UTC)
Type: Timestamp
Required: No

 ** [name](#API_CreateCampaign_RequestSyntax) **   <a name="iotfleetwise-CreateCampaign-request-name"></a>
 The name of the campaign to create.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z\d\-_:]+`
Required: Yes

 ** [postTriggerCollectionDuration](#API_CreateCampaign_RequestSyntax) **   <a name="iotfleetwise-CreateCampaign-request-postTriggerCollectionDuration"></a>
How long (in milliseconds) to collect raw data after a triggering event initiates the collection. If it's not specified, `0` is used.
Default: `0`
Type: Long
Valid Range: Minimum value of 0. Maximum value of 4294967295.
Required: No

 ** [priority](#API_CreateCampaign_RequestSyntax) **   <a name="iotfleetwise-CreateCampaign-request-priority"></a>
 *This parameter has been deprecated.*
A number indicating the priority of one campaign over another campaign for a certain vehicle or fleet. A campaign with the lowest value is deployed to vehicles before any other campaigns. If it's not specified, `0` is used.
Default: `0`
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** [signalCatalogArn](#API_CreateCampaign_RequestSyntax) **   <a name="iotfleetwise-CreateCampaign-request-signalCatalogArn"></a>
The Amazon Resource Name (ARN) of the signal catalog to associate with the campaign.
Type: String
Required: Yes

 ** [signalsToCollect](#API_CreateCampaign_RequestSyntax) **   <a name="iotfleetwise-CreateCampaign-request-signalsToCollect"></a>
A list of information about signals to collect.
If you upload a signal as a condition in a data partition for a campaign, then those same signals must be included in `signalsToCollect`.
Type: Array of [SignalInformation](API_SignalInformation.md) objects
Array Members: Minimum number of 0 items. Maximum number of 1000 items.
Required: No

 ** [signalsToFetch](#API_CreateCampaign_RequestSyntax) **   <a name="iotfleetwise-CreateCampaign-request-signalsToFetch"></a>
A list of information about signals to fetch.
Type: Array of [SignalFetchInformation](API_SignalFetchInformation.md) objects
Array Members: Minimum number of 1 item. Maximum number of 2 items.
Required: No

 ** [spoolingMode](#API_CreateCampaign_RequestSyntax) **   <a name="iotfleetwise-CreateCampaign-request-spoolingMode"></a>
Determines whether to store collected data after a vehicle lost a connection with the cloud. After a connection is re-established, the data is automatically forwarded to AWS IoT FleetWise. If you want to store collected data when a vehicle loses connection with the cloud, use `TO_DISK`. If it's not specified, `OFF` is used.
Default: `OFF`
Type: String
Valid Values: `OFF | TO_DISK`
Required: No

 ** [startTime](#API_CreateCampaign_RequestSyntax) **   <a name="iotfleetwise-CreateCampaign-request-startTime"></a>
The time, in milliseconds, to deliver a campaign after it was approved. If it's not specified, `0` is used.
Default: `0`
Type: Timestamp
Required: No

 ** [tags](#API_CreateCampaign_RequestSyntax) **   <a name="iotfleetwise-CreateCampaign-request-tags"></a>
Metadata that can be used to manage the campaign.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** [targetArn](#API_CreateCampaign_RequestSyntax) **   <a name="iotfleetwise-CreateCampaign-request-targetArn"></a>
 The ARN of the vehicle or fleet to deploy a campaign to.
Type: String
Required: Yes

## Response Syntax
<a name="API_CreateCampaign_ResponseSyntax"></a>

```
{
   "arn": "string",
   "name": "string"
}
```

## Response Elements
<a name="API_CreateCampaign_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_CreateCampaign_ResponseSyntax) **   <a name="iotfleetwise-CreateCampaign-response-arn"></a>
 The ARN of the created campaign.
Type: String
Pattern: `arn:aws:iotfleetwise:[a-z0-9-]+:[0-9]{12}:campaign/[a-zA-Z\d\-_:]{1,100}`

 ** [name](#API_CreateCampaign_ResponseSyntax) **   <a name="iotfleetwise-CreateCampaign-response-name"></a>
The name of the created campaign.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z\d\-_:]+`

## Errors
<a name="API_CreateCampaign_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient permission to perform this action.
HTTP Status Code: 400

 ** ConflictException **
The request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.
 ** resource **
The resource on which there are conflicting operations.
 ** resourceType **
The type of resource on which there are conflicting operations..
HTTP Status Code: 400

 ** InternalServerException **
The request couldn't be completed because the server temporarily failed.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the command.
HTTP Status Code: 500

 ** LimitExceededException **
A service quota was exceeded.
 ** resourceId **
The identifier of the resource that was exceeded.
 ** resourceType **
The type of resource that was exceeded.
HTTP Status Code: 400

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
<a name="API_CreateCampaign_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotfleetwise-2021-06-17/CreateCampaign)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotfleetwise-2021-06-17/CreateCampaign)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotfleetwise-2021-06-17/CreateCampaign)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotfleetwise-2021-06-17/CreateCampaign)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotfleetwise-2021-06-17/CreateCampaign)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotfleetwise-2021-06-17/CreateCampaign)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotfleetwise-2021-06-17/CreateCampaign)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotfleetwise-2021-06-17/CreateCampaign)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iotfleetwise-2021-06-17/CreateCampaign)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotfleetwise-2021-06-17/CreateCampaign)
