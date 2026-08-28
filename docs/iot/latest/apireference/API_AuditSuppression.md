---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_AuditSuppression.html
---

# AuditSuppression
<a name="API_AuditSuppression"></a>

 Filters out specific findings of a Device Defender audit.

## Contents
<a name="API_AuditSuppression_Contents"></a>

 ** checkName **   <a name="iot-Type-AuditSuppression-checkName"></a>
An audit check name. Checks must be enabled for your account. (Use `DescribeAccountAuditConfiguration` to see the list of all checks, including those that are enabled or use `UpdateAccountAuditConfiguration` to select which checks are enabled.)
Type: String
Required: Yes

 ** resourceIdentifier **   <a name="iot-Type-AuditSuppression-resourceIdentifier"></a>
Information that identifies the noncompliant resource.
Type: [ResourceIdentifier](API_ResourceIdentifier.md) object
Required: Yes

 ** description **   <a name="iot-Type-AuditSuppression-description"></a>
 The description of the audit suppression.
Type: String
Length Constraints: Maximum length of 1000.
Pattern: `[\p{Graph}\x20]*`
Required: No

 ** expirationDate **   <a name="iot-Type-AuditSuppression-expirationDate"></a>
 The expiration date (epoch timestamp in seconds) that you want the suppression to adhere to.
Type: Timestamp
Required: No

 ** suppressIndefinitely **   <a name="iot-Type-AuditSuppression-suppressIndefinitely"></a>
 Indicates whether a suppression should exist indefinitely or not.
Type: Boolean
Required: No

## See Also
<a name="API_AuditSuppression_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/AuditSuppression)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/AuditSuppression)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/AuditSuppression)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
