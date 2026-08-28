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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift Data API. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift-data` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
