---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ConfirmProductInstance.html
---

# ConfirmProductInstance
<a name="API_ConfirmProductInstance"></a>

Determines whether a product code is associated with an instance. This action can only be used by the owner of the product code. It is useful when a product code owner must verify whether another user's instance is eligible for support.

## Request Parameters
<a name="API_ConfirmProductInstance_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the operation, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **InstanceId**
The ID of the instance.
Type: String
Required: Yes

 **ProductCode**
The product code. This must be a product code that you own.
Type: String
Required: Yes

## Response Elements
<a name="API_ConfirmProductInstance_ResponseElements"></a>

The following elements are returned by the service.

 **ownerId**
The AWS account ID of the instance owner. This is only present if the product code is attached to the instance.
Type: String

 **requestId**
The ID of the request.
Type: String

 **return**
The return value of the request. Returns `true` if the specified product code is owned by the requester and associated with the specified instance.
Type: Boolean

## Errors
<a name="API_ConfirmProductInstance_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_ConfirmProductInstance_Examples"></a>

### Example
<a name="API_ConfirmProductInstance_Example_1"></a>

This example determines whether the specified product code is associated with the specified instance.

#### Sample Request
<a name="API_ConfirmProductInstance_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=ConfirmProductInstance
&ProductCode=774F4FF8
&InstanceId=i-1234567890abcdef0
&AUTHPARAMS
```

#### Sample Response
<a name="API_ConfirmProductInstance_Example_1_Response"></a>

```
<ConfirmProductInstanceResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
  <requestId>59dbff89-35bd-4eac-99ed-be587EXAMPLE</requestId>
  <return>true</return>
  <ownerId>111122223333</ownerId>
</ConfirmProductInstanceResponse>
```

## See Also
<a name="API_ConfirmProductInstance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/ConfirmProductInstance)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/ConfirmProductInstance)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ConfirmProductInstance)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/ConfirmProductInstance)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ConfirmProductInstance)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/ConfirmProductInstance)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/ConfirmProductInstance)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/ConfirmProductInstance)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/ConfirmProductInstance)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ConfirmProductInstance)
