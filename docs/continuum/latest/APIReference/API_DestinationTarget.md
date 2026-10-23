---
source_url: https://docs.aws.amazon.com/continuum/latest/APIReference/API_DestinationTarget.html
---

# DestinationTarget
<a name="API_DestinationTarget"></a>

The destination Target.

## Contents
<a name="API_DestinationTarget_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** github **   <a name="continuum-Type-DestinationTarget-github"></a>
The github.
Type: [GitHubTarget](API_GitHubTarget.md) object
Required: No

 ** s3 **   <a name="continuum-Type-DestinationTarget-s3"></a>
The s3.
Type: [S3Target](API_S3Target.md) object
Required: No

## See Also
<a name="API_DestinationTarget_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/continuum-2022-07-26/DestinationTarget)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/continuum-2022-07-26/DestinationTarget)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/continuum-2022-07-26/DestinationTarget)
