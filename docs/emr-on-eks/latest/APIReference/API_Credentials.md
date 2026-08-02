---
source_url: https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_Credentials.html
---

# Credentials
<a name="API_Credentials"></a>

The structure containing the session token being returned.

## Contents
<a name="API_Credentials_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** token **   <a name="emroneks-Type-Credentials-token"></a>
The actual session token being returned.
Type: String
Length Constraints: Minimum length of 1.
Pattern: `^.*\S.*$`
Required: No

## See Also
<a name="API_Credentials_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/emr-containers-2020-10-01/Credentials)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/emr-containers-2020-10-01/Credentials)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/emr-containers-2020-10-01/Credentials)
