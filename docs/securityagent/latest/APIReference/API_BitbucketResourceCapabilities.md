---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_BitbucketResourceCapabilities.html
---

# BitbucketResourceCapabilities
<a name="API_BitbucketResourceCapabilities"></a>

Capabilities for an integrated Bitbucket repository.

## Contents
<a name="API_BitbucketResourceCapabilities_Contents"></a>

 ** leaveComments **   <a name="securityagent-Type-BitbucketResourceCapabilities-leaveComments"></a>
Whether to post code review comments on pull requests.
Type: Boolean
Required: No

 ** remediateCode **   <a name="securityagent-Type-BitbucketResourceCapabilities-remediateCode"></a>
Whether to create pull requests with automated fixes.
Type: Boolean
Required: No

 ** triggerFilterGroups **   <a name="securityagent-Type-BitbucketResourceCapabilities-triggerFilterGroups"></a>
The filter groups that control which pull request events start an automatic code review when `leaveComments` is enabled. A review starts when any group matches. If you omit this, a review starts on `PULL_REQUEST_READY_FOR_REVIEW` events.
Type: Array of [TriggerFilterGroup](API_TriggerFilterGroup.md) objects
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Required: No

## See Also
<a name="API_BitbucketResourceCapabilities_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/BitbucketResourceCapabilities)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/BitbucketResourceCapabilities)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/BitbucketResourceCapabilities)
