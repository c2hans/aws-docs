---
source_url: https://docs.aws.amazon.com/connect/latest/adminguide/example-contact-lens-output-locations.html
---

# Output file locations for files analyzed by conversational analytics
<a name="example-contact-lens-output-locations"></a>

Following are examples of what the path looks like for conversational analytics output files when they are stored in the Amazon S3 bucket for your instance.
+ Original analyzed transcript file (JSON)
  + /connect-instance- bucket/**Analysis/Voice**/2020/02/04/{{contact's\_ID}}\_analysis\_2020-02-04T21:14:16Z.json
  + /connect-instance- bucket/**Analysis/Chat**/2020/02/04/{{contact's\_ID}}\_analysis\_2020-02-04T21:14:16Z.json
  + /connect-instance- bucket/**Analysis/Email**/2026/03/10/{{contact's\_ID}}\_analysis\_20260310T22:35\_UTC.json
+ Redacted analyzed transcript file in (JSON)
  + /connect-instance- bucket/**Analysis/Voice/Redacted**/2020/02/04/{{contact's\_ID}}\_**analysis\_redacted**\_2020-02-04T21:14:16Z.json
  + /connect-instance- bucket/**Analysis/Chat/Redacted**/2020/02/04/{{contact's\_ID}}\_**analysis\_redacted**\_2020-02-04T21:14:16Z.json
  + /connect-instance- bucket/**Analysis/Email/Redacted**/2026/03/10/{{contact's\_ID}}\_**analysis\_redacted**\_20260310T22:35\_UTC.json
+ Redacted audio file
  + /connect-instance- bucket/**Analysis/Voice/Redacted**/2020/02/04/{{contact's\_ID}}\_**call\_recording\_redacted**\_2020-02-04T21:14:16Z.**wav**

**Important**
To delete a recording, you must delete the files for both the redacted and unredacted recordings.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
