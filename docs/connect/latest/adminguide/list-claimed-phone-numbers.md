---
source_url: https://docs.aws.amazon.com/connect/latest/adminguide/list-claimed-phone-numbers.html
---

# List or export to a CSV the phone numbers claimed to your Connect Customer instance
<a name="list-claimed-phone-numbers"></a>

You can list the phone numbers claimed to your Connect Customer instance by using the Connect Customer admin website, or by using the [ListPhoneNumbersV2](https://docs.aws.amazon.com/connect/latest/APIReference/API_ListPhoneNumbersV2.html) API.

**To list phone numbers by using the Connect Customer admin website**

1. Log in to the Connect Customer admin website at https://{{instance name}}.my.connect.aws/.

1. On the navigation menu, choose **Channels**, **Phone numbers**.

   The list of phone numbers claimed to your Connect Customer instance is displayed.

**To download phone numbers to a CSV file**

1. Log in to the Connect Customer admin website at https://{{instance name}}.my.connect.aws/.

1. On the navigation menu, choose **Channels**, **Phone numbers**, **Download CSV**.
   + ALL of the phone numbers listed on that page are downloaded to the CSV file, regardless of which ones are selected.
   + It does not download all of the phone numbers claimed by your Connect Customer instance.
   + To download numbers listed on a page 2 of results, you need to paginate to page 2 and then choose **Download CSV** again.
![The Phone numbers page, the Download CSV button.](http://docs.aws.amazon.com/connect/latest/adminguide/images/download-phonenumbers-csv.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
