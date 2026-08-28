---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_AnomalyObject.html
---

# AnomalyObject
<a name="API_AnomalyObject"></a>

Contains information about the unusual anomalies.

## Contents
<a name="API_AnomalyObject_Contents"></a>

 ** observations **   <a name="guardduty-Type-AnomalyObject-observations"></a>
The recorded value.
Type: [Observations](API_Observations.md) object
Required: No

 ** profileSubtype **   <a name="guardduty-Type-AnomalyObject-profileSubtype"></a>
The frequency of the anomaly.
Type: String
Valid Values: `FREQUENT | INFREQUENT | UNSEEN | RARE | COUNT | AVERAGE`
Required: No

 ** profileType **   <a name="guardduty-Type-AnomalyObject-profileType"></a>
The type of behavior of the profile.
Type: String
Valid Values: `FREQUENCY | VOLUME`
Required: No

## See Also
<a name="API_AnomalyObject_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/AnomalyObject)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/AnomalyObject)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/AnomalyObject)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GuardDuty. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query guardduty` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
