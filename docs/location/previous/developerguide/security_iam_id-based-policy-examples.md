---
source_url: https://docs.aws.amazon.com/location/previous/developerguide/security_iam_id-based-policy-examples.html
---

# Identity-based policy examples for Amazon Location Service
<a name="security_iam_id-based-policy-examples"></a>

By default, users and roles don't have permission to create or modify Amazon Location resources. To grant users permission to perform actions on the resources that they need, an IAM administrator can create IAM policies.

To learn how to create an IAM identity-based policy by using these example JSON policy documents, see [Create IAM policies (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create-console.html) in the *IAM User Guide*.

For details about actions and resource types defined by Amazon Location, including the format of the ARNs for each of the resource types, see [Actions, Resources, and Condition Keys for Amazon Location Service](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonlocation.html) in the *Service Authorization Reference*.

**Topics**
+ [Policy best practices](#security_iam_service-with-iam-policy-best-practices)
+ [Using the Amazon Location console](#security_iam_id-based-policy-examples-console)
+ [Allow users to view their own permissions](#security_iam_id-based-policy-examples-view-own-permissions)
+ [Using Amazon Location Service resources in policy](#security_iam_id-based-policy-examples-using-resources)
+ [Permissions for updating device positions](#security_iam_id-based-policy-examples-update-device-positions)
+ [Read-only policy for tracker resources](#security_iam_id-based-policy-examples-read-only-trackers)
+ [Policy for creating geofences](#security_iam_id-based-policy-examples-create-geofences)
+ [Read-only policy for geofences](#security_iam_id-based-policy-examples-read-only-geofences)
+ [Permissions for rendering a map resource](#security_iam_id-based-policy-examples-get-map-tiles)
+ [Permissions to allow search operations](#security_iam_id-based-policy-examples-search-for-place)
+ [Read-only policy for route calculators](#security_iam_id-based-policy-examples-calculate-route)
+ [Control resource access based on condition keys](#security_iam_condition-key-example)
+ [Control resource access based on tags](#security_iam_tag-based-policy-example)

## Policy best practices
<a name="security_iam_service-with-iam-policy-best-practices"></a>

Identity-based policies determine whether someone can create, access, or delete Amazon Location resources in your account. These actions can incur costs for your AWS account. When you create or edit identity-based policies, follow these guidelines and recommendations:
+ **Get started with AWS managed policies and move toward least-privilege permissions** – To get started granting permissions to your users and workloads, use the *AWS managed policies* that grant permissions for many common use cases. They are available in your AWS account. We recommend that you reduce permissions further by defining AWS customer managed policies that are specific to your use cases. For more information, see [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) or [AWS managed policies for job functions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html) in the *IAM User Guide*.
+ **Apply least-privilege permissions** – When you set permissions with IAM policies, grant only the permissions required to perform a task. You do this by defining the actions that can be taken on specific resources under specific conditions, also known as *least-privilege permissions*. For more information about using IAM to apply permissions, see [ Policies and permissions in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html) in the *IAM User Guide*.
+ **Use conditions in IAM policies to further restrict access** – You can add a condition to your policies to limit access to actions and resources. For example, you can write a policy condition to specify that all requests must be sent using SSL. You can also use conditions to grant access to service actions if they are used through a specific AWS service, such as CloudFormation. For more information, see [ IAM JSON policy elements: Condition](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html) in the *IAM User Guide*.
+ **Use IAM Access Analyzer to validate your IAM policies to ensure secure and functional permissions** – IAM Access Analyzer validates new and existing policies so that the policies adhere to the IAM policy language (JSON) and IAM best practices. IAM Access Analyzer provides more than 100 policy checks and actionable recommendations to help you author secure and functional policies. For more information, see [Validate policies with IAM Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-policy-validation.html) in the *IAM User Guide*.
+ **Require multi-factor authentication (MFA)** – If you have a scenario that requires IAM users or a root user in your AWS account, turn on MFA for additional security. To require MFA when API operations are called, add MFA conditions to your policies. For more information, see [ Secure API access with MFA](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_configure-api-require.html) in the *IAM User Guide*.

For more information about best practices in IAM, see [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) in the *IAM User Guide*.

## Using the Amazon Location console
<a name="security_iam_id-based-policy-examples-console"></a>

To access the Amazon Location Service console, you must have a minimum set of permissions. These permissions must allow you to list and view details about the Amazon Location resources in your AWS account. If you create an identity-based policy that is more restrictive than the minimum required permissions, the console won't function as intended for entities (users or roles) with that policy.

You don't need to allow minimum console permissions for users that are making calls only to the AWS CLI or the AWS API. Instead, allow access to only the actions that match the API operation that they're trying to perform.

To ensure that users and roles can use the Amazon Location console, attach the following policy to the entities. For more information, see [Adding permissions to a user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_change-permissions.html#users_change_permissions-add-console) in the *IAM User Guide*.

The following policy gives access to the Amazon Location Service console, to be able to create, delete, list and view details about Amazon Location resources in your AWS account.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "GeoPowerUser",
      "Effect": "Allow",
      "Action": [
        "geo:*"
      ],
      "Resource": "*"
    }
  ]
}
```

Alternatively, you can grant read-only permissions to facilitate read-only access. With read-only permissions, an error message will appear if the user attempts write actions such as creating or deleting resources. As an example, see [Read-only policy for tracker resources](#security_iam_id-based-policy-examples-read-only-trackers)

## Allow users to view their own permissions
<a name="security_iam_id-based-policy-examples-view-own-permissions"></a>

This example shows how you might create a policy that allows IAM users to view the inline and managed policies that are attached to their user identity. This policy includes permissions to complete this action on the console or programmatically using the AWS CLI or AWS API.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "ViewOwnUserInfo",
            "Effect": "Allow",
            "Action": [
                "iam:GetUserPolicy",
                "iam:ListGroupsForUser",
                "iam:ListAttachedUserPolicies",
                "iam:ListUserPolicies",
                "iam:GetUser"
            ],
            "Resource": ["arn:aws:iam::*:user/${aws:username}"]
        },
        {
            "Sid": "NavigateInConsole",
            "Effect": "Allow",
            "Action": [
                "iam:GetGroupPolicy",
                "iam:GetPolicyVersion",
                "iam:GetPolicy",
                "iam:ListAttachedGroupPolicies",
                "iam:ListGroupPolicies",
                "iam:ListPolicyVersions",
                "iam:ListPolicies",
                "iam:ListUsers"
            ],
            "Resource": "*"
        }
    ]
}
```

## Using Amazon Location Service resources in policy
<a name="security_iam_id-based-policy-examples-using-resources"></a>

Amazon Location Service uses the following prefixes for resources:

**Amazon Location resource prefix**

| Resource | Resource prefix |
| --- | --- |
| Map resources | map |
| Place resources | place-index |
| Route resources | route-calculator |
| Tracking resources | tracker |
| Geofence Collection resources | geofence-collection |

Use the following ARN syntax:

```
arn:{{Partition}}:geo:{{Region}}:{{Account}}:{{ResourcePrefix}}/{{ResourceName}}
```

For more information about the format of ARNs, see [Amazon Resource Names (ARNs) and AWS Service Namespaces](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html).

**Examples**
+ Use the following ARN to allow access to a specified map resource.

  ```
  "Resource": "arn:aws:geo:us-west-2:{{account-id}}:map/{{map-resource-name}}"
  ```
+ To specify access to all `map` resources that belong to a specific account, use the wildcard (\*):

  ```
  "Resource": "arn:aws:geo:us-west-2:{{account-id}}:map/*"
  ```
+ Some Amazon Location actions, such as those for creating resources, can't be performed on a specific resource. In those cases, you must use the wildcard (\*).

  ```
  "Resource": "*"
  ```

To see a list of Amazon Location resource types and their ARNs, see [Resources Defined by Amazon Location Service](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonlocation.html#amazonlocation-resources-for-iam-policies) in the *Service Authorization Reference*. To learn with which actions you can specify the ARN of each resource, see [Actions Defined by Amazon Location Service](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonlocation.html#amazonlocation-actions-as-permissions).

## Permissions for updating device positions
<a name="security_iam_id-based-policy-examples-update-device-positions"></a>

 To update device positions for multiple trackers, you'll want to grant a user access to one or more of your tracker resources. You will also want to allow the user to update a batch of device positions.

In this example, in addition to granting access to the {{Tracker1}} and {{Tracker2}} resources, the following policy grants permission to use the `geo:BatchUpdateDevicePosition` action against the {{Tracker1}} and {{Tracker2}} resources.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "UpdateDevicePositions",
      "Effect": "Allow",
      "Action": [
        "geo:BatchUpdateDevicePosition"
      ],
      "Resource": [
        "arn:aws:geo:us-west-2:{{account-id}}:tracker/{{Tracker1}}",
        "arn:aws:geo:us-west-2:{{account-id}}:tracker/{{Tracker2}}"
      ]
    }
  ]
}
```

If you want to limit the user to only be able to update device positions for a specific device, you can add a condition key for that device id.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "UpdateDevicePositions",
      "Effect": "Allow",
      "Action": [
        "geo:BatchUpdateDevicePosition"
      ],
      "Resource": [
        "arn:aws:geo:us-west-2:{{account-id}}:tracker/{{Tracker1}}",
        "arn:aws:geo:us-west-2:{{account-id}}:tracker/{{Tracker2}}"
      ],
      "Condition":{
        "ForAllValues:StringLike":{
          "geo:DeviceIds":[
            "{{deviceId}}"
          ]
        }
      }
    }
  ]
}
```

## Read-only policy for tracker resources
<a name="security_iam_id-based-policy-examples-read-only-trackers"></a>

To create a read-only policy for all tracker resources in your AWS account, you'll need to grant access to all tracker resources. You'll also want to grant a user access to actions that allow them to get the device position for multiple devices, get the device position from a single device and get the position history.

In this example, the following policy grants permission to the following actions:
+ `geo:BatchGetDevicePosition` to retrieve the position of multiple devices.
+ `geo:GetDevicePosition` to retrieve the position of a single device.
+ `geo:GetDevicePositionHistory` to retrieve the position history of a device.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "GetDevicePositions",
      "Effect": "Allow",
      "Action": [
        "geo:BatchGetDevicePosition",
        "geo:GetDevicePosition",
        "geo:GetDevicePositionHistory"
      ],
      "Resource": "arn:aws:geo:us-west-2:{{account-id}}:tracker/*"
    }
  ]
}
```

## Policy for creating geofences
<a name="security_iam_id-based-policy-examples-create-geofences"></a>

To create a policy to allow a user to create geofences, you'll need to grant access to specific actions that allow users to create one or more geofences on a geofence collection.

The policy below grants permission to the following actions on {{Collection}}:
+ `geo:BatchPutGeofence` to create multiple geofences.
+ `geo:PutGeofence` to create a single geofence.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "CreateGeofences",
      "Effect": "Allow",
      "Action": [
        "geo:BatchPutGeofence",
        "geo:PutGeofence"
      ],
      "Resource": "arn:aws:geo:us-west-2:{{account-id}}:geofence-collection/{{Collection}}"
    }
  ]
}
```

## Read-only policy for geofences
<a name="security_iam_id-based-policy-examples-read-only-geofences"></a>

To create a read-only policy for geofences stored in a geofence collection in your AWS account, you'll need to grant access to actions that read from the geofence collection storing the geofences.

The policy below grants permission to the following actions on {{Collection}}:
+ `geo:ListGeofences` to list geofences in the specified geofence collection.
+ `geo:GetGeofence` to retrieve a geofence from the geofence collection.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "GetGeofences",
      "Effect": "Allow",
      "Action": [
        "geo:ListGeofences",
        "geo:GetGeofence"
      ],
      "Resource": "arn:aws:geo:us-west-2:{{account-id}}:geofence-collection/{{Collection}}"
    }
  ]
}
```

## Permissions for rendering a map resource
<a name="security_iam_id-based-policy-examples-get-map-tiles"></a>

To grant sufficient permissions to render maps, you'll need to grant access to map tiles, sprites, glyphs, and the style descriptor:
+ `geo:GetMapTile` retrieves map tiles used to selectively render features on a map.
+ `geo:GetMapSprites` retrieves the PNG sprite sheet and corresponding JSON document describing offsets within it.
+ `geo:GetMapGlyphs` retrieves the glyphs used for displaying text.
+ `geo:GetMapStyleDescriptor` retrieves the map’s style descriptor, containing rendering rules.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "GetTiles",
      "Effect": "Allow",
      "Action": [
        "geo:GetMapTile",
        "geo:GetMapSprites",
        "geo:GetMapGlyphs",
        "geo:GetMapStyleDescriptor"
      ],
      "Resource": "arn:aws:geo:us-west-2:{{account-id}}:map/{{Map}}"
    }
  ]
}
```

## Permissions to allow search operations
<a name="security_iam_id-based-policy-examples-search-for-place"></a>

To create a policy to allow search operations, you'll first need to grant access to the place index resource in your AWS account. You'll also want to grant access to actions that let the user search using text by geocoding and search using a position by reverse geocoding.

In this example, in addition to granting access to {{PlaceIndex}}, the following policy also grants permission to the following actions:
+ `geo:SearchPlaceIndexForPosition` allows you to search for places, or points of interest near a given position.
+ `geo:SearchPlaceIndexForText` allows you to search for an address, name, city or region using free-form text.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "Search",
      "Effect": "Allow",
      "Action": [
        "geo:SearchPlaceIndexForPosition",
        "geo:SearchPlaceIndexForText"
      ],
      "Resource": "arn:aws:geo:us-west-2:{{account-id}}:place-index/{{PlaceIndex}}"
    }
  ]
}
```

## Read-only policy for route calculators
<a name="security_iam_id-based-policy-examples-calculate-route"></a>

You can create a read-only policy to allow a user access to a route calculator resource to calculate a route.

In this example, in addition to granting access to {{ExampleCalculator}}, the following policy grants permission to the following operation:
+ `geo:CalculateRoute` calculates a route given a departure position, destination positon, and a list of waypoint positions.

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
      "Resource": "arn:aws:geo:us-west-2:{{accountID}}:route-calculator/{{ExampleCalculator}}"
    }
  ]
}
```

## Control resource access based on condition keys
<a name="security_iam_condition-key-example"></a>

When you create an IAM policy to grant access to use geofences or device positions, you can use [ Condition operators](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition_operators.html) for more precise control over which geofences or devices a user can access. You can do this by including the geofence id or device id in the `Condition` element of your policy.

The following example policy shows how you might create a policy that allows a user to update device positions for a specific device.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "UpdateDevicePositions",
      "Effect": "Allow",
      "Action": [
        "geo:BatchUpdateDevicePosition"
      ],
      "Resource": [
        "arn:aws:geo:us-west-2:{{account-id}}:tracker/{{Tracker}}"
      ],
      "Condition":{
        "ForAllValues:StringLike":{
          "geo:DeviceIds":[
            "{{deviceId}}"
          ]
        }
      }
    }
  ]
}
```

## Control resource access based on tags
<a name="security_iam_tag-based-policy-example"></a>

When you create an IAM policy to grant access to use your Amazon Location resources, you can use [attribute-based access control](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_attribute-based-access-control.html) for better control over which resources a user can modify, use, or delete. You can do this by including tag information in the `Condition` element of your policy to control access based on your resource [tags](tagging.md).

The following example policy shows how you might create a policy that allows a user to create geofences. This grants the permission to the following actions to create one or more geofences on a geofence collection called {{Collection}}:
+ `geo:BatchPutGeofence` to create multiple geofences.
+ `geo:PutGeofence` to create a single geofence.

However, this policy uses the `Condition` element to grant the permission only if the {{Collection}} tag, `Owner`, has the value of that user's user name.
+ For example, if a user named `richard-roe` attempts to view an Amazon Location {{Collection}}, the {{Collection}} must be tagged `Owner=richard-roe` or `owner=richard-roe`. Otherwise the user is denied access.
**Note**
The condition tag key `Owner` matches both `Owner` and `owner` because condition key names are not case-sensitive. For more information, see [IAM JSON Policy Elements: Condition](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html) in the *IAM User Guide*.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "CreateGeofencesIfOwner",
      "Effect": "Allow",
      "Action": [
        "geo:BatchPutGeofence",
        "geo:PutGeofence"
      ],
      "Resource": "arn:aws:geo:us-west-2:{{account-id}}:geofence-collection/{{Collection}}",
      "Condition": {
                "StringEquals": {"geo:ResourceTag/Owner": "${aws:{{username}}}"}
      }
    }
  ]
}
```

For a tutorial about [how to define permissions to access AWS resources based on tags](https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_attribute-based-access-control.html), see the *AWS Identity and Access Management User Guide*.
