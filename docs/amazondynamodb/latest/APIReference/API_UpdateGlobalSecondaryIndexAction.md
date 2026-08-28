---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_UpdateGlobalSecondaryIndexAction.html
---

# UpdateGlobalSecondaryIndexAction
<a name="API_UpdateGlobalSecondaryIndexAction"></a>

Represents the new provisioned throughput settings to be applied to a global secondary index.

## Contents
<a name="API_UpdateGlobalSecondaryIndexAction_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** IndexName **   <a name="DDB-Type-UpdateGlobalSecondaryIndexAction-IndexName"></a>
The name of the global secondary index to be updated.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 255.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** OnDemandThroughput **   <a name="DDB-Type-UpdateGlobalSecondaryIndexAction-OnDemandThroughput"></a>
Updates the maximum number of read and write units for the specified global secondary index. If you use this parameter, you must specify `MaxReadRequestUnits`, `MaxWriteRequestUnits`, or both.
Type: [OnDemandThroughput](API_OnDemandThroughput.md) object
Required: No

 ** ProvisionedThroughput **   <a name="DDB-Type-UpdateGlobalSecondaryIndexAction-ProvisionedThroughput"></a>
Represents the provisioned throughput settings for the specified global secondary index.
For current minimum and maximum provisioned throughput values, see [Service, Account, and Table Quotas](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Limits.html) in the *Amazon DynamoDB Developer Guide*.
Type: [ProvisionedThroughput](API_ProvisionedThroughput.md) object
Required: No

 ** WarmThroughput **   <a name="DDB-Type-UpdateGlobalSecondaryIndexAction-WarmThroughput"></a>
Represents the warm throughput value of the new provisioned throughput settings to be applied to a global secondary index.
Type: [WarmThroughput](API_WarmThroughput.md) object
Required: No

## See Also
<a name="API_UpdateGlobalSecondaryIndexAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/UpdateGlobalSecondaryIndexAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/UpdateGlobalSecondaryIndexAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/UpdateGlobalSecondaryIndexAction)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DynamoDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazondynamodb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
