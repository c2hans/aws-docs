---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_ProcessingInput.html
---

# ProcessingInput
<a name="API_ProcessingInput"></a>

Input source for processing. Specify exactly one option.

## Contents
<a name="API_ProcessingInput_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** dataset **   <a name="iotsitewise-Type-ProcessingInput-dataset"></a>
A dataset containing multiple items to process.
Type: [DatasetItem](API_DatasetItem.md) object
Required: No

 ** timeseries **   <a name="iotsitewise-Type-ProcessingInput-timeseries"></a>
List of individual timeseries items to process.
Type: Array of [TimeseriesItem](API_TimeseriesItem.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: No

## See Also
<a name="API_ProcessingInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/ProcessingInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/ProcessingInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/ProcessingInput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT SiteWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-sitewise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
