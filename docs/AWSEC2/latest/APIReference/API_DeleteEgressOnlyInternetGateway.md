---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteEgressOnlyInternetGateway.html
---

# DeleteEgressOnlyInternetGateway
<a name="API_DeleteEgressOnlyInternetGateway"></a>

Deletes an egress-only internet gateway.

## Request Parameters
<a name="API_DeleteEgressOnlyInternetGateway_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **EgressOnlyInternetGatewayId**
The ID of the egress-only internet gateway.
Type: String
Required: Yes

## Response Elements
<a name="API_DeleteEgressOnlyInternetGateway_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **returnCode**
Returns `true` if the request succeeds; otherwise, it returns an error.
Type: Boolean

## Errors
<a name="API_DeleteEgressOnlyInternetGateway_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DeleteEgressOnlyInternetGateway_Examples"></a>

### Example
<a name="API_DeleteEgressOnlyInternetGateway_Example_1"></a>

This example deletes the specified egress-only internet gateway.

#### Sample Request
<a name="API_DeleteEgressOnlyInternetGateway_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=DeleteEgressOnlyInternetGateway
&EgressOnlyInternetGatewayId=eigw-015e0e244e24dfe8a
&AUTHPARAMS
```

#### Sample Response
<a name="API_DeleteEgressOnlyInternetGateway_Example_1_Response"></a>

```
<DeleteEgressOnlyInternetGateway xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
  <requestId>59dbff89-35bd-4eac-99ed-be587EXAMPLE</requestId>
  <returnCode>true</returnCode>
</DeleteEgressOnlyInternetGateway>
```

## See Also
<a name="API_DeleteEgressOnlyInternetGateway_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DeleteEgressOnlyInternetGateway)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DeleteEgressOnlyInternetGateway)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DeleteEgressOnlyInternetGateway)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DeleteEgressOnlyInternetGateway)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DeleteEgressOnlyInternetGateway)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DeleteEgressOnlyInternetGateway)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DeleteEgressOnlyInternetGateway)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DeleteEgressOnlyInternetGateway)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DeleteEgressOnlyInternetGateway)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DeleteEgressOnlyInternetGateway)
