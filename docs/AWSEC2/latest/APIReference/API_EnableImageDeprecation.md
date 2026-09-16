---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_EnableImageDeprecation.html
---

# EnableImageDeprecation
<a name="API_EnableImageDeprecation"></a>

Enables deprecation of the specified AMI at the specified date and time.

For more information, see [Deprecate an AMI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ami-deprecate.html) in the *Amazon EC2 User Guide*.

## Request Parameters
<a name="API_EnableImageDeprecation_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DeprecateAt**
The date and time to deprecate the AMI, in UTC, in the following format: *YYYY*-*MM*-*DD*T*HH*:*MM*:*SS*Z. If you specify a value for seconds, Amazon EC2 rounds the seconds to the nearest minute.
You can’t specify a date in the past. The upper limit for `DeprecateAt` is 10 years from now, except for public AMIs, where the upper limit is 2 years from the creation date.
Type: Timestamp
Required: Yes

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **ImageId**
The ID of the AMI.
Type: String
Required: Yes

## Response Elements
<a name="API_EnableImageDeprecation_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **return**
Returns `true` if the request succeeds; otherwise, it returns an error.
Type: Boolean

## Errors
<a name="API_EnableImageDeprecation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_EnableImageDeprecation_Examples"></a>

### Example
<a name="API_EnableImageDeprecation_Example_1"></a>

This example deprecates the specified AMI at the specified date and time. If you specify a value for seconds, Amazon EC2 rounds the seconds to the nearest minute.

#### Sample Request
<a name="API_EnableImageDeprecation_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=EnableImageDeprecation
&ImageId=ami-0123456789EXAMPLE
&DeprecateAt="2022-06-15T13:17:00.000Z"
&AUTHPARAMS
```

#### Sample Response
<a name="API_EnableImageDeprecation_Example_1_Response"></a>

```
<EnableImageDeprecationResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
  <requestId>59dbff89-35bd-4eac-99ed-be587EXAMPLE</requestId>
  <return>true</return>
</EnableImageDeprecationResponse>
```

## See Also
<a name="API_EnableImageDeprecation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/EnableImageDeprecation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/EnableImageDeprecation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/EnableImageDeprecation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/EnableImageDeprecation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/EnableImageDeprecation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/EnableImageDeprecation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/EnableImageDeprecation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/EnableImageDeprecation)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/EnableImageDeprecation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/EnableImageDeprecation)
