---
source_url: https://docs.aws.amazon.com/ses/latest/dg/create-shared-credentials-file.html
---

# Creating a shared credentials file to use when sending email through Amazon SES using an AWS SDK
<a name="create-shared-credentials-file"></a>

The following procedure shows how to create a shared credentials file in your home directory. For the SDK sample code to function properly, you must create this file.

1. In a text editor, create a new file. In the file, paste the following code:

   ```
   1. [default]
   2. aws_access_key_id = YOUR_AWS_ACCESS_KEY_ID
   3. aws_secret_access_key = YOUR_AWS_SECRET_ACCESS_KEY
   ```

1. In the text file you just created, replace `YOUR_AWS_ACCESS_KEY` with your unique AWS access key ID, and replace `YOUR_AWS_SECRET_ACCESS_KEY` with your unique AWS secret access key.

1. Save the file. The following table shows the correct location and file name for your operating system.
[See the AWS documentation website for more details](http://docs.aws.amazon.com/ses/latest/dg/create-shared-credentials-file.html)
**Important**
Don't include a file extension when saving the credentials file.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Email Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ses` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
