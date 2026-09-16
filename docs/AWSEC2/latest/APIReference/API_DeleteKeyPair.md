---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteKeyPair.html
---

# DeleteKeyPair
<a name="API_DeleteKeyPair"></a>

Deletes the specified key pair, by removing the public key from Amazon EC2.

## Request Parameters
<a name="API_DeleteKeyPair_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **KeyName**
The name of the key pair.
Type: String
Required: No

 **KeyPairId**
The ID of the key pair.
Type: String
Required: No

## Response Elements
<a name="API_DeleteKeyPair_ResponseElements"></a>

The following elements are returned by the service.

 **keyPairId**
The ID of the key pair.
Type: String

 **requestId**
The ID of the request.
Type: String

 **return**
Is `true` if the request succeeds, and an error otherwise.
Type: Boolean

## Errors
<a name="API_DeleteKeyPair_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DeleteKeyPair_Examples"></a>

### Example 1
<a name="API_DeleteKeyPair_Example_1"></a>

This example request deletes the key pair named `my-key-pair`.

#### Sample Request
<a name="API_DeleteKeyPair_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=DeleteKeyPair
&KeyName=my-key-pair
&AUTHPARAMS
```

#### Sample Response
<a name="API_DeleteKeyPair_Example_1_Response"></a>

```
<DeleteKeyPairResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
  <return>true</return>
  <keyPairId>key-12345abcdeEXAMPLE</keyPairId>
</DeleteKeyPairResponse>
```

### Example 2
<a name="API_DeleteKeyPair_Example_2"></a>

This example request deletes a key pair with the ID `key-abcd12345eEXAMPLE`.

#### Sample Request
<a name="API_DeleteKeyPair_Example_2_Request"></a>

```
https://ec2.amazonaws.com/?Action=DeleteKeyPair
&KeyPairId=key-abcd12345eEXAMPLE
&AUTHPARAMS
```

#### Sample Response
<a name="API_DeleteKeyPair_Example_2_Response"></a>

```
<DeleteKeyPairResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
  <return>true</return>
  <keyPairId>key-abcd12345eEXAMPLE</keyPairId>
</DeleteKeyPairResponse>
```

## See Also
<a name="API_DeleteKeyPair_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DeleteKeyPair)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DeleteKeyPair)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DeleteKeyPair)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DeleteKeyPair)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DeleteKeyPair)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DeleteKeyPair)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DeleteKeyPair)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DeleteKeyPair)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DeleteKeyPair)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DeleteKeyPair)
