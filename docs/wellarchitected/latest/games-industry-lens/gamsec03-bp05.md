---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gamsec03-bp05.html
---

# GAMESEC03-BP05 Provide an option for players to set up multi-factor authentication (MFA) on their accounts
<a name="gamsec03-bp05"></a>

 Player accounts can be an asset to bad actors, particularly in games that support in-game currency and purchases. Due to the pervasiveness of player account hacking and social engineering attacks, provide players with the option to enhance the security of their accounts by configuring multi-factor authentication (MFA).

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance-23"></a>

 When a player attempts to access their account by using MFA, a temporary code is sent to their email address, phone number, or a purpose-built multi-factor authentication mobile app. To successfully authenticate, the player must then enter the code into the login system within a limited time frame.

 MFA can also be used to help protect accounts that are attempting to authenticate from a new geo-location, accounts that have been flagged by player support for potential malicious activity, and even for accounts that have not logged into the game for an extended period.

 For example, Amazon Cognito user pools can [configure multi-factor authentication](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-mfa.html) on user directories.

### Implementation steps
<a name="implementation-steps-23"></a>
+  Enable multi-factor authentication (MFA) to enhance player account security.
+  Use temporary codes sent via email, phone, or MFA apps to verify account access.
+  Apply MFA for new geo-locations, flagged accounts, or accounts with extended inactivity.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
