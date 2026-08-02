---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RegisterInstanceTagAttributeRequest.html
---

# RegisterInstanceTagAttributeRequest
<a name="API_RegisterInstanceTagAttributeRequest"></a>

Information about the tag keys to register for the current Region. You can either specify individual tag keys or register all tag keys in the current Region. You must specify either `IncludeAllTagsOfInstance` or `InstanceTagKeys` in the request

## Contents
<a name="API_RegisterInstanceTagAttributeRequest_Contents"></a>

 ** IncludeAllTagsOfInstance **
Indicates whether to register all tag keys in the current Region. Specify `true` to register all tag keys.
Type: Boolean
Required: No

 ** InstanceTagKey.N **
The tag keys to register.
Type: Array of strings
Required: No

## See Also
<a name="API_RegisterInstanceTagAttributeRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/RegisterInstanceTagAttributeRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/RegisterInstanceTagAttributeRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/RegisterInstanceTagAttributeRequest)
