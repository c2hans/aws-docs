---
source_url: https://docs.aws.amazon.com/odb/latest/APIReference/API_AutonomousDatabasePeerSummary.html
---

# AutonomousDatabasePeerSummary
<a name="API_AutonomousDatabasePeerSummary"></a>

A summary of a peer database of an Autonomous Database.

## Contents
<a name="API_AutonomousDatabasePeerSummary_Contents"></a>

 ** autonomousDatabaseArn **   <a name="odb-Type-AutonomousDatabasePeerSummary-autonomousDatabaseArn"></a>
The Amazon Resource Name (ARN) of the peer Autonomous Database.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:(?:aws|aws-cn|aws-us-gov|aws-iso-{0,1}[a-z]{0,1}):[a-z0-9-]+:[a-z0-9-]*:[0-9]+:[a-z0-9-]+/[a-z0-9-_]{6,64}`
Required: No

 ** autonomousDatabaseId **   <a name="odb-Type-AutonomousDatabasePeerSummary-autonomousDatabaseId"></a>
The unique identifier of the peer Autonomous Database.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 64.
Pattern: `[a-zA-Z0-9_~.-]+`
Required: No

 ** ocid **   <a name="odb-Type-AutonomousDatabasePeerSummary-ocid"></a>
The Oracle Cloud Identifier (OCID) of the peer Autonomous Database.
Type: String
Required: No

 ** region **   <a name="odb-Type-AutonomousDatabasePeerSummary-region"></a>
The AWS Region where the peer Autonomous Database is located.
Type: String
Required: No

## See Also
<a name="API_AutonomousDatabasePeerSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/odb-2024-08-20/AutonomousDatabasePeerSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/odb-2024-08-20/AutonomousDatabasePeerSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/odb-2024-08-20/AutonomousDatabasePeerSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Oracle Database@AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query odb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
