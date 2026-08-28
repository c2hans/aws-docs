---
source_url: https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_QueryFilter.html
---

# QueryFilter
<a name="API_QueryFilter"></a>

A structure that defines a key and values that you can use to filter the results. The only performance events that are returned are those that have values matching the ones that you specify in one of your `QueryFilter` structures.

For example, you could specify `Browser` as the `Name` and specify `Chrome,Firefox` as the `Values` to return events generated only from those browsers.

Specifying `Invert` as the `Name` works as a "not equal to" filter. For example, specify `Invert` as the `Name` and specify `Chrome` as the value to return all events except events from user sessions with the Chrome browser.

## Contents
<a name="API_QueryFilter_Contents"></a>

 ** Name **   <a name="cloudwatchrum-Type-QueryFilter-Name"></a>
The name of a key to search for. The filter returns only the events that match the `Name` and `Values` that you specify.
Valid values for `Name` are `Browser` \| `Device` \| `Country` \| `Page` \| `OS` \| `EventType` \| `Invert`
Type: String
Required: No

 ** Values **   <a name="cloudwatchrum-Type-QueryFilter-Values"></a>
The values of the `Name` that are to be be included in the returned results.
Type: Array of strings
Required: No

## See Also
<a name="API_QueryFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rum-2018-05-10/QueryFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rum-2018-05-10/QueryFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rum-2018-05-10/QueryFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for CloudWatch RUM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudwatchrum` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
