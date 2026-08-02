---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetVpcResourcesBlockingEncryptionEnforcement.html
---

# GetVpcResourcesBlockingEncryptionEnforcement
<a name="API_GetVpcResourcesBlockingEncryptionEnforcement"></a>

Gets information about resources in a VPC that are blocking encryption enforcement.

For more information, see [Enforce VPC encryption in transit](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-encryption-controls.html) in the *Amazon VPC User Guide*.

## Request Parameters
<a name="API_GetVpcResourcesBlockingEncryptionEnforcement_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **MaxResults**
The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output. For more information, see [Pagination](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html#api-pagination).
Type: Integer
Valid Range: Minimum value of 5. Maximum value of 1000.
Required: No

 **NextToken**
The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.
Type: String
Required: No

 **VpcId**
The ID of the VPC to check for resources blocking encryption enforcement.
Type: String
Required: Yes

## Response Elements
<a name="API_GetVpcResourcesBlockingEncryptionEnforcement_ResponseElements"></a>

The following elements are returned by the service.

 **nextToken**
The token to include in another request to get the next page of items. This value is `null` when there are no more items to return.
Type: String

 **nonCompliantResourceSet**
Information about resources that are blocking encryption enforcement.
Type: Array of [VpcEncryptionNonCompliantResource](API_VpcEncryptionNonCompliantResource.md) objects

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_GetVpcResourcesBlockingEncryptionEnforcement_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_GetVpcResourcesBlockingEncryptionEnforcement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/GetVpcResourcesBlockingEncryptionEnforcement)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/GetVpcResourcesBlockingEncryptionEnforcement)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/GetVpcResourcesBlockingEncryptionEnforcement)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/GetVpcResourcesBlockingEncryptionEnforcement)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/GetVpcResourcesBlockingEncryptionEnforcement)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/GetVpcResourcesBlockingEncryptionEnforcement)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/GetVpcResourcesBlockingEncryptionEnforcement)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/GetVpcResourcesBlockingEncryptionEnforcement)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/GetVpcResourcesBlockingEncryptionEnforcement)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/GetVpcResourcesBlockingEncryptionEnforcement)
