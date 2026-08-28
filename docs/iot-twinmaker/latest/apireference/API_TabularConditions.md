---
source_url: https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_TabularConditions.html
---

# TabularConditions
<a name="API_TabularConditions"></a>

The tabular conditions.

## Contents
<a name="API_TabularConditions_Contents"></a>

 ** orderBy **   <a name="tm-Type-TabularConditions-orderBy"></a>
Filter criteria that orders the output. It can be sorted in ascending or descending order.
Type: Array of [OrderBy](API_OrderBy.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** propertyFilters **   <a name="tm-Type-TabularConditions-propertyFilters"></a>
You can filter the request using various logical operators and a key-value format. For example:
 `{"key": "serverType", "value": "webServer"}`
Type: Array of [PropertyFilter](API_PropertyFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

## See Also
<a name="API_TabularConditions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iottwinmaker-2021-11-29/TabularConditions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iottwinmaker-2021-11-29/TabularConditions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iottwinmaker-2021-11-29/TabularConditions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for IoT TwinMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-twinmaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
