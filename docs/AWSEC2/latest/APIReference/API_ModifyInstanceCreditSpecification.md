---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyInstanceCreditSpecification.html
---

# ModifyInstanceCreditSpecification
<a name="API_ModifyInstanceCreditSpecification"></a>

Modifies the credit option for CPU usage on a running or stopped burstable performance instance. The credit options are `standard` and `unlimited`.

For more information, see [Burstable performance instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/burstable-performance-instances.html) in the *Amazon EC2 User Guide*.

## Request Parameters
<a name="API_ModifyInstanceCreditSpecification_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **ClientToken**
A unique, case-sensitive token that you provide to ensure idempotency of your modification request. For more information, see [Ensuring Idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html).
Type: String
Required: No

 **DryRun**
Checks whether you have the required permissions for the operation, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **InstanceCreditSpecification.N**
Information about the credit option for CPU usage.
Type: Array of [InstanceCreditSpecificationRequest](API_InstanceCreditSpecificationRequest.md) objects
Required: Yes

## Response Elements
<a name="API_ModifyInstanceCreditSpecification_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **successfulInstanceCreditSpecificationSet**
Information about the instances whose credit option for CPU usage was successfully modified.
Type: Array of [SuccessfulInstanceCreditSpecificationItem](API_SuccessfulInstanceCreditSpecificationItem.md) objects

 **unsuccessfulInstanceCreditSpecificationSet**
Information about the instances whose credit option for CPU usage was not modified.
Type: Array of [UnsuccessfulInstanceCreditSpecificationItem](API_UnsuccessfulInstanceCreditSpecificationItem.md) objects

## Errors
<a name="API_ModifyInstanceCreditSpecification_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_ModifyInstanceCreditSpecification_Examples"></a>

### Example
<a name="API_ModifyInstanceCreditSpecification_Example_1"></a>

This request modifies the credit option for CPU usage of the specified instance in the specified Region to `unlimited`. Valid credit options are `standard` and `unlimited`.

#### Sample Request
<a name="API_ModifyInstanceCreditSpecification_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=ModifyInstanceCreditSpecification
&Region=us-east-1
&InstanceCreditSpecification.1.InstanceId=i-1234567890abcdef0
&InstanceCreditSpecification.1.CpuCredits=unlimited
&AUTHPARAMS
```

#### Sample Response
<a name="API_ModifyInstanceCreditSpecification_Example_1_Response"></a>

```
<ModifyInstanceCreditSpecificationResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>11111111-2222-3333-4444-5555EXAMPLE</requestId>
    <unsuccessfulInstanceCreditSpecificationSet/>
    <successfulInstanceCreditSpecificationSet>
        <item>
            <instanceId>i-1234567890abcdef0</instanceId>
        </item>
    </successfulInstanceCreditSpecificationSet>
```

## See Also
<a name="API_ModifyInstanceCreditSpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/ModifyInstanceCreditSpecification)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/ModifyInstanceCreditSpecification)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ModifyInstanceCreditSpecification)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/ModifyInstanceCreditSpecification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ModifyInstanceCreditSpecification)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/ModifyInstanceCreditSpecification)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/ModifyInstanceCreditSpecification)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/ModifyInstanceCreditSpecification)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/ModifyInstanceCreditSpecification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ModifyInstanceCreditSpecification)
