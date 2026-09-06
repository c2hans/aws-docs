---
source_url: https://docs.aws.amazon.com/redshift-data/latest/APIReference/API_SqlParameter.html
---

# SqlParameter
<a name="API_SqlParameter"></a>

A parameter used in a SQL statement.

## Contents
<a name="API_SqlParameter_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** name **   <a name="redshiftdata-Type-SqlParameter-name"></a>
The name of the parameter.
Type: String
Pattern: `[0-9a-zA-Z_]+`
Required: Yes

 ** value **   <a name="redshiftdata-Type-SqlParameter-value"></a>
The value of the parameter. Amazon Redshift implicitly converts to the proper data type. For more information, see [Data types](https://docs.aws.amazon.com/redshift/latest/dg/c_Supported_data_types.html) in the *Amazon Redshift Database Developer Guide*.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

## See Also
<a name="API_SqlParameter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-data-2019-12-20/SqlParameter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-data-2019-12-20/SqlParameter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-data-2019-12-20/SqlParameter)
