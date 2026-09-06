---
source_url: https://docs.aws.amazon.com/arc-zonal-shift/latest/api/API_ControlCondition.html
---

# ControlCondition
<a name="API_ControlCondition"></a>

A control condition is an alarm that you specify for a practice run. When you configure practice runs with zonal autoshift for a resource, you specify Amazon CloudWatch alarms, which you create in CloudWatch to use with the practice run. The alarms that you specify are an *outcome alarm*, to monitor application health during practice runs and, optionally, a *blocking alarm*, to block practice runs from starting or to interrupt a practice run in progress.

Control condition alarms do not apply for autoshifts.

For more information, see [ Considerations when you configure zonal autoshift](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-autoshift.considerations.html) in the Amazon Application Recovery Controller Developer Guide.

## Contents
<a name="API_ControlCondition_Contents"></a>

 ** alarmIdentifier **   <a name="zonalshift-Type-ControlCondition-alarmIdentifier"></a>
The Amazon Resource Name (ARN) for an Amazon CloudWatch alarm that you specify as a control condition for a practice run.
Type: String
Length Constraints: Minimum length of 8. Maximum length of 1024.
Pattern: `.*`
Required: Yes

 ** type **   <a name="zonalshift-Type-ControlCondition-type"></a>
The type of alarm specified for a practice run. You can only specify Amazon CloudWatch alarms for practice runs, so the only valid value is `CLOUDWATCH`.
Type: String
Valid Values: `CLOUDWATCH`
Required: Yes

## See Also
<a name="API_ControlCondition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/arc-zonal-shift-2022-10-30/ControlCondition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/arc-zonal-shift-2022-10-30/ControlCondition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/arc-zonal-shift-2022-10-30/ControlCondition)
