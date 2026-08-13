---
source_url: https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_FailureInfo.html
---

# FailureInfo
<a name="API_FailureInfo"></a>

Information about the errors that are returned for each failed resource. This information can include `InternalServiceException` and `InvalidParameterException` errors. It can also include any valid error code returned by the AWS service that hosts the resource that the ARN key represents.

The following are common error codes that you might receive from other AWS services:
+  **InternalServiceException** – This can mean that the Resource Groups Tagging API didn't receive a response from another AWS service. It can also mean that the resource type in the request is not supported by the Resource Groups Tagging API. In these cases, it's safe to retry the request and then call [GetResources](https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_GetResources.html) to verify the changes.
+  **AccessDeniedException** – This can mean that you need permission to call the tagging operations in the AWS service that contains the resource. For example, to use the Resource Groups Tagging API to tag a Amazon CloudWatch alarm resource, you need permission to call both [`TagResources`](https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_TagResources.html) *and* [`TagResource`](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_TagResource.html) in the CloudWatch API.

For more information on errors that are generated from other AWS services, see the documentation for that service.

## Contents
<a name="API_FailureInfo_Contents"></a>

 ** ErrorCode **   <a name="resourcegrouptagging-Type-FailureInfo-ErrorCode"></a>
The code of the common error. Valid values include `InternalServiceException`, `InvalidParameterException`, and any valid error code returned by the AWS service that hosts the resource that you want to tag.
Type: String
Valid Values: `InternalServiceException | InvalidParameterException`
Required: No

 ** ErrorMessage **   <a name="resourcegrouptagging-Type-FailureInfo-ErrorMessage"></a>
The message of the common error.
Type: String
Required: No

 ** StatusCode **   <a name="resourcegrouptagging-Type-FailureInfo-StatusCode"></a>
The HTTP status code of the common error.
Type: Integer
Required: No

## See Also
<a name="API_FailureInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resourcegroupstaggingapi-2017-01-26/FailureInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resourcegroupstaggingapi-2017-01-26/FailureInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resourcegroupstaggingapi-2017-01-26/FailureInfo)
