---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/userguide/launching-instances-synchronous-provisioning.html
---

# Launching instances with synchronous provisioning
<a name="launching-instances-synchronous-provisioning"></a>

You can use the LaunchInstances API to synchronously launch a specific number of instances in your Auto Scaling group. The API launches instances in the Availability Zone or subnet that you specify and immediately returns the instance IDs or error information.

## Prerequisites
<a name="prerequisites-synchronous-provisioning"></a>

Before you can use the LaunchInstances API, you must have:
+ An Auto Scaling group that uses a launch template (launch configurations are not supported)
+ You must have permissions for the following IAM actions:
  + `autoscaling:LaunchInstances`
  + `ec2:CreateFleet`
  + `ec2:DescribeLaunchTemplateVersions`

## Launch instances with synchronous provisioning
<a name="launch-instances-cli"></a>

You can launch instances with synchronous provisioning through the AWS CLI.

### AWS CLI
<a name="aws-cli-launch-instances"></a>

To launch instances with synchronous provisioning:

```
aws autoscaling launch-instances \
        --auto-scaling-group-name {{group-name}} \
        --requested-capacity {{number}} \
        [--availability-zones {{zone-name}}] \
        [--subnet-ids {{subnet-id}}] \
        [--availability-zone-ids {{zone-id}}] \
        [--retry-strategy {{none}}|{{retry-with-group-configuration}}] \
        [--client-token {{token}}]
```

#### Examples
<a name="examples-launch-instances"></a>

**Launching instances in a specific Availability Zone**

```
aws autoscaling launch-instances \
        --auto-scaling-group-name {{my-asg}} \
        --requested-capacity {{3}} \
        --availability-zones {{us-east-1a}} \
        --retry-strategy {{retry-with-group-configuration}}
```

**Launching instances in a specific subnet**

```
aws autoscaling launch-instances \
        --auto-scaling-group-name {{my-asg}} \
        --requested-capacity {{2}} \
        --subnet-ids {{subnet-12345678}} \
        --retry-strategy {{none}} \
        --client-token {{my-unique-token-123}}
```

#### Handling responses
<a name="handling-responses"></a>

**Example of a successful response:**

```
{
    "AutoScalingGroupName": "my-asg",
    "ClientToken": "my-unique-token-123",
    "Instances": [
        {
            "InstanceType": "m5.xlarge",
            "AvailabilityZone": "us-east-1a",
            "AvailabilityZoneId": "use1-az1",
            "SubnetId": "subnet-12345678",
            "MarketType": "OnDemand",
            "InstanceIds": ["i-0123456789abcdef0", "i-0fedcba9876543210"]
        }
    ],
    "Errors": []
}
```

**Example of a response with errors**

```
{
    "AutoScalingGroupName": "my-asg",
    "ClientToken": "my-unique-token-123",
    "Instances": [],
    "Errors": [
       {
        "InstanceType": "m5.large",
        "AvailabilityZone": "us-east-1a",
        "AvailabilityZoneId": "use1-az1",
        "SubnetId": "subnet-12345678",
        "MarketType": "OnDemand",
        "ErrorCode": "InsufficientInstanceCapacity",
        "ErrorMessage": "There is not enough capacity to fulfill your request for instance type 'm5.large' in 'us-east-1a'"
        }
    ]
}
```

## Handle launch failures and retries
<a name="handle-launch-failures-retries"></a>

When the LaunchInstances API encounters failures, you can implement retry strategies using idempotency tokens and appropriate retry policies.

You can use the client-token parameter to retry requests. You can also use the following retry strategies:
+ `RetryStrategy: none` (default) - If the API call fails, the Auto Scaling group's desired capacity remains unchanged and no automatic retry occurs.
+ `RetryStrategy: retry-with-group-configuration` - If the API call fails, the Auto Scaling group's desired capacity is increased by the requested amount, and Auto Scaling will automatically retry launching instances using the group's standard configuration and processes.

Retry behavior for `RetryStrategy: retry-with-group-configuration` depends on the failure type:
+ **Validation errors**: Desired capacity is not increased since the operation can't proceed. For example, invalid parameters or unsupported configurations.
+ **Capacity errors**: Desired capacity is increased and Auto Scaling will retry launching instances asynchronously using the group's normal scaling processes.

### Using client tokens for idempotency
<a name="client-tokens-sp"></a>

The `client-token` parameter ensures idempotent operations and enables safe retries of launch requests.

Key behaviors:
+ Client tokens have an 8-hour lifetime from the initial request
+ Retrying with the same client token within 8 hours returns the cached response instead of launching new instances
+ After 8 hours, the same client token will initiate a new launch operation

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
