---
source_url: https://docs.aws.amazon.com/dlm/latest/APIReference/API_LifecyclePolicy.html
---

# LifecyclePolicy
<a name="API_LifecyclePolicy"></a>

Information about a lifecycle policy.

## Contents
<a name="API_LifecyclePolicy_Contents"></a>

 ** DateCreated **   <a name="dlm-Type-LifecyclePolicy-DateCreated"></a>
The local date and time when the lifecycle policy was created.
Type: Timestamp
Required: No

 ** DateModified **   <a name="dlm-Type-LifecyclePolicy-DateModified"></a>
The local date and time when the lifecycle policy was last modified.
Type: Timestamp
Required: No

 ** DefaultPolicy **   <a name="dlm-Type-LifecyclePolicy-DefaultPolicy"></a>
Indicates whether the policy is a default lifecycle policy or a custom lifecycle policy.
+  `true` - the policy is a default policy.
+  `false` - the policy is a custom policy.
Type: Boolean
Required: No

 ** Description **   <a name="dlm-Type-LifecyclePolicy-Description"></a>
The description of the lifecycle policy.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Pattern: `[0-9A-Za-z _-]+`
Required: No

 ** ExecutionRoleArn **   <a name="dlm-Type-LifecyclePolicy-ExecutionRoleArn"></a>
The Amazon Resource Name (ARN) of the IAM role used to run the operations specified by the lifecycle policy.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `arn:aws(-[a-z]{1,4}){0,2}:iam::\d+:role/.*`
Required: No

 ** PolicyArn **   <a name="dlm-Type-LifecyclePolicy-PolicyArn"></a>
The Amazon Resource Name (ARN) of the policy.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `^arn:aws(-[a-z]{1,4}){0,2}:dlm:[A-Za-z0-9_/.-]{0,63}:\d+:policy/[0-9A-Za-z_-]{1,128}$`
Required: No

 ** PolicyDetails **   <a name="dlm-Type-LifecyclePolicy-PolicyDetails"></a>
The configuration of the lifecycle policy
Type: [PolicyDetails](API_PolicyDetails.md) object
Required: No

 ** PolicyId **   <a name="dlm-Type-LifecyclePolicy-PolicyId"></a>
The identifier of the lifecycle policy.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Pattern: `policy-[a-f0-9]+`
Required: No

 ** State **   <a name="dlm-Type-LifecyclePolicy-State"></a>
The activation state of the lifecycle policy.
Type: String
Valid Values: `ENABLED | DISABLED | ERROR`
Required: No

 ** StatusMessage **   <a name="dlm-Type-LifecyclePolicy-StatusMessage"></a>
The description of the status.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Pattern: `[\p{all}]*`
Required: No

 ** Tags **   <a name="dlm-Type-LifecyclePolicy-Tags"></a>
The tags.
Type: String to string map
Map Entries: Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[a-zA-Z+-=._:/]+$`
Value Length Constraints: Maximum length of 256.
Value Pattern: `[\p{all}]*`
Required: No

## See Also
<a name="API_LifecyclePolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dlm-2018-01-12/LifecyclePolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dlm-2018-01-12/LifecyclePolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dlm-2018-01-12/LifecyclePolicy)
