---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeregisterInstanceTagAttributeRequest.html
---

# DeregisterInstanceTagAttributeRequest
<a name="API_DeregisterInstanceTagAttributeRequest"></a>

Information about the tag keys to deregister for the current Region. You can either specify individual tag keys or deregister all tag keys in the current Region. You must specify either `IncludeAllTagsOfInstance` or `InstanceTagKeys` in the request

## Contents
<a name="API_DeregisterInstanceTagAttributeRequest_Contents"></a>

 ** IncludeAllTagsOfInstance **
Indicates whether to deregister all tag keys in the current Region. Specify `false` to deregister all tag keys.
Type: Boolean
Required: No

 ** InstanceTagKey.N **
Information about the tag keys to deregister.
Type: Array of strings
Required: No

## See Also
<a name="API_DeregisterInstanceTagAttributeRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DeregisterInstanceTagAttributeRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DeregisterInstanceTagAttributeRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DeregisterInstanceTagAttributeRequest)
