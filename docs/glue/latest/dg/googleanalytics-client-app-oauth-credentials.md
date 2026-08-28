---
source_url: https://docs.aws.amazon.com/glue/latest/dg/googleanalytics-client-app-oauth-credentials.html
---

# Steps to create a client app and OAuth 2.0 credentials
<a name="googleanalytics-client-app-oauth-credentials"></a>

 For more information, see [ Google Analytics4 API documentation ](https://developers.google.com/analytics/devguides/reporting/data/v1).

1.  Create and set up your account by logging in to your [ Google Analytics Account ](https://analytics.google.com/) with your credentials. Then navigate to **Admin** > **Create Account**.

1.  Create property for the account you have created by choosing **Create Property**. Set up the property with required details. Once all the details provided corresponding property id will be generated.

1.  Add Data Stream for the created property by choosing **Data Streams** > **Add Stream** > **Web** from the drop-down. Provide the website details such as URL and other required fields. After providing all details, the corresponding **stream id **and **measurement id** will be generated.

1.  Set up Google Analytics in your website by copying the measurement id and add to your website's configuration.

1.  Create Report from Google Analytics by navigating to **Reports** and generating the required report.

1.  Authorize your app by navigating to [ console.cloud.google.com ]( https://console.cloud.google.com) and search for Google Analytics Data API, then enable the API.

   1.  Navigate to the API and Services page and choose **Credentials** > **setup OAuth 2.0 Client IDs**.

   1.  Provide redirect URL by adding the AWS Glue Redirect URL.

1.  Copy the client id and client secret which will require further for creating connection.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
