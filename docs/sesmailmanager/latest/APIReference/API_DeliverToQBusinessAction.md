---
source_url: https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_DeliverToQBusinessAction.html
---

# DeliverToQBusinessAction
<a name="API_DeliverToQBusinessAction"></a>

The action to deliver incoming emails to an Amazon Q Business application for indexing.

## Contents
<a name="API_DeliverToQBusinessAction_Contents"></a>

 ** ApplicationId **   <a name="sesmailmanager-Type-DeliverToQBusinessAction-ApplicationId"></a>
The unique identifier of the Amazon Q Business application instance where the email content will be delivered.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-z0-9-]+`
Required: Yes

 ** IndexId **   <a name="sesmailmanager-Type-DeliverToQBusinessAction-IndexId"></a>
The identifier of the knowledge base index within the Amazon Q Business application where the email content will be stored and indexed.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-z0-9-]+`
Required: Yes

 ** RoleArn **   <a name="sesmailmanager-Type-DeliverToQBusinessAction-RoleArn"></a>
The Amazon Resource Name (ARN) of the IAM Role to use while delivering to Amazon Q Business. This role must have access to the `qbusiness:BatchPutDocument` API for the given application and index.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `[a-zA-Z0-9:_/+=,@.#-]+`
Required: Yes

 ** ActionFailurePolicy **   <a name="sesmailmanager-Type-DeliverToQBusinessAction-ActionFailurePolicy"></a>
A policy that states what to do in the case of failure. The action will fail if there are configuration errors. For example, the specified application has been deleted or the role lacks necessary permissions to call the `qbusiness:BatchPutDocument` API.
Type: String
Valid Values: `CONTINUE | DROP`
Required: No

## See Also
<a name="API_DeliverToQBusinessAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mailmanager-2023-10-17/DeliverToQBusinessAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mailmanager-2023-10-17/DeliverToQBusinessAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mailmanager-2023-10-17/DeliverToQBusinessAction)
