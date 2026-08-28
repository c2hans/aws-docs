---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_ManagedActionHistoryItem.html
---

# ManagedActionHistoryItem
<a name="API_ManagedActionHistoryItem"></a>

The record of a completed or failed managed action.

## Contents
<a name="API_ManagedActionHistoryItem_Contents"></a>

 ** ActionDescription **
A description of the managed action.
Type: String
Required: No

 ** ActionId **
A unique identifier for the managed action.
Type: String
Required: No

 ** ActionType **
The type of the managed action.
Type: String
Valid Values: `InstanceRefresh | PlatformUpdate | Unknown`
Required: No

 ** ExecutedTime **
The date and time that the action started executing.
Type: Timestamp
Required: No

 ** FailureDescription **
If the action failed, a description of the failure.
Type: String
Required: No

 ** FailureType **
If the action failed, the type of failure.
Type: String
Valid Values: `UpdateCancelled | CancellationFailed | RollbackFailed | RollbackSuccessful | InternalFailure | InvalidEnvironmentState | PermissionsError`
Required: No

 ** FinishedTime **
The date and time that the action finished executing.
Type: Timestamp
Required: No

 ** Status **
The status of the action.
Type: String
Valid Values: `Completed | Failed | Unknown`
Required: No

## See Also
<a name="API_ManagedActionHistoryItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticbeanstalk-2010-12-01/ManagedActionHistoryItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticbeanstalk-2010-12-01/ManagedActionHistoryItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticbeanstalk-2010-12-01/ManagedActionHistoryItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elastic Beanstalk. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elasticbeanstalk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
