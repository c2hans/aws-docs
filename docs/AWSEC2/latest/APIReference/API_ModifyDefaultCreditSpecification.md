---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyDefaultCreditSpecification.html
---

# ModifyDefaultCreditSpecification
<a name="API_ModifyDefaultCreditSpecification"></a>

Modifies the default credit option for CPU usage of burstable performance instances. The default credit option is set at the account level per AWS Region, and is specified per instance family. All new burstable performance instances in the account launch using the default credit option.

 `ModifyDefaultCreditSpecification` is an asynchronous operation, which works at an AWS Region level and modifies the credit option for each Availability Zone. All zones in a Region are updated within five minutes. But if instances are launched during this operation, they might not get the new credit option until the zone is updated. To verify whether the update has occurred, you can call `GetDefaultCreditSpecification` and check `DefaultCreditSpecification` for updates.

For more information, see [Burstable performance instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/burstable-performance-instances.html) in the *Amazon EC2 User Guide*.

## Request Parameters
<a name="API_ModifyDefaultCreditSpecification_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **CpuCredits**
The credit option for CPU usage of the instance family.
Valid Values: `standard` \| `unlimited`
Type: String
Required: Yes

 **DryRun**
Checks whether you have the required permissions for the operation, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **InstanceFamily**
The instance family.
Type: String
Valid Values: `t2 | t3 | t3a | t4g`
Required: Yes

## Response Elements
<a name="API_ModifyDefaultCreditSpecification_ResponseElements"></a>

The following elements are returned by the service.

 **instanceFamilyCreditSpecification**
The default credit option for CPU usage of the instance family.
Type: [InstanceFamilyCreditSpecification](API_InstanceFamilyCreditSpecification.md) object

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_ModifyDefaultCreditSpecification_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_ModifyDefaultCreditSpecification_Examples"></a>

### Example 1
<a name="API_ModifyDefaultCreditSpecification_Example_1"></a>

This example modifies the default credit option for CPU usage to `unlimited` for all instances in the T2 instance family in the specified Region.

#### Sample Request
<a name="API_ModifyDefaultCreditSpecification_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=ModifyDefaultCreditSpecification
&Region=us-east-1
&InstanceFamily=t2
&CpuCredits=unlimited
&AUTHPARAMS
```

#### Sample Response
<a name="API_ModifyDefaultCreditSpecification_Example_1_Response"></a>

```
<ModifyDefaultCreditSpecificationResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>11111111-2222-3333-4444-5555EXAMPLE</requestId>
    <instanceFamilyCreditSpecification>
        <cpuCredits>unlimited</cpuCredits>
        <instanceFamily>t2</instanceFamily>
    </instanceFamilyCreditSpecification>
</ModifyDefaultCreditSpecificationResponse>
```

### Example 2
<a name="API_ModifyDefaultCreditSpecification_Example_2"></a>

This example modifies the default credit option for CPU usage to `standard` for all instances in the T3 instance family in the specified Region.

#### Sample Request
<a name="API_ModifyDefaultCreditSpecification_Example_2_Request"></a>

```
https://ec2.amazonaws.com/?Action=ModifyDefaultCreditSpecification
&Region=us-east-1
&InstanceFamily=t3
&CpuCredits=standard
&AUTHPARAMS
```

#### Sample Response
<a name="API_ModifyDefaultCreditSpecification_Example_2_Response"></a>

```
<ModifyDefaultCreditSpecificationResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>11111111-2222-3333-4444-5555EXAMPLE</requestId>
    <instanceFamilyCreditSpecification>
        <cpuCredits>standard</cpuCredits>
        <instanceFamily>t3</instanceFamily>
    </instanceFamilyCreditSpecification>
</ModifyDefaultCreditSpecificationResponse>
```

## See Also
<a name="API_ModifyDefaultCreditSpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/ModifyDefaultCreditSpecification)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/ModifyDefaultCreditSpecification)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ModifyDefaultCreditSpecification)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/ModifyDefaultCreditSpecification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ModifyDefaultCreditSpecification)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/ModifyDefaultCreditSpecification)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/ModifyDefaultCreditSpecification)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/ModifyDefaultCreditSpecification)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/ModifyDefaultCreditSpecification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ModifyDefaultCreditSpecification)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
