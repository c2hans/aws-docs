---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_HoursOfOperationOverride.html
---

# HoursOfOperationOverride
<a name="API_HoursOfOperationOverride"></a>

Information about the hours of operations override.

## Contents
<a name="API_HoursOfOperationOverride_Contents"></a>

 ** Config **   <a name="connect-Type-HoursOfOperationOverride-Config"></a>
Configuration information for the hours of operation override: day, start time, and end time.
Type: Array of [HoursOfOperationOverrideConfig](API_HoursOfOperationOverrideConfig.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Required: No

 ** Description **   <a name="connect-Type-HoursOfOperationOverride-Description"></a>
The description of the hours of operation override.
Type: String
Pattern: `^[\P{C}\r\n\t]{1,250}$`
Required: No

 ** EffectiveFrom **   <a name="connect-Type-HoursOfOperationOverride-EffectiveFrom"></a>
The date from which the hours of operation override would be effective.
Type: String
Pattern: `^\d{4}-\d{2}-\d{2}$`
Required: No

 ** EffectiveTill **   <a name="connect-Type-HoursOfOperationOverride-EffectiveTill"></a>
The date until the hours of operation override is effective.
Type: String
Pattern: `^\d{4}-\d{2}-\d{2}$`
Required: No

 ** HoursOfOperationArn **   <a name="connect-Type-HoursOfOperationOverride-HoursOfOperationArn"></a>
The Amazon Resource Name (ARN) for the hours of operation.
Type: String
Required: No

 ** HoursOfOperationId **   <a name="connect-Type-HoursOfOperationOverride-HoursOfOperationId"></a>
The identifier for the hours of operation.
Type: String
Required: No

 ** HoursOfOperationOverrideId **   <a name="connect-Type-HoursOfOperationOverride-HoursOfOperationOverrideId"></a>
The identifier for the hours of operation override.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 36.
Required: No

 ** Name **   <a name="connect-Type-HoursOfOperationOverride-Name"></a>
The name of the hours of operation override.
Type: String
Pattern: `^[\P{C}\r\n\t]{1,127}$`
Required: No

 ** OverrideType **   <a name="connect-Type-HoursOfOperationOverride-OverrideType"></a>
Whether the override will be defined as a *standard* or as a *recurring event*.
Type: String
Valid Values: `STANDARD | OPEN | CLOSED`
Required: No

 ** RecurrenceConfig **   <a name="connect-Type-HoursOfOperationOverride-RecurrenceConfig"></a>
Configuration for a recurring event.
Type: [RecurrenceConfig](API_RecurrenceConfig.md) object
Required: No

## See Also
<a name="API_HoursOfOperationOverride_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/HoursOfOperationOverride)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/HoursOfOperationOverride)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/HoursOfOperationOverride)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
