---
source_url: https://docs.aws.amazon.com/awssupport/latest/APIReference/API_CommunicationTypeOptions.html
---

# CommunicationTypeOptions
<a name="API_CommunicationTypeOptions"></a>

A JSON-formatted object that contains the CommunicationTypeOptions for creating a case for a certain communication channel. It is contained in the response from a [DescribeCreateCaseOptions](API_DescribeCreateCaseOptions.md) request. **CommunicationTypeOptions** contains the following fields:
+  **datesWithoutSupport** - A JSON-formatted list containing date and time ranges for periods without support in UTC time. Date and time format is RFC 3339 : 'yyyy-MM-dd'T'HH:mm:ss.SSSZZ'.
+  **supportedHours** - A JSON-formatted list containing time ranges when support are available. Time format is RFC 3339 : 'HH:mm:ss.SSS'.
+  **type** - A string value indicating the communication type that the aforementioned rules apply to. At the moment the type value can assume one of 3 values at the moment `chat`, `web` and `call`.

## Contents
<a name="API_CommunicationTypeOptions_Contents"></a>

 ** datesWithoutSupport **   <a name="AWSSupport-Type-CommunicationTypeOptions-datesWithoutSupport"></a>
 A JSON-formatted list containing date and time ranges for periods without support
Type: Array of [DateInterval](API_DateInterval.md) objects

 ** supportedHours **   <a name="AWSSupport-Type-CommunicationTypeOptions-supportedHours"></a>
 A JSON-formatted list containing time ranges when support is available.
Type: Array of [SupportedHour](API_SupportedHour.md) objects

 ** type **   <a name="AWSSupport-Type-CommunicationTypeOptions-type"></a>
 A string value indicating the communication type. At the moment the type value can assume one of 3 values at the moment chat, web and call.
Type: String

## See Also
<a name="API_CommunicationTypeOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/support-2013-04-15/CommunicationTypeOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/support-2013-04-15/CommunicationTypeOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/support-2013-04-15/CommunicationTypeOptions)
