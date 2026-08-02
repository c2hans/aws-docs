---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/ou-structure-landing-zone/migration-verification.html
---

# OU migration and verification
<a name="migration-verification"></a>

For the multinational pharmaceutical company in our example, cloud platform engineering and change management teams agreed on a migration plan and schedule. AWS accounts were reviewed and ranked according to business impact and criticality as part of the planning.

The new OU structure was deployed side by side with the existing OU structure to allow for staging of new policies and incremental migration. We created new empty OUs with child OUs and assigned AWS Organizations policies and AWS Control Tower controls to those child OUs.

The AWS Organizations policies were migrated manually by applying the desired policies on the new structure. We used manual spot checking to verify AWS Organizations policies and automated mechanisms to verify AWS Control Tower controls. AWS accounts were moved to the new OUs only after these checks were successful.

Account migration was semi-automated and followed a staggered or batched approach. The initial migration targeted AWS accounts that were considered less critical, using a batch of five AWS accounts per migration run. Migration batches did not exceed 10 accounts. When the accounts were migrated, reviewers and testers used the AWS Control Tower console to verify that these accounts were moved to the correct OU and monitored AWS CloudTrail logs for errors. Reviewers also checked the AWS Service Catalog and AWS Control Tower consoles for any [drift](https://docs.aws.amazon.com/controltower/latest/userguide/drift.html) or accounts in tainted or unknown states.

Changes to OU placement of accounts did not affect the connectivity or accessibility of resources. No outage in a production application was reported.
