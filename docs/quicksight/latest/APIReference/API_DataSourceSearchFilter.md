---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DataSourceSearchFilter.html
---

# DataSourceSearchFilter
<a name="API_DataSourceSearchFilter"></a>

A filter that you apply when searching for data sources.

## Contents
<a name="API_DataSourceSearchFilter_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Name **   <a name="QS-Type-DataSourceSearchFilter-Name"></a>
The name of the value that you want to use as a filter, for example, `"Name": "DIRECT_QUICKSIGHT_OWNER"`.
Valid values are defined as follows:
+  `DIRECT_QUICKSIGHT_VIEWER_OR_OWNER`: Provide an ARN of a user or group, and any data sources with that ARN listed as one of the owners or viewers of the data sources are returned. Implicit permissions from folders or groups are not considered.
+  `DIRECT_QUICKSIGHT_OWNER`: Provide an ARN of a user or group, and any data sources with that ARN listed as one of the owners if the data source are returned. Implicit permissions from folders or groups are not considered.
+  `DIRECT_QUICKSIGHT_SOLE_OWNER`: Provide an ARN of a user or group, and any data sources with that ARN listed as the only owner of the data source are returned. Implicit permissions from folders or groups are not considered.
+  `DATASOURCE_NAME`: Any data sources whose names have a substring match to the provided value are returned.
Type: String
Valid Values: `DIRECT_QUICKSIGHT_VIEWER_OR_OWNER | DIRECT_QUICKSIGHT_OWNER | DIRECT_QUICKSIGHT_SOLE_OWNER | DATASOURCE_NAME`
Required: Yes

 ** Operator **   <a name="QS-Type-DataSourceSearchFilter-Operator"></a>
The comparison operator that you want to use as a filter, for example `"Operator": "StringEquals"`. Valid values are `"StringEquals"` and `"StringLike"`.
If you set the operator value to `"StringEquals"`, you need to provide an ownership related filter in the `"NAME"` field and the arn of the user or group whose data sources you want to search in the `"Value"` field. For example, `"Name":"DIRECT_QUICKSIGHT_OWNER", "Operator": "StringEquals", "Value": "arn:aws:quicksight:us-east-1:1:user/default/UserName1"`.
If you set the value to `"StringLike"`, you need to provide the name of the data sources you are searching for. For example, `"Name":"DATASOURCE_NAME", "Operator": "StringLike", "Value": "Test"`. The `"StringLike"` operator only supports the `NAME` value `DATASOURCE_NAME`.
Type: String
Valid Values: `StringEquals | StringLike`
Required: Yes

 ** Value **   <a name="QS-Type-DataSourceSearchFilter-Value"></a>
The value of the named item, for example `DIRECT_QUICKSIGHT_OWNER`, that you want to use as a filter, for example, `"Value": "arn:aws:quicksight:us-east-1:1:user/default/UserName1"`.
Type: String
Required: Yes

## See Also
<a name="API_DataSourceSearchFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/DataSourceSearchFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/DataSourceSearchFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/DataSourceSearchFilter)
