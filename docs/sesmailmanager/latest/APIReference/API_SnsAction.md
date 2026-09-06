---
source_url: https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_SnsAction.html
---

# SnsAction
<a name="API_SnsAction"></a>

The action to publish the email content to an Amazon SNS topic. When executed, this action will send the email as a notification to the specified SNS topic.

## Contents
<a name="API_SnsAction_Contents"></a>

 ** RoleArn **   <a name="sesmailmanager-Type-SnsAction-RoleArn"></a>
The Amazon Resource Name (ARN) of the IAM Role to use while writing to Amazon SNS. This role must have access to the `sns:Publish` API for the given topic.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `[a-zA-Z0-9:_/+=,@.#-]+`
Required: Yes

 ** TopicArn **   <a name="sesmailmanager-Type-SnsAction-TopicArn"></a>
The Amazon Resource Name (ARN) of the Amazon SNS Topic to which notification for the email received will be published.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:(aws|aws-cn|aws-us-gov|aws-eusc):sns:[a-z0-9-]+:\d{12}:[\w\-]{1,256}`
Required: Yes

 ** ActionFailurePolicy **   <a name="sesmailmanager-Type-SnsAction-ActionFailurePolicy"></a>
A policy that states what to do in the case of failure. The action will fail if there are configuration errors. For example, specified SNS topic has been deleted or the role lacks necessary permissions to call the `sns:Publish` API.
Type: String
Valid Values: `CONTINUE | DROP`
Required: No

 ** Encoding **   <a name="sesmailmanager-Type-SnsAction-Encoding"></a>
The encoding to use for the email within the Amazon SNS notification. The default value is `UTF-8`. Use `BASE64` if you need to preserve all special characters, especially when the original message uses a different encoding format.
Type: String
Valid Values: `UTF-8 | BASE64`
Required: No

 ** PayloadType **   <a name="sesmailmanager-Type-SnsAction-PayloadType"></a>
The expected payload type within the Amazon SNS notification. `CONTENT` attempts to publish the full email content with 20KB of headers content. `HEADERS` extracts up to 100KB of header content to include in the notification, email content will not be included to the notification. The default value is `CONTENT`.
Type: String
Valid Values: `HEADERS | CONTENT`
Required: No

## See Also
<a name="API_SnsAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mailmanager-2023-10-17/SnsAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mailmanager-2023-10-17/SnsAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mailmanager-2023-10-17/SnsAction)
