---
source_url: https://docs.aws.amazon.com/directoryservice/latest/devguide/API_HybridUpdateActivities.html
---

# HybridUpdateActivities
<a name="API_HybridUpdateActivities"></a>

Contains information about update activities for different components of a hybrid directory.

## Contents
<a name="API_HybridUpdateActivities_Contents"></a>

 ** HybridAdministratorAccount **   <a name="DirectoryService-Type-HybridUpdateActivities-HybridAdministratorAccount"></a>
A list of update activities related to hybrid directory administrator account changes.
Type: Array of [HybridUpdateInfoEntry](API_HybridUpdateInfoEntry.md) objects
Required: No

 ** SelfManagedInstances **   <a name="DirectoryService-Type-HybridUpdateActivities-SelfManagedInstances"></a>
A list of update activities related to the self-managed instances with SSM in the self-managed instances with SSM hybrid directory configuration.
Type: Array of [HybridUpdateInfoEntry](API_HybridUpdateInfoEntry.md) objects
Required: No

## See Also
<a name="API_HybridUpdateActivities_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ds-2015-04-16/HybridUpdateActivities)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ds-2015-04-16/HybridUpdateActivities)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ds-2015-04-16/HybridUpdateActivities)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Directory Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query directoryservice` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
