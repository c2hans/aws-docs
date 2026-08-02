---
source_url: https://docs.aws.amazon.com/neptune/latest/apiref/API_DescribeEventCategories.html
---

# DescribeEventCategories
<a name="API_DescribeEventCategories"></a>

Displays a list of categories for all event source types, or, if specified, for a specified source type.

## Request Parameters
<a name="API_DescribeEventCategories_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 **Filters.Filter.N**
This parameter is not currently supported.
Type: Array of [Filter](API_Filter.md) objects
Required: No

 ** SourceType **
The type of source that is generating the events.
Valid values: db-instance \| db-parameter-group \| db-security-group \| db-snapshot
Type: String
Required: No

## Response Elements
<a name="API_DescribeEventCategories_ResponseElements"></a>

The following element is returned by the service.

 **EventCategoriesMapList.EventCategoriesMap.N**
A list of EventCategoriesMap data types.
Type: Array of [EventCategoriesMap](API_EventCategoriesMap.md) objects

## Errors
<a name="API_DescribeEventCategories_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_DescribeEventCategories_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/neptune-2014-10-31/DescribeEventCategories)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/neptune-2014-10-31/DescribeEventCategories)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/neptune-2014-10-31/DescribeEventCategories)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/neptune-2014-10-31/DescribeEventCategories)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-2014-10-31/DescribeEventCategories)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/neptune-2014-10-31/DescribeEventCategories)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/neptune-2014-10-31/DescribeEventCategories)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/neptune-2014-10-31/DescribeEventCategories)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/neptune-2014-10-31/DescribeEventCategories)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/neptune-2014-10-31/DescribeEventCategories)
