---
source_url: https://docs.aws.amazon.com/datazone/latest/userguide/create-domain-unit.html
---

# Create domain units in Amazon DataZone
<a name="create-domain-unit"></a>

In Amazon DataZone, domain units enable you to organize your assets and other domain entities under specific business units and teams. For more information, see [Amazon DataZone terminology and concepts](datazone-concepts.md).

**To create a domain unit**

1. Navigate to the Amazon DataZone data portal using the data portal URL and log in using your SSO or AWS credentials. If you’re an Amazon DataZone administrator, you can obtain the data portal URL by accessing the Amazon DataZone console at [https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone) in the AWS account where the Amazon DataZone domain was created.

1. Choose **View domains** and choose the domain where you want to create domain units.

1. On the domain details page, navigate to the **Domain units** tab.

1. Choose **Create domain unit**.

1. Specify the following and then choose **Create domain unit**:
   + Under **Domain unit details**, for **Name**, specify the domain unit name.
   + Under **Domain unit details**, for **Description**, specify the domain unit description.
   + **Domain unit parent** - choose the parent domain unit under which you'd like to add the new domain unit.
   + **Domain unit owners** - specify domain unit owners who can edit this domain unit.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
