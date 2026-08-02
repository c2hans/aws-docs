---
source_url: https://docs.aws.amazon.com/location/previous/developerguide/authenticating-using-cognito.html
---

# Allow unauthenticated guest access to your application using Amazon Cognito
<a name="authenticating-using-cognito"></a>

You can use Amazon Cognito authentication as an alternative to directly using AWS Identity and Access Management (IAM) with both front end SDKs and direct HTTPS requests.

You may want to use this form of authentication for the following reasons:
+ **Unauthenticated users** – If you have a website with anonymous users, you can use Amazon Cognito identity pools. For more information, see the section on [Allow unauthenticated guest access to your application using Amazon Cognito](#authenticating-using-cognito).
+ **Your own authentication** – If you would like to use your own authentication process, or combine multiple authentication methods, you can use Amazon Cognito Federated Identities. For more information, see [Getting Started with Federated Identities](https://docs.aws.amazon.com/cognito/latest/developerguide/getting-started-with-identity-pools.html) in the *Amazon Cognito Developer Guide*.

Amazon Cognito provides authentication, authorization, and user management for web and mobile apps. You can use Amazon Cognito unauthenticated identity pools with Amazon Location as a way for applications to retrieve temporary, scoped-down AWS credentials.

For more information, see [Getting Started with User Pools](https://docs.aws.amazon.com/cognito/latest/developerguide/getting-started-with-cognito-user-pools.html) in the *Amazon Cognito Developer Guide*.

**Note**
For mobile developers, Amazon Location provides mobile authentication SDKs for both iOS and Android, see the following GitHub repositories for more information:
[Amazon Location Service Mobile Authentication SDK for iOS](https://github.com/aws-geospatial/amazon-location-mobile-auth-sdk-ios/)
[Amazon Location Service Mobile Authentication SDK for Android](https://github.com/aws-geospatial/amazon-location-mobile-auth-sdk-android/)

## Create an Amazon Cognito identity pool
<a name="cognito-create-user-pool"></a>

You can create Amazon Cognito identity pools to allow unauthenticated guest access to your application through the Amazon Cognito console, the AWS CLI, or the Amazon Cognito APIs.

**Important**
The pool that you create must be in the same AWS account and AWS Region as the Amazon Location Service resources that you're using.

You can use IAM policies associated with unauthenticated identity roles with the following actions:
+ `geo:GetMap*`
+ `geo:SearchPlaceIndex*`
+ `geo:GetPlace`
+ `geo:CalculateRoute*`
+ `geo:GetGeofence`
+ `geo:ListGeofences`
+ `geo:PutGeofence`
+ `geo:BatchDeleteGeofence`
+ `geo:BatchPutGeofence`
+ `geo:BatchEvaluateGeofences`
+ `geo:GetDevicePosition*`
+ `geo:ListDevicePositions`
+ `geo:BatchDeleteDevicePositionHistory`
+ `geo:BatchGetDevicePosition`
+  `geo:BatchUpdateDevicePosition`

Including other Amazon Location actions will have no effect, and unauthenticated identities will be unable to call them.

**Example**
**To create an identity pool using the Amazon Cognito console**

1. Go to the [Amazon Cognito console](https://console.aws.amazon.com/cognito/home).

1. Choose **Manage Identity Pools.**

1. Choose **Create new identity pool**, then enter a name for your identity pool.

1. From the **Unauthenticated identities** collapsible section, choose **Enable access to unauthenticated identities**.

1. Choose **Create Pool**.

1. Choose which IAM roles you want to use with your identity pool.

1. Expand **View Details**.

1. Under **Unauthenticated identities**, enter a role name.

1. Expand the **View Policy Document** section, then choose **Edit** to add your policy.

1. Add your policy to grant access to your resources.

   The following are policy examples for Maps, Places, Trackers, and Routes. To use the examples for your own policy, replace the {{region}} and {{accountID}} placeholders:

------
#### [ Maps policy example ]

   The following policy grants read-only access to a map resource named {{ExampleMap}}.

   ```
   {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Sid": "MapsReadOnly",
         "Effect": "Allow",
         "Action": [
           "geo:GetMapStyleDescriptor",
           "geo:GetMapGlyphs",
           "geo:GetMapSprites",
           "geo:GetMapTile"
         ],
         "Resource": "arn:aws:geo:{{region}}:{{accountID}}:map/{{ExampleMap}}"
       }
     ]
   }
   ```

   Adding an [IAM condition](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html) that matches `aws:referer` lets you limit browser access to your resources to a list of URLs or URL prefixes. The following example allows access to a map resource named `RasterEsriImagery` from only the website `example.com`:

**Warning**
 While `aws:referer` can limit access, it is not a security mechanism. It is dangerous to include a publicly known referer header value. Unauthorized parties can use modified or custom browsers to provide any `aws:referer` value that they choose. As a result, `aws:referer` should not be used to prevent unauthorized parties from making direct AWS requests. It is offered only to allow customers to protect their digital content, such as content stored in Amazon S3, from being referenced on unauthorized third-party sites. For more information, see [AWS:referer](https://docs.aws.amazon.com//IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-referer).

   ```
   {
       "Version": "2012-10-17",
       "Statement": [
           {
               "Effect": "Allow",
               "Action": "geo:GetMap*",
               "Resource": "arn:aws:geo:us-west-2:111122223333:map/RasterEsriImagery",
               "Condition": {
                   "StringLike": {
                       "aws:referer": [
                           "https://example.com/*",
                           "https://www.example.com/*"
                       ]
                   }
               }
           }
       ]
   }
   ```

   If you're [using Tangram](https://docs.aws.amazon.com/location/previous/developerguide/tutorial-tangram.html) to display a map, it doesn't use the style descriptors, glyphs, or sprites returned by the Maps API. Instead, it's configured by pointing to a .zip file that contains style rules and necessary assets. The following policy grants read-only access to a map resource named {{ExampleMap}} for the `GetMapTile` operation.

   ```
   {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Sid": "MapsReadOnly",
         "Effect": "Allow",
         "Action": [
           "geo:GetMapTile"
         ],
         "Resource": "arn:aws:geo:{{region}}:{{accountID}}:map/{{ExampleMap}}"
       }
     ]
   }
   ```

------
#### [ Places policy example ]

   The following policy grants read-only access to a place index resource named {{ExamplePlaceIndex}} to search for places by text or positions.

   ```
   {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Sid": "PlacesReadOnly",
         "Effect": "Allow",
         "Action": [
             "geo:SearchPlaceIndex*",
             "geo:GetPlace"
         ],
         "Resource": "arn:aws:geo:{{region}}:{{accountID}}:place-index/{{ExamplePlaceIndex}}"
       }
     ]
   }
   ```

   Adding an [IAM condition](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html) that matches `aws:referer` lets you limit browser access to your resources to a list of URLs or URL prefixes. The following example denies access to a place index resource named {{ExamplePlaceIndex}} from all referring websites, except `example.com`.

**Warning**
 While `aws:referer` can limit access, it is not a security mechanism. It is dangerous to include a publicly known referer header value. Unauthorized parties can use modified or custom browsers to provide any `aws:referer` value that they choose. As a result, `aws:referer` should not be used to prevent unauthorized parties from making direct AWS requests. It is offered only to allow customers to protect their digital content, such as content stored in Amazon S3, from being referenced on unauthorized third-party sites. For more information, see [AWS:referrer](https://docs.aws.amazon.com//IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-referer).

   ```
   {
       "Version": "2012-10-17",
       "Statement": [
           {
               "Effect": "Allow",
               "Action": "geo:*",
               "Resource": "arn:aws:geo:us-west-2:111122223333:place-index/{{ExamplePlaceIndex}}",
               "Condition": {
                   "StringLike": {
                       "aws:referer": [
                           "https://example.com/*",
                           "https://www.example.com/*"
                       ]
                   }
               }
           }
       ]
   }
   ```

------
#### [ Trackers policy example ]

   The following policy grants access to a tracker resource named {{ExampleTracker}} to update device positions.

   ```
   {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Sid": "UpdateDevicePosition",
         "Effect": "Allow",
         "Action": [
           "geo:BatchUpdateDevicePosition"
         ],
         "Resource": "arn:aws:geo:{{region}}:{{accountID}}:tracker/{{ExampleTracker}}"
       }
     ]
   }
   ```

   Adding an [IAM condition](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html) that matches `aws:referrer` lets you limit browser access to your resources to a list of URLs or URL prefixes. The following example denies access to a tracker resource named {{ExampleTracker}} from all referring websites, except `example.com`.

**Warning**
 While `aws:referrer` can limit access, it is not a security mechanism. It is dangerous to include a publicly known referrer header value. Unauthorized parties can use modified or custom browsers to provide any `aws:referrer` value that they choose. As a result, `aws:referrer` should not be used to prevent unauthorized parties from making direct AWS requests. It is offered only to allow customers to protect their digital content, such as content stored in Amazon S3, from being referenced on unauthorized third-party sites. For more information, see [AWS:referrer](https://docs.aws.amazon.com//IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-referer).

   ```
   {
       "Version": "2012-10-17",
       "Statement": [
           {
               "Effect": "Allow",
               "Action": "geo:GetDevice*",
               "Resource": "arn:aws:geo:us-west-2:111122223333:tracker/{{ExampleTracker}}",
               "Condition": {
                   "StringLike": {
                       "aws:referer": [
                           "https://example.com/*",
                           "https://www.example.com/*"
                       ]
                   }
               }
           }
       ]
   }
   ```

------
#### [ Routes policy example ]

   The following policy grants access to a route calculator resource named {{ExampleCalculator}} to calculate a route.

   ```
   {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Sid": "RoutesReadOnly",
         "Effect": "Allow",
         "Action": [
           "geo:CalculateRoute"
         ],
         "Resource": "arn:aws:geo:{{region}}:{{accountID}}:route-calculator/{{ExampleCalculator}}"
       }
     ]
   }
   ```

   Adding an [IAM condition](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html) that matches `aws:referrer` lets you limit browser access to your resources to a list of URLs or URL prefixes. The following example denies access to a route calculator named {{ExampleCalculator}} from all referring websites, except `example.com`.

**Warning**
 While `aws:referrer` can limit access, it is not a security mechanism. It is dangerous to include a publicly known referrer header value. Unauthorized parties can use modified or custom browsers to provide any `aws:referrer` value that they choose. As a result, `aws:referrer` should not be used to prevent unauthorized parties from making direct AWS requests. It is offered only to allow customers to protect their digital content, such as content stored in Amazon S3, from being referenced on unauthorized third-party sites. For more information, see [AWS:referrer](https://docs.aws.amazon.com//IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-referer).

   ```
   {
       "Version": "2012-10-17",
       "Statement": [
           {
               "Effect": "Allow",
               "Action": "geo:*",
               "Resource": "arn:aws:geo:us-west-2:111122223333:route-calculator/{{ExampleCalculator}}",
               "Condition": {
                   "StringLike": {
                       "aws:referer": [
                           "https://example.com/*",
                           "https://www.example.com/*"
                       ]
                   }
               }
           }
       ]
   }
   ```

------
**Note**
While unauthenticated identity pools are intended for exposure on unsecured internet sites, note that they will be exchanged for standard, time-limited AWS credentials.
It's important to scope the IAM roles associated with unauthenticated identity pools appropriately.

1. Choose** Allow** to create your identity pools.

The resulting identity pool follows the syntax `<{{region}}>:<{{GUID}}>.`

For example:

```
us-east-1:1sample4-5678-90ef-aaaa-1234abcd56ef
```

For more policy examples specific to Amazon Location, see [Identity-based policy examples for Amazon Location Service](security_iam_id-based-policy-examples.md).

## Use the Amazon Cognito identity pools in JavaScript
<a name="identity-pool-js"></a>

The following example exchanges the unauthenticated identity pool that you've created for credentials that are then used to fetch the style descriptor for your map resource {{ExampleMap}}.

```
const AWS = require("aws-sdk");

const credentials = new AWS.CognitoIdentityCredentials({
   IdentityPoolId: "<identity pool ID>" // for example, us-east-1:1sample4-5678-90ef-aaaa-1234abcd56ef
});

const client = new AWS.Location({
   credentials,
   region: AWS.config.region || "<region>"
});

console.log(await client.getMapStyleDescriptor("{{ExampleMap}}").promise());
```

**Note**
Retrieved credentials from unauthenticated identities are valid for **one hour**.

The following is an example of a function that automatically renews credentials before they expire.

```
async function refreshCredentials() {
  await credentials.refreshPromise();
  // schedule the next credential refresh when they're about to expire
  setTimeout(refreshCredentials, credentials.expireTime - new Date());
}
```

To simplify this work, you can use the Amazon Location [JavaScript Authentication helper](loc-sdk-auth.md). This is in place of both getting the credentials, and refreshing them. This example uses the AWS SDK for JavaScript v3.

```
import { LocationClient, GetMapStyleDescriptorCommand } from "@aws-sdk/client-location";
import { withIdentityPoolId } from "@aws/amazon-location-utilities-auth-helper";

const identityPoolId = "<identity pool ID>"; // for example, us-east-1:1sample4-5678-90ef-aaaa-1234abcd56ef

// Create an authentication helper instance using credentials from Cognito
const authHelper = await withIdentityPoolId(identityPoolId);

const client = new LocationClient({
  region: "<region>", // The region containing both the identity pool and tracker resource
  ...authHelper.getLocationClientConfig(), // Provides configuration required to make requests to Amazon Location
});

const input = {
  MapName: "ExampleMap",
};

const command = new GetMapStyleDescriptorCommand(input);

console.log(await client.send(command));
```

## Next steps
<a name="access-next-steps"></a>
+ To modify your roles, go to the [IAM console](https://console.aws.amazon.com/iam/).
+ To manage your identity pools, go to the [Amazon Cognito console](https://console.aws.amazon.com/cognito/home).
