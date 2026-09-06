---
source_url: https://docs.aws.amazon.com/sdkref/latest/guide/access-temp-idc.html
---

# Using short-term credentials to authenticate AWS SDKs and tools
<a name="access-temp-idc"></a>

 We recommend configuring your AWS SDK or tool to use [Using IAM Identity Center to authenticate AWS SDK and tools](access-sso.md) with extended session duration options. However, you can copy and use temporary credentials that are available in the AWS access portal. New credentials will need to be copied when these expire. You can use the temporary credentials in a profile or use them as values for system properties and environment variables.

Best practice: Instead of manually managing access keys and a token in the credentials file, we recommend your application uses temporary credentials delivered from:
+ An AWS compute service, such as running your application on Amazon Elastic Compute Cloud or in AWS Lambda.
+ Another option in the credential provider chain, such as [Using IAM Identity Center to authenticate AWS SDK and tools](access-sso.md).
+ Or use the [Process credential provider](feature-process-credentials.md) to retrieve temporary credentials.

**Set up a credentials file using short-term credentials retrieved from AWS access portal**

1. [Create a shared credentials file](https://docs.aws.amazon.com/sdkref/latest/guide/file-location.html).

1. In the credentials file, paste the following placeholder text until you paste in working temporary credentials.

   ```
   [default]
   aws_access_key_id={{<value from AWS access portal>}}
   aws_secret_access_key={{<value from AWS access portal>}}
   aws_session_token={{<value from AWS access portal>}}
   ```

1. Save the file. The file `~/.aws/credentials` should now exist on your local development system. This file contains the [[default] profile](https://docs.aws.amazon.com/sdkref/latest/guide/file-format.html#file-format-profile) that the SDK or tool uses if a specific named profile is not specified.

1. [Sign in to the AWS access portal](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtosignin.html).

1. Follow these instructions for [Manual credential refresh](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtogetcredentials.html#how-to-get-temp-credentials) to copy IAM role credentials from the AWS access portal.

   1. For step 4 in the linked instructions, choose the IAM role name that grants access for your development needs. This role typically has a name like **PowerUserAccess** or **Developer**.

   1. For step 7 in the linked instructions, select the **Manually add a profile to your AWS credentials file** option and copy the contents.

1. Paste the copied credentials into your local `credentials` file. The generated profile name is not needed if you are using the `default` profile. Your file should resemble the following.

   ```
   [default]
   aws_access_key_id={{AKIAIOSFODNN7EXAMPLE}}
   aws_secret_access_key={{wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY}}
   aws_session_token={{IQoJb3JpZ2luX2IQoJb3JpZ2luX2IQoJb3JpZ2luX2IQoJb3JpZ2luX2IQoJb3JpZVERYLONGSTRINGEXAMPLE}}
   ```

1. Save the `credentials` file.

When the SDK creates a service client, it will access these temporary credentials and use them for each request. The settings for the IAM role chosen in step 5a determine [how long the temporary credentials are valid](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtosessionduration.html). The maximum duration is twelve hours.

After the temporary credentials expire, repeat steps 4 through 7.
