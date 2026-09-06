---
source_url: https://docs.aws.amazon.com/documentdb/latest/APIReference/API_Tag.html
---

# Tag
<a name="API_Tag"></a>

Metadata assigned to an Amazon DocumentDB resource consisting of a key-value pair.

## Contents
<a name="API_Tag_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Key **
The required name of the tag. The string value can be from 1 to 128 Unicode characters in length and can't be prefixed with "`aws:`" or "`rds:`". The string can contain only the set of Unicode letters, digits, white space, '\_', '.', '/', '=', '\+', '-' (Java regex: "^([\\\\p{L}\\\\p{Z}\\\\p{N}\_.:/=\+\\\\-]\*)$").
Type: String
Required: No

 ** Value **
The optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and can't be prefixed with "`aws:`" or "`rds:`". The string can contain only the set of Unicode letters, digits, white space, '\_', '.', '/', '=', '\+', '-' (Java regex: "^([\\\\p{L}\\\\p{Z}\\\\p{N}\_.:/=\+\\\\-]\*)$").
Type: String
Required: No

## See Also
<a name="API_Tag_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/docdb-2014-10-31/Tag)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/docdb-2014-10-31/Tag)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/docdb-2014-10-31/Tag)
