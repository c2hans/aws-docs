---
source_url: https://docs.aws.amazon.com/apigateway/latest/developerguide/apiportal-portals-access.html
---

# Control access to a documentation portal with Amazon Cognito

A documentation portal has two levels of access control, both based on an Amazon Cognito user pool.
+ **Portal authorization** requires readers to sign in with your user pool before they can see anything. Every signed-in user sees the whole portal.
+ **Fine-grained access control** (granular authorization) additionally limits which products, and which pages within a product, each reader can see. It uses an Amazon Cognito identity pool to map readers to IAM roles, and the role's policy decides which products the reader can view.

## Considerations
<a name="apiportal-portals-access-considerations"></a>
+ The user pool, app client, and identity pool must be in the same Region as each other. They can be in a different Region from the portal.
+ Portal authorization controls who can read documentation. It doesn't control who can call the APIs; that's set on the APIs themselves.
+ Fine-grained access control requires portal authorization. You can't enable it on a portal with authorization set to **None**.
+ A reader who isn't mapped to a role with any product permissions can sign in but sees no products.
+ After you change the portal's authorization settings (the authorization type or the Amazon Cognito identifiers), publish the portal again. Changes that you make in Amazon Cognito itself, or to the IAM roles mapped to its users and groups, take effect immediately without republishing.

## Require sign-in
<a name="apiportal-portals-access-cognito"></a>

Before you begin, create a user pool with an app client that uses the authorization code grant and has the portal's URL as a callback URL, and a user pool domain for the hosted sign-in pages. For more information, see [Amazon Cognito user pools](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-identity-pools.html).

**To require sign-in**

1. On the portal detail page, choose **Edit portal** (or set this when you create the portal).

1. For **Portal authorization**, choose **Require authorization**.

1. Choose the user pool's Region, then the **User pool**, **Application client**, and **User pool domain**.

1. Leave **Granular authorization** set to **Disabled**, save, and publish the portal.

## Limit which products each reader can see
<a name="apiportal-portals-access-granular"></a>

With fine-grained access control, API Portal exchanges the reader's user pool token for IAM credentials through an identity pool, and shows a product or page only if those credentials are allowed to read it. You control visibility with ordinary IAM policies on the roles that the identity pool assigns.

**Step 1: Create the identity pool and roles**

1. In the Amazon Cognito console, create an identity pool with your user pool and app client as the authenticated identity provider. Don't allow unauthenticated identities.

1. Create an IAM role for each audience, trusted by the identity pool (`cognito-identity.amazonaws.com` with the `aud` condition set to your identity pool ID and `amr` = `authenticated`). Attach a policy that allows `apiportal:GetProduct`, `apiportal:GetProductPage`, and `apiportal:GetProductApiPage` on the products and pages that audience may see. The following policy lets readers see one product and all of its pages:

   ```json
   {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Effect": "Allow",
         "Action": [
           "apiportal:GetProduct",
           "apiportal:GetProductPage",
           "apiportal:GetProductApiPage"
         ],
         "Resource": [
           "arn:aws:apiportal:us-east-1:{{111122223333}}:products/{{product-id}}",
           "arn:aws:apiportal:us-east-1:{{111122223333}}:products/{{product-id}}/*"
         ]
       }
     ]
   }
   ```

   To grant only some pages of a product, list the page ARNs (`…:products/{{product-id}}/productpages/{{page-id}}` and `…/apipages/{{page-id}}`) instead of `/*`. The reader must also be allowed `apiportal:GetProduct` on the product itself.

1. Create a user pool group for each audience and set its **IAM role** to the matching role. Add readers to groups.

1. In the identity pool, under **Role settings**, choose **Choose role with rules** or **Choose role from token** for your user pool provider, so that each reader gets their group's role. Set the default authenticated role to a role with no product permissions.

**Step 2: Enable fine-grained access control on the portal**

1. On the portal detail page, choose **Edit portal**.

1. Under **Portal authorization**, with **Require authorization** selected, set **Granular authorization** to **Enabled**.

1. For **Identity pool**, choose the identity pool you created.

1. Save, and publish the portal.

Readers now see only the products and pages their role allows. To change what a reader sees, change their group membership or the role's policy; no republish is needed for policy changes.

Using the AWS CLI:

```
aws apiportal update-portal \
    --portal-id {{portal-id}} \
    --authorization '{"authorizationConfig":{"cognitoConfig":{"userPoolArn":"arn:aws:cognito-idp:us-east-1:{{111122223333}}:userpool/{{us-east-1_EXAMPLE}}","appClientId":"{{app-client-id}}","userPoolDomain":"{{example.auth.us-east-1.amazoncognito.com}}","identityPoolId":"us-east-1:{{11111111-2222-3333-4444-555555555555}}"}},"fineGrainedAccessControl":"ENABLED"}' \
    --region us-east-1
```
