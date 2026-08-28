---
source_url: https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_AppSyncParameters.html
---

# AppSyncParameters
<a name="API_AppSyncParameters"></a>

Contains the GraphQL operation to be parsed and executed, if the event target is an AWS AppSync API.

## Contents
<a name="API_AppSyncParameters_Contents"></a>

 ** GraphQLOperation **   <a name="eventbridge-Type-AppSyncParameters-GraphQLOperation"></a>
The GraphQL operation; that is, the query, mutation, or subscription to be parsed and executed by the GraphQL service.
For more information, see [Operations](https://docs.aws.amazon.com/appsync/latest/devguide/graphql-architecture.html#graphql-operations) in the * AWS AppSync User Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1048576.
Required: No

## See Also
<a name="API_AppSyncParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridge-2015-10-07/AppSyncParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridge-2015-10-07/AppSyncParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridge-2015-10-07/AppSyncParameters)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EventBridge. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query eventbridge` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
