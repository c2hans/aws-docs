---
source_url: https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_DestinationSummary.html
---

# DestinationSummary
<a name="API_DestinationSummary"></a>

Structure describing a destination for IoT managed integrations to deliver notifications for a device.

## Contents
<a name="API_DestinationSummary_Contents"></a>

 ** DeliveryDestinationArn **   <a name="managedintegrations-Type-DestinationSummary-DeliveryDestinationArn"></a>
The Amazon Resource Name (ARN) of the customer-managed destination.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws:[0-9a-zA-Z]+:[0-9a-zA-Z-]+:[0-9]+:[0-9a-zA-Z]+/[0-9a-zA-Z._-]+`
Required: No

 ** DeliveryDestinationType **   <a name="managedintegrations-Type-DestinationSummary-DeliveryDestinationType"></a>
The destination type for the customer-managed destination.
Type: String
Valid Values: `KINESIS`
Required: No

 ** Description **   <a name="managedintegrations-Type-DestinationSummary-Description"></a>
The description of the customer-managed destination.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[0-9A-Za-z_\- ]+`
Required: No

 ** Name **   <a name="managedintegrations-Type-DestinationSummary-Name"></a>
The name of the customer-managed destination.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\p{L}\p{N} ._-]+`
Required: No

 ** RoleArn **   <a name="managedintegrations-Type-DestinationSummary-RoleArn"></a>
The Amazon Resource Name (ARN) of the delivery destination.
Type: String
Required: No

## See Also
<a name="API_DestinationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-managed-integrations-2025-03-03/DestinationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-managed-integrations-2025-03-03/DestinationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-managed-integrations-2025-03-03/DestinationSummary)
