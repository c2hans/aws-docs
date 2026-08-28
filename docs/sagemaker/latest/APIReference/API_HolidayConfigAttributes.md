---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HolidayConfigAttributes.html
---

# HolidayConfigAttributes
<a name="API_HolidayConfigAttributes"></a>

Stores the holiday featurization attributes applicable to each item of time-series datasets during the training of a forecasting model. This allows the model to identify patterns associated with specific holidays.

## Contents
<a name="API_HolidayConfigAttributes_Contents"></a>

 ** CountryCode **   <a name="sagemaker-Type-HolidayConfigAttributes-CountryCode"></a>
The country code for the holiday calendar.
For the list of public holiday calendars supported by AutoML job V2, see [Country Codes](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-timeseries-forecasting-holiday-calendars.html#holiday-country-codes). Use the country code corresponding to the country of your choice.
Type: String
Length Constraints: Fixed length of 2.
Pattern: `[A-Z]{2}`
Required: No

## See Also
<a name="API_HolidayConfigAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/HolidayConfigAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/HolidayConfigAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/HolidayConfigAttributes)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
