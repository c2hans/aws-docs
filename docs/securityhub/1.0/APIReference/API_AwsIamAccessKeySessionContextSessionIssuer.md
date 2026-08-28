---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsIamAccessKeySessionContextSessionIssuer.html
---

# AwsIamAccessKeySessionContextSessionIssuer
<a name="API_AwsIamAccessKeySessionContextSessionIssuer"></a>

Information about the entity that created the session.

## Contents
<a name="API_AwsIamAccessKeySessionContextSessionIssuer_Contents"></a>

 ** AccountId **   <a name="securityhub-Type-AwsIamAccessKeySessionContextSessionIssuer-AccountId"></a>
The identifier of the AWS account that created the session.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Arn **   <a name="securityhub-Type-AwsIamAccessKeySessionContextSessionIssuer-Arn"></a>
The ARN of the session.
Type: String
Pattern: `.*\S.*`
Required: No

 ** PrincipalId **   <a name="securityhub-Type-AwsIamAccessKeySessionContextSessionIssuer-PrincipalId"></a>
The principal ID of the principal (user, role, or group) that created the session.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Type **   <a name="securityhub-Type-AwsIamAccessKeySessionContextSessionIssuer-Type"></a>
The type of principal (user, role, or group) that created the session.
Type: String
Pattern: `.*\S.*`
Required: No

 ** UserName **   <a name="securityhub-Type-AwsIamAccessKeySessionContextSessionIssuer-UserName"></a>
The name of the principal that created the session.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsIamAccessKeySessionContextSessionIssuer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsIamAccessKeySessionContextSessionIssuer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsIamAccessKeySessionContextSessionIssuer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsIamAccessKeySessionContextSessionIssuer)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
