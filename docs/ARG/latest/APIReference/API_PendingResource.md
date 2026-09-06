---
source_url: https://docs.aws.amazon.com/ARG/latest/APIReference/API_PendingResource.html
---

# PendingResource
<a name="API_PendingResource"></a>

A structure that identifies a resource that is currently pending addition to the group as a member. Adding a resource to a resource group happens asynchronously as a background task and this one isn't completed yet.

## Contents
<a name="API_PendingResource_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ResourceArn **   <a name="ARG-Type-PendingResource-ResourceArn"></a>
The Amazon resource name (ARN) of the resource that's in a pending state.
Type: String
Pattern: `arn:aws(-[a-z]+)*:[a-z0-9\-]*:([a-z]{2}(-[a-z]+)+-\d{1})?:([0-9]{12})?:.+`
Required: No

## See Also
<a name="API_PendingResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resource-groups-2017-11-27/PendingResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resource-groups-2017-11-27/PendingResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resource-groups-2017-11-27/PendingResource)
