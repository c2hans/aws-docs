---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iotsitewise-portal.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTSiteWise::Portal
<a name="aws-resource-iotsitewise-portal"></a>

**Important**
The AWS IoT SiteWise Monitor feature will no longer be open to new customers starting November 7, 2025 . If you would like to use the AWS IoT SiteWise Monitor feature, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [AWS IoT SiteWise Monitor availability change](https://docs.aws.amazon.com/iot-sitewise/latest/appguide/iotsitewise-monitor-availability-change.html).

Creates a portal, which can contain projects and dashboards. AWS IoT SiteWise Monitor uses IAM Identity Center or IAM to authenticate portal users and manage user permissions.

**Note**
Before you can sign in to a new portal, you must add at least one identity to that portal. For more information, see [Adding or removing portal administrators](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/administer-portals.html#portal-change-admins) in the *AWS IoT SiteWise User Guide*.

## Syntax
<a name="aws-resource-iotsitewise-portal-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-iotsitewise-portal-syntax.json"></a>

```
{
  "Type" : "AWS::IoTSiteWise::Portal",
  "Properties" : {
      "[Alarms](#cfn-iotsitewise-portal-alarms)" : {{Alarms}},
      "[NotificationSenderEmail](#cfn-iotsitewise-portal-notificationsenderemail)" : {{String}},
      "[PortalAuthMode](#cfn-iotsitewise-portal-portalauthmode)" : {{String}},
      "[PortalContactEmail](#cfn-iotsitewise-portal-portalcontactemail)" : {{String}},
      "[PortalDescription](#cfn-iotsitewise-portal-portaldescription)" : {{String}},
      "[PortalName](#cfn-iotsitewise-portal-portalname)" : {{String}},
      "[PortalType](#cfn-iotsitewise-portal-portaltype)" : {{String}},
      "[PortalTypeConfiguration](#cfn-iotsitewise-portal-portaltypeconfiguration)" : {{{{{Key}}: {{Value}}, ...}}},
      "[RoleArn](#cfn-iotsitewise-portal-rolearn)" : {{String}},
      "[Tags](#cfn-iotsitewise-portal-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-iotsitewise-portal-syntax.yaml"></a>

```
Type: AWS::IoTSiteWise::Portal
Properties:
  [Alarms](#cfn-iotsitewise-portal-alarms): {{
    Alarms}}
  [NotificationSenderEmail](#cfn-iotsitewise-portal-notificationsenderemail): {{String}}
  [PortalAuthMode](#cfn-iotsitewise-portal-portalauthmode): {{String}}
  [PortalContactEmail](#cfn-iotsitewise-portal-portalcontactemail): {{String}}
  [PortalDescription](#cfn-iotsitewise-portal-portaldescription): {{String}}
  [PortalName](#cfn-iotsitewise-portal-portalname): {{String}}
  [PortalType](#cfn-iotsitewise-portal-portaltype): {{String}}
  [PortalTypeConfiguration](#cfn-iotsitewise-portal-portaltypeconfiguration): {{
    {{Key}}: {{Value}}}}
  [RoleArn](#cfn-iotsitewise-portal-rolearn): {{String}}
  [Tags](#cfn-iotsitewise-portal-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-iotsitewise-portal-properties"></a>

`Alarms`  <a name="cfn-iotsitewise-portal-alarms"></a>
Contains the configuration information of an alarm created in an AWS IoT SiteWise Monitor portal. You can use the alarm to monitor an asset property and get notified when the asset property value is outside a specified range. For more information, see [Monitoring with alarms](https://docs.aws.amazon.com/iot-sitewise/latest/appguide/monitor-alarms.html) in the *AWS IoT SiteWise Application Guide*.
*Required*: No
*Type*: [Alarms](aws-properties-iotsitewise-portal-alarms.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NotificationSenderEmail`  <a name="cfn-iotsitewise-portal-notificationsenderemail"></a>
The email address that sends alarm notifications.
If you use the [AWS IoT Events managed Lambda function](https://docs.aws.amazon.com/iotevents/latest/developerguide/lambda-support.html) to manage your emails, you must [verify the sender email address in Amazon SES](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/verify-email-addresses.html).
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PortalAuthMode`  <a name="cfn-iotsitewise-portal-portalauthmode"></a>
The service to use to authenticate users to the portal. Choose from the following options:
+ `SSO` – The portal uses AWS IAM Identity Center to authenticate users and manage user permissions. Before you can create a portal that uses IAM Identity Center, you must enable IAM Identity Center. For more information, see [Enabling IAM Identity Center](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/monitor-get-started.html#mon-gs-sso) in the *AWS IoT SiteWise User Guide*. This option is only available in AWS Regions other than the China Regions.
+ `IAM` – The portal uses AWS Identity and Access Management to authenticate users and manage user permissions.
You can't change this value after you create a portal.
Default: `SSO`
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PortalContactEmail`  <a name="cfn-iotsitewise-portal-portalcontactemail"></a>
The AWS administrator's contact email address.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PortalDescription`  <a name="cfn-iotsitewise-portal-portaldescription"></a>
A description for the portal.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PortalName`  <a name="cfn-iotsitewise-portal-portalname"></a>
A friendly name for the portal.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PortalType`  <a name="cfn-iotsitewise-portal-portaltype"></a>
Define the type of portal. The value for AWS IoT SiteWise Monitor (Classic) is `SITEWISE_PORTAL_V1`. The value for AWS IoT SiteWise Monitor (AI-aware) is `SITEWISE_PORTAL_V2`.
*Required*: No
*Type*: String
*Allowed values*: `SITEWISE_PORTAL_V1 | SITEWISE_PORTAL_V2`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PortalTypeConfiguration`  <a name="cfn-iotsitewise-portal-portaltypeconfiguration"></a>
Property description not available.
*Required*: No
*Type*: Object of [PortalTypeEntry](aws-properties-iotsitewise-portal-portaltypeentry.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RoleArn`  <a name="cfn-iotsitewise-portal-rolearn"></a>
The [ARN](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of a service role that allows the portal's users to access your AWS IoT SiteWise resources on your behalf. For more information, see [Using service roles for AWS IoT SiteWise Monitor](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/monitor-service-role.html) in the *AWS IoT SiteWise User Guide*.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-iotsitewise-portal-tags"></a>
A list of key-value pairs that contain metadata for the portal. For more information, see [Tagging your AWS IoT SiteWise resources](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/tag-resources.html) in the *AWS IoT SiteWise User Guide*.
*Required*: No
*Type*: Array of [Tag](aws-properties-iotsitewise-portal-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-iotsitewise-portal-return-values"></a>

### Ref
<a name="aws-resource-iotsitewise-portal-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the `PortalId`.

### Fn::GetAtt
<a name="aws-resource-iotsitewise-portal-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-iotsitewise-portal-return-values-fn--getatt-fn--getatt"></a>

`PortalArn`  <a name="PortalArn-fn::getatt"></a>
The [ARN](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the portal, which has the following format.
 `arn:${Partition}:iotsitewise:${Region}:${Account}:portal/${PortalId}`
For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

`PortalClientId`  <a name="PortalClientId-fn::getatt"></a>
The IAM Identity Center application generated client ID (used with IAM Identity Center APIs).
For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

`PortalId`  <a name="PortalId-fn::getatt"></a>
The ID of the created portal.
For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

`PortalStartUrl`  <a name="PortalStartUrl-fn::getatt"></a>
The public URL for the AWS IoT SiteWise Monitor portal.
For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).
