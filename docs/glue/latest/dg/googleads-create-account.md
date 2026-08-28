---
source_url: https://docs.aws.amazon.com/glue/latest/dg/googleads-create-account.html
---

# Creating a Google Ads account
<a name="googleads-create-account"></a>

1.  Log in to [Google Ads Developer Account](https://console.cloud.google.com) with your credentials, and go to \*MyProject.
![The screenshot shows the welcome screen to log in to the Google Ads Developer Account.](http://docs.aws.amazon.com/glue/latest/dg/images/google-ads-log-in-developer-account.png)

1.  Choose **New Project** and provide the information which is required for creating Google project if you don't have any registered application in it.
![The screenshot shows the select a project page. Choose New Project in the upper right hand corner.](http://docs.aws.amazon.com/glue/latest/dg/images/google-ads-new-project.png)
![The screenshot shows the New Project window to enter a project name and choose a location.](http://docs.aws.amazon.com/glue/latest/dg/images/google-ads-new-project-name-location.png)

1.  Choose the **Navigation Tab**, then **API and Setting**, and **Create Client Id** and **ClientSecret** which will require further configuration for creating a connection between AWS Glue and GoogleAds. For more information, see [API credentials](https://console.cloud.google.com/apis/credentials).
![The screenshot shows the APIs and services configuration page.](http://docs.aws.amazon.com/glue/latest/dg/images/google-ads-apis-and-services.png)

1.  Choose **CREATE CREDENTIALS** and choose **OAuth client ID**.
![The screenshot shows the APIs and services configuration page with the Create Credentials drop-down and the Oauth client ID option highlighted.](http://docs.aws.amazon.com/glue/latest/dg/images/google-ads-create-credentials.png)

1.  Select the **Application type** as **Web application**.
![The screenshot shows the Create OAuth client ID page and the Application type as Web application.](http://docs.aws.amazon.com/glue/latest/dg/images/google-ads-oauth-client-id-application-type.png)

1.  Under **Authorised redirect URIs**, add the OAuth Redirect URIs and choose **Create**. You can add multiple redirect URIs if required.
![The screenshot shows the Create OAuth client ID page and the Authorised redirect URIs section. Here, add the URIs and choose ADD URI if needed. Once done, choose CREATE.](http://docs.aws.amazon.com/glue/latest/dg/images/google-ads-oauth-redirect-uris.png)

1.  Your **Client Id** and **Client Secret** will be generated when creating a connection between AWS Glue and Google Ads.
![The screenshot shows the Create OAuth client ID page and the Authorised redirect URIs section. Here, add the URIs and choose ADD URI if needed. Once done, choose CREATE.](http://docs.aws.amazon.com/glue/latest/dg/images/google-ads-oauth-client-created.png)

1.  Add the scopes according to your application need based, choose **OAuth consent screen** and provide the required information and add the scopes based on requirements.
![The screenshot shows the Update selected scopes page. Select your scopes as needed.](http://docs.aws.amazon.com/glue/latest/dg/images/google-ads-selected-scopes.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
