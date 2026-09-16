---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_UnmonitorInstances.html
---

# UnmonitorInstances
<a name="API_UnmonitorInstances"></a>

Disables detailed monitoring for a running instance. For more information, see [Monitoring your instances and volumes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-cloudwatch.html) in the *Amazon EC2 User Guide*.

## Request Parameters
<a name="API_UnmonitorInstances_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the operation, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **InstanceId.N**
The IDs of the instances.
Type: Array of strings
Required: Yes

## Response Elements
<a name="API_UnmonitorInstances_ResponseElements"></a>

The following elements are returned by the service.

 **instancesSet**
The monitoring information.
Type: Array of [InstanceMonitoring](API_InstanceMonitoring.md) objects

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_UnmonitorInstances_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_UnmonitorInstances_Examples"></a>

### Example
<a name="API_UnmonitorInstances_Example_1"></a>

This example disables detailed monitoring for the specified instances.

#### Sample Request
<a name="API_UnmonitorInstances_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=UnmonitorInstances
&InstanceId.1=i-1234567890abcdef0
&InstanceId.2=i-0598c7d356eba48d7
&AUTHPARAMS
```

#### Sample Response
<a name="API_UnmonitorInstances_Example_1_Response"></a>

```
<UnmonitorInstancesResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
   <requestId>59dbff89-35bd-4eac-99ed-be587EXAMPLE</requestId>
   <instancesSet>
      <item>
         <instanceId>i-1234567890abcdef0</instanceId>
         <monitoring>
            <state>disabled</state>
         </monitoring>
      </item>
      <item>
         <instanceId>i-0598c7d356eba48d7</instanceId>
         <monitoring>
            <state>disabled</state>
         </monitoring>
      </item>
   </instancesSet>
</UnmonitorInstancesResponse>
```

## See Also
<a name="API_UnmonitorInstances_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/UnmonitorInstances)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/UnmonitorInstances)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/UnmonitorInstances)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/UnmonitorInstances)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/UnmonitorInstances)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/UnmonitorInstances)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/UnmonitorInstances)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/UnmonitorInstances)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/UnmonitorInstances)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/UnmonitorInstances)
