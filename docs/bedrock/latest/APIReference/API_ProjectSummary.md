---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_ProjectSummary.html
---

# ProjectSummary

A project. The same field set every project-returning operation uses: create, get, update, and archive all return the full project, and list returns one per project.

## Contents
<a name="API_ProjectSummary_Contents"></a>

 ** arn **   <a name="bedrock-Type-ProjectSummary-arn"></a>
The Amazon Resource Name (ARN) of the project.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws(-[^:]+)?:bedrock:[0-9a-z-]{1,20}:[0-9]{12}:project/[a-zA-Z0-9_-]+`
Required: Yes

 ** createdAt **   <a name="bedrock-Type-ProjectSummary-createdAt"></a>
The time the project was created.
Type: Timestamp
Required: Yes

 ** dataRetention **   <a name="bedrock-Type-ProjectSummary-dataRetention"></a>
The project's data retention setting. A mode of `inherit` defers to the account setting or model default.
Type: [ProjectDataRetention](API_ProjectDataRetention.md) object
Required: Yes

 ** id **   <a name="bedrock-Type-ProjectSummary-id"></a>
The project ID. The account's default project uses `default`; a named project's generated ID starts with `proj_`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

 ** name **   <a name="bedrock-Type-ProjectSummary-name"></a>
The project's display name. Project names do not have to be unique.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `.*\S.*`
Required: Yes

 ** status **   <a name="bedrock-Type-ProjectSummary-status"></a>
The project's lifecycle status.
Type: String
Valid Values: `active | archived`
Required: Yes

 ** archivedAt **   <a name="bedrock-Type-ProjectSummary-archivedAt"></a>
The time the project was archived.
Type: Timestamp
Required: No

## See Also
<a name="API_ProjectSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/ProjectSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/ProjectSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/ProjectSummary)
