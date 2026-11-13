---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_InvestigationFilterCriteria.html
---

# InvestigationFilterCriteria
<a name="API_InvestigationFilterCriteria"></a>

Contains the criteria used to filter investigations.

## Contents
<a name="API_InvestigationFilterCriteria_Contents"></a>

 ** criterion **   <a name="guardduty-Type-InvestigationFilterCriteria-criterion"></a>
A map of investigation attributes to the conditions that they must match. When you specify more than one attribute, an investigation must match the conditions for every attribute. Valid attributes and values:
+  `STATUS` – `RUNNING`, `COMPLETED`, and `FAILED`.
+  `RISK_LEVEL` – `Info`, `Low`, `Medium`, `High`, and `Critical`.
+  `CONFIDENCE` – `Unknown`, `Low`, `Medium`, and `High`.
+  `FINDING_ID` – A finding ID, which is 32 lowercase hexadecimal characters.
+  `INVESTIGATION_TYPE` – `FINDING`, `ACCOUNT`, and `ORGANIZATION`.
Values are case sensitive. GuardDuty sets the risk level, confidence, and investigation type of an investigation only when the investigation completes.
Type: String to [InvestigationFilterCondition](API_InvestigationFilterCondition.md) object map
Valid Keys: `STATUS | RISK_LEVEL | CONFIDENCE | FINDING_ID | INVESTIGATION_TYPE`
Required: No

## See Also
<a name="API_InvestigationFilterCriteria_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/InvestigationFilterCriteria)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/InvestigationFilterCriteria)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/InvestigationFilterCriteria)
