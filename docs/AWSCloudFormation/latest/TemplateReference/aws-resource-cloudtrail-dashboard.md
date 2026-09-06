---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudtrail-dashboard.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudTrail::Dashboard
<a name="aws-resource-cloudtrail-dashboard"></a>

**Important**
CloudTrail Lake will no longer be open to new customers starting May 31, 2026. If you would like to use CloudTrail Lake, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [CloudTrail Lake availability change](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-lake-service-availability-change.html).

 Creates a custom dashboard or the Highlights dashboard.
+ **Custom dashboards** - Custom dashboards allow you to query events in any event data store type. You can add up to 10 widgets to a custom dashboard. You can manually refresh a custom dashboard, or you can set a refresh schedule.
+ **Highlights dashboard** - You can create the Highlights dashboard to see a summary of key user activities and API usage across all your event data stores. CloudTrail Lake manages the Highlights dashboard and refreshes the dashboard every 6 hours. To create the Highlights dashboard, you must set and enable a refresh schedule.

 CloudTrail runs queries to populate the dashboard's widgets during a manual or scheduled refresh. CloudTrail must be granted permissions to run the `StartQuery` operation on your behalf. To provide permissions, run the `PutResourcePolicy` operation to attach a resource-based policy to each event data store. For more information, see [Example: Allow CloudTrail to run queries to populate a dashboard](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/security_iam_resource-based-policy-examples.html#security_iam_resource-based-policy-examples-eds-dashboard) in the *AWS CloudTrail User Guide*.

 To set a refresh schedule, CloudTrail must be granted permissions to run the `StartDashboardRefresh` operation to refresh the dashboard on your behalf. To provide permissions, run the `PutResourcePolicy` operation to attach a resource-based policy to the dashboard. For more information, see [ Resource-based policy example for a dashboard](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/security_iam_resource-based-policy-examples.html#security_iam_resource-based-policy-examples-dashboards) in the *AWS CloudTrail User Guide*.

For more information about dashboards, see [CloudTrail Lake dashboards](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/lake-dashboard.html) in the *AWS CloudTrail User Guide*.

## Syntax
<a name="aws-resource-cloudtrail-dashboard-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-cloudtrail-dashboard-syntax.json"></a>

```
{
  "Type" : "AWS::CloudTrail::Dashboard",
  "Properties" : {
      "[Name](#cfn-cloudtrail-dashboard-name)" : {{String}},
      "[RefreshSchedule](#cfn-cloudtrail-dashboard-refreshschedule)" : {{RefreshSchedule}},
      "[Tags](#cfn-cloudtrail-dashboard-tags)" : {{[ Tag, ... ]}},
      "[TerminationProtectionEnabled](#cfn-cloudtrail-dashboard-terminationprotectionenabled)" : {{Boolean}},
      "[Widgets](#cfn-cloudtrail-dashboard-widgets)" : {{[ Widget, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-cloudtrail-dashboard-syntax.yaml"></a>

```
Type: AWS::CloudTrail::Dashboard
Properties:
  [Name](#cfn-cloudtrail-dashboard-name): {{String}}
  [RefreshSchedule](#cfn-cloudtrail-dashboard-refreshschedule): {{
    RefreshSchedule}}
  [Tags](#cfn-cloudtrail-dashboard-tags): {{
    - Tag}}
  [TerminationProtectionEnabled](#cfn-cloudtrail-dashboard-terminationprotectionenabled): {{Boolean}}
  [Widgets](#cfn-cloudtrail-dashboard-widgets): {{
    - Widget}}
```

## Properties
<a name="aws-resource-cloudtrail-dashboard-properties"></a>

`Name`  <a name="cfn-cloudtrail-dashboard-name"></a>
 The name of the dashboard. The name must be unique to your account.
To create the Highlights dashboard, the name must be `AWSCloudTrail-Highlights`.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9_\-]+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RefreshSchedule`  <a name="cfn-cloudtrail-dashboard-refreshschedule"></a>
 The schedule for a dashboard refresh.
*Required*: No
*Type*: [RefreshSchedule](aws-properties-cloudtrail-dashboard-refreshschedule.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-cloudtrail-dashboard-tags"></a>
A list of tags.
*Required*: No
*Type*: Array of [Tag](aws-properties-cloudtrail-dashboard-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TerminationProtectionEnabled`  <a name="cfn-cloudtrail-dashboard-terminationprotectionenabled"></a>
 Specifies whether termination protection is enabled for the dashboard. If termination protection is enabled, you cannot delete the dashboard until termination protection is disabled.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Widgets`  <a name="cfn-cloudtrail-dashboard-widgets"></a>
 An array of widgets for a custom dashboard. A custom dashboard can have a maximum of ten widgets.
You do not need to specify widgets for the Highlights dashboard.
*Required*: No
*Type*: Array of [Widget](aws-properties-cloudtrail-dashboard-widget.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-cloudtrail-dashboard-return-values"></a>

### Ref
<a name="aws-resource-cloudtrail-dashboard-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-cloudtrail-dashboard-return-values-fn--getatt"></a>

####
<a name="aws-resource-cloudtrail-dashboard-return-values-fn--getatt-fn--getatt"></a>

`CreatedTimestamp`  <a name="CreatedTimestamp-fn::getatt"></a>
 The timestamp that shows when the dashboard was created.

`DashboardArn`  <a name="DashboardArn-fn::getatt"></a>
 The ARN for the dashboard.

`Status`  <a name="Status-fn::getatt"></a>
 The status of the dashboard.

`Type`  <a name="Type-fn::getatt"></a>
 The type of dashboard.

`UpdatedTimestamp`  <a name="UpdatedTimestamp-fn::getatt"></a>
 The timestamp that shows when the dashboard was updated.

## Examples
<a name="aws-resource-cloudtrail-dashboard--examples"></a>

### Example: Create a custom dashboard
<a name="aws-resource-cloudtrail-dashboard--examples--Example:_Create_a_custom_dashboard"></a>

The following example creates a custom dashboard named `AccountActivityDashboard` with four widgets. In this example, a refresh schedule has been set for every 6 hours and termination protection is enabled to prevent the dashboard from being accidentally deleted.

#### JSON
<a name="aws-resource-cloudtrail-dashboard--examples--Example:_Create_a_custom_dashboard--json"></a>

```
{
    "Resources": {
        "Dashboard": {
            "Type": "AWS::CloudTrail::Dashboard",
            "Properties": {
                "Name": "AccountActivityDashboard",
                "RefreshSchedule": {
                    "Frequency": {
                        "Unit": "HOURS",
                        "Value": 6
                    },
                    "Status": "ENABLED",
                    "TimeOfDay": "00:00"
                },
                "Tags": [{
                        "Key": "k1",
                        "Value": "v1"
                    },
                    {
                        "Key": "k2",
                        "Value": "v2"
                    }
                ],
                "TerminationProtectionEnabled": true,
                "Widgets": [{
                        "ViewProperties": {
                            "Height": "2",
                            "Width": "4",
                            "Title": "TopErrors",
                            "View": "Table"
                        },
                        "QueryStatement": "SELECT errorCode, COUNT(*) AS eventCount FROM eds WHERE eventTime > '?' AND eventTime < '?' AND (errorCode is not null) GROUP BY errorCode ORDER BY eventCount DESC LIMIT 100",
                        "QueryParameters": ["$StartTime$", "$EndTime$"]
                    },
                    {
                        "ViewProperties": {
                            "Height": "2",
                            "Width": "4",
                            "Title": "MostActiveRegions",
                            "View": "PieChart",
                            "LabelColumn": "awsRegion",
                            "ValueColumn": "eventCount",
                            "FilterColumn": "awsRegion"
                        },
                        "QueryStatement": "SELECT awsRegion, COUNT(*) AS eventCount FROM eds where eventTime > '?' and eventTime < '?' GROUP BY awsRegion ORDER BY eventCount LIMIT 100",
                        "QueryParameters": ["$StartTime$", "$EndTime$"]
                    },
                    {
                        "ViewProperties": {
                            "Height": "2",
                            "Width": "4",
                            "Title": "AccountActivity",
                            "View": "LineChart",
                            "YAxisColumn": "eventCount",
                            "XAxisColumn": "eventDate",
                            "FilterColumn": "readOnly"
                        },
                        "QueryStatement": "SELECT DATE_TRUNC('?', eventTime) AS eventDate, IF(readOnly, 'read', 'write') AS readOnly, COUNT(*) as eventCount FROM eds WHERE eventTime > '?' AND eventTime < '?' GROUP BY DATE_TRUNC('?', eventTime), readOnly ORDER BY DATE_TRUNC('?', eventTime), readOnly",
                        "QueryParameters": ["$Period$", "$StartTime$", "$EndTime$", "$Period$", "$Period$"]
                    },
                    {
                        "ViewProperties": {
                            "Height": "2",
                            "Width": "4",
                            "Title": "TopServices",
                            "View": "BarChart",
                            "LabelColumn": "service",
                            "ValueColumn": "eventCount",
                            "FilterColumn": "service",
                            "Orientation": "Horizontal"
                        },
                        "QueryStatement": "SELECT REPLACE(eventSource, '.amazonaws.com') AS service, COUNT(*) AS eventCount FROM eds WHERE eventTime > '?' AND eventTime < '?' GROUP BY eventSource ORDER BY eventCount DESC LIMIT 100",
                        "QueryParameters": ["$StartTime$", "$EndTime$"]
                    }
                ]
            }
        }
    }
}
```

#### YAML
<a name="aws-resource-cloudtrail-dashboard--examples--Example:_Create_a_custom_dashboard--yaml"></a>

```
Resources:
  Dashboard:
    Type: 'AWS::CloudTrail::Dashboard'
    Properties:
      Name: "AccountActivityDashboard"
      TerminationProtectionEnabled: true
      RefreshSchedule:
        Frequency:
          Unit: "HOURS"
          Value: 6
        Status: "ENABLED"
        TimeOfDay: "00:00"
      Tags:
        - Key: "k1"
          Value: "v1"
        - Key: "k2"
          Value: "v2"
      Widgets:
        - QueryStatement: "SELECT errorCode, COUNT(*) AS eventCount FROM eds WHERE eventTime > '?' AND eventTime < '?' AND (errorCode is not null) GROUP BY errorCode ORDER BY eventCount DESC LIMIT 100"
          QueryParameters:
            - "$StartTime$"
            - "$EndTime$"
          ViewProperties:
            Height: "2"
            Width: "4"
            Title: "TopErrors"
            View: "Table"
        - QueryStatement: "SELECT awsRegion, COUNT(*) AS eventCount FROM eds where eventTime > '?' and eventTime < '?' GROUP BY awsRegion ORDER BY eventCount LIMIT 100"
          QueryParameters:
            - "$StartTime$"
            - "$EndTime$"
          ViewProperties:
            Height: "2"
            Width: "4"
            Title: "MostActiveRegions"
            View: "PieChart"
            LabelColumn: "awsRegion"
            ValueColumn: "eventCount"
            FilterColumn: "awsRegion"
        - QueryStatement: "SELECT DATE_TRUNC('?', eventTime) AS eventDate, IF(readOnly, 'read', 'write') AS readOnly, COUNT(*) as eventCount FROM eds WHERE eventTime > '?' AND eventTime < '?' GROUP BY DATE_TRUNC('?', eventTime), readOnly ORDER BY DATE_TRUNC('?', eventTime), readOnly"
          QueryParameters:
            - "$Period$"
            - "$StartTime$"
            - "$EndTime$"
            - "$Period$"
            - "$Period$"
          ViewProperties:
            Height: "2"
            Width: "4"
            Title: "AccountActivity"
            View: "LineChart"
            YAxisColumn: "eventCount"
            XAxisColumn: "eventDate"
            FilterColumn: "readOnly"
        - QueryStatement: "SELECT REPLACE(eventSource, '.amazonaws.com') AS service, COUNT(*) AS eventCount FROM eds WHERE eventTime > '?' AND eventTime < '?' GROUP BY eventSource ORDER BY eventCount DESC LIMIT 100"
          QueryParameters:
            - "$StartTime$"
            - "$EndTime$"
          ViewProperties:
            Height: "2"
            Width: "4"
            Title: "TopServices"
            View: "BarChart"
            LabelColumn: "service"
            ValueColumn: "eventCount"
            FilterColumn: "service"
            Orientation: "Horizontal"
```
