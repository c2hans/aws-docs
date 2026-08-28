---
source_url: https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_SignalFetchInformation.html
---

# SignalFetchInformation
<a name="API_SignalFetchInformation"></a>

Information about the signal to be fetched.

**Important**
 AWS IoT FleetWise is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS IoT FleetWise availability change](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/iotfleetwise-availability-change.html).

## Contents
<a name="API_SignalFetchInformation_Contents"></a>

 ** actions **   <a name="iotfleetwise-Type-SignalFetchInformation-actions"></a>
The actions to be performed by the signal fetch.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 2 items.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** fullyQualifiedName **   <a name="iotfleetwise-Type-SignalFetchInformation-fullyQualifiedName"></a>
The fully qualified name of the signal to be fetched.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 150.
Pattern: `[a-zA-Z0-9_.]+`
Required: Yes

 ** signalFetchConfig **   <a name="iotfleetwise-Type-SignalFetchInformation-signalFetchConfig"></a>
The configuration of the signal fetch operation.
Type: [SignalFetchConfig](API_SignalFetchConfig.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** conditionLanguageVersion **   <a name="iotfleetwise-Type-SignalFetchInformation-conditionLanguageVersion"></a>
The version of the condition language used.
Type: Integer
Valid Range: Fixed value of 1.
Required: No

## See Also
<a name="API_SignalFetchInformation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotfleetwise-2021-06-17/SignalFetchInformation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotfleetwise-2021-06-17/SignalFetchInformation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotfleetwise-2021-06-17/SignalFetchInformation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT FleetWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-fleetwise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
