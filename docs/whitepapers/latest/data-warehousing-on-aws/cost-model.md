---
source_url: https://docs.aws.amazon.com/whitepapers/latest/data-warehousing-on-aws/cost-model.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Cost model
<a name="cost-model"></a>

 Amazon Redshift requires no long-term commitments or upfront costs. This pricing approach frees you from the capital expense and complexity of planning and purchasing data warehouse capacity ahead of your needs. Charges are based on the size and number of nodes in your cluster. If you use Amazon Redshift-managed storage (RMS) with an RA3 instance, you pay separately for the amount of compute and RMS that you use.

 If you need additional compute power to handle workload spikes, you can enable concurrency scaling. For every 24 hours that your main cluster runs, you accumulate one hour of credit to use this feature for free. Beyond that, you will be charged the per-second on-demand rate.

 There is no additional charge for backup storage, up to 100 percent of your provisioned storage. For example, if you have an active cluster with two XL nodes for a total of four terabytes (TB) of storage, AWS provides up to four TB of backup storage on S3 at no additional charge. Backup storage beyond the provisioned storage size, and backups stored after your cluster is terminated, are billed at standard [Amazon S3 rates.](https://aws.amazon.com/s3/pricing/) There is no data transfer charge for communication between S3 and Amazon Redshift.

 If you use Redshift Spectrum to access data store in your data lake, you pay for the query cost based on how much data the query scans.

 For more information, see [Amazon Redshift Pricing.](https://aws.amazon.com/redshift/pricing/)
