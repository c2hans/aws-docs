---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_OrganizationEnrollmentConfiguration.html
---

# OrganizationEnrollmentConfiguration

An organization enrollment configuration sets the organization rule mode on an account, organizational unit (OU), or the organization root and enables Automation for affected member accounts that have opted in to Compute Optimizer.

## Contents
<a name="API_automation_OrganizationEnrollmentConfiguration_Contents"></a>

 ** targetId **   <a name="computeoptimizer-Type-automation_OrganizationEnrollmentConfiguration-targetId"></a>
The ID of the account, organizational unit (OU), or organization root on which the configuration is stored.
Type: String
Required: Yes

 ** targetType **   <a name="computeoptimizer-Type-automation_OrganizationEnrollmentConfiguration-targetType"></a>
The type of target on which the configuration is stored.
Type: String
Valid Values: `Account | OrganizationalUnit`
Required: Yes

 ** organizationRuleMode **   <a name="computeoptimizer-Type-automation_OrganizationEnrollmentConfiguration-organizationRuleMode"></a>
The organization rule mode set on the target by the organization enrollment configuration.
Type: String
Valid Values: `AnyAllowed | NoneAllowed`
Required: No

## See Also
<a name="API_automation_OrganizationEnrollmentConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-automation-2025-09-22/OrganizationEnrollmentConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-automation-2025-09-22/OrganizationEnrollmentConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-automation-2025-09-22/OrganizationEnrollmentConfiguration)
