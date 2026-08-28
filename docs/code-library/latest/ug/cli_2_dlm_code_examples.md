---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/cli_2_dlm_code_examples.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Amazon Data Lifecycle Manager examples using AWS CLI
<a name="cli_2_dlm_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with Amazon Data Lifecycle Manager.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)

## Actions
<a name="actions"></a>

### `create-default-role`
<a name="dlm_CreateDefaultRole_cli_2_topic"></a>

The following code example shows how to use `create-default-role`.

**AWS CLI**
**To create the required IAM role for Amazon DLM**
The following `dlm create-default-role` example creates the AWSDataLifecycleManagerDefaultRole default role for managing snapshots.

```
aws dlm create-default-role \
    --resource-type {{snapshot}}
```
This command produces no output.
For more information, see [Default service roles for Amazon Data Lifecycle Manager](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/service-role.html#default-service-roles) in the *Amazon Elastic Compute Cloud User Guide*.
+  For API details, see [CreateDefaultRole](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dlm/create-default-role.html) in *AWS CLI Command Reference*.

### `create-lifecycle-policy`
<a name="dlm_CreateLifecyclePolicy_cli_2_topic"></a>

The following code example shows how to use `create-lifecycle-policy`.

**AWS CLI**
**To create a lifecycle policy**
The following `create-lifecycle-policy` example creates a lifecycle policy that creates a daily snapshot of volumes at the specified time. The specified tags are added to the snapshots, and tags are also copied from the volume and added to the snapshots. If creating a new snapshot exceeds the specified maximum count, the oldest snapshot is deleted.

```
aws dlm create-lifecycle-policy \
    --description {{"My first policy"}} \
    --state {{ENABLED}} \
    --execution-role-arn {{arn:aws:iam::12345678910:role/AWSDataLifecycleManagerDefaultRole}} \
    --policy-details {{file://policyDetails.json}}
```
Contents of `policyDetails.json`:

```
{
    "ResourceTypes": [
        "VOLUME"
    ],
    "TargetTags": [
        {
            "Key": "costCenter",
            "Value": "115"
        }
    ],
    "Schedules":[
        {
            "Name": "DailySnapshots",
            "CopyTags": true,
            "TagsToAdd": [
                {
                    "Key": "type",
                     "Value": "myDailySnapshot"
                }
            ],
            "CreateRule": {
                "Interval": 24,
                "IntervalUnit": "HOURS",
                "Times": [
                    "03:00"
                ]
            },
            "RetainRule": {
                "Count":5
            }
        }
    ]
}
```
Output:

```
{
    "PolicyId": "policy-0123456789abcdef0"
}
```
+  For API details, see [CreateLifecyclePolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dlm/create-lifecycle-policy.html) in *AWS CLI Command Reference*.

### `delete-lifecycle-policy`
<a name="dlm_DeleteLifecyclePolicy_cli_2_topic"></a>

The following code example shows how to use `delete-lifecycle-policy`.

**AWS CLI**
**To delete a lifecycle policy**
The following example deletes the specified lifecycle policy.:

```
aws dlm delete-lifecycle-policy --policy-id {{policy-0123456789abcdef0}}
```
+  For API details, see [DeleteLifecyclePolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dlm/delete-lifecycle-policy.html) in *AWS CLI Command Reference*.

### `get-lifecycle-policies`
<a name="dlm_GetLifecyclePolicies_cli_2_topic"></a>

The following code example shows how to use `get-lifecycle-policies`.

**AWS CLI**
**To get a summary of your lifecycle policies**
The following `get-lifecycle-policies` example lists all of your lifecycle policies.

```
aws dlm get-lifecycle-policies
```
Output:

```
{
    "Policies": [
        {
            "PolicyId": "policy-0123456789abcdef0",
            "Description": "My first policy",
            "State": "ENABLED"
        }
    ]
}
```
+  For API details, see [GetLifecyclePolicies](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dlm/get-lifecycle-policies.html) in *AWS CLI Command Reference*.

### `get-lifecycle-policy`
<a name="dlm_GetLifecyclePolicy_cli_2_topic"></a>

The following code example shows how to use `get-lifecycle-policy`.

**AWS CLI**
**To describe a lifecycle policy**
The following `get-lifecycle-policy` example displays details for the specified lifecycle policy.

```
aws dlm get-lifecycle-policy \
    --policy-id {{policy-0123456789abcdef0}}
```
Output:

```
{
    "Policy": {
        "PolicyId": "policy-0123456789abcdef0",
        "Description": "My policy",
        "State": "ENABLED",
        "ExecutionRoleArn": "arn:aws:iam::123456789012:role/AWSDataLifecycleManagerDefaultRole",
        "DateCreated": "2019-08-08T17:45:42Z",
        "DateModified": "2019-08-08T17:45:42Z",
        "PolicyDetails": {
            "PolicyType": "EBS_SNAPSHOT_MANAGEMENT",
            "ResourceTypes": [
                "VOLUME"
            ],
            "TargetTags": [
              {
                  "Key": "costCenter",
                  "Value": "115"
              }
            ],
            "Schedules": [
              {
                  "Name": "DailySnapshots",
                  "CopyTags": true,
                  "TagsToAdd": [
                    {
                        "Key": "type",
                        "Value": "myDailySnapshot"
                    }
                  ],
                  "CreateRule": {
                    "Interval": 24,
                    "IntervalUnit": "HOURS",
                    "Times": [
                        "03:00"
                    ]
                  },
                  "RetainRule": {
                    "Count": 5
                  }
              }
            ]
        }
    }
}
```
+  For API details, see [GetLifecyclePolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dlm/get-lifecycle-policy.html) in *AWS CLI Command Reference*.

### `update-lifecycle-policy`
<a name="dlm_UpdateLifecyclePolicy_cli_2_topic"></a>

The following code example shows how to use `update-lifecycle-policy`.

**AWS CLI**
**Example 1: To enable a lifecycle policy**
The following `update-lifecycle-policy` example enables the specified lifecycle policy.

```
aws dlm update-lifecycle-policy \
    --policy-id {{policy-0123456789abcdef0}} \
    --state {{ENABLED}}
```
**Example 2: To disable a lifecycle policy**
The following `update-lifecycle-policy` example disables the specified lifecycle policy.

```
aws dlm update-lifecycle-policy \
    --policy-id {{policy-0123456789abcdef0}} \
    --state {{DISABLED}}
```
**Example 3: To update the details for lifecycle policy**
The following `update-lifecycle-policy` example updates the target tags for the specified lifecycle policy.

```
aws dlm update-lifecycle-policy \
    --policy-id {{policy-0123456789abcdef0}}
    --policy-details {{file://policyDetails.json}}
```
Contents of `policyDetails.json`. Other details not referenced in this file are not changed by the command.

```
{
    "TargetTags": [
        {
            "Key": "costCenter",
            "Value": "120"
        },
        {
            "Key": "project",
            "Value": "lima"
        }
    ]
}
```
+  For API details, see [UpdateLifecyclePolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dlm/update-lifecycle-policy.html) in *AWS CLI Command Reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
