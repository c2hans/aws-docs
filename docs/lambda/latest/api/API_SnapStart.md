---
source_url: https://docs.aws.amazon.com/lambda/latest/api/API_SnapStart.html
---

# SnapStart
<a name="API_SnapStart"></a>

The function's [Lambda SnapStart](https://docs.aws.amazon.com/lambda/latest/dg/snapstart.html) setting. Set `ApplyOn` to `PublishedVersions` to create a snapshot of the initialized execution environment when you publish a function version.

## Contents
<a name="API_SnapStart_Contents"></a>

 ** ApplyOn **   <a name="lambda-Type-SnapStart-ApplyOn"></a>
Set to `PublishedVersions` to create a snapshot of the initialized execution environment when you publish a function version.
Type: String
Valid Values: `PublishedVersions | None`
Required: No

## See Also
<a name="API_SnapStart_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-2015-03-31/SnapStart)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-2015-03-31/SnapStart)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-2015-03-31/SnapStart)
