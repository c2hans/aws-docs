---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_DesiredPlayerSession.html
---

# DesiredPlayerSession
<a name="API_DesiredPlayerSession"></a>

Player information for use when creating player sessions using a game session placement request.

## Contents
<a name="API_DesiredPlayerSession_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** PlayerData **   <a name="gameliftservers-Type-DesiredPlayerSession-PlayerData"></a>
Developer-defined information related to a player. Amazon GameLift Servers does not use this data, so it can be formatted as needed for use in the game.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** PlayerId **   <a name="gameliftservers-Type-DesiredPlayerSession-PlayerId"></a>
A unique identifier for a player to associate with the player session.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

## See Also
<a name="API_DesiredPlayerSession_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/DesiredPlayerSession)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/DesiredPlayerSession)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/DesiredPlayerSession)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GameLift Servers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query gameliftservers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
