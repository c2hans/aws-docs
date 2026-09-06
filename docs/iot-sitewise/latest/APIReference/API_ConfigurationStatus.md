---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_ConfigurationStatus.html
---

# ConfigurationStatus
<a name="API_ConfigurationStatus"></a>

Contains current status information for the configuration.

## Contents
<a name="API_ConfigurationStatus_Contents"></a>

 ** state **   <a name="iotsitewise-Type-ConfigurationStatus-state"></a>
The current state of the configuration.
Type: String
Valid Values: `ACTIVE | UPDATE_IN_PROGRESS | UPDATE_FAILED`
Required: Yes

 ** error **   <a name="iotsitewise-Type-ConfigurationStatus-error"></a>
Contains associated error information, if any.
Type: [ConfigurationErrorDetails](API_ConfigurationErrorDetails.md) object
Required: No

## See Also
<a name="API_ConfigurationStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/ConfigurationStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/ConfigurationStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/ConfigurationStatus)
