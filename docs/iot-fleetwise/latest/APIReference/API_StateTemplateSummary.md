---
source_url: https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_StateTemplateSummary.html
---

# StateTemplateSummary
<a name="API_StateTemplateSummary"></a>

Information about a state template.

**Important**
 AWS IoT FleetWise is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS IoT FleetWise availability change](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/iotfleetwise-availability-change.html).

## Contents
<a name="API_StateTemplateSummary_Contents"></a>

 ** arn **   <a name="iotfleetwise-Type-StateTemplateSummary-arn"></a>
The Amazon Resource Name (ARN) of the state template.
Type: String
Required: No

 ** creationTime **   <a name="iotfleetwise-Type-StateTemplateSummary-creationTime"></a>
The time the state template was created, in seconds since epoch (January 1, 1970 at midnight UTC time).
Type: Timestamp
Required: No

 ** description **   <a name="iotfleetwise-Type-StateTemplateSummary-description"></a>
A brief description of the state template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\u0000-\u001F\u007F]+`
Required: No

 ** id **   <a name="iotfleetwise-Type-StateTemplateSummary-id"></a>
The unique ID of the state template.
Type: String
Length Constraints: Fixed length of 26.
Pattern: `[A-Z0-9]+`
Required: No

 ** lastModificationTime **   <a name="iotfleetwise-Type-StateTemplateSummary-lastModificationTime"></a>
The time the state template was last updated, in seconds since epoch (January 1, 1970 at midnight UTC time).
Type: Timestamp
Required: No

 ** name **   <a name="iotfleetwise-Type-StateTemplateSummary-name"></a>
The name of the state template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z\d\-_:]+`
Required: No

 ** signalCatalogArn **   <a name="iotfleetwise-Type-StateTemplateSummary-signalCatalogArn"></a>
The Amazon Resource Name (ARN) of the signal catalog associated with the state template.
Type: String
Required: No

## See Also
<a name="API_StateTemplateSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotfleetwise-2021-06-17/StateTemplateSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotfleetwise-2021-06-17/StateTemplateSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotfleetwise-2021-06-17/StateTemplateSummary)
