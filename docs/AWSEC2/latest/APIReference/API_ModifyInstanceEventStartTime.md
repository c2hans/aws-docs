---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyInstanceEventStartTime.html
---

# ModifyInstanceEventStartTime
<a name="API_ModifyInstanceEventStartTime"></a>

Modifies the start time for a scheduled Amazon EC2 instance event.

## Request Parameters
<a name="API_ModifyInstanceEventStartTime_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the operation, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **InstanceEventId**
The ID of the event whose date and time you are modifying.
Type: String
Required: Yes

 **InstanceId**
The ID of the instance with the scheduled event.
Type: String
Required: Yes

 **NotBefore**
The new date and time when the event will take place.
Type: Timestamp
Required: Yes

## Response Elements
<a name="API_ModifyInstanceEventStartTime_ResponseElements"></a>

The following elements are returned by the service.

 **event**
Information about the event.
Type: [InstanceStatusEvent](API_InstanceStatusEvent.md) object

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_ModifyInstanceEventStartTime_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_ModifyInstanceEventStartTime_Examples"></a>

### Example
<a name="API_ModifyInstanceEventStartTime_Example_1"></a>

The following example shows how to modify the event start time for the specified instance. The event ID is specified by the `InstanceEventId` parameter and the new date and time is specified by the `NotBefore` parameter.

#### Sample Request
<a name="API_ModifyInstanceEventStartTime_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=ModifyInstanceEventStartTime
&InstanceId=i-1234567890abcdef0
&InstanceEventId=instance-event-0abcdef1234567890
&NotBefore=2019-03-25T10:00:00.000
&AUTHPARAMS
```

## See Also
<a name="API_ModifyInstanceEventStartTime_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/ModifyInstanceEventStartTime)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/ModifyInstanceEventStartTime)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ModifyInstanceEventStartTime)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/ModifyInstanceEventStartTime)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ModifyInstanceEventStartTime)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/ModifyInstanceEventStartTime)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/ModifyInstanceEventStartTime)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/ModifyInstanceEventStartTime)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/ModifyInstanceEventStartTime)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ModifyInstanceEventStartTime)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
