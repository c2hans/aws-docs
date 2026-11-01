---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/cli_2_ssm-incidents_code_examples.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Incident Manager examples using AWS CLI
<a name="cli_2_ssm-incidents_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with Incident Manager.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)

## Actions
<a name="actions"></a>

### `create-replication-set`
<a name="ssm-incidents_CreateReplicationSet_cli_2_topic"></a>

The following code example shows how to use `create-replication-set`.

**AWS CLI**
**To create the replication set**
The following `create-replication-set` example creates the replication set Incident Manager uses to replicate and encrypt data in your Amazon Web Services account. This example uses the us-east-1 and us-east-2 Regions while creating the replication set.

```
aws ssm-incidents create-replication-set \
    --regions '{{{"us-east-1": {"sseKmsKeyId": "arn:aws:kms:us-east-1:123456789012:key/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"}, "us-east-2": {"sseKmsKeyId": "arn:aws:kms:us-east-1:123456789012:key/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"}}}}'
```
Output:

```
{
    "arn": "arn:aws:ssm-incidents::123456789012:replication-set/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222"
}
```
For more information, see [Configuring replication sets and Findings in Incident Manager](https://docs.aws.amazon.com/incident-manager/latest/userguide/general-settings.html) in the *Incident Manager User Guide*.
+  For API details, see [CreateReplicationSet](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm-incidents/create-replication-set.html) in *AWS CLI Command Reference*.

### `create-response-plan`
<a name="ssm-incidents_CreateResponsePlan_cli_2_topic"></a>

The following code example shows how to use `create-response-plan`.

**AWS CLI**
**To create a response plan**
The following `create-response-plan` example creates a response plan with the specified details.

```
aws ssm-incidents create-response-plan \
    --chat-channel '{{{"chatbotSns": ["arn:aws:sns:us-west-2:123456789012:Standard_User"]}}}' \
    --display-name {{"Example response plan"}} \
    --incident-template '{{{"impact": 5, "title": "example-incident"}}}' \
    --name {{"example-response"}} \
    --actions '{{[{"ssmAutomation": {"documentName": "AWSIncidents-CriticalIncidentRunbookTemplate", "documentVersion": "$DEFAULT", "roleArn": "arn:aws:iam::123456789012:role/aws-service-role/ssm-incidents.amazonaws.com/AWSServiceRoleForIncidentManager", "targetAccount": "RESPONSE_PLAN_OWNER_ACCOUNT"}}]}}' \
    --engagements '{{["arn:aws:ssm-contacts:us-west-2:123456789012:contact/example"]}}'
```
Output:

```
{
    "arn": "arn:aws:ssm-incidents::123456789012:response-plan/example-response"
}
```
For more information, see [Incident preparation](https://docs.aws.amazon.com/incident-manager/latest/userguide/incident-response.html) in the *Incident Manager User Guide*.
+  For API details, see [CreateResponsePlan](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm-incidents/create-response-plan.html) in *AWS CLI Command Reference*.

### `create-timeline-event`
<a name="ssm-incidents_CreateTimelineEvent_cli_2_topic"></a>

The following code example shows how to use `create-timeline-event`.

**AWS CLI**
**Example 1: To create a custom timeline event**
The following `create-timeline-event` example creates a custom timeline event at the specified time on the specified incident.

```
aws ssm-incidents create-timeline-event \
    --event-data "\"example timeline event\"" \
    --event-time {{2022-10-01T20:30:00.000}} \
    --event-type {{"Custom Event"}} \
    --incident-record-arn {{"arn:aws:ssm-incidents::123456789012:incident-record/Example-Response-Plan/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"}}
```
Output:

```
{
    "eventId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
    "incidentRecordArn": "arn:aws:ssm-incidents::123456789012:incident-record/Example-Response-Plan/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
}
```
**Example 2: To create a timeline event with an incident note**
The following `create-timeline-event` example creates a timeline event that is listed in the 'Incident notes' panel.

```
aws ssm-incidents create-timeline-event \
    --event-data "\"New {{Note}}\"" \
    --event-type "Note" \
    --incident-record-arn {{"arn:aws:ssm-incidents::123456789012:incident-record/Test/a1b2c3d4-5678-90ab-cdef-EXAMPLE33333"}} \
    --event-time {{2023-06-20T12:06:00.000}} \
    --event-references '{{[{"resource":"arn:aws:ssm-incidents::123456789012:incident-record/Test/a1b2c3d4-5678-90ab-cdef-EXAMPLE33333"}]}}'
```
Output:

```
{
    "eventId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE44444",
    "incidentRecordArn": "arn:aws:ssm-incidents::123456789012:incident-record/Example-Response-Plan/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
}
```
For more information, see [Incident details](https://docs.aws.amazon.com/incident-manager/latest/userguide/tracking-details.html) in the *Incident Manager User Guide*.
+  For API details, see [CreateTimelineEvent](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm-incidents/create-timeline-event.html) in *AWS CLI Command Reference*.

### `delete-incident-record`
<a name="ssm-incidents_DeleteIncidentRecord_cli_2_topic"></a>

The following code example shows how to use `delete-incident-record`.

**AWS CLI**
**To delete an incident record**
The following `delete-incident-record` example deletes the specified incident record.

```
aws ssm-incidents delete-incident-record \
    --arn {{"arn:aws:ssm-incidents::123456789012:incident-record/Example-Response-Plan/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"}}
```
This command produces no output.
For more information, see [Incident tracking](https://docs.aws.amazon.com/incident-manager/latest/userguide/tracking.html) in the *Incident Manager User Guide*.
+  For API details, see [DeleteIncidentRecord](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm-incidents/delete-incident-record.html) in *AWS CLI Command Reference*.

### `delete-replication-set`
<a name="ssm-incidents_DeleteReplicationSet_cli_2_topic"></a>

The following code example shows how to use `delete-replication-set`.

**AWS CLI**
**To delete the replication set**
The following `delete-replication-set` example deletes the replication set from your Amazon Web Services account. Deleting the replication set also deletes all Incident Manager data. This can't be undone.

```
aws ssm-incidents delete-replication-set \
    --arn {{"arn:aws:ssm-incidents::123456789012:replication-set/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"}}
```
This command produces no output.
For more information, see [Configuring replication sets and Findings in Incident Manager](https://docs.aws.amazon.com/incident-manager/latest/userguide/general-settings.html) in the *Incident Manager User Guide*.
+  For API details, see [DeleteReplicationSet](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm-incidents/delete-replication-set.html) in *AWS CLI Command Reference*.

### `delete-resource-policy`
<a name="ssm-incidents_DeleteResourcePolicy_cli_2_topic"></a>

The following code example shows how to use `delete-resource-policy`.

**AWS CLI**
**To delete a resource policy**
The following `delete-resource-policy` example deletes a resource policy from a response plan. This will revoke access from the principal or organization that the response plan was shared with.

```
aws ssm-incidents delete-resource-policy \
    --policy-id {{"be8b57191f0371f1c6827341aa3f0a03"}} \
    --resource-arn {{"arn:aws:ssm-incidents::123456789012:response-plan/Example-Response-Plan"}}
```
This command produces no output.
For more information, see [Working with shared contacts and response plans](https://docs.aws.amazon.com/incident-manager/latest/userguide/sharing.html) in the *Incident Manager User Guide*.
+  For API details, see [DeleteResourcePolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm-incidents/delete-resource-policy.html) in *AWS CLI Command Reference*.

### `delete-response-plan`
<a name="ssm-incidents_DeleteResponsePlan_cli_2_topic"></a>

The following code example shows how to use `delete-response-plan`.

**AWS CLI**
**To delete a response plan**
The following `delete-response-plan` example deletes the specified response plan.

```
aws ssm-incidents delete-response-plan \
    --arn {{"arn:aws:ssm-incidents::123456789012:response-plan/example-response"}}
```
This command produces no output.
For more information, see [Incident preparation](https://docs.aws.amazon.com/incident-manager/latest/userguide/incident-response.html) in the *Incident Manager User Guide*.
+  For API details, see [DeleteResponsePlan](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm-incidents/delete-response-plan.html) in *AWS CLI Command Reference*.

### `delete-timeline-event`
<a name="ssm-incidents_DeleteTimelineEvent_cli_2_topic"></a>

The following code example shows how to use `delete-timeline-event`.

**AWS CLI**
**To delete a timeline event**
The following `delete-timeline-event` example deletes a custom timeline event from the specified incident record.

```
aws ssm-incidents delete-timeline-event \
    --event-id {{"a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"}} \
    --incident-record-arn {{"arn:aws:ssm-incidents::123456789012:incident-record/Example-Response-Plan/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222"}}
```
This command produces no output.
For more information, see [Incident details](https://docs.aws.amazon.com/incident-manager/latest/userguide/tracking-details.html) in the *Incident Manager User Guide*.
+  For API details, see [DeleteTimelineEvent](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm-incidents/delete-timeline-event.html) in *AWS CLI Command Reference*.

### `get-incident-record`
<a name="ssm-incidents_GetIncidentRecord_cli_2_topic"></a>

The following code example shows how to use `get-incident-record`.

**AWS CLI**
**To get an incident record**
The following `get-incident-record` example gets details about the specified incident record.

```
aws ssm-incidents get-incident-record \
    --arn {{"arn:aws:ssm-incidents::123456789012:incident-record/Example-Response-Plan/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"}}
```
Output:

```
{
    "incidentRecord": {
        "arn": "arn:aws:ssm-incidents::123456789012:incident-record/Example-Response-Plan/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
        "automationExecutions": [],
        "creationTime": "2021-05-21T18:16:57.579000+00:00",
        "dedupeString": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
        "impact": 5,
        "incidentRecordSource": {
            "createdBy": "arn:aws:iam::123456789012:user/draliatp",
            "invokedBy": "arn:aws:iam::123456789012:user/draliatp",
            "source": "aws.ssm-incidents.custom"
        },
        "lastModifiedBy": "arn:aws:iam::123456789012:user/draliatp",
        "lastModifiedTime": "2021-05-21T18:16:59.149000+00:00",
        "notificationTargets": [],
        "status": "OPEN",
        "title": "Example-Incident"
    }
}
```
For more information, see [Incident details](https://docs.aws.amazon.com/incident-manager/latest/userguide/tracking-details.html) in the *Incident Manager User Guide*.
+  For API details, see [GetIncidentRecord](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm-incidents/get-incident-record.html) in *AWS CLI Command Reference*.

### `get-replication-set`
<a name="ssm-incidents_GetReplicationSet_cli_2_topic"></a>

The following code example shows how to use `get-replication-set`.

**AWS CLI**
**To get the replication set**
The following `get-replication-set` example gets the details of the replication set Incident Manager uses to replicate and encrypt data in your Amazon Web Services account.

```
aws ssm-incidents get-replication-set \
    --arn {{"arn:aws:ssm-incidents::123456789012:replication-set/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"}}
```
Output:

```
{
    "replicationSet": {
        "createdBy": "arn:aws:sts::123456789012:assumed-role/Admin/username",
        "createdTime": "2021-05-14T17:57:22.010000+00:00",
        "deletionProtected": false,
        "lastModifiedBy": "arn:aws:sts::123456789012:assumed-role/Admin/username",
        "lastModifiedTime": "2021-05-14T17:57:22.010000+00:00",
        "regionMap": {
            "us-east-1": {
                "sseKmsKeyId": "DefaultKey",
                "status": "ACTIVE"
            },
            "us-east-2": {
                "sseKmsKeyId": "DefaultKey",
                "status": "ACTIVE",
                "statusMessage": "Tagging inaccessible"
            }
        },
        "status": "ACTIVE"
    }
}
```
For more information, see [Configuring replication sets and Findings in Incident Manager](https://docs.aws.amazon.com/incident-manager/latest/userguide/general-settings.html) in the *Incident Manager User Guide*.
+  For API details, see [GetReplicationSet](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm-incidents/get-replication-set.html) in *AWS CLI Command Reference*.

### `get-resource-policies`
<a name="ssm-incidents_GetResourcePolicies_cli_2_topic"></a>

The following code example shows how to use `get-resource-policies`.

**AWS CLI**
**To list resource policies for a response plan**
The following `get-resource-policies` example lists the resource policies associated with the specified response plan.

```
aws ssm-incidents get-resource-policies \
    --resource-arn {{"arn:aws:ssm-incidents::123456789111:response-plan/Example-Response-Plan"}}
```
Output:

```
{
    "resourcePolicies": [
        {
            "policyDocument": "{\"Version\":\"2012-10-17\",\"Statement\":[{\"Sid\":\"d901b37a-dbb0-458a-8842-75575c464219-external-principals\",\"Effect\":\"Allow\",\"Principal\":{\"AWS\":\"arn:aws:iam::123456789222:root\"},\"Action\":[\"ssm-incidents:GetResponsePlan\",\"ssm-incidents:StartIncident\",\"ssm-incidents:UpdateIncidentRecord\",\"ssm-incidents:GetIncidentRecord\",\"ssm-incidents:CreateTimelineEvent\",\"ssm-incidents:UpdateTimelineEvent\",\"ssm-incidents:GetTimelineEvent\",\"ssm-incidents:ListTimelineEvents\",\"ssm-incidents:UpdateRelatedItems\",\"ssm-incidents:ListRelatedItems\"],\"Resource\":[\"arn:aws:ssm-incidents:*:123456789111:response-plan/Example-Response-Plan\",\"arn:aws:ssm-incidents:*:123456789111:incident-record/Example-Response-Plan/*\"]}]}",
            "policyId": "be8b57191f0371f1c6827341aa3f0a03",
            "ramResourceShareRegion": "us-west-2"
        }
    ]
}
```
For more information, see [Working with shared contacts and response plans](https://docs.aws.amazon.com/incident-manager/latest/userguide/sharing.html) in the *Incident Manager User Guide*.
+  For API details, see [GetResourcePolicies](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm-incidents/get-resource-policies.html) in *AWS CLI Command Reference*.

### `get-response-plan`
<a name="ssm-incidents_GetResponsePlan_cli_2_topic"></a>

The following code example shows how to use `get-response-plan`.

**AWS CLI**
**To get details of a response plan**
The following `get-response-plan` example gets details about a specified response plan in your AWS account.

```
aws ssm-incidents get-response-plan \
    --arn {{"arn:aws:ssm-incidents::123456789012:response-plan/Example-Response-Plan"}}
```
Output:

```
{
    "actions": [
        {
            "ssmAutomation": {
                "documentName": "AWSIncidents-CriticalIncidentRunbookTemplate",
                "documentVersion": "$DEFAULT",
                "roleArn": "arn:aws:iam::123456789012:role/aws-service-role/ssm-incidents.amazonaws.com/AWSServiceRoleForIncidentManager",
                "targetAccount": "RESPONSE_PLAN_OWNER_ACCOUNT"
            }
        }
    ],
    "arn": "arn:aws:ssm-incidents::123456789012:response-plan/Example-Response-Plan",
    "chatChannel": {
        "chatbotSns": [
            "arn:aws:sns:us-west-2:123456789012:Standard_User"
        ]
    },
    "displayName": "Example response plan",
    "engagements": [
        "arn:aws:ssm-contacts:us-west-2:123456789012:contact/example"
    ],
    "incidentTemplate": {
        "impact": 5,
        "title": "Example-Incident"
    },
    "name": "Example-Response-Plan"
}
```
For more information, see [Incident preparation](https://docs.aws.amazon.com/incident-manager/latest/userguide/incident-response.html) in the *Incident Manager User Guide*.
+  For API details, see [GetResponsePlan](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm-incidents/get-response-plan.html) in *AWS CLI Command Reference*.

### `get-timeline-event`
<a name="ssm-incidents_GetTimelineEvent_cli_2_topic"></a>

The following code example shows how to use `get-timeline-event`.

**AWS CLI**
**To get details of a timeline event**
The following `get-timeline-event` example returns details of the specified timeline event.

```
aws ssm-incidents get-timeline-event \
    --event-id {{a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}} \
    --incident-record-arn {{"arn:aws:ssm-incidents::123456789012:incident-record/Example-Response-Plan/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222"}}
```
Output:

```
{
    "event": {
        "eventData": "\"Incident Started\"",
        "eventId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
        "eventTime": "2021-05-21T18:16:57+00:00",
        "eventType": "Custom Event",
        "eventUpdatedTime": "2021-05-21T18:16:59.944000+00:00",
        "incidentRecordArn": "arn:aws:ssm-incidents::123456789012:incident-record/Example-Response-Plan/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222"
    }
}
```
For more information, see [Incident details](https://docs.aws.amazon.com/incident-manager/latest/userguide/tracking-details.html) in the *Incident Manager User Guide*.
+  For API details, see [GetTimelineEvent](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm-incidents/get-timeline-event.html) in *AWS CLI Command Reference*.

### `list-incident-records`
<a name="ssm-incidents_ListIncidentRecords_cli_2_topic"></a>

The following code example shows how to use `list-incident-records`.

**AWS CLI**
**To list incident records**
The following `list-incident-records` example lists the incident records in your Amazon Web Services account.

```
aws ssm-incidents list-incident-records
```
Output:

```
{
    "incidentRecordSummaries": [
        {
            "arn": "arn:aws:ssm-incidents::123456789012:incident-record/Example-Response-Plan/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
            "creationTime": "2021-05-21T18:16:57.579000+00:00",
            "impact": 5,
            "incidentRecordSource": {
                "createdBy": "arn:aws:iam::123456789012:user/draliatp",
                "invokedBy": "arn:aws:iam::123456789012:user/draliatp",
                "source": "aws.ssm-incidents.custom"
            },
            "status": "OPEN",
            "title": "Example-Incident"
        }
    ]
}
```
For more information, see [Incident list](https://docs.aws.amazon.com/incident-manager/latest/userguide/tracking-list.html) in the *Incident Manager User Guide*.
+  For API details, see [ListIncidentRecords](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm-incidents/list-incident-records.html) in *AWS CLI Command Reference*.

### `list-related-items`
<a name="ssm-incidents_ListRelatedItems_cli_2_topic"></a>

The following code example shows how to use `list-related-items`.

**AWS CLI**
**To list related items**
The following `list-related-items` example lists the related items of the specified incident.

```
aws ssm-incidents list-related-items \
    --incident-record-arn {{"arn:aws:ssm-incidents::123456789012:incident-record/Example-Response-Plan/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"}}
```
Output:

```
{
    "relatedItems": [
        {
            "identifier": {
                "type": "OTHER",
                "value": {
                    "url": "https://console.aws.amazon.com/systems-manager/opsitems/oi-8ef82158e190/workbench?region=us-west-2"
                }
            },
            "title": "Example related item"
        },
        {
            "identifier": {
                "type": "PARENT",
                "value": {
                    "arn": "arn:aws:ssm:us-west-2:123456789012:opsitem/oi-8084126392ac"
                }
            },
            "title": "parentItem"
        }
    ]
}
```
For more information, see [Incident details](https://docs.aws.amazon.com/incident-manager/latest/userguide/tracking-details.html) in the *Incident Manager User Guide*.
+  For API details, see [ListRelatedItems](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm-incidents/list-related-items.html) in *AWS CLI Command Reference*.

### `list-replication-sets`
<a name="ssm-incidents_ListReplicationSets_cli_2_topic"></a>

The following code example shows how to use `list-replication-sets`.

**AWS CLI**
**To list the replication set**
The following `list-replication-sets` example lists the replication set Incident Manager uses to replicate and encrypt data in your AWS account.

```
aws ssm-incidents list-replication-sets
```
Output:

```
{
    "replicationSetArns": [
        "arn:aws:ssm-incidents::123456789012:replication-set/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
    ]
}
```
For more information, see [Configuring replication sets and Findings in Incident Manager](https://docs.aws.amazon.com/incident-manager/latest/userguide/general-settings.html) in the *Incident Manager User Guide*.
+  For API details, see [ListReplicationSets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm-incidents/list-replication-sets.html) in *AWS CLI Command Reference*.

### `list-response-plans`
<a name="ssm-incidents_ListResponsePlans_cli_2_topic"></a>

The following code example shows how to use `list-response-plans`.

**AWS CLI**
**To list the available response plans**
The following `list-response-plans` example lists the available response plans in your Amazon Web Services account.

```
aws ssm-incidents list-response-plans
```
Output:

```
{
    "responsePlanSummaries": [
        {
            "arn": "arn:aws:ssm-incidents::123456789012:response-plan/Example-Response-Plan",
            "displayName": "Example response plan",
            "name": "Example-Response-Plan"
        }
    ]
}
```
For more information, see [Incident preparation](https://docs.aws.amazon.com/incident-manager/latest/userguide/incident-response.html) in the *Incident Manager User Guide*.
+  For API details, see [ListResponsePlans](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm-incidents/list-response-plans.html) in *AWS CLI Command Reference*.

### `list-tags-for-resource`
<a name="ssm-incidents_ListTagsForResource_cli_2_topic"></a>

The following code example shows how to use `list-tags-for-resource`.

**AWS CLI**
**To list tags for a response plan**
The following `list-tags-for-resource` example lists the tags associated with the specified response plan.

```
aws ssm-incidents list-tags-for-resource \
    --resource-arn {{"arn:aws:ssm-incidents::123456789012:response-plan/Example-Response-Plan"}}
```
Output:

```
{
    "tags": {
    "group1": "1"
    }
}
```
For more information, see [Tagging](https://docs.aws.amazon.com/incident-manager/latest/userguide/tagging.html) in the *Incident Manager User Guide*.
+  For API details, see [ListTagsForResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm-incidents/list-tags-for-resource.html) in *AWS CLI Command Reference*.

### `list-timeline-events`
<a name="ssm-incidents_ListTimelineEvents_cli_2_topic"></a>

The following code example shows how to use `list-timeline-events`.

**AWS CLI**
**To list timeline events of an incident**
The following `list-timeline-events` example lists the timeline events of the specified incident.

```
aws ssm-incidents list-timeline-events \
    --incident-record-arn {{"arn:aws:ssm-incidents::123456789012:incident-record/Example-Response-Plan/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"}}
```
Output:

```
{
    "eventSummaries": [
        {
            "eventId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
            "eventTime": "2021-05-21T22:36:13.766000+00:00",
            "eventType": "SSM Incident Record Update",
            "eventUpdatedTime": "2021-05-21T22:36:13.766000+00:00",
            "incidentRecordArn": "arn:aws:ssm-incidents::123456789012:incident-record/Example-Response-Plan/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
        },
        {
            "eventId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE33333",
            "eventTime": "2021-05-21T18:58:46.443000+00:00",
            "eventType": "SSM Incident Record Update",
            "eventUpdatedTime": "2021-05-21T18:58:46.443000+00:00",
            "incidentRecordArn": "arn:aws:ssm-incidents::123456789012:incident-record/Example-Response-Plan/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
        },
        {
            "eventId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE44444",
            "eventTime": "2021-05-21T18:16:59.149000+00:00",
            "eventType": "SSM Incident Record Update",
            "eventUpdatedTime": "2021-05-21T18:16:59.149000+00:00",
            "incidentRecordArn": "arn:aws:ssm-incidents::123456789012:incident-record/Example-Response-Plan/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
        },
        {
            "eventId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE55555",
            "eventTime": "2021-05-21T18:16:58+00:00",
            "eventType": "SSM Automation Execution Start Failure for Incident",
            "eventUpdatedTime": "2021-05-21T18:16:58.689000+00:00",
            "incidentRecordArn": "arn:aws:ssm-incidents::123456789012:incident-record/Example-Response-Plan/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
        },
        {
            "eventId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE66666",
            "eventTime": "2021-05-21T18:16:57+00:00",
            "eventType": "Custom Event",
            "eventUpdatedTime": "2021-05-21T18:16:59.944000+00:00",
            "incidentRecordArn": "arn:aws:ssm-incidents::123456789012:incident-record/Example-Response-Plan/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
        },
        {
            "eventId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE77777",
            "eventTime": "2020-10-01T20:30:00+00:00",
            "eventType": "Custom Event",
            "eventUpdatedTime": "2021-05-21T22:28:26.299000+00:00",
            "incidentRecordArn": "arn:aws:ssm-incidents::123456789012:incident-record/Example-Response-Plan/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
        }
    ]
}
```
For more information, see [Incident details](https://docs.aws.amazon.com/incident-manager/latest/userguide/tracking-details.html) in the *Incident Manager User Guide*.
+  For API details, see [ListTimelineEvents](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm-incidents/list-timeline-events.html) in *AWS CLI Command Reference*.

### `put-resource-policy`
<a name="ssm-incidents_PutResourcePolicy_cli_2_topic"></a>

The following code example shows how to use `put-resource-policy`.

**AWS CLI**
**To share a response plan and incidents**
The following `put-resource-policy` example adds a resource policy to the Example-Response-Plan that shares the response plan and associated incidents with the specified principal.

```
aws ssm-incidents put-resource-policy \
    --resource-arn {{"arn:aws:ssm-incidents::123456789111:response-plan/Example-Response-Plan"}} \
    --policy "{\"Version\":\"2012-10-17\",\"Statement\":[{\"Sid\":\"ExampleResourcePolciy\",\"Effect\":\"Allow\",\"Principal\":{\"AWS\":\"arn:aws:iam::123456789222:root\"},\"Action\":[\"ssm-incidents:GetResponsePlan\",\"ssm-incidents:StartIncident\",\"ssm-incidents:UpdateIncidentRecord\",\"ssm-incidents:GetIncidentRecord\",\"ssm-incidents:CreateTimelineEvent\",\"ssm-incidents:UpdateTimelineEvent\",\"ssm-incidents:GetTimelineEvent\",\"ssm-incidents:ListTimelineEvents\",\"ssm-incidents:UpdateRelatedItems\",\"ssm-incidents:ListRelatedItems\"],\"Resource\":[\"arn:aws:ssm-incidents:*:123456789111:response-plan/Example-Response-Plan\",\"arn:aws:ssm-incidents:*:123456789111:incident-record/Example-Response-Plan/*\"]}]}"
```
Output:

```
{
    "policyId": "be8b57191f0371f1c6827341aa3f0a03"
}
```
For more information, see [Working with shared contacts and response plans](https://docs.aws.amazon.com/incident-manager/latest/userguide/sharing.html) in the *Incident Manager User Guide*.
+  For API details, see [PutResourcePolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm-incidents/put-resource-policy.html) in *AWS CLI Command Reference*.

### `start-incident`
<a name="ssm-incidents_StartIncident_cli_2_topic"></a>

The following code example shows how to use `start-incident`.

**AWS CLI**
**To start an incident**
The following `start-incident` example starts an incident using the specified response plan.

```
aws ssm-incidents start-incident \
    --response-plan-arn {{"arn:aws:ssm-incidents::123456789012:response-plan/Example-Response-Plan"}}
```
Output:

```
{
    "incidentRecordArn": "arn:aws:ssm-incidents::123456789012:incident-record/Example-Response-Plan/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
}
```
For more information, see [Incident creation](https://docs.aws.amazon.com/incident-manager/latest/userguide/incident-creation.html) in the *Incident Manager User Guide*.
+  For API details, see [StartIncident](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm-incidents/start-incident.html) in *AWS CLI Command Reference*.

### `tag-resource`
<a name="ssm-incidents_TagResource_cli_2_topic"></a>

The following code example shows how to use `tag-resource`.

**AWS CLI**
**To tag a response plan**
The following `tag-resource` example tags a specified response plan with the provided tag key-value pair.

```
aws ssm-incidents tag-resource \
    --resource-arn {{"arn:aws:ssm-incidents::123456789012:response-plan/Example-Response-Plan"}} \
    --tags '{{{"group1":"1"}}}'
```
This command produces no output.
For more information, see [Tagging](https://docs.aws.amazon.com/incident-manager/latest/userguide/tagging.html) in the *Incident Manager User Guide*.
+  For API details, see [TagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm-incidents/tag-resource.html) in *AWS CLI Command Reference*.

### `untag-resource`
<a name="ssm-incidents_UntagResource_cli_2_topic"></a>

The following code example shows how to use `untag-resource`.

**AWS CLI**
**To remove tags from a response plan**
The following `untag-resource` example removes the specified tags from the response plan.

```
aws ssm-incidents untag-resource \
    --resource-arn {{"arn:aws:ssm-incidents::123456789012:response-plan/Example-Response-Plan"}} \
    --tag-keys '{{["group1"]}}'
```
This command produces no output.
For more information, see [Tagging](https://docs.aws.amazon.com/incident-manager/latest/userguide/tagging.html) in the *Incident Manager User Guide*.
+  For API details, see [UntagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm-incidents/untag-resource.html) in *AWS CLI Command Reference*.

### `update-deletion-protection`
<a name="ssm-incidents_UpdateDeletionProtection_cli_2_topic"></a>

The following code example shows how to use `update-deletion-protection`.

**AWS CLI**
**To update replication set deletion protection**
The following `update-deletion-protection` example updates the deletion protection in your account to protect you from deleting the last Region in your replication set.

```
aws ssm-incidents update-deletion-protection \
    --arn {{"arn:aws:ssm-incidents::123456789012:replication-set/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"}} \
    --deletion-protected
```
This command produces no output.
For more information, see [Configuring replication sets and Findings in Incident Manager](https://docs.aws.amazon.com/incident-manager/latest/userguide/general-settings.html) in the *Incident Manager User Guide*.
+  For API details, see [UpdateDeletionProtection](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm-incidents/update-deletion-protection.html) in *AWS CLI Command Reference*.

### `update-incident-record`
<a name="ssm-incidents_UpdateIncidentRecord_cli_2_topic"></a>

The following code example shows how to use `update-incident-record`.

**AWS CLI**
**To update an incident record**
The following `update-incident-record` example resolves the specified incident.

```
aws ssm-incidents update-incident-record \
    --arn {{"arn:aws:ssm-incidents::123456789012:incident-record/Example-Response-Plan/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"}} \
    --status {{"RESOLVED"}}
```
This command produces no output.
For more information, see [Incident details](https://docs.aws.amazon.com/incident-manager/latest/userguide/tracking-details.html) in the *Incident Manager User Guide*.
+  For API details, see [UpdateIncidentRecord](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm-incidents/update-incident-record.html) in *AWS CLI Command Reference*.

### `update-related-items`
<a name="ssm-incidents_UpdateRelatedItems_cli_2_topic"></a>

The following code example shows how to use `update-related-items`.

**AWS CLI**
**To update an incidents related item**
The following `update-related-items` example removes a related item from the specified incident record.

```
aws ssm-incidents update-related-items \
    --incident-record-arn {{"arn:aws:ssm-incidents::123456789012:incident-record/Example-Response-Plan/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"}} \
    --related-items-update '{{{"itemToRemove": {"type": "OTHER", "value": {"url": "https://console.aws.amazon.com/systems-manager/opsitems/oi-8ef82158e190/workbench?region=us-west-2"}}}}}'
```
This command produces no output.
For more information, see [Incident details](https://docs.aws.amazon.com/incident-manager/latest/userguide/tracking-details.html) in the *Incident Manager User Guide*.
+  For API details, see [UpdateRelatedItems](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm-incidents/update-related-items.html) in *AWS CLI Command Reference*.

### `update-replication-set`
<a name="ssm-incidents_UpdateReplicationSet_cli_2_topic"></a>

The following code example shows how to use `update-replication-set`.

**AWS CLI**
**To update a replication set**
The following `update-replication-set` example deletes the us-west-2 Region from the replication set.

```
aws ssm-incidents update-replication-set \
    --arn {{"arn:aws:ssm-incidents::123456789012:replication-set/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"}} \
    --actions '{{[{"deleteRegionAction": {"regionName": "us-west-2"}}]}}'
```
This command produces no output.
For more information, see [Configuring replication sets and Findings in Incident Manager](https://docs.aws.amazon.com/incident-manager/latest/userguide/general-settings.html) in the *Incident Manager User Guide*.
+  For API details, see [UpdateReplicationSet](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm-incidents/update-replication-set.html) in *AWS CLI Command Reference*.

### `update-response-plan`
<a name="ssm-incidents_UpdateResponsePlan_cli_2_topic"></a>

The following code example shows how to use `update-response-plan`.

**AWS CLI**
**To update a response plan**
The following `update-response-plan` example removes a chat channel from the specified response plan.

```
aws ssm-incidents update-response-plan \
    --arn {{"arn:aws:ssm-incidents::123456789012:response-plan/Example-Response-Plan"}} \
    --chat-channel '{{{"empty":{}}}}'
```
This command produces no output.
For more information, see [Incident preparation](https://docs.aws.amazon.com/incident-manager/latest/userguide/incident-response.html) in the *Incident Manager User Guide*.
+  For API details, see [UpdateResponsePlan](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm-incidents/update-response-plan.html) in *AWS CLI Command Reference*.

### `update-timeline-event`
<a name="ssm-incidents_UpdateTimelineEvent_cli_2_topic"></a>

The following code example shows how to use `update-timeline-event`.

**AWS CLI**
**To update a timeline event**
The following `update-timeline-event` example updates the time that the event occurred.

```
aws ssm-incidents update-timeline-event \
    --event-id {{a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}} \
    --incident-record-arn {{"arn:aws:ssm-incidents::123456789012:incident-record/Example-Response-Plan/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222"}} \
    --event-time {{"2021-05-21T18:10:57+00:00"}}
```
This command produces no output.
For more information, see [Incident details](https://docs.aws.amazon.com/incident-manager/latest/userguide/tracking-details.html) in the *Incident Manager User Guide*.
+  For API details, see [UpdateTimelineEvent](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm-incidents/update-timeline-event.html) in *AWS CLI Command Reference*.
