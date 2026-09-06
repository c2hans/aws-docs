---
source_url: https://docs.aws.amazon.com/location/previous/developerguide/qs-setup-authentication-web.html
---

# Set up authentication for your Amazon Location application
<a name="qs-setup-authentication-web"></a>

The application that you create in this tutorial has anonymous usage, meaning that your users are not required to sign into AWS to use the application. However, by default, the Amazon Location Service APIs require authentication to use. You can use either Amazon Cognito or API keys to provide authentication and authorization for anonymous users. In this tutorial, you will create API keys for use in the sample application.

**Note**
For more information about using API keys or Amazon Cognito with Amazon Location Service, see [Grant access to Amazon Location Service](how-to-access.md).

**To set up authentication for your application**

1. Go to the [Amazon Location console](https://console.aws.amazon.com/location), and choose **API keys** from the left menu.

1. Choose **Create API key**.
**Important**
The API key that you create must be in the same AWS account and AWS Region as the Amazon Location Service resources that you created in the previous section.

1. One the **Create API key** page, fill in the following information.
   + **Name** – A name for your API key, such as `MyWebAppKey`.
   + **Resources** – Choose the Amazon Location Map and Place index resources that you created in the previous section. You can add more than one resource by choosing **Add resource**. This will allow the API key to be used with those resources.
   + **Actions** – Specify the actions you want to authorize with this API key. You must select at least **geo:GetMap\*** and **geo:SearchPlaceIndexfForPosition** so that the tutorial will work as expected.
   + You can optionally add a **Description**, **Expiration time**, or **Tags** to your API key. You can also add a referrer (such as `*.example.com`), to limit the key to only being used from a particular domain. This will mean that the tutorial will only work from that domain.
**Note**
It is recommended that you protect your API key usage by setting either an expiration time or a referrer, if not both.

1. Choose **Create API key** to create the API key.

1. Choose **Show API key**, and copy the key value for use later in the tutorial. It will be in the form `v1.public.{{a1b2c3d4...}}`.
**Important**
You will need this key when writing the code for your application later in this tutorial.
