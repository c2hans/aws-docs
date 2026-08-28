---
source_url: https://docs.aws.amazon.com/b2bi/latest/userguide/inbound-tutorial-step2-profile.html
---

# Step 2: Create your business profile
<a name="inbound-tutorial-step2-profile"></a>

A profile stores your business contact information and serves as the foundation for all your AWS B2B Data Interchange activities. It represents your organization in trading partnerships and provides logging configuration for monitoring transformations.

**To create a business profile**

1. Open the AWS B2B Data Interchange console at [https://console.aws.amazon.com/b2bi/](https://console.aws.amazon.com/b2bi/).

1. In the navigation pane, choose **Profiles**.

1. Choose **Create profile**.

1. In the **Profile details** section, enter the profile information for your tutorial.

1. Leave **Logging** enabled (recommended for monitoring).

1. Optionally, add tags such as Environment: Tutorial and Department: Procurement.

1. Choose **Create profile**.

## Required fields
<a name="tutorial-profile-required-fields"></a>
+ Profile name
+ Business name
+ Email address
+ Phone number

## Example data for this tutorial
<a name="inbound-step2-example-data"></a>
+ **Profile name**: **AcmeCorpProfile**
+ **Business name**: **Acme Corporation**
+ **Email**: **edi-admin@acmecorp.example.com**
+ **Phone**: **\+1-555-012-3456**

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS B2B Data Interchange. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query b2bi` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
