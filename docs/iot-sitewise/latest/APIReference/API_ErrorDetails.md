---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_ErrorDetails.html
---

# ErrorDetails
<a name="API_ErrorDetails"></a>

Contains the details of an AWS IoT SiteWise error.

## Contents
<a name="API_ErrorDetails_Contents"></a>

 ** code **   <a name="iotsitewise-Type-ErrorDetails-code"></a>
The error code.
Type: String
Valid Values: `VALIDATION_ERROR | INTERNAL_FAILURE`
Required: Yes

 ** message **   <a name="iotsitewise-Type-ErrorDetails-message"></a>
The error message.
Type: String
Required: Yes

 ** details **   <a name="iotsitewise-Type-ErrorDetails-details"></a>
 A list of detailed errors.
Type: Array of [DetailedError](API_DetailedError.md) objects
Required: No

## See Also
<a name="API_ErrorDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/ErrorDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/ErrorDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/ErrorDetails)
