---
source_url: https://docs.aws.amazon.com/directoryservice/latest/admin-guide/multi-region-global-region-features.html
---

# Global vs Regional features
<a name="multi-region-global-region-features"></a>

When you add an AWS Region to your directory using multi-Region replication, Directory Service enhances the scope of all features so that they become Region-aware. These features are listed on various tabs of the details page that appears when you choose the ID of a directory in the Directory Service console. This means that all features are enabled, configured, or managed based on the Region that you select in the **Multi-Region replication** section of the console. Changes you make to features in each Region are either applied globally or per Region.

Multi-Region replication is only supported for the **Enterprise Edition** of AWS Managed Microsoft AD.

## Global features
<a name="multi-region-global"></a>

Any changes that you make to global features while the [Primary Region](multi-region-global-primary-additional.md#multi-region-primary) is selected will be applied across all Regions.

You can identify the features that are used globally on the **Directory details** page because they display **Applied to all replicated Regions** next to them. Alternatively, if you selected another Region in the list that is not the primary Region, you can identify the globally used features because they display **Inherited from primary Region**.

## Regional features
<a name="multi-region-regional"></a>

Any changes that you make to a feature in an [Additional Region](multi-region-global-primary-additional.md#multi-region-additional) will be applied only to that Region.

You can identify the features that are Regional on the **Directory details** page because they do ***not*** display **Applied to all replicated Regions** or **Inherited from primary Region** next to them.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Directory Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query directoryservice` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
