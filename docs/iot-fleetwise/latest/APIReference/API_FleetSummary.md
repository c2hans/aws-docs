---
source_url: https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_FleetSummary.html
---

# FleetSummary
<a name="API_FleetSummary"></a>

Information about a fleet.

You can use the [ListFleets](API_ListFleets.md) API operation to return this information about multiple fleets.

## Contents
<a name="API_FleetSummary_Contents"></a>

 ** arn **   <a name="iotfleetwise-Type-FleetSummary-arn"></a>
The Amazon Resource Name (ARN) of the fleet.
Type: String
Required: Yes

 ** creationTime **   <a name="iotfleetwise-Type-FleetSummary-creationTime"></a>
The time the fleet was created, in seconds since epoch (January 1, 1970 at midnight UTC time).
Type: Timestamp
Required: Yes

 ** id **   <a name="iotfleetwise-Type-FleetSummary-id"></a>
The unique ID of the fleet.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z0-9:_-]+`
Required: Yes

 ** signalCatalogArn **   <a name="iotfleetwise-Type-FleetSummary-signalCatalogArn"></a>
The ARN of the signal catalog associated with the fleet.
Type: String
Required: Yes

 ** description **   <a name="iotfleetwise-Type-FleetSummary-description"></a>
A brief description of the fleet.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\u0000-\u001F\u007F]+`
Required: No

 ** lastModificationTime **   <a name="iotfleetwise-Type-FleetSummary-lastModificationTime"></a>
The time the fleet was last updated in seconds since epoch (January 1, 1970 at midnight UTC time).
Type: Timestamp
Required: No

## See Also
<a name="API_FleetSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotfleetwise-2021-06-17/FleetSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotfleetwise-2021-06-17/FleetSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotfleetwise-2021-06-17/FleetSummary)
