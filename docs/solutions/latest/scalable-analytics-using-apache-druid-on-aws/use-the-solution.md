---
source_url: https://docs.aws.amazon.com/solutions/latest/scalable-analytics-using-apache-druid-on-aws/use-the-solution.html
---

# Use the guidance
<a name="use-the-solution"></a>

This section provides a user guide for using the Scalable Analytics using Apache Druid on AWS Guidance.

## Access the Druid web console
<a name="access-the-druid-web-console"></a>

1. Using the deployment output, get the website URL starting with `druid-base-url`.

1. Open the URL in your browser (we recommend using Chrome). You will be redirected to the sign-in page for the username and password.
**Note**
During the deployment process, an administrative user account is created with the username admin. To retrieve the password for this account from AWS Secrets Manager, search for the entry with a description *Administrator user credentials* for Druid cluster. You have the option to use the administrative user account to sign in, or create a new user account with reduced access permissions.

1. After signing in, the Apache Druid web console is displayed. The web console displays the Druid components deployed in your AWS account using the configuration that you used during the deployment process.
![Apache Druid web console.](https://docs.aws.amazon.com/solutions/latest/scalable-analytics-using-apache-druid-on-aws/images/image11.png)

For more information on how to ingest external data, refer to the [Apache Druid tutorial documentation](https://druid.apache.org/docs/latest/tutorials/).

## Sign out of the Druid web console
<a name="sign-out-of-the-druid-web-console"></a>

The Druid UI doesn’t have a sign out button. As an alternative, you can adjust your browser settings to delete all cookies when you close the browser. Usually, you can find this setting by searching for `cookies` or `cache`. Upon the next sign in, the user must enter their username and password.

The following images show examples of this procedure.

![In your browser settings, search for cookies or cache. Select the option to delete cookies when the browser is closed.](https://docs.aws.amazon.com/solutions/latest/scalable-analytics-using-apache-druid-on-aws/images/delete-cookies.png)

![Delete your browsing history, cookies, and cached files.](https://docs.aws.amazon.com/solutions/latest/scalable-analytics-using-apache-druid-on-aws/images/delete-browsing-data.png)
