---
source_url: https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_DeregistrationPolicy.html
---

# DeregistrationPolicy
<a name="API_DeregistrationPolicy"></a>

The deregistration policy for the data that's stored in AWS Audit Manager. You can use this attribute to determine how your data is handled when you [deregister Audit Manager](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_DeregisterAccount.html).

By default, Audit Manager retains evidence data for two years from the time of its creation. Other Audit Manager resources (including assessments, custom controls, and custom frameworks) remain in Audit Manager indefinitely, and are available if you [re-register Audit Manager](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_RegisterAccount.html) in the future. For more information about data retention, see [Data Protection](https://docs.aws.amazon.com/audit-manager/latest/userguide/data-protection.html) in the * AWS Audit Manager User Guide*.

**Important**
If you choose to delete all data, this action permanently deletes all evidence data in your account within seven days. It also deletes all of the Audit Manager resources that you created, including assessments, custom controls, and custom frameworks. Your data will not be available if you re-register Audit Manager in the future.

## Contents
<a name="API_DeregistrationPolicy_Contents"></a>

 ** deleteResources **   <a name="auditmanager-Type-DeregistrationPolicy-deleteResources"></a>
Specifies which Audit Manager data will be deleted when you deregister Audit Manager.
+ If you set the value to `ALL`, all of your data is deleted within seven days of deregistration.
+ If you set the value to `DEFAULT`, none of your data is deleted at the time of deregistration. However, keep in mind that the Audit Manager data retention policy still applies. As a result, any evidence data will be deleted two years after its creation date. Your other Audit Manager resources will continue to exist indefinitely.
Type: String
Valid Values: `ALL | DEFAULT`
Required: No

## See Also
<a name="API_DeregistrationPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/auditmanager-2017-07-25/DeregistrationPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/auditmanager-2017-07-25/DeregistrationPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/auditmanager-2017-07-25/DeregistrationPolicy)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Audit Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query audit-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
