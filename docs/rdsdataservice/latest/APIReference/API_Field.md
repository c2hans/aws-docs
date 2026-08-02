---
source_url: https://docs.aws.amazon.com/rdsdataservice/latest/APIReference/API_Field.html
---

# Field
<a name="API_Field"></a>

Contains a value.

## Contents
<a name="API_Field_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** arrayValue **   <a name="rdsdtataservice-Type-Field-arrayValue"></a>
An array of values.
Type: [ArrayValue](API_ArrayValue.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** blobValue **   <a name="rdsdtataservice-Type-Field-blobValue"></a>
A value of BLOB data type.
Type: Base64-encoded binary data object
Required: No

 ** booleanValue **   <a name="rdsdtataservice-Type-Field-booleanValue"></a>
A value of Boolean data type.
Type: Boolean
Required: No

 ** doubleValue **   <a name="rdsdtataservice-Type-Field-doubleValue"></a>
A value of double data type.
Type: Double
Required: No

 ** isNull **   <a name="rdsdtataservice-Type-Field-isNull"></a>
A NULL value.
Type: Boolean
Required: No

 ** longValue **   <a name="rdsdtataservice-Type-Field-longValue"></a>
A value of long data type.
Type: Long
Required: No

 ** stringValue **   <a name="rdsdtataservice-Type-Field-stringValue"></a>
A value of string data type.
Type: String
Required: No

## See Also
<a name="API_Field_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-data-2018-08-01/Field)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-data-2018-08-01/Field)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-data-2018-08-01/Field)
