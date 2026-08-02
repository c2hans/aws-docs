---
source_url: https://docs.aws.amazon.com/location/previous/developerguide/qs-setup-authentication-ios.html
---

# Set up authentication for your Amazon Location application
<a name="qs-setup-authentication-ios"></a>

The application that you create in this tutorial has anonymous usage, meaning that your users are not required to sign into AWS to use the application. However, the Amazon Location Service APIs require authentication to use. You will use Amazon Cognito to provide authentication and authorization for anonymous users. This tutorial will use Amazon Cognito to authenticate your application.

**Note**
For more information about using Amazon Cognito with Amazon Location Service, see [Grant access to Amazon Location Service](how-to-access.md).

The following tutorials show you how to set up authentication for the map, the place index, and tracker you created in as well setting up permissions for Amazon Location.

**Create an IAM policy for tracking**

1. Sign in to the IAM console at https://console.aws.amazon.com/iam/ with your user that has administrator permissions.

1. In the navigation pane, choose Policies.

1. In the content pane, choose Create policy.

1. Choose the **JSON** option, then copy and paste this JSON policy into the JSON text box.

   ```
   {
           "Version": "2012-10-17",
           "Statement": [
               {
                   "Effect": "Allow",
                   "Action": [
                       "geo:GetMapTile",
                       "geo:GetMapStyleDescriptor",
                       "geo:GetMapSprites",
                       "geo:GetMapGlyphs",
                       "geo:SearchPlaceIndexForPosition",
                       "geo:GetDevicePositionHistory",
                       "geo:BatchUpdateDevicePosition"
                   ],
                   "Resource": [
                       "arn:aws:geo:{Region}:{Account}:map/{MapName}",
                       "arn:aws:geo:{Region}:{Account}:place-index/{IndexName}",
                       "arn:aws:geo:{Region}:{Account}:tracker/{TrackerName}"
                   ]
               }
           ]
       }
   ```

   This is a policy example for Tracking. To use the example for your own policy, replace the `Region`, `Account`, `IndexName`, `MapName` and **TrackerName** placeholders.
**Note**
While unauthenticated identity pools are intended for exposure on unsecured internet sites, note that they will be exchanged for standard, time-limited AWS credentials.
It's important to scope the IAM roles associated with unauthenticated identity pools appropriately. For more information about using and appropriately scoping policies in Amazon Cognito with Amazon Location Service, see [Granting access to Amazon Location Service](location/previous/developerguide/how-to-access.html).

1. On the Review and Create page, provide a name for the policy name field. Review the permissions granted by your policy, and then choose Create Policy to save your work.

The new policy appears in the list of managed policies and is ready to attach.

**Set up authentication for your tracking**

1. Set up authentication for your map application in the [Amazon Cognito console](https://console.aws.amazon.com/cognito/home/).

1. Open the **Identity pools** page.
**Note**
The pool that you create must be in the same AWS account and AWS Region as the Amazon Location Service resources that you created in the previous section.

1. Choose **Create Identity pool**.

1. Starting with the **Configure identity pool trust** step. For user access authentication, select **Guest access**, and press next.

1. On the **Configure permissions** page select the **Use an existing IAM role** and enter the name of the IAM role you created in the previous step. When ready press next to move on to the next step.

1. On the **Configure properties** page, provide a name for your identity pool. Then press **Next**.

1. On the **Review and create** page, review all the information present then press **Create identity pool**.

1. Open the **Identity pools** page, and select the identity pool you just created. Then copy or write down the IdentityPoolId that you will use later in your browser script.
