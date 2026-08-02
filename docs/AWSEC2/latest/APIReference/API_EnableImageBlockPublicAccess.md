---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_EnableImageBlockPublicAccess.html
---

# EnableImageBlockPublicAccess
<a name="API_EnableImageBlockPublicAccess"></a>

Enables *block public access for AMIs* at the account level in the specified AWS Region. This prevents the public sharing of your AMIs. However, if you already have public AMIs, they will remain publicly available.

The API can take up to 10 minutes to configure this setting. During this time, if you run [GetImageBlockPublicAccessState](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetImageBlockPublicAccessState.html), the response will be `unblocked`. When the API has completed the configuration, the response will be `block-new-sharing`.

For more information, see [Block public access to your AMIs](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/block-public-access-to-amis.html) in the *Amazon EC2 User Guide*.

## Request Parameters
<a name="API_EnableImageBlockPublicAccess_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **ImageBlockPublicAccessState**
Specify `block-new-sharing` to enable block public access for AMIs at the account level in the specified Region. This will block any attempt to publicly share your AMIs in the specified Region.
Type: String
Valid Values: `block-new-sharing`
Required: Yes

## Response Elements
<a name="API_EnableImageBlockPublicAccess_ResponseElements"></a>

The following elements are returned by the service.

 **imageBlockPublicAccessState**
Returns `block-new-sharing` if the request succeeds; otherwise, it returns an error.
Type: String
Valid Values: `block-new-sharing`

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_EnableImageBlockPublicAccess_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_EnableImageBlockPublicAccess_Examples"></a>

### Example
<a name="API_EnableImageBlockPublicAccess_Example_1"></a>

This example enables *block public access for AMIs* at the account level in the specified Region to prevent users in your account from publicly sharing your AMIs in the specified Region. If you already have public AMIs, they will remain publicly available.

#### Sample Request
<a name="API_EnableImageBlockPublicAccess_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=EnableImageBlockPublicAccess
&Region=us-east-1
&ImageBlockPublicAccessState=block-new-sharing
&AUTHPARAMS
```

#### Sample Response
<a name="API_EnableImageBlockPublicAccess_Example_1_Response"></a>

```
<EnableImageBlockPublicAccessResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
  <requestId>11aabb229-4eac-35bd-99ed-be587EXAMPLE</requestId>
  <return>block-new-sharing</return>
</EnableImageBlockPublicAccessResponse>
```

## See Also
<a name="API_EnableImageBlockPublicAccess_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/EnableImageBlockPublicAccess)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/EnableImageBlockPublicAccess)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/EnableImageBlockPublicAccess)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/EnableImageBlockPublicAccess)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/EnableImageBlockPublicAccess)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/EnableImageBlockPublicAccess)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/EnableImageBlockPublicAccess)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/EnableImageBlockPublicAccess)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/EnableImageBlockPublicAccess)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/EnableImageBlockPublicAccess)
