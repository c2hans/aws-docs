---
source_url: https://docs.aws.amazon.com/odb/latest/APIReference/API_AutonomousDatabaseWalletDetails.html
---

# AutonomousDatabaseWalletDetails
<a name="API_AutonomousDatabaseWalletDetails"></a>

The wallet details for an Autonomous Database.

## Contents
<a name="API_AutonomousDatabaseWalletDetails_Contents"></a>

 ** passwordSourceSummary **   <a name="odb-Type-AutonomousDatabaseWalletDetails-passwordSourceSummary"></a>
The summary of the password source configuration for the Autonomous Database wallet.
Type: [WalletPasswordSourceSummary](API_WalletPasswordSourceSummary.md) object
Required: No

 ** status **   <a name="odb-Type-AutonomousDatabaseWalletDetails-status"></a>
The current status of the Autonomous Database wallet.
Type: String
Valid Values: `ACTIVE | UPDATING`
Required: No

 ** timeRotated **   <a name="odb-Type-AutonomousDatabaseWalletDetails-timeRotated"></a>
The date and time when the Autonomous Database wallet was last rotated.
Type: Timestamp
Required: No

## See Also
<a name="API_AutonomousDatabaseWalletDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/odb-2024-08-20/AutonomousDatabaseWalletDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/odb-2024-08-20/AutonomousDatabaseWalletDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/odb-2024-08-20/AutonomousDatabaseWalletDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Oracle Database@AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query odb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
