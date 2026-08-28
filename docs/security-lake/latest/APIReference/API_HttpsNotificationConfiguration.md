---
source_url: https://docs.aws.amazon.com/security-lake/latest/APIReference/API_HttpsNotificationConfiguration.html
---

# HttpsNotificationConfiguration
<a name="API_HttpsNotificationConfiguration"></a>

The configurations used for HTTPS subscriber notification.

## Contents
<a name="API_HttpsNotificationConfiguration_Contents"></a>

 ** endpoint **   <a name="securitylake-Type-HttpsNotificationConfiguration-endpoint"></a>
The subscription endpoint in Security Lake. If you prefer notification with an HTTPs endpoint, populate this field.
Type: String
Pattern: `https?://.+`
Required: Yes

 ** targetRoleArn **   <a name="securitylake-Type-HttpsNotificationConfiguration-targetRoleArn"></a>
The Amazon Resource Name (ARN) of the EventBridge API destinations IAM role that you created. For more information about ARNs and how to use them in policies, see [Managing data access](https://docs.aws.amazon.com//security-lake/latest/userguide/subscriber-data-access.html) and [AWS Managed Policies](https://docs.aws.amazon.com/security-lake/latest/userguide/security-iam-awsmanpol.html) in the *Amazon Security Lake User Guide*.
Type: String
Pattern: `arn:(aws[a-zA-Z-]*)?:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`
Required: Yes

 ** authorizationApiKeyName **   <a name="securitylake-Type-HttpsNotificationConfiguration-authorizationApiKeyName"></a>
The key name for the notification subscription.
Type: String
Required: No

 ** authorizationApiKeyValue **   <a name="securitylake-Type-HttpsNotificationConfiguration-authorizationApiKeyValue"></a>
The key value for the notification subscription.
Type: String
Required: No

 ** httpMethod **   <a name="securitylake-Type-HttpsNotificationConfiguration-httpMethod"></a>
The HTTPS method used for the notification subscription.
Type: String
Valid Values: `POST | PUT`
Required: No

## See Also
<a name="API_HttpsNotificationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securitylake-2018-05-10/HttpsNotificationConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securitylake-2018-05-10/HttpsNotificationConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securitylake-2018-05-10/HttpsNotificationConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Security Lake. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query security-lake` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
