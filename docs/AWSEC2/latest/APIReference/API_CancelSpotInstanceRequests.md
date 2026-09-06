---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CancelSpotInstanceRequests.html
---

# CancelSpotInstanceRequests
<a name="API_CancelSpotInstanceRequests"></a>

Cancels one or more Spot Instance requests.

**Important**
Canceling a Spot Instance request does not terminate running Spot Instances associated with the request.

## Request Parameters
<a name="API_CancelSpotInstanceRequests_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **SpotInstanceRequestId.N**
The IDs of the Spot Instance requests.
Type: Array of strings
Required: Yes

## Response Elements
<a name="API_CancelSpotInstanceRequests_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **spotInstanceRequestSet**
The Spot Instance requests.
Type: Array of [CancelledSpotInstanceRequest](API_CancelledSpotInstanceRequest.md) objects

## Errors
<a name="API_CancelSpotInstanceRequests_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_CancelSpotInstanceRequests_Examples"></a>

### Example
<a name="API_CancelSpotInstanceRequests_Example_1"></a>

This example cancels the specified Spot Instance request.

#### Sample Request
<a name="API_CancelSpotInstanceRequests_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=CancelSpotInstanceRequests
&SpotInstanceRequestId.1=sir-1a2b3c4d
&AUTHPARAMS
```

#### Sample Response
<a name="API_CancelSpotInstanceRequests_Example_1_Response"></a>

```
<CancelSpotInstanceRequestsResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
  <requestId>59dbff89-35bd-4eac-99ed-be587EXAMPLE</requestId>
  <spotInstanceRequestSet>
    <item>
      <spotInstanceRequestId>sir-1a2b3c4d</spotInstanceRequestId>
      <state>cancelled</state>
    </item>
  </spotInstanceRequestSet>
</CancelSpotInstanceRequestsResponse>
```

## See Also
<a name="API_CancelSpotInstanceRequests_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/CancelSpotInstanceRequests)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/CancelSpotInstanceRequests)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CancelSpotInstanceRequests)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/CancelSpotInstanceRequests)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CancelSpotInstanceRequests)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/CancelSpotInstanceRequests)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/CancelSpotInstanceRequests)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/CancelSpotInstanceRequests)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/CancelSpotInstanceRequests)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CancelSpotInstanceRequests)
