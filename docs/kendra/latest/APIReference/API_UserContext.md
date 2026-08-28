---
source_url: https://docs.aws.amazon.com/kendra/latest/APIReference/API_UserContext.html
---

# UserContext
<a name="API_UserContext"></a>

Provides information about the user context for an Amazon Kendra index.

User context filtering is a kind of personalized search with the benefit of controlling access to documents. For example, not all teams that search the company portal for information should access top-secret company documents, nor are these documents relevant to all users. Only specific users or groups of teams given access to top-secret documents should see these documents in their search results.

You provide one of the following:
+ User token
+ User ID, the groups the user belongs to, and any data sources the groups can access.

If you provide both, an exception is thrown.

**Important**
If you're using an Amazon Kendra Gen AI Enterprise Edition index, you can use `UserId`, `Groups`, and `DataSourceGroups` to filter content. If you set the `UserId` to a particular user ID, it also includes all public documents.
Amazon Kendra Gen AI Enterprise Edition indices don't support token based document filtering. If you're using an Amazon Kendra Gen AI Enterprise Edition index, Amazon Kendra returns a `ValidationException` error if the `Token` field has a non-null value.

## Contents
<a name="API_UserContext_Contents"></a>

 ** DataSourceGroups **   <a name="kendra-Type-UserContext-DataSourceGroups"></a>
The list of data source groups you want to filter search results based on groups' access to documents in that data source.
Type: Array of [DataSourceGroup](API_DataSourceGroup.md) objects
Array Members: Minimum number of 1 item. Maximum number of 2048 items.
Required: No

 ** Groups **   <a name="kendra-Type-UserContext-Groups"></a>
The list of groups you want to filter search results based on the groups' access to documents.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 2048 items.
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `^\P{C}*$`
Required: No

 ** Token **   <a name="kendra-Type-UserContext-Token"></a>
The user context token for filtering search results for a user. It must be a JWT or a JSON token.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100000.
Pattern: `^\P{C}*$`
Required: No

 ** UserId **   <a name="kendra-Type-UserContext-UserId"></a>
The identifier of the user you want to filter search results based on their access to documents.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `^\P{C}*$`
Required: No

## See Also
<a name="API_UserContext_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kendra-2019-02-03/UserContext)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kendra-2019-02-03/UserContext)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kendra-2019-02-03/UserContext)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Kendra. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kendra` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
