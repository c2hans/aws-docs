---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_AccessConfiguration.html
---

# AccessConfiguration
<a name="API_AccessConfiguration"></a>

Used to configure access permissions for a document.

## Contents
<a name="API_AccessConfiguration_Contents"></a>

 ** accessControls **   <a name="qbusiness-Type-AccessConfiguration-accessControls"></a>
A list of `AccessControlList` objects.
Type: Array of [AccessControl](API_AccessControl.md) objects
Required: Yes

 ** memberRelation **   <a name="qbusiness-Type-AccessConfiguration-memberRelation"></a>
Describes the member relation within the `AccessControlList` object.
Type: String
Valid Values: `AND | OR`
Required: No

## See Also
<a name="API_AccessConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/AccessConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/AccessConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/AccessConfiguration)
