---
source_url: https://docs.aws.amazon.com/cloudsearch/latest/developerguide/getting-started-delete-domain.html
---

# Step 4: Delete Your Amazon CloudSearch Movies Domain
<a name="getting-started-delete-domain"></a>

 When you are finished experimenting with your movies domain, **you must delete it to avoid incurring additional usage fees. **

**Important**
Deleting a domain deletes the index associated with the domain and takes the domain's document and search endpoints offline permanently.

**To delete your imdb-movies domain**

1. Go to the Amazon CloudSearch console at [https://console.aws.amazon.com/cloudsearch/home](https://console.aws.amazon.com/cloudsearch/home) and navigate to the list of domains.

1. Select the checkbox for the *movies* domain, then choose **Delete** and confirm deletion.

**Note**
It can take around 15 minutes to delete the domain and its resources.

Wondering where to go next? [Are You New to Amazon CloudSearch?](what-is-cloudsearch.md#new-to-cloudsearch) has a guide to the rest of the Amazon CloudSearch developer documentation. For more information about the Amazon CloudSearch query language, see [Searching Your Data with Amazon CloudSearch](searching.md). If you're ready to set up a domain with your own data, see [Preparing Your Data](preparing-data.md) and [Uploading Data to an Amazon CloudSearch Domain](uploading-data.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Cloud Search. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudsearch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
