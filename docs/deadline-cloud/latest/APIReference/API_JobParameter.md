---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_JobParameter.html
---

# JobParameter
<a name="API_JobParameter"></a>

The details of job parameters.

## Contents
<a name="API_JobParameter_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** bool **   <a name="deadlinecloud-Type-JobParameter-bool"></a>
A boolean value represented as a string. Accepted values are `true`, `false`, `yes`, `no`, `on`, `off`, `1`, and `0`, case-insensitive.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 5.
Pattern: `([Tt][Rr][Uu][Ee]|[Ff][Aa][Ll][Ss][Ee]|[Yy][Ee][Ss]|[Nn][Oo]|[Oo][Nn]|[Oo][Ff][Ff]|[01])`
Required: No

 ** boolList **   <a name="deadlinecloud-Type-JobParameter-boolList"></a>
A list of boolean values, each represented as a string.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 512 items.
Length Constraints: Minimum length of 1. Maximum length of 5.
Pattern: `([Tt][Rr][Uu][Ee]|[Ff][Aa][Ll][Ss][Ee]|[Yy][Ee][Ss]|[Nn][Oo]|[Oo][Nn]|[Oo][Ff][Ff]|[01])`
Required: No

 ** float **   <a name="deadlinecloud-Type-JobParameter-float"></a>
A double precision IEEE-754 floating point number represented as a string.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 26.
Pattern: `[-]?(0|[1-9][0-9]*)([.][0-9]+)?([eE][+-]?[0-9]+)?`
Required: No

 ** floatList **   <a name="deadlinecloud-Type-JobParameter-floatList"></a>
A list of double precision IEEE-754 floating point numbers, each represented as a string.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 512 items.
Length Constraints: Minimum length of 1. Maximum length of 26.
Pattern: `[-]?(0|[1-9][0-9]*)([.][0-9]+)?([eE][+-]?[0-9]+)?`
Required: No

 ** int **   <a name="deadlinecloud-Type-JobParameter-int"></a>
A signed integer represented as a string.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `[-]?(0|[1-9][0-9]*)`
Required: No

 ** intList **   <a name="deadlinecloud-Type-JobParameter-intList"></a>
A list of signed integers, each represented as a string.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 512 items.
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `[-]?(0|[1-9][0-9]*)`
Required: No

 ** intListList **   <a name="deadlinecloud-Type-JobParameter-intListList"></a>
A list of lists of signed integers, each represented as a string.
Type: Array of arrays of strings
Array Members: Minimum number of 0 items. Maximum number of 512 items.
Array Members: Minimum number of 0 items. Maximum number of 64 items.
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `[-]?(0|[1-9][0-9]*)`
Required: No

 ** path **   <a name="deadlinecloud-Type-JobParameter-path"></a>
A file system path represented as a string.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** pathList **   <a name="deadlinecloud-Type-JobParameter-pathList"></a>
A list of file system paths, each represented as a string.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 64 items.
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** rangeExpr **   <a name="deadlinecloud-Type-JobParameter-rangeExpr"></a>
An Open Job Description range expression represented as a string, such as `1-10:2`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** string **   <a name="deadlinecloud-Type-JobParameter-string"></a>
A UTF-8 string.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** stringList **   <a name="deadlinecloud-Type-JobParameter-stringList"></a>
A list of UTF-8 strings.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 64 items.
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

## See Also
<a name="API_JobParameter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/JobParameter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/JobParameter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/JobParameter)
