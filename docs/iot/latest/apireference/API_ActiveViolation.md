---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_ActiveViolation.html
---

# ActiveViolation
<a name="API_ActiveViolation"></a>

Information about an active Device Defender security profile behavior violation.

## Contents
<a name="API_ActiveViolation_Contents"></a>

 ** behavior **   <a name="iot-Type-ActiveViolation-behavior"></a>
The behavior that is being violated.
Type: [Behavior](API_Behavior.md) object
Required: No

 ** lastViolationTime **   <a name="iot-Type-ActiveViolation-lastViolationTime"></a>
The time the most recent violation occurred.
Type: Timestamp
Required: No

 ** lastViolationValue **   <a name="iot-Type-ActiveViolation-lastViolationValue"></a>
The value of the metric (the measurement) that caused the most recent violation.
Type: [MetricValue](API_MetricValue.md) object
Required: No

 ** securityProfileName **   <a name="iot-Type-ActiveViolation-securityProfileName"></a>
The security profile with the behavior is in violation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9:_-]+`
Required: No

 ** thingName **   <a name="iot-Type-ActiveViolation-thingName"></a>
The name of the thing responsible for the active violation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** verificationState **   <a name="iot-Type-ActiveViolation-verificationState"></a>
The verification state of the violation (detect alarm).
Type: String
Valid Values: `FALSE_POSITIVE | BENIGN_POSITIVE | TRUE_POSITIVE | UNKNOWN`
Required: No

 ** verificationStateDescription **   <a name="iot-Type-ActiveViolation-verificationStateDescription"></a>
The description of the verification state of the violation.
Type: String
Length Constraints: Maximum length of 1000.
Pattern: `[^\p{Cntrl}]*`
Required: No

 ** violationEventAdditionalInfo **   <a name="iot-Type-ActiveViolation-violationEventAdditionalInfo"></a>
 The details of a violation event.
Type: [ViolationEventAdditionalInfo](API_ViolationEventAdditionalInfo.md) object
Required: No

 ** violationId **   <a name="iot-Type-ActiveViolation-violationId"></a>
The ID of the active violation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9\-]+`
Required: No

 ** violationStartTime **   <a name="iot-Type-ActiveViolation-violationStartTime"></a>
The time the violation started.
Type: Timestamp
Required: No

## See Also
<a name="API_ActiveViolation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/ActiveViolation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/ActiveViolation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/ActiveViolation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
