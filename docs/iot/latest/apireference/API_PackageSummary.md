---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_PackageSummary.html
---

# PackageSummary
<a name="API_PackageSummary"></a>

A summary of information about a software package.

## Contents
<a name="API_PackageSummary_Contents"></a>

 ** creationDate **   <a name="iot-Type-PackageSummary-creationDate"></a>
The date that the package was created.
Type: Timestamp
Required: No

 ** defaultVersionName **   <a name="iot-Type-PackageSummary-defaultVersionName"></a>
The name of the default package version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9-_.]+`
Required: No

 ** lastModifiedDate **   <a name="iot-Type-PackageSummary-lastModifiedDate"></a>
The date that the package was last updated.
Type: Timestamp
Required: No

 ** packageName **   <a name="iot-Type-PackageSummary-packageName"></a>
The name for the target software package.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9-_.]+`
Required: No

## See Also
<a name="API_PackageSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/PackageSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/PackageSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/PackageSummary)
