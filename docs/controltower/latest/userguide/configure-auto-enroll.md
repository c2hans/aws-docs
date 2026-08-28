---
source_url: https://docs.aws.amazon.com/controltower/latest/userguide/configure-auto-enroll.html
---

# Optionally configure auto-enrollment for accounts
<a name="configure-auto-enroll"></a>

When you enable this feature during setup, or later, accounts that are moved between two registered OUs, or moved into your AWS Control Tower environment for the first time, no longer show a state of inheritance drift. The accounts automatically inherit the baselines and controls that are enabled on the new OU. Controls and baselines from the previous OU are removed.

To opt in for auto-enrollment at any time after setup, navigate to the landing zone **Settings** page and choose **Update** landing zone, or call the AWS Control Tower `UpdateLandingZone` API.

You can move an account between OUs by means of the AWS Organizations API, or by means of the AWS Control Tower console. If you move an account outside an OU that's registered, AWS Control Tower removes all deployed baselines and controls, automatically. It essentially unenrolls the account from AWS Control Tower.

**Note**
If you choose to enable the auto-enroll capability after initial setup of the landing zone, AWS Control Tower does not retroactively resolve the inheritance drift that was caused by moving accounts between OUs before the auto-enroll capability was enabled. The automatic drift resolution goes into effect for accounts that are moved after you enable this setting.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Control Tower. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query controltower` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
