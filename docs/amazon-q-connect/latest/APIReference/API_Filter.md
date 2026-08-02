---
source_url: https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_Filter.html
---

# Filter
<a name="API_amazon-q-connect_Filter"></a>

A search filter.

## Contents
<a name="API_amazon-q-connect_Filter_Contents"></a>

 ** field **   <a name="connect-Type-amazon-q-connect_Filter-field"></a>
The field on which to filter.
Type: String
Valid Values: `NAME`
Required: Yes

 ** operator **   <a name="connect-Type-amazon-q-connect_Filter-operator"></a>
The operator to use for comparing the field’s value with the provided value.
Type: String
Valid Values: `EQUALS`
Required: Yes

 ** value **   <a name="connect-Type-amazon-q-connect_Filter-value"></a>
The desired field value on which to filter.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: Yes

## See Also
<a name="API_amazon-q-connect_Filter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/Filter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/Filter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/Filter)
