---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gamesec03-bp04.html
---

# GAMESEC03-BP04 Enforce a strict security policy for player user accounts by requiring a strong password
<a name="gamesec03-bp04"></a>

 If a game provides players with the ability to create a user account with a password, you should require players' passwords to adhere to strong policies. For example, Amazon Cognito user pools provide you with the ability to [define password requirements](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-policies.html) for user accounts. Establishing a strong password policy can protect your players' accounts from being overtaken through social engineering and brute force attacks.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance-22"></a>

 **Customer example**

 AnyCompany Games faced a crisis when their popular title experienced a wave of account hijackings due to weak password policies. Players who were using simple passwords like "password123" were becoming victims of automated brute force attacks, resulting in lost items and compromised in-game currency. To combat this, AnyCompany Games revamped their login system and mandated that passwords not be previously used, include at least one uppercase letter, one number, one special character, and a minimum length of 15 characters.

### Implementation steps
<a name="implementation-steps-22"></a>
+  Require strong password policies for player accounts to enhance security.
+  Use Amazon Cognito user pools to define and enforce password requirements.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
