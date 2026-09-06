---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ResponseError.html
---

# ResponseError
<a name="API_ResponseError"></a>

Describes the error that's returned when you cannot delete a launch template version.

## Contents
<a name="API_ResponseError_Contents"></a>

 ** code **
The error code.
Type: String
Valid Values: `launchTemplateIdDoesNotExist | launchTemplateIdMalformed | launchTemplateNameDoesNotExist | launchTemplateNameMalformed | launchTemplateVersionDoesNotExist | unexpectedError`
Required: No

 ** message **
The error message, if applicable.
Type: String
Required: No

## See Also
<a name="API_ResponseError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ResponseError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ResponseError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ResponseError)
