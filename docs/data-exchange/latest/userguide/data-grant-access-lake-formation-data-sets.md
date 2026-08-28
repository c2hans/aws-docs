---
source_url: https://docs.aws.amazon.com/data-exchange/latest/userguide/data-grant-access-lake-formation-data-sets.html
---

# Access an AWS Data Exchange data set containing AWS Lake Formation data sets (Preview)
<a name="data-grant-access-lake-formation-data-sets"></a>

**Overview for recipients**

An AWS Lake Formation data set is a data set that contains AWS Lake Formation data permission assets.

As a recipient, you can accept a data grant containing AWS Lake Formation data sets. Once you're entitled to an AWS Data Exchange for AWS Lake Formation data set, you can query, transform, and share access to the data within your AWS account using AWS Lake Formation, or across your AWS organization using AWS License Manager.

After you accept a data grant containing an AWS Lake Formation data set, you can use Lake Formation compatible query engines, like Amazon Athena, to query your data.

**After acceptance of the data grant is complete, you must do the following:**

1. Accept the AWS Resource Access Manager (AWS RAM) share within 12 hours after you accept the data grant. You can accept the AWS RAM share from your entitled data sets page for your AWS Lake Formation data permission data set on the AWS Data Exchange console. You only need to accept an AWS RAM share once per provider. For more information about accepting a resource share invitation from AWS RAM, see [Accepting a resource share invitation from AWS RAM](https://docs.aws.amazon.com/lake-formation/latest/dg/accepting-ram-invite.html).

1. Navigate to AWS Lake Formation and create resource links from the new shared resources.

1. Navigate to Amazon Athena or another AWS Lake Formation compatible query engine to query your data.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Data Exchange. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query data-exchange` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
