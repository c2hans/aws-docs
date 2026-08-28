---
source_url: https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_UpdateReplicationSetAction.html
---

# UpdateReplicationSetAction
<a name="API_UpdateReplicationSetAction"></a>

Details used when updating the replication set.

## Contents
<a name="API_UpdateReplicationSetAction_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** addRegionAction **   <a name="IncidentManager-Type-UpdateReplicationSetAction-addRegionAction"></a>
Details about the AWS Region that you're adding to the replication set.
Type: [AddRegionAction](API_AddRegionAction.md) object
Required: No

 ** deleteRegionAction **   <a name="IncidentManager-Type-UpdateReplicationSetAction-deleteRegionAction"></a>
Details about the AWS Region that you're deleting to the replication set.
Type: [DeleteRegionAction](API_DeleteRegionAction.md) object
Required: No

## See Also
<a name="API_UpdateReplicationSetAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-incidents-2018-05-10/UpdateReplicationSetAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-incidents-2018-05-10/UpdateReplicationSetAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-incidents-2018-05-10/UpdateReplicationSetAction)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager Incident Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query incident-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
