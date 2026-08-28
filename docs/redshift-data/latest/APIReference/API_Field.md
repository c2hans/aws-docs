---
source_url: https://docs.aws.amazon.com/redshift-data/latest/APIReference/API_Field.html
---

# Field
<a name="API_Field"></a>

A data value in a column.

## Contents
<a name="API_Field_Contents"></a>

**Note**
In the following list, the required parameters are described first.

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** blobValue **   <a name="redshiftdata-Type-Field-blobValue"></a>
A value of the BLOB data type.
Type: Base64-encoded binary data object
Required: No

 ** booleanValue **   <a name="redshiftdata-Type-Field-booleanValue"></a>
A value of the Boolean data type.
Type: Boolean
Required: No

 ** doubleValue **   <a name="redshiftdata-Type-Field-doubleValue"></a>
A value of the double data type.
Type: Double
Required: No

 ** isNull **   <a name="redshiftdata-Type-Field-isNull"></a>
A value that indicates whether the data is NULL.
Type: Boolean
Required: No

 ** longValue **   <a name="redshiftdata-Type-Field-longValue"></a>
A value of the long data type.
Type: Long
Required: No

 ** stringValue **   <a name="redshiftdata-Type-Field-stringValue"></a>
A value of the string data type.
Type: String
Required: No

## See Also
<a name="API_Field_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-data-2019-12-20/Field)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-data-2019-12-20/Field)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-data-2019-12-20/Field)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift Data API. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift-data` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
