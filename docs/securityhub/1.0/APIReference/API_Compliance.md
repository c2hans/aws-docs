---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_Compliance.html
---

# Compliance
<a name="API_Compliance"></a>

This object typically provides details about a control finding, such as applicable standards and the status of control checks. While finding providers can add custom content in `Compliance` object fields, they are typically used to review details of Security Hub CSPM control findings.

## Contents
<a name="API_Compliance_Contents"></a>

 ** AssociatedStandards **   <a name="securityhub-Type-Compliance-AssociatedStandards"></a>
Typically provides an array of enabled security standards in which a security control is currently enabled.
Type: Array of [AssociatedStandard](API_AssociatedStandard.md) objects
Required: No

 ** RelatedRequirements **   <a name="securityhub-Type-Compliance-RelatedRequirements"></a>
Typically provides the industry or regulatory framework requirements that are related to a control. The check for that control is aligned with these requirements.
Array Members: Maximum number of 32 items.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

 ** SecurityControlId **   <a name="securityhub-Type-Compliance-SecurityControlId"></a>
 Typically provides the unique identifier of a control across standards. For Security Hub CSPM controls, this field consists of an AWS service and a unique number, such as `APIGateway.5`.
Type: String
Pattern: `.*\S.*`
Required: No

 ** SecurityControlParameters **   <a name="securityhub-Type-Compliance-SecurityControlParameters"></a>
 Typically an object that includes security control parameter names and values.
Type: Array of [SecurityControlParameter](API_SecurityControlParameter.md) objects
Required: No

 ** Status **   <a name="securityhub-Type-Compliance-Status"></a>
Typically summarizes the result of a control check.
For Security Hub CSPM controls, valid values for `Status` are as follows.
+
  +  `PASSED` - Standards check passed for all evaluated resources.
  +  `WARNING` - Some information is missing or this check is not supported for your configuration.
  +  `FAILED` - Standards check failed for at least one evaluated resource.
  +  `NOT_AVAILABLE` - Check could not be performed due to a service outage, API error, or because the result of the AWS Config evaluation was `NOT_APPLICABLE`. If the AWS Config evaluation result was `NOT_APPLICABLE` for a Security Hub CSPM control, Security Hub CSPM automatically archives the finding after 3 days.
Type: String
Valid Values: `PASSED | WARNING | FAILED | NOT_AVAILABLE`
Required: No

 ** StatusReasons **   <a name="securityhub-Type-Compliance-StatusReasons"></a>
Typically used to provide a list of reasons for the value of `Status`.
Type: Array of [StatusReason](API_StatusReason.md) objects
Required: No

## See Also
<a name="API_Compliance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/Compliance)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/Compliance)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/Compliance)
