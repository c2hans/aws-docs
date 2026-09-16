---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeImageReferences.html
---

# DescribeImageReferences
<a name="API_DescribeImageReferences"></a>

Describes your AWS resources that are referencing the specified images.

For more information, see [Identify your resources referencing specified AMIs](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-ami-references.html) in the *Amazon EC2 User Guide*.

## Request Parameters
<a name="API_DescribeImageReferences_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **ImageId.N**
The IDs of the images to check for resource references.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: Yes

 **IncludeAllResourceTypes**
Specifies whether to check all supported AWS resource types for image references. When specified, default values are applied for `ResourceTypeOptions`. For the default values, see [How AMI reference checks work](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-ami-references.html#how-ami-references-works) in the *Amazon EC2 User Guide*. If you also specify `ResourceTypes` with `ResourceTypeOptions`, your specified values override the default values.
Supported resource types: `ec2:Instance` \| `ec2:LaunchTemplate` \| `ssm:Parameter` \| `imagebuilder:ImageRecipe` \| `imagebuilder:ContainerRecipe`
Either `IncludeAllResourceTypes` or `ResourceTypes` must be specified.
Type: Boolean
Required: No

 **MaxResults**
 The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output. For more information, see [Pagination](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html#api-pagination).
Type: Integer
Valid Range: Minimum value of 5.
Required: No

 **NextToken**
The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.
Type: String
Required: No

 **ResourceType.N**
The AWS resource types to check for image references.
Either `IncludeAllResourceTypes` or `ResourceTypes` must be specified.
Type: Array of [ResourceTypeRequest](API_ResourceTypeRequest.md) objects
Required: No

## Response Elements
<a name="API_DescribeImageReferences_ResponseElements"></a>

The following elements are returned by the service.

 **imageReferenceSet**
The resources that are referencing the specified images.
Type: Array of [ImageReference](API_ImageReference.md) objects

 **nextToken**
The token to include in another request to get the next page of items. This value is `null` when there are no more items to return.
Type: String

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_DescribeImageReferences_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_DescribeImageReferences_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DescribeImageReferences)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DescribeImageReferences)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DescribeImageReferences)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DescribeImageReferences)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DescribeImageReferences)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DescribeImageReferences)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DescribeImageReferences)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DescribeImageReferences)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DescribeImageReferences)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DescribeImageReferences)
