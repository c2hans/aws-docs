---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_RetentionPeriod.html
---

# RetentionPeriod
<a name="API_RetentionPeriod"></a>

The number of days your data is kept in the hot tier. By default, your data is kept indefinitely in the hot tier.

## Contents
<a name="API_RetentionPeriod_Contents"></a>

 ** numberOfDays **   <a name="iotsitewise-Type-RetentionPeriod-numberOfDays"></a>
The number of days that your data is kept.
If you specified a value for this parameter, the `unlimited` parameter must be `false`.
Type: Integer
Required: No

 ** unlimited **   <a name="iotsitewise-Type-RetentionPeriod-unlimited"></a>
If true, your data is kept indefinitely.
If configured to `true`, you must not specify a value for the `numberOfDays` parameter.
Type: Boolean
Required: No

## See Also
<a name="API_RetentionPeriod_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/RetentionPeriod)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/RetentionPeriod)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/RetentionPeriod)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT SiteWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-sitewise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
