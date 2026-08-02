---
source_url: https://docs.aws.amazon.com/appsync/latest/APIReference/API_DataSourceIntrospectionResult.html
---

# DataSourceIntrospectionResult
<a name="API_DataSourceIntrospectionResult"></a>

Represents the output of a `DataSourceIntrospectionResult`. This is the populated result of a `GetDataSourceIntrospection` operation.

## Contents
<a name="API_DataSourceIntrospectionResult_Contents"></a>

 ** models **   <a name="appsync-Type-DataSourceIntrospectionResult-models"></a>
The array of `DataSourceIntrospectionModel` objects.
Type: Array of [DataSourceIntrospectionModel](API_DataSourceIntrospectionModel.md) objects
Required: No

 ** nextToken **   <a name="appsync-Type-DataSourceIntrospectionResult-nextToken"></a>
Determines the number of types to be returned in a single response before paginating. This value is typically taken from `nextToken` value from the previous response.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 65536.
Pattern: `[\S]+`
Required: No

## See Also
<a name="API_DataSourceIntrospectionResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appsync-2017-07-25/DataSourceIntrospectionResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appsync-2017-07-25/DataSourceIntrospectionResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appsync-2017-07-25/DataSourceIntrospectionResult)
