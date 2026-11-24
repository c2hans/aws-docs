---
source_url: https://docs.aws.amazon.com/apigateway/latest/developerguide/apiportal-portals-create.html
---

# Create a documentation portal in API Portal

**To create a documentation portal**

1. In the main navigation pane, under **API Portal**, choose **Documentation portals**, and then choose **Create documentation portal**.

1. For **Portal name**, enter a name. Optionally, enter a description.

1. For **Portal authorization**, choose **None** to let anyone on the internet view the portal, or **Require authorization** to require sign-in with an Amazon Cognito user pool. See [Control access to a documentation portal with Amazon Cognito](apiportal-portals-access.md).

1. For **Domain configuration**, choose **Custom prefix** and enter a prefix for an AWS-owned domain name, or **Custom domain name** and enter your domain and its ACM certificate. See [Use a custom domain name for a documentation portal](apiportal-portals-domain.md).

1. (Optional) Choose an CloudWatch RUM app monitor. See [Monitor a documentation portal with CloudWatch RUM](apiportal-portals-monitor.md). Choose **Next**.

1. (Optional) On the **Select products** page, add products from your account or shared with you. Choose **Next**.

1. (Optional) On the **Customize portal** page, upload a logo and choose a theme, or choose **Custom theme** and set each color. Choose **Next**.

1. Review and choose **Create**.

The portal detail page opens. It shows the portal's status, URL, authorization, and whether it has unpublished changes, with **Edit portal**, **Preview**, and **Publish portal** buttons, and tabs for **Products**, **Portal design**, **Publish history**, and **Tags**. The portal isn't available to consumers until you publish it. See [Preview, publish, and update a documentation portal](apiportal-portals-publish.md).

To add or remove products later, choose the **Products** tab, then **Add products** or **Remove**. To change the name, description, theme, or logo, choose **Edit portal**.

Using the AWS CLI:

```
aws apiportal create-portal \
    --portal-content '{"displayName":"Payments developer docs","theme":{"customColors":{"backgroundColor":"#FFFFFF","navigationColor":"#232F3E","headerColor":"#232F3E","textColor":"#111111","accentColor":"#FF9900","errorValidationColor":"#D13212"}}}' \
    --endpoint-configuration '{"none":{}}' \
    --authorization '{"authorizationConfig":{"none":{}},"fineGrainedAccessControl":"DISABLED"}' \
    --included-product-arns arn:aws:apiportal:us-east-1:{{111122223333}}:products/{{product-id}} \
    --region us-east-1
```
