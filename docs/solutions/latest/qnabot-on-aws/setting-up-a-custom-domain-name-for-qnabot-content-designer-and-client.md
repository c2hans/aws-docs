---
source_url: https://docs.aws.amazon.com/solutions/latest/qnabot-on-aws/setting-up-a-custom-domain-name-for-qnabot-content-designer-and-client.html
---

# Setting up a custom domain name for QnABot content designer and client
<a name="setting-up-a-custom-domain-name-for-qnabot-content-designer-and-client"></a>

This section provides information on how to set up a custom domain name and configure the QnABot on AWS solution to use the custom domain name for the content designer and client user interfaces. The setup and configuration involve the following steps.

## Step 1: Set up custom domain name for API Gateway
<a name="step-1-set-up-custom-domain-name-for-api-gateway"></a>

Use the AWS account and Region where you have deployed the QnABot on AWS solution for the following steps. See [Setting up custom domain names for REST APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-custom-domains.html) in the *Amazon API Gateway Developer Guide*.
+ Registering a domain name.
+ Creating DNS records.
+ Creating an SSL certificate for the custom domain name.
+ Choosing a security policy. It is best security practice to specify a TLS 1.2 security policy.
+ Creating a custom domain in API Gateway.

**Note**
Deactivate the default API gateway endpoint since the custom domain name is used.

## Step 2: Custom domain API mapping setup in API Gateway
<a name="step-2-custom-domain-api-mapping-setup-in-api-gateway"></a>

When mapping the API to the custom domain in API Gateway for the QnABot deployment, use the following settings:

## Mapping 1
<a name="mapping-1"></a>
+  **API** - Select the QnABot deployment you would like to use. The QnABot API takes on the same name as the CloudFormation Stack name you used when you deployed the QnABot on AWS solution.
+  **Stage** - Use **prod**. This is the default stage created for the QnABot deployment.

## Mapping 2
<a name="mapping-2"></a>
+  **API** - Select the QnABot deployment you would like to use. The QnABot API takes on the same name as the CloudFormation Stack name you used when you deployed the QnABot on AWS solution.
+  **Stage** - Use **prod**. This is the default stage created for the QnABot deployment.
+  **Path** - Use **prod**. This is used for routing requests.

## Step 3: Update QnABot API Resources in API Gateway
<a name="step-3-update-qnabot-api-resources-in-api-gateway"></a>

1. Navigate to the [API Gateway console](https://aws.amazon.com/api-gateway/) and select the QnABot API.

1. The QnABot API takes on the same name as the CloudFormation Stack name you used when you deployed the QnABot on AWS solution.

1. Navigate to the Resources section from the menu.

### Step 3a: Update the /pages/client resource
<a name="step-3a-update-the-pagesclient-resource"></a>

1. Select the GET method for the `/pages/client` resource.

1. Choose **Integration Response**.

1. Expand the **302 Method Response Status**.

1. Edit the location **Response** header and replace the API Gateway endpoint with your custom domain name The API Gateway endpoint has an endpoint such as: ` <api-id> `.execute-api.` <region> `.amazonaws.com.

1. Make a note of the URL encoding in the values.

1. Choose the **{tick}** icon to update the value.

1. Choose **Save**.

### Step 3b: Update the /pages/designer resource
<a name="step-3b-update-the-pagesdesigner-resource"></a>

1. Select the GET method for `/pages/designer` resource.

1. Choose **Integration Response**.

1. Expand the **302 Method Response Status**.

1. Edit the location **Response** header and replace the API Gateway endpoint with your custom domain name The API Gateway endpoint will have the endpoint such as: ` <api-id> `.execute-api.`[.red]#<region>`.`amazonaws.com`.

1. Make note of the URL encoding in the values.

1. Choose the ** `{tick}` ** icon to update the value.

1. Choose **Save**.

## Step 4: Update QnABot Cognito user pool
<a name="step-4-update-qnabot-cognito-user-pool"></a>

To access the **QnABot** content designer user interface, the deployment sets up authentication using Amazon Cognito. Update the user pool settings to update the Callback URLs to use the custom domain name.

1. Navigate to the [Amazon Cognito console](https://console.aws.amazon.com/cognito/home).

1. Choose **User Pools**.

1. Choose the **QnABot** user pool.

1. The QnABot user pool takes on the same name as the CloudFormation stack name you used when you deployed the QnABot on AWS solution. For example, `UserPool-[.red]` *<stack-name>*``

1. Navigate to **App Integration** \| **App client settings**.

1. Update the callback URLs for app clients: `UserPool-<stack-name> `-client`.

1. Use the custom domain name instead of the API Gateway endpoint. For example: `https://<your-custom-domain-name> \/prod/static/client.html`.

1. Choose **Save Changes**.

### Update the callback URLs for app clients: UserPool-`{stackname}`-designer
<a name="update-the-callback-urls-for-app-clients-userpool-stackname-designer"></a>

1. Use the custom domain name instead of the API Gateway endpoint. For example: `https://<your-custom-domain-name> ` `/prod/static/index.html`.

1. Choose **Save Changes**.

## Step 5: Deploy API
<a name="step-5-deploy-api"></a>

Now that we have updated the configurations, we will deploy the API for the changes to take effect.

1. Choose **Actions**.

1. Choose **Deploy API**.

    **Deploy API action**
![image39](http://docs.aws.amazon.com/solutions/latest/qnabot-on-aws/images/image39.png)

1. Choose the following:
   + Deployment stage: **prod**.
   + Deployment description: Enter **Updated** ` <location> ` response header in the GET method for the `/pages/designer` and the `/pages/client` resources.

1. Choose **Deploy**.

## Step 6: Update the API Stage variables
<a name="step-6-update-the-api-stage-variables"></a>

Once the API is deployed, the **Stage Editor** page appears.

1. Choose the **Stage Variables** tab.

1. Update the values for **ClientLoginUrl** and **DesignerLoginUrl** variables to use the custom domain name.

 **Update stage variables**

![image40](http://docs.aws.amazon.com/solutions/latest/qnabot-on-aws/images/image40.png)

## Step 7: Test the updates using the custom domain name
<a name="step-7-test-the-updates-using-the-custom-domain-name"></a>

Launch the **QnABot** content designer in a new browser session using the custom domain name `https:// <your-custom-domain-name> /prod/pags/designer` to test the updates.

## Known limitation
<a name="known-limitation"></a>

A CloudFormation stack update of QnABot on AWS performed after the above steps, will overwrite the changes made in Steps 3, 4, 5, and 6 above. We are looking at better ways to automate this process, but in the meantime, if you perform a stack update after the above steps, you will need to manually re-apply the above steps 3, 4, 5, and 6 again.
