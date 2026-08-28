---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DisableImageBlockPublicAccess.html
---

# DisableImageBlockPublicAccess
<a name="API_DisableImageBlockPublicAccess"></a>

Disables *block public access for AMIs* at the account level in the specified AWS Region. This removes the *block public access* restriction from your account. With the restriction removed, you can publicly share your AMIs in the specified AWS Region.

For more information, see [Block public access to your AMIs](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/block-public-access-to-amis.html) in the *Amazon EC2 User Guide*.

## Request Parameters
<a name="API_DisableImageBlockPublicAccess_RequestParameters"></a>

For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

## Response Elements
<a name="API_DisableImageBlockPublicAccess_ResponseElements"></a>

The following elements are returned by the service.

 **imageBlockPublicAccessState**
Returns `unblocked` if the request succeeds; otherwise, it returns an error.
Type: String
Valid Values: `unblocked`

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_DisableImageBlockPublicAccess_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DisableImageBlockPublicAccess_Examples"></a>

### Example
<a name="API_DisableImageBlockPublicAccess_Example_1"></a>

This example disables *block public access for AMIs* at the account level in the specified Region to allow users in your account to publicly share your AMIs in the specified Region.

#### Sample Request
<a name="API_DisableImageBlockPublicAccess_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=DisableImageBlockPublicAccess
&Region=us-east-1
&AUTHPARAMS
```

#### Sample Response
<a name="API_DisableImageBlockPublicAccess_Example_1_Response"></a>

```
<DisableImageBlockPublicAccessResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
  <requestId>11aabb229-4eac-35bd-99ed-be587EXAMPLE</requestId>
  <return>unblocked</return>
</DisableImageBlockPublicAccessResponse>
```

## See Also
<a name="API_DisableImageBlockPublicAccess_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DisableImageBlockPublicAccess)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DisableImageBlockPublicAccess)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DisableImageBlockPublicAccess)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DisableImageBlockPublicAccess)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DisableImageBlockPublicAccess)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DisableImageBlockPublicAccess)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DisableImageBlockPublicAccess)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DisableImageBlockPublicAccess)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DisableImageBlockPublicAccess)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DisableImageBlockPublicAccess)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
