---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_ProgramNumberConfiguration.html
---

# ProgramNumberConfiguration
<a name="API_ProgramNumberConfiguration"></a>

The configuration settings for the program number.

## Contents
<a name="API_ProgramNumberConfiguration_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** passthrough **   <a name="mediaconnect-Type-ProgramNumberConfiguration-passthrough"></a>
The program number configuration that passes through the program number from the source.
Type: [Passthrough](API_Passthrough.md) object
Required: No

 ** set **   <a name="mediaconnect-Type-ProgramNumberConfiguration-set"></a>
The program number to use for the router output.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 65535.
Required: No

## See Also
<a name="API_ProgramNumberConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/ProgramNumberConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/ProgramNumberConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/ProgramNumberConfiguration)
