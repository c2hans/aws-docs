---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetCapacityManagerAttributes.html
---

# GetCapacityManagerAttributes
<a name="API_GetCapacityManagerAttributes"></a>

 Retrieves the current configuration and status of EC2 Capacity Manager for your account, including enablement status, Organizations access settings, and data ingestion status.

## Request Parameters
<a name="API_GetCapacityManagerAttributes_RequestParameters"></a>

For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
 Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

## Response Elements
<a name="API_GetCapacityManagerAttributes_ResponseElements"></a>

The following elements are returned by the service.

 **capacityManagerStatus**
 The current status of Capacity Manager.
Type: String
Valid Values: `enabled | disabled`

 **dataExportCount**
 The number of active data export configurations for this account. This count includes all data exports regardless of their current delivery status.
Type: Integer

 **earliestDatapointTimestamp**
 The timestamp of the earliest data point available in Capacity Manager, in milliseconds since epoch. This indicates how far back historical data is available for queries.
Type: Timestamp

 **ingestionStatus**
 The current data ingestion status. Initial ingestion may take several hours after enabling Capacity Manager.
Type: String
Valid Values: `initial-ingestion-in-progress | ingestion-complete | ingestion-failed`

 **ingestionStatusMessage**
 A descriptive message providing additional details about the current ingestion status. This may include error information if ingestion has failed or progress details during initial setup.
Type: String

 **latestDatapointTimestamp**
 The timestamp of the most recent data point ingested by Capacity Manager, in milliseconds since epoch. This indicates how current your capacity data is.
Type: Timestamp

 **organizationsAccess**
 Indicates whether Organizations access is enabled for cross-account data aggregation.
Type: Boolean

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_GetCapacityManagerAttributes_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_GetCapacityManagerAttributes_Examples"></a>

### Example
<a name="API_GetCapacityManagerAttributes_Example_1"></a>

This example retrieves the current Capacity Manager attributes for your account.

#### Sample Request
<a name="API_GetCapacityManagerAttributes_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=GetCapacityManagerAttributes
&AUTHPARAMS
```

#### Sample Response
<a name="API_GetCapacityManagerAttributes_Example_1_Response"></a>

```
<GetCapacityManagerAttributesResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>d4904fd9-82c2-4ea5-adfe-a9cc3EXAMPLE</requestId>
    <capacityManagerStatus>enabled</capacityManagerStatus>
    <organizationsAccess>true</organizationsAccess>
    <dataExportCount>2</dataExportCount>
    <ingestionStatus>ingestion-complete</ingestionStatus>
    <ingestionStatusMessage>Data ingestion is up to date.</ingestionStatusMessage>
    <earliestDatapointTimestamp>2025-12-23T20:00:00+00:00</earliestDatapointTimestamp>
    <latestDatapointTimestamp>2026-03-23T15:00:00+00:00</latestDatapointTimestamp>
</GetCapacityManagerAttributesResponse>
```

## See Also
<a name="API_GetCapacityManagerAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/GetCapacityManagerAttributes)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/GetCapacityManagerAttributes)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/GetCapacityManagerAttributes)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/GetCapacityManagerAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/GetCapacityManagerAttributes)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/GetCapacityManagerAttributes)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/GetCapacityManagerAttributes)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/GetCapacityManagerAttributes)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/GetCapacityManagerAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/GetCapacityManagerAttributes)
