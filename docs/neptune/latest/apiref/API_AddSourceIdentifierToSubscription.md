---
source_url: https://docs.aws.amazon.com/neptune/latest/apiref/API_AddSourceIdentifierToSubscription.html
---

# AddSourceIdentifierToSubscription
<a name="API_AddSourceIdentifierToSubscription"></a>

Adds a source identifier to an existing event notification subscription.

## Request Parameters
<a name="API_AddSourceIdentifierToSubscription_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** SourceIdentifier **
The identifier of the event source to be added.
Constraints:
+ If the source type is a DB instance, then a `DBInstanceIdentifier` must be supplied.
+ If the source type is a DB security group, a `DBSecurityGroupName` must be supplied.
+ If the source type is a DB parameter group, a `DBParameterGroupName` must be supplied.
+ If the source type is a DB snapshot, a `DBSnapshotIdentifier` must be supplied.
Type: String
Required: Yes

 ** SubscriptionName **
The name of the event notification subscription you want to add a source identifier to.
Type: String
Required: Yes

## Response Elements
<a name="API_AddSourceIdentifierToSubscription_ResponseElements"></a>

The following element is returned by the service.

 ** EventSubscription **
Contains the results of a successful invocation of the [DescribeEventSubscriptions](API_DescribeEventSubscriptions.md) action.
Type: [EventSubscription](API_EventSubscription.md) object

## Errors
<a name="API_AddSourceIdentifierToSubscription_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** SourceNotFound **
The source could not be found.
HTTP Status Code: 404

 ** SubscriptionNotFound **
The designated subscription could not be found.
HTTP Status Code: 404

## See Also
<a name="API_AddSourceIdentifierToSubscription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/neptune-2014-10-31/AddSourceIdentifierToSubscription)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/neptune-2014-10-31/AddSourceIdentifierToSubscription)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/neptune-2014-10-31/AddSourceIdentifierToSubscription)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/neptune-2014-10-31/AddSourceIdentifierToSubscription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-2014-10-31/AddSourceIdentifierToSubscription)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/neptune-2014-10-31/AddSourceIdentifierToSubscription)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/neptune-2014-10-31/AddSourceIdentifierToSubscription)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/neptune-2014-10-31/AddSourceIdentifierToSubscription)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/neptune-2014-10-31/AddSourceIdentifierToSubscription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/neptune-2014-10-31/AddSourceIdentifierToSubscription)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Neptune. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query neptune` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
