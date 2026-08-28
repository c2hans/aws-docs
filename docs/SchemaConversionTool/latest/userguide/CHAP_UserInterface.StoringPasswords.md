---
source_url: https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_UserInterface.StoringPasswords.html
---

# Storing passwords in the AWS Schema Conversion Tool
<a name="CHAP_UserInterface.StoringPasswords"></a>

You can store a database password or SSL certificate in the AWS SCT cache. To store a password, choose **Store Password** when you create a connection.

The password is encrypted using the randomly generated token in the `seed.dat` file. The password is then stored with the user name in the cache file. If you lose the `seed.dat` file or it becomes corrupted, the database password might be unencrypted incorrectly. In this case, the connection fails.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Schema Conversion Tool User Guide. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query SchemaConversionTool` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
