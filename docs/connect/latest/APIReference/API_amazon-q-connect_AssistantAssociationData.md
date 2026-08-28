---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_amazon-q-connect_AssistantAssociationData.html
---

# AssistantAssociationData
<a name="API_amazon-q-connect_AssistantAssociationData"></a>

Information about the assistant association.

## Contents
<a name="API_amazon-q-connect_AssistantAssociationData_Contents"></a>

 ** assistantArn **   <a name="connect-Type-amazon-q-connect_AssistantAssociationData-assistantArn"></a>
The Amazon Resource Name (ARN) of the Amazon Q in Connect assistant.
Type: String
Pattern: `arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}`
Required: Yes

 ** assistantAssociationArn **   <a name="connect-Type-amazon-q-connect_AssistantAssociationData-assistantAssociationArn"></a>
The Amazon Resource Name (ARN) of the assistant association.
Type: String
Pattern: `arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}`
Required: Yes

 ** assistantAssociationId **   <a name="connect-Type-amazon-q-connect_AssistantAssociationData-assistantAssociationId"></a>
The identifier of the assistant association.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

 ** assistantId **   <a name="connect-Type-amazon-q-connect_AssistantAssociationData-assistantId"></a>
The identifier of the Amazon Q in Connect assistant.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

 ** associationData **   <a name="connect-Type-amazon-q-connect_AssistantAssociationData-associationData"></a>
A union type that currently has a single argument, the knowledge base ID.
Type: [AssistantAssociationOutputData](API_amazon-q-connect_AssistantAssociationOutputData.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** associationType **   <a name="connect-Type-amazon-q-connect_AssistantAssociationData-associationType"></a>
The type of association.
Type: String
Valid Values: `KNOWLEDGE_BASE | EXTERNAL_BEDROCK_KNOWLEDGE_BASE`
Required: Yes

 ** tags **   <a name="connect-Type-amazon-q-connect_AssistantAssociationData-tags"></a>
The tags used to organize, track, or control access for this resource.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `(?!aws:)[a-zA-Z+-=._:/]+`
Value Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## See Also
<a name="API_amazon-q-connect_AssistantAssociationData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/AssistantAssociationData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/AssistantAssociationData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/AssistantAssociationData)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
