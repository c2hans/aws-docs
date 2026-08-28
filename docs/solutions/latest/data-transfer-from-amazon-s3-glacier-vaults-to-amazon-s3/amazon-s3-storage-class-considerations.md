---
source_url: https://docs.aws.amazon.com/solutions/latest/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/amazon-s3-storage-class-considerations.html
---

# Amazon S3 storage class considerations
<a name="amazon-s3-storage-class-considerations"></a>

 When you deploy this Guidance, you must choose a storage class to apply to all of your transferred data. Before you choose this storage class, consider the availability, durability, minimum storage duration, and cost of each storage class. After your data is stored in the Amazon S3 service, you can change the storage class for each object. Some storage classes have minimum durations, so it's important to plan accordingly. For more information, see [Comparing the Amazon S3 storage classes](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html#sc-compare) in the *Amazon Simple Storage Service User Guide* and [Amazon S3 pricing](https://aws.amazon.com/s3/pricing/).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Data Transfer from Amazon S3 Glacier Vaults to Amazon S3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
